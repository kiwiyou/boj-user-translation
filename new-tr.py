from http.client import HTTPSConnection
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
        elif s[i] == '<' and s[i+1] == 'i' and s[i+2] == 'm' and s[i+3] == 'g':
            pass
        elif s[i] == '<':
            t += 1
    raise AssertionError("unreachable")


regex = re.compile(r'<section\s+id="(\w+)"\s+class="problem-section">')
meaningless = re.compile(r'[\n\r\t]+(<|$)')
try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = HTTPSConnection('www.acmicpc.net')
    req.request('GET', f'/problem/{args.id}', headers=headers)
    res = req.getresponse()
    text = res.read().decode()
    title_index = text.index('"problem_title"')
    title, _, text = text[title_index+16:].partition("</span>")
    match = None
    sections = {"title": title}
    while (match := regex.search(text)):
        elem_id = match.group(1)
        content, text = find_tag_end(text[match.end(0):])
        sections[elem_id] = re.sub(
            meaningless, lambda match: f' {match.group(1)}', content)
    directory = f'src/{args.id}'
    realname = f'{args.language}-{args.author}'
    filename = f'{realname}.json'
    os.makedirs(directory, exist_ok=True)
    if os.access(f'{directory}/{filename}', os.F_OK):
        print(repr(filename), 'already exists.')
        exit(1)
    dump(sections, open(f'{directory}/{filename}',
         'w+t', encoding='utf-8'), indent=2, sort_keys=False, ensure_ascii=False)
    print(f'Generated {directory}/{filename}.')
    index = load(open('index', 'rt', encoding='utf-8'))
    key = str(args.id)
    if key not in index:
        index[key] = []
    if realname not in index[key]:
        index[key].append(realname)
        dump(index, open('index', 'wt', encoding='utf-8'), indent=2, sort_keys=True)
    print('Saved index.')
except Exception as e:
    print("Error:", e)
