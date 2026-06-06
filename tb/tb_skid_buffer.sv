// -----------------------------------------------------------------------------
// tb_skid_buffer.sv -- self-checking testbench for axi_skid_buffer
//
// Methodology: drive stimulus and sample outputs on the NEGEDGE, when all
// posedge-registered state has settled.  The output is registered, so the
// scoreboard uses "resolve-previous" timing (the value/handshake read at a
// negedge reflects the posedge just before it).  The stability check snapshots
// the out_ready *being driven* (which governs the next posedge).  Checks:
//   * data integrity + ordering   (queue scoreboard, no latency assumption)
//   * no beat lost / duplicated   (sent == recv at end)
//   * producer-side protocol      (out_valid held & out_data stable until ready)
// Prints a single PASS/FAIL line and $finish.
// -----------------------------------------------------------------------------
`timescale 1ns/1ps
module tb_skid_buffer;
  localparam int W = 16;
  localparam int N = 2000;

  logic             clk = 1'b0, rst_n;
  logic             in_valid, in_ready;
  logic [W-1:0]     in_data;
  logic             out_valid, out_ready;
  logic [W-1:0]     out_data;

  axi_skid_buffer #(.WIDTH(W)) dut (
    .clk(clk), .rst_n(rst_n),
    .in_valid(in_valid), .in_ready(in_ready), .in_data(in_data),
    .out_valid(out_valid), .out_ready(out_ready), .out_data(out_data));

  always #5 clk = ~clk;

  logic [W-1:0] q [$];
  int           sent = 0, recv = 0, errors = 0, cyc = 0, stalls = 0;
  logic [W-1:0] data_ctr, exp;
  logic         in_fire, out_fire;
  logic         ov_prev, or_prev;       // out_valid / driven-out_ready last cycle
  logic [W-1:0] od_prev;

  initial begin
    rst_n = 0; in_valid = 0; in_data = 0; out_ready = 0; data_ctr = 0;
    ov_prev = 0; or_prev = 0; od_prev = 0;
    repeat (4) @(negedge clk);
    rst_n = 1;

    forever begin
      @(negedge clk);
      cyc++;

      // producer-side protocol: if a beat was presented last cycle and the
      // out_ready that governed this posedge was low, the beat must persist.
      if (ov_prev && !or_prev) begin
        stalls++;
        if (!out_valid)           begin errors++; $error("[%0t] out_valid dropped before ready", $time); end
        if (out_data !== od_prev) begin errors++; $error("[%0t] out_data changed during stall", $time); end
      end

      // INPUT (resolve-previous): TB-driven data is stable across the capture
      // posedge, so the value read now is what the DUT captured last posedge.
      in_fire = in_valid & in_ready;
      if (in_fire) begin q.push_back(in_data); sent++; data_ctr = data_ctr + 1; end
      if (in_valid && !in_ready) begin
        // hold valid + data until accepted (AXI rule)
      end else begin
        in_valid = (sent < N) && ($urandom_range(0, 99) < 70);
        in_data  = data_ctr;
      end

      // OUTPUT (decide-and-record): the registered output is overwritten at the
      // consuming posedge, so sample out_data in the cycle out_ready is driven.
      out_ready = ($urandom_range(0, 99) < 70);
      out_fire  = out_valid & out_ready;
      if (out_fire) begin
        if (q.size() == 0) begin errors++; $error("[%0t] output beat with empty model", $time); end
        else begin
          exp = q.pop_front();
          if (out_data !== exp) begin errors++; $error("[%0t] DATA mismatch got=%0h exp=%0h", $time, out_data, exp); end
        end
        recv++;
      end

      // snapshot: or_prev = out_ready that governs the NEXT posedge
      ov_prev = out_valid; od_prev = out_data; or_prev = out_ready;

      if (sent >= N && q.size() == 0 && recv == sent) break;
      if (cyc > 50*N) begin errors++; $error("TIMEOUT sent=%0d recv=%0d", sent, recv); break; end
    end

    if (errors == 0 && sent == recv && sent >= N && stalls > 0)
      $display("PASS tb_skid_buffer: sent=%0d recv=%0d stalls_observed=%0d cycles=%0d", sent, recv, stalls, cyc);
    else
      $display("FAIL tb_skid_buffer: errors=%0d sent=%0d recv=%0d stalls=%0d", errors, sent, recv, stalls);
    $finish;
  end
endmodule
