// -----------------------------------------------------------------------------
// cdc_sync_2ff.sv  -- multi-stage flip-flop synchronizer
//
// function   : metastability-hardening synchronizer for crossing a *stable*
//              value (single-bit level or a Gray-coded bus, where at most one
//              bit changes per step) into the `clk` domain.  This is the only
//              sanctioned CDC primitive in the fabric.
// parameters : WIDTH  - bits to synchronize
//              STAGES - number of FF stages (>=2; default 2)
// latency    : STAGES `clk` cycles.
// throughput : combinational pass-through of a slowly-changing value.
// interfaces : d_async (source domain) -> q_sync (clk domain)
// reset      : async assert, sync via the supplied (already-synchronized) rst_n.
// -----------------------------------------------------------------------------
module cdc_sync_2ff #(
  parameter int WIDTH  = 1,
  parameter int STAGES = 2
) (
  input  logic             clk,
  input  logic             rst_n,
  input  logic [WIDTH-1:0] d_async,
  output logic [WIDTH-1:0] q_sync
);
  // verilator lint_off LITENDIAN
  initial begin
    if (STAGES < 2)
      $error("cdc_sync_2ff: STAGES must be >= 2 (got %0d)", STAGES);
  end
  // verilator lint_on LITENDIAN

  logic [WIDTH-1:0] sync_q [STAGES];

  always_ff @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
      for (int i = 0; i < STAGES; i++) sync_q[i] <= '0;
    end else begin
      sync_q[0] <= d_async;
      for (int i = 1; i < STAGES; i++) sync_q[i] <= sync_q[i-1];
    end
  end

  assign q_sync = sync_q[STAGES-1];

endmodule
