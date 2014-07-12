import sys
import json


def main():
    with open(sys.argv[1]) as f:
        sents = {}
        for line in f:
            word, score = line.split('\t')
            sents[word] = int(score)

    with open(sys.argv[2]) as f:
        for line in f:
            data = json.loads(line)
            text = data.get('text', '')
            score = sum(sents.get(w, 0) for w in text.split())
            print(score)


if __name__ == '__main__':
    main()
