import json
from collections import defaultdict

class MapReduce:

    def __init__(self):
        self.intermediate = defaultdict(list)
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value)

    def execute(self, data, mapper, reducer):
        for line in data:
            record = json.loads(line)
            mapper(record)

        for key, data in self.intermediate.items():
            reducer(key, data)

        #jenc = json.JSONEncoder(encoding='latin-1')
        jenc = json.JSONEncoder()
        for item in self.result:
            print jenc.encode(item)
