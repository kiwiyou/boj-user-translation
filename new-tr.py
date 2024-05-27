from http.client import HTTPSConnection
from argparse import ArgumentParser
from json import dump, load, loads
from ssl import SSLContext, PROTOCOL_TLS_CLIENT, VerifyMode
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
        if s[i] == '<':
            if s[i+1] == '/':
                if t == 0:
                    return s[:i], s[i:]
                t -= 1
            elif s[i+1] == 'i' and s[i+2] == 'm' and s[i+3] == 'g':
                pass
            elif s[i+1] == 'b' and s[i+2] == 'r':
                pass
            else:
                t += 1
    raise AssertionError("unreachable")


is_multilingual_typo = args.author == "typo" and args.language != "Original"
regex = re.compile(r'<section\s+id="(\w+)"\s+class="problem-section">')
try:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'}
    context = SSLContext(PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = VerifyMode.CERT_NONE
    req = HTTPSConnection('www.acmicpc.net', context=context)
    req.request('GET', f'/problem/{args.id}', headers=headers)
    res = req.getresponse()
    text = res.read().decode()
    if is_multilingual_typo:
        from base64 import b64decode
        lang_index = text.index('"problem-lang-base64"')
        lang_base64, _, _ = text[lang_index+22:].partition("</div>")
        lang = {trans["problem_lang_tcode"]: trans for trans in loads(b64decode(lang_base64))}[args.language]
    title_index = text.index('"problem_title"')
    title, _, text = text[title_index+16:].partition("</span>")
    if is_multilingual_typo:
        title = lang["title"]
    match = None
    sections = [{"id": "title", "content": title}]
    while (match := regex.search(text)):
        elem_id = match.group(1)
        content, text = find_tag_end(text[match.end(0):])
        if is_multilingual_typo and elem_id in lang:
            text_index = content.index('"problem-text"')
            pre = content[:text_index+15]
            post = content[text_index+15:]
            post = post[post.rfind("</div>"):]
            content = pre + lang[elem_id] + post
        sections.append({"id": elem_id, "content": content})
    directory = f'src/{args.id}'
    realname = f'{args.language}-{args.author}'
    filename = f'{realname}.html'
    os.makedirs(directory, exist_ok=True)
    if os.access(f'{directory}/{filename}', os.F_OK):
        print(repr(filename), 'already exists.')
        exit(1)
    with open(f'{directory}/{filename}', 'wt', encoding='utf-8') as f:
        f.writelines(
            f"<section id=\"{section['id']}\">{section['content']}</section>\n" for section in sections)
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
