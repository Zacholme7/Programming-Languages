# 7.10: A thread safe list class
from threading import RLock
from typing import List

class IntListThreadsafe:
    def __init__(self, wrapped_list: List[int]):
        self._lock = RLock()
        self._inner_list = wrapped_list

    def indices_of(self, to_find: int) -> List[int]:
        # lock the lock
        with self._lock:
            enumerator = enumerate(self._inner_list)
            return [index for index, value in enumerator if value == to_find]
        
    def find_and_replace(self, to_replace: int, replace_with: int) -> None:
        with self._lock:
            indicies = self.indices_of(to_replace)
            for index in indicies:
                self._inner_list[index] = replace_with

threadsafe_list = IntListThreadsafe([1, 2, 1, 2, 1])
threadsafe_list.find_and_replace(1, 2)
print(threadsafe_list._inner_list)
