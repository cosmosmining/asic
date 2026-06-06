// -----------------------------------------------------------------------------
// axi_skid_buffer.sv  -- 2-entry registered handshake buffer
//
// function   : break the combinational valid/ready path of an AXI-style
//              handshake while sustaining full throughput.  The output payload
//              and `out_valid` are registered, and `in_ready` is registered
//              (depends only on the backup-slot occupancy), so there is no
//              combinational path from out_ready -> in_ready or in_valid ->
//              out_valid.  A second (skid/backup) slot captures the in-flight
//              beat in the cycle out_ready falls, so no beat is ever lost.
// parameters : WIDTH - payload width in bits
// latency    : 1 cycle (registered output)
// throughput : 1 transfer/cycle when downstream is ready
// interfaces : in_*  (upstream),  out_* (downstream); standard valid/ready.
// reset      : sync active-low; output and backup slots clear to empty.
// -----------------------------------------------------------------------------
module axi_skid_buffer #(
  parameter int WIDTH = 32
) (
  input  logic             clk,
  input  logic             rst_n,
  // upstream (producer) side
  input  logic             in_valid,
  output logic             in_ready,
  input  logic [WIDTH-1:0] in_data,
  // downstream (consumer) side
  output logic             out_valid,
  input  logic             out_ready,
  output logic [WIDTH-1:0] out_data
);
  logic [WIDTH-1:0] out_data_q;
  logic             out_valid_q;
  logic [WIDTH-1:0] skid_data;
  logic             skid_valid;   // backup slot occupied

  assign out_valid = out_valid_q;
  assign out_data  = out_data_q;
  assign in_ready  = ~skid_valid; // registered: depends only on a flop

  logic in_fire;
  assign in_fire = in_valid & in_ready;

  // output slot is "free" this cycle if empty or being consumed
  logic out_free;
  assign out_free = ~out_valid_q | out_ready;

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      out_valid_q <= 1'b0;
      out_data_q  <= '0;
      skid_valid  <= 1'b0;
      skid_data   <= '0;
    end else begin
      // --- output register ---
      if (out_free) begin
        if (skid_valid) begin
          out_data_q  <= skid_data;   // drain backup first (preserves order)
          out_valid_q <= 1'b1;
        end else begin
          out_data_q  <= in_data;
          out_valid_q <= in_fire;     // load if a beat is arriving, else empty
        end
      end

      // --- backup (skid) slot ---
      if (in_fire & out_valid_q & ~out_ready & ~skid_valid) begin
        // output stalled+occupied and a new beat arrived -> stash it
        skid_data  <= in_data;
        skid_valid <= 1'b1;
      end else if (skid_valid & out_free) begin
        skid_valid <= 1'b0;           // backup drained into output this cycle
      end
    end
  end

endmodule
