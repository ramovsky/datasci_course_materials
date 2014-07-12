import sys
import json
from collections import defaultdict

STATES = {
    'ALASKA': 'AK',
    'ALABAMA': 'AL',
    'AMERICAN SAMOA': 'AS',
    'ARIZONA': 'AZ',
    'ARKANSAS': 'AR',
    'CALIFORNIA': 'CA',
    'COLORADO': 'CO',
    'CONNECTICUT': 'CT',
    'DELAWARE': 'DE',
    'DISTRICT OF COLUMBIA': 'DC',
    'FLORIDA': 'FL',
    'GEORGIA': 'GA',
    'GUAM': 'GU',
    'HAWAII': 'HI',
    'IDAHO': 'ID',
    'ILLINOIS': 'IL',
    'INDIANA': 'IN',
    'IOWA': 'IA',
    'KANSAS': 'KS',
    'KENTUCKY': 'KY',
    'LOUISIANA': 'LA',
    'MAINE': 'ME',
    'MARYLAND': 'MD',
    'MASSACHUSETTS': 'MA',
    'MICHIGAN': 'MI',
    'MINNESOTA': 'MN',
    'MISSISSIPPI': 'MS',
    'MISSOURI': 'MO',
    'MONTANA': 'MT',
    'NATIONAL': 'NA',
    'NEBRASKA': 'NE',
    'NEVADA': 'NV',
    'NEW HAMPSHIRE': 'NH',
    'NEW JERSEY': 'NJ',
    'NEW MEXICO': 'NM',
    'NEW YORK': 'NY',
    'NORTH CAROLINA': 'NC',
    'NORTH DAKOTA': 'ND',
    'NORTHERN MARIANA ISLANDS': 'MP',
    'OHIO': 'OH',
    'OKLAHOMA': 'OK',
    'OREGON': 'OR',
    'PENNSYLVANIA': 'PA',
    'PUERTO RICO': 'PR',
    'RHODE ISLAND': 'RI',
    'SOUTH CAROLINA': 'SC',
    'SOUTH DAKOTA': 'SD',
    'TENNESSEE': 'TN',
    'TEXAS': 'TX',
    'UTAH': 'UT',
    'VERMONT': 'VT',
    'VIRGIN ISLANDS': 'VI',
    'VIRGINIA': 'VA',
    'WASHINGTON': 'WA',
    'WEST VIRGINIA': 'WV',
    'WISCONSIN': 'WI',
    'WYOMING': 'WY'
    }


def get_state(data):
    place = data.get('place')
    state = ''

    if place:
        if place.get('country_code') != u'US':
            return

        city, state = place['full_name'].split(',')

    else:
        try:
            city, state = data['user']['location'].split(',')
        except:
            pass

    state = state.strip().upper()

    if state in STATES:
        return STATES[state]

    elif state in STATES.values():
        return state


def main():
    with open(sys.argv[1]) as f:
        sents = {}
        for line in f:
            word, score = line.split('\t')
            sents[word] = int(score)

    counter = defaultdict(list)
    with open(sys.argv[2]) as f:
        for line in f:
            data = json.loads(line)
            state = get_state(data)
            if state is None:
                continue

            text = data.get('text', '')
            scores = [sents[w] for w in text.split() if w in sents] or [0]
            counter[state] += scores

    counter = {k: float(sum(v))/len(v) for k, v in counter.items()}
    l = sorted(counter, key=counter.get, reverse=True)
    print(l[0])


if __name__ == '__main__':
    main()
