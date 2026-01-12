from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class CognitiveManifest(BaseModel):
    """
    Defines the capability surface area of a specific node.
    Functionally equivalent to a service discovery record.
    """
    node_id: str = Field(..., description="Unique identifier for the runtime instance.")
    heuristic_capabilities: list[str] = Field(default_factory=list, description="List of executable logic vectors this node supports.")

class DelegationVector(BaseModel):
    """
    Represents a unit of work to be executed by a remote shard.
    Encapsulates the intent and necessary context.
    """
    task_id: str
    intent_classification: str
    payload_context: Dict[str, Any]
    
class ExecutionArtifact(BaseModel):
    """
    The structured output resulting from a node's processing cycle.
    """
    status_code: int
    result_data: Dict[str, Any]
    latency_ms: Optional[float] = None
