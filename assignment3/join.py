import sys
from MapReduce import MapReduce

mr = MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    mr.emit_intermediate(record[1], record)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    orders = [r for r in list_of_values if r[0]=='order']
    items = [r for r in list_of_values if r[0]=='line_item']
    for o in orders:
        for i in items:
            mr.emit(o+i)

# Part 4
with open(sys.argv[1]) as f:
    mr.execute(f, mapper, reducer)
