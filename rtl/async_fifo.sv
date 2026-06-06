// -----------------------------------------------------------------------------
// async_fifo.sv  -- dual-clock FIFO with Gray-coded pointers
//
// function   : safely move a data word from the `wclk` domain to the `rclk`
//              domain.  Write/read pointers are (AW+1) bits, Gray-encoded so
//              that exactly one bit changes per step; each pointer is passed to
//              the opposite domain through a 2-FF synchronizer (cdc_sync_2ff).
//              full/empty are registered.  This is the only data-CDC mechanism
//              in the fabric.
// parameters : WIDTH - data width
//              DEPTH - entries (power of 2, >= 4)
// latency    : >= 2 destination cycles (synchronizer) + FIFO occupancy.
// throughput : 1 word/cycle on each side when not full/empty.
// interfaces : write side {wclk,wrst_n,wpush,wdata,wfull};
//              read  side {rclk,rrst_n,rpop,rdata,rempty}.
// reset      : per-domain async-assert/sync-deassert resets; FIFO comes up empty.
// -----------------------------------------------------------------------------
module async_fifo #(
  parameter int WIDTH = 32,
  parameter int DEPTH = 8
) (
  // write domain
  input  logic             wclk,
  input  logic             wrst_n,
  input  logic             wpush,
  input  logic [WIDTH-1:0] wdata,
  output logic             wfull,
  // read domain
  input  logic             rclk,
  input  logic             rrst_n,
  input  logic             rpop,
  output logic [WIDTH-1:0] rdata,
  output logic             rempty
);
  localparam int AW = $clog2(DEPTH);

  initial begin
    if ((DEPTH & (DEPTH-1)) != 0)
      $error("async_fifo: DEPTH must be a power of 2 (got %0d)", DEPTH);
    if (DEPTH < 4)
      $error("async_fifo: DEPTH must be >= 4 (got %0d)", DEPTH);
  end

  logic [WIDTH-1:0] mem [DEPTH];

  logic [AW:0] wbin, wgray, wbin_nxt, wgray_nxt;
  logic [AW:0] rbin, rgray, rbin_nxt, rgray_nxt;
  logic [AW:0] wgray_s; // write-gray synchronized into read domain
  logic [AW:0] rgray_s; // read-gray  synchronized into write domain
  logic        wfull_r, rempty_r;

  // -------------------- write domain --------------------
  assign wbin_nxt  = wbin + {{AW{1'b0}}, (wpush & ~wfull_r)};
  assign wgray_nxt = wbin_nxt ^ (wbin_nxt >> 1);

  always_ff @(posedge wclk or negedge wrst_n) begin
    if (!wrst_n) begin wbin <= '0; wgray <= '0; end
    else         begin wbin <= wbin_nxt; wgray <= wgray_nxt; end
  end

  always_ff @(posedge wclk) begin
    if (wpush & ~wfull_r) mem[wbin[AW-1:0]] <= wdata;
  end

  // full when the next write pointer would catch the (synced) read pointer,
  // i.e. equal with the top two Gray bits inverted.
  logic wfull_val;
  assign wfull_val = (wgray_nxt == {~rgray_s[AW:AW-1], rgray_s[AW-2:0]});
  always_ff @(posedge wclk or negedge wrst_n) begin
    if (!wrst_n) wfull_r <= 1'b0;
    else         wfull_r <= wfull_val;
  end
  assign wfull = wfull_r;

  // -------------------- read domain --------------------
  assign rbin_nxt  = rbin + {{AW{1'b0}}, (rpop & ~rempty_r)};
  assign rgray_nxt = rbin_nxt ^ (rbin_nxt >> 1);

  always_ff @(posedge rclk or negedge rrst_n) begin
    if (!rrst_n) begin rbin <= '0; rgray <= '0; end
    else         begin rbin <= rbin_nxt; rgray <= rgray_nxt; end
  end

  assign rdata = mem[rbin[AW-1:0]];

  // empty when the next read pointer equals the (synced) write pointer.
  logic rempty_val;
  assign rempty_val = (rgray_nxt == wgray_s);
  always_ff @(posedge rclk or negedge rrst_n) begin
    if (!rrst_n) rempty_r <= 1'b1;
    else         rempty_r <= rempty_val;
  end
  assign rempty = rempty_r;

  // -------------------- pointer synchronizers --------------------
  cdc_sync_2ff #(.WIDTH(AW+1)) u_w2r (
    .clk(rclk), .rst_n(rrst_n), .d_async(wgray), .q_sync(wgray_s));
  cdc_sync_2ff #(.WIDTH(AW+1)) u_r2w (
    .clk(wclk), .rst_n(wrst_n), .d_async(rgray), .q_sync(rgray_s));

endmodule
