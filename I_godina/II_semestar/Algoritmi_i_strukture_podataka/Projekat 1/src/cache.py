import os
import json
from src.get_path import get_relative_path

class Cache:
    def __init__(self, filename):
        self.cache = {}
        self.filename = filename

    def get(self, key):
        return self.cache.get(key, None)

    def put(self, key, value):
        if key not in self.cache:
            self.cache[key] = value

    def clear(self):
        self.cache.clear()

    def load(self):
        try:
            with open(get_relative_path(["cache", self.filename]), 'r') as file:
                text = file.read()
                if text == "":
                    return
                self.cache = json.loads(text)
        except:
            print("Unable to load cache")

    def save(self):
        with open(get_relative_path(["cache", self.filename]), 'w') as file:
            file.write(json.dumps(self.cache))

class CacheRecord:
    def __init__(self, moves = None, heuristic = None):
        self.moves = moves
        self.heuristic = heuristic


scores = Cache("scores.json")
moves = Cache("moves.json")