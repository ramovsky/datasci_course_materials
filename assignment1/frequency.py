import sys
import json
from collections import Counter


def main():
    c = Counter()
    with open(sys.argv[1]) as f:
        for line in f:
            data = json.loads(line)
            c += Counter(data.get('text', '').split())

    sums = sum(c.values()) or 1

    for word, score in c.items():
        print(u'{} {}'.format(word, float(score)/sums))


if __name__ == '__main__':
    main()
