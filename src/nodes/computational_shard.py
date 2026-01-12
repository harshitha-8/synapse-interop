from fastapi import FastAPI, HTTPException
from ..core.semantic_schema import CognitiveManifest, DelegationVector, ExecutionArtifact
import math

# Initialization of the runtime environment
runtime_shard = FastAPI()

# Operational constraints
NODE_IDENTITY = "Shard-Alpha-01"
CAPABILITY_SET = ["arithmetic_operation", "logic_gate_simulation"]

@runtime_shard.get("/manifest", response_model=CognitiveManifest)
async def broadcast_identity():
    """
    Exposes the node's capabilities to the discovery layer.
    """
    return CognitiveManifest(
        node_id=NODE_IDENTITY,
        heuristic_capabilities=CAPABILITY_SET
    )

@runtime_shard.post("/execute", response_model=ExecutionArtifact)
async def process_vector(vector: DelegationVector):
    """
    Ingests a DelegationVector and applies local compute resources.
    """
    if vector.intent_classification not in CAPABILITY_SET:
        raise HTTPException(status_code=400, detail="Intent vector mismatch: Capability not resident on this shard.")
    
    # Simulation of a computational workload
    try:
        # Example logic: processing a simple arithmetic payload
        operand_a = vector.payload_context.get("a", 0)
        result = math.sin(operand_a) # Arbitrary complexity simulation
        
        return ExecutionArtifact(
            status_code=200,
            result_data={"computed_value": result, "derivation": "sine_transform"}
        )
    except Exception as e:
        return ExecutionArtifact(status_code=500, result_data={"error_trace": str(e)})

# Entry point for the ASGI server would typically be configured in pyproject.toml
