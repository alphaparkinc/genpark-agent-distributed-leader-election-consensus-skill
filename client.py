"""Distributed Leader Election Consensus Engine.
100% Python Standard Library.
"""

import time
from typing import Dict, Any, Optional

class DistributedLeaderElectionConsensus:
    """Maintains a single active leader lease preventing split-brain decision conflicts."""
    def __init__(self, lease_duration_sec: float = 3.0):
        self.lease_duration = lease_duration_sec
        self.current_leader: Optional[str] = None
        self.lease_expires_at: float = 0.0

    def campaign(self, candidate_id: str) -> Dict[str, Any]:
        now = time.time()
        if self.current_leader is None or now >= self.lease_expires_at or self.current_leader == candidate_id:
            self.current_leader = candidate_id
            self.lease_expires_at = now + self.lease_duration
            return {
                "role": "LEADER",
                "candidate_id": candidate_id,
                "lease_remaining_sec": self.lease_duration
            }
        else:
            return {
                "role": "FOLLOWER",
                "candidate_id": candidate_id,
                "current_leader": self.current_leader,
                "lease_remaining_sec": max(0.0, round(self.lease_expires_at - now, 2))
            }
