import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    key, value = record
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key, list(set(list_of_values))))

# Part 4
with open(sys.argv[1]) as f:
    mr.execute(f, mapper, reducer)
