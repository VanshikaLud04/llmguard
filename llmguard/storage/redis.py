
from .base import BaseStorage

class RedisStorage(BaseStorage):
    def __init__(self, redis_url: str = "redis://localhost:6379/0"):
        self.redis_url = redis_url
       
        print("Redis storage initialized (Template)")

    def save(self, record: dict) -> None:
        pass 

    def get_recent(self, user_id: str, window_seconds: int = 60) -> list[tuple]:
        return []

    def get_total_today(self, user_id: str) -> float:
        return 0.0 
    def get_history(self, user_id: str, limit: int = 100) -> list[tuple]:
        return []