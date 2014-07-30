import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    person, friend = record
    if person < friend:
        mr.emit_intermediate((person, friend), 1)
    else:
        mr.emit_intermediate((friend, person), -1)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if sum(list_of_values):
        f, s = key
        mr.emit((f, s))
        mr.emit((s, f))

# Part 4
with open(sys.argv[1]) as f:
    mr.execute(f, mapper, reducer)
