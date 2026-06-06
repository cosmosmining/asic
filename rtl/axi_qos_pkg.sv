// -----------------------------------------------------------------------------
// axi_qos_pkg.sv  -- shared constants/types for the axi-qos-fabric
//
// function   : common AXI response codes and arbiter-policy encodings used
//              across the fabric.  No state, no logic.
// parameters : none (pure package).
// interfaces : imported via `import axi_qos_pkg::*;`
// -----------------------------------------------------------------------------
package axi_qos_pkg;

  // AXI4 xRESP encodings (AMBA IHI0022)
  localparam logic [1:0] RESP_OKAY   = 2'b00;
  localparam logic [1:0] RESP_SLVERR = 2'b10;
  localparam logic [1:0] RESP_DECERR = 2'b11;

  // qos_arbiter policy encodings (also mirrored in csr_apb ARB_POLICY)
  localparam logic [1:0] POLICY_FIXED = 2'd0; // lowest index wins
  localparam logic [1:0] POLICY_RR    = 2'd1; // round-robin
  localparam logic [1:0] POLICY_WRR   = 2'd2; // weighted round-robin (QoS)

endpackage
