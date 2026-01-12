import httpx
import asyncio
from ..core.semantic_schema import DelegationVector

# Configuration of remote endpoints
REMOTE_SHARD_ENDPOINT = "http://localhost:8000"

async def dispatch_intent(value: float):
    """
    Asynchronously negotiates with the remote shard to execute a logic packet.
    """
    transport_client = httpx.AsyncClient()
    
    # Constructing the work packet
    vector = DelegationVector(
        task_id="vec-9921",
        intent_classification="arithmetic_operation",
        payload_context={"a": value}
    )
    
    print(f"[*] Transmitting intent vector to {REMOTE_SHARD_ENDPOINT}...")
    
    try:
        response = await transport_client.post(
            f"{REMOTE_SHARD_ENDPOINT}/execute", 
            json=vector.dict()
        )
        
        if response.status_code == 200:
            artifact = response.json()
            print(f"[+] Artifact received: {artifact['result_data']}")
        else:
            print(f"[-] Signal rejection: {response.text}")
            
    except Exception as transport_err:
        print(f"[!] Transport Layer Exception: {transport_err}")
    finally:
        await transport_client.aclose()

if __name__ == "__main__":
    # Execution entry point
    asyncio.run(dispatch_intent(3.14159))
