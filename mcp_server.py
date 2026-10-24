import sys
import json
from client import DistributedLeaderElectionConsensus

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "campaign_leadership",
                        "description": "Attempts to acquire or renew primary leader lease for a candidate node.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "candidate_id": {"type": "string"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        arbiter = DistributedLeaderElectionConsensus()
        res = arbiter.campaign(args.get("candidate_id", "node_1"))
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    arbiter = DistributedLeaderElectionConsensus()
    print(json.dumps(arbiter.campaign("local_agent"), indent=2))

if __name__ == "__main__":
    main()
