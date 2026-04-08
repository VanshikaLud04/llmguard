from .sqlite import SQLiteStorage as Storage
# Swap this out for RedisStorage when moving to production
__all__ = ["Storage"]