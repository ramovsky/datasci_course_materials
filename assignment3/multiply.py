import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    mat, i, j, val = record
    if mat == 'a':
        for k in range(5):
            mr.emit_intermediate((i, k), record)
    else:
        for k in range(5):
            mr.emit_intermediate((k, j), record)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a = {j: v for m, i, j, v in list_of_values if m=='a'}
    b = {i: v for m, i, j, v in list_of_values if m=='b'}
    val = sum(v*b.get(k, 0) for k, v in a.items()),
    mr.emit(key+val)

# Part 4
with open(sys.argv[1]) as f:
    mr.execute(f, mapper, reducer)
