// -----------------------------------------------------------------------------
// tb_async_fifo.sv -- self-checking testbench for async_fifo
//
// Two asynchronous, non-harmonic clocks (100 MHz write / ~71 MHz read).  Each
// domain drives and samples on its own NEGEDGE.  The FIFO read port is
// first-word-fall-through (rdata = mem[rptr]), so the reader samples rdata in
// the same cycle it asserts rpop (decide-and-record), before the pop advances
// the pointer.  The writer uses resolve-previous timing for wdata.  Checks:
//   * data integrity + FIFO ordering across the CDC (queue scoreboard)
//   * no loss / no duplication (pushed == popped at end)
// Prints a single PASS/FAIL line and $finish.
// -----------------------------------------------------------------------------
`timescale 1ns/1ps
module tb_async_fifo;
  localparam int W = 16, DEPTH = 8, N = 2000;

  logic             wclk = 1'b0, rclk = 1'b0, wrst_n, rrst_n;
  logic             wpush, wfull;
  logic [W-1:0]     wdata;
  logic             rpop, rempty;
  logic [W-1:0]     rdata;

  async_fifo #(.WIDTH(W), .DEPTH(DEPTH)) dut (
    .wclk(wclk), .wrst_n(wrst_n), .wpush(wpush), .wdata(wdata), .wfull(wfull),
    .rclk(rclk), .rrst_n(rrst_n), .rpop(rpop), .rdata(rdata), .rempty(rempty));

  always #5 wclk = ~wclk;   // 100 MHz
  always #7 rclk = ~rclk;   // ~71.4 MHz, asynchronous

  logic [W-1:0] q [$];
  int           pushed = 0, popped = 0, errors = 0;
  logic [W-1:0] wctr, rexp;

  // ---- writer (negedge wclk, resolve-previous) ----
  initial begin
    wrst_n = 0; wpush = 0; wdata = 0; wctr = 0;
    repeat (4) @(negedge wclk);
    wrst_n = 1;
    forever begin
      @(negedge wclk);
      // resolve the request that hit the just-passed posedge
      if (wpush && !wfull) begin q.push_back(wdata); pushed++; wctr = wctr + 1; end
      // decide next request (hold same value if previous was blocked by full)
      if (wpush && wfull) begin
        // retry: keep wpush=1 and wdata
      end else begin
        wpush = (pushed < N) && ($urandom_range(0, 99) < 60);
        wdata = wctr;
      end
      if (pushed >= N) begin wpush = 0; break; end
    end
  end

  // ---- reader (negedge rclk, decide-and-record for FWFT read) ----
  initial begin
    rrst_n = 0; rpop = 0;
    repeat (4) @(negedge rclk);
    rrst_n = 1;
    forever begin
      @(negedge rclk);
      rpop = ($urandom_range(0, 99) < 60);     // governs the upcoming posedge
      if (rpop && !rempty) begin               // rdata now is the word to be popped
        if (q.size() == 0) begin errors++; $error("[%0t] pop with empty model", $time); end
        else begin
          rexp = q.pop_front();
          if (rdata !== rexp) begin errors++; $error("[%0t] DATA mismatch got=%0h exp=%0h", $time, rdata, rexp); end
        end
        popped++;
      end
      if (popped >= N) begin rpop = 0; break; end
    end
  end

  // ---- completion / watchdog ----
  initial begin
    wait (pushed >= N);
    wait (popped >= N);
    repeat (20) @(negedge rclk);
    if (errors == 0 && pushed == popped && pushed >= N)
      $display("PASS tb_async_fifo: pushed=%0d popped=%0d", pushed, popped);
    else
      $display("FAIL tb_async_fifo: errors=%0d pushed=%0d popped=%0d", errors, pushed, popped);
    $finish;
  end

  initial begin
    #5_000_000;
    $display("FAIL tb_async_fifo: TIMEOUT pushed=%0d popped=%0d errors=%0d", pushed, popped, errors);
    $finish;
  end
endmodule
