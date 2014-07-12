import sys
import json
from collections import Counter


def main():
    c = Counter()
    with open(sys.argv[1]) as f:
        for line in f:
            data = json.loads(line)
            try:
                tags = data['entities']['hashtags']
                for obj in tags:
                    c += Counter({obj['text']: 1})
            except KeyError:
                pass

    for i, tag in enumerate(sorted(c, key=c.get, reverse=True)):
        print(u'{} {}'.format(tag, c[tag]))
        if i >= 9:
            break


if __name__ == '__main__':
    main()
