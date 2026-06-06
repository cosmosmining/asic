// -----------------------------------------------------------------------------
// reset_sync.sv  -- reset synchronizer (async assert / sync de-assert)
//
// function   : produce a clean active-low reset for a clock domain.  The raw
//              asynchronous reset asserts the output immediately (no clock
//              required) and de-asserts it synchronized to `clk`, so downstream
//              flops never see a recovery/removal-time violation.
// parameters : STAGES - synchronizer depth (>=2; default 2)
// latency    : de-assertion appears after STAGES `clk` edges.
// interfaces : arst_n (raw async reset) -> rst_n (clk-domain reset)
// -----------------------------------------------------------------------------
module reset_sync #(
  parameter int STAGES = 2
) (
  input  logic clk,
  input  logic arst_n,   // raw asynchronous active-low reset
  output logic rst_n     // synchronized active-low reset for `clk`
);
  initial begin
    if (STAGES < 2)
      $error("reset_sync: STAGES must be >= 2 (got %0d)", STAGES);
  end

  logic [STAGES-1:0] sync_q;

  always_ff @(posedge clk or negedge arst_n) begin
    if (!arst_n) sync_q <= '0;                       // async assert
    else         sync_q <= {sync_q[STAGES-2:0], 1'b1}; // sync de-assert
  end

  assign rst_n = sync_q[STAGES-1];

endmodule
