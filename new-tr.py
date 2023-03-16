from requests import get
from argparse import ArgumentParser
from json import dump, load
import re
import os
parser = ArgumentParser(description="Generates a new translation document.")
parser.add_argument('id')
parser.add_argument('language')
parser.add_argument('author')
args = parser.parse_args()


def find_tag_end(s):
    t = 0
    for i, c in enumerate(s):
        if s[i] == '<' and s[i+1] == '/':
            if t == 0:
                return s[:i], s[i:]
            t -= 1
        elif s[i] == '<':
            t += 1
    raise AssertionError("unreachable")


regex = re.compile(r'<section\s+id="(\w+)"\s+class="problem-section">')
try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = get(f'https://www.acmicpc.net/problem/{args.id}', headers=headers)
    text = req.text
    match = None
    sections = {}
    while (match := regex.search(text)):
        elem_id = match.group(1)
        content, text = find_tag_end(text[match.end(0):])
        sections[elem_id] = content
    directory = f'src/{args.id}'
    realname = f'{args.language}-{args.author}'
    filename = f'{realname}.html'
    os.makedirs(directory, exist_ok=True)
    if os.access(f'{directory}/{filename}', os.F_OK):
        print(repr(filename), 'already exists.')
        exit(1)
    dump(sections, open(f'{directory}/{filename}',
         'w+t'), indent=2, sort_keys=False, ensure_ascii=False)
    print(f'Generated {directory}/{filename}.')
    index = load(open('index', 'rt'))
    key = str(args.id)
    if key not in index:
        index[key] = []
    if realname not in index[key]:
        index[key].append(realname)
        dump(index, open('index', 'wt'), indent=2, sort_keys=True)
    print('Saved index.')
except Exception as e:
    print("Error:", e)
