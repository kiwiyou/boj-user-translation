from json import load
from argparse import ArgumentParser
from os.path import splitext
parser = ArgumentParser(
    description="Transform v1 translation document into v2.")
parser.add_argument('filename', nargs="+")
args = parser.parse_args()

for filename in args.filename:
    name, ext = splitext(filename)
    if ext != ".json":
        continue
    with open(filename, 'rt') as f:
        json = load(f)
    if json:
        with open(name + ".html", 'wt') as f:
            f.writelines(
                f"<section id=\"{key}\">{json[key]}</section>\n" for key in json)
