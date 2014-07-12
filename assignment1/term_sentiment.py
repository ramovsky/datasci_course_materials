import sys
import json
from collections import defaultdict


def main():
    with open(sys.argv[1]) as f:
        sents = {}
        for line in f:
            word, score = line.split('\t')
            sents[word] = int(score)

    unkonwn = defaultdict(list)
    with open(sys.argv[2]) as f:
        for line in f:
            data = json.loads(line)
            text = data.get('text', '')
            words = text.split()
            scores = [sents[w] for w in words if w in sents]
            for w in words:
                if w not in sents:
                    unkonwn[w] += scores or [0]

    for w, scores in unkonwn.items():
        print(u'{} {}'.format(w, float(sum(scores))/len(scores)))


if __name__ == '__main__':
    main()
