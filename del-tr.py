from argparse import ArgumentParser
from json import dump, load
import os
parser = ArgumentParser(description="Deletes a translation document.")
parser.add_argument('id')
parser.add_argument('language')
parser.add_argument('author')
args = parser.parse_args()

try:
    directory = f'src/{args.id}'
    realname = f'{args.language}-{args.author}'
    filename = f'{realname}.html'
    if os.access(f'{directory}/{filename}', os.F_OK):
        os.remove(f'{directory}/{filename}')
        print(f'Removed {directory}/{filename}.')
    index = load(open('index', 'rt', encoding='utf-8'))
    key = str(args.id)
    if key in index:
        index[key].remove(realname)
        if not index[key]:
            del index[key]
        dump(index, open('index', 'wt', encoding='utf-8'), indent=2, sort_keys=True)
    print('Saved index.')
except Exception as e:
    print("Error:", e)
