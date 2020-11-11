class CacheManager:
    def has_key(self, key: str) -> bool:
        raise NotImplementedError

    def add_key(self, key: str):
        raise NotImplementedError

    def clear_cache(self):
        raise NotImplementedError


class LocalTestCacheManager(CacheManager):
    keystore = set()

    def has_key(self, key: str) -> bool:
        return key in self.keystore

    def add_key(self, key: str):
        self.keystore.add(key)

    def clear_cache(self):
        self.keystore.clear()
