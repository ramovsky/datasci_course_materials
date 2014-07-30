import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    key, seq = record
    mr.emit_intermediate(seq[:-10], 1)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit(key)

# Part 4
with open(sys.argv[1]) as f:
    mr.execute(f, mapper, reducer)
