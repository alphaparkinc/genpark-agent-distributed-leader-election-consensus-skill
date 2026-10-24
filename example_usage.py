from client import DistributedLeaderElectionConsensus

arbiter = DistributedLeaderElectionConsensus(lease_duration_sec=2.0)
agent_a = arbiter.campaign("node_us_east_1")
agent_b = arbiter.campaign("node_eu_west_1")

print("=== Leader Election Telemetry ===")
print("Agent A Role:", agent_a["role"])
print("Agent B Role:", agent_b["role"], f"(Leader is: {agent_b.get('current_leader')})")
