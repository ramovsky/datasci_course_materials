import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    person, friend = record
    mr.emit_intermediate(person, friend)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key, len(list_of_values)))

# Part 4
with open(sys.argv[1]) as f:
    mr.execute(f, mapper, reducer)
