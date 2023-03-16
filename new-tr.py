from requests import get
from argparse import ArgumentParser
from os import makedirs
from json import dump, load
parser = ArgumentParser(description="Generates a new translation document.")
parser.add_argument('id')
parser.add_argument('language')
parser.add_argument('author')
args = parser.parse_args()
try:
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = get(f'https://www.acmicpc.net/problem/{args.id}', headers=headers)
    text = req.text
    begin = '<div id="problem-body" class="">'
    end = '\t' * 17 + '<div class="col-md-12">'
    text = text[text.index(begin) + len(begin):]
    text = text[:text.index(end)]
    directory = f'src/{args.id}'
    filename = f'{args.language}-{args.author}.html'
    makedirs(directory, exist_ok=True)
    with open(f'{directory}/{filename}', 'w+t') as f:
        f.write(text.strip())
    print(f'Generated {directory}/{filename}.')
    index = load(open('index', 'rt'))
    key = str(args.id)
    if key not in index:
        index[key] = []
    index[key].append(f'{args.language}-{args.author}')
    dump(index, open('index', 'wt'), indent=2, sort_keys=True)
    print('Saved index.')
except Exception as e:
    print("Error:", e)
