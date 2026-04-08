from abc import ABC, abstractmethod
class BaseStorage(ABC):
    @abstractmethod
    def save(self, record: dict) -> None: pass
    @abstractmethod
    def get_recent(self, user_id: str, window_seconds: int = 60) -> list[tuple]: pass
    @abstractmethod
    def get_total_today(self, user_id: str) -> float: pass
    @abstractmethod
    def get_history(self, user_id: str, limit: int = 100) -> list[tuple]: pass