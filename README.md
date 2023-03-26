<div align="center">
    <h1>boj-user-translation</h1>
    <p>English / <a href="https://github.com/kiwiyou/boj-user-translation/blob/main/README-ko.md">한국어</a></p>
</div>

User translation repository for Baekjoon Online Judge.

To view translations on the problem page, see [o-ey.](https://github.com/kiwiyou/o-ey)

## How to Contribute

Requires git and python 3.

Fork and clone the repository, and type the following commands
inside the repository directory.

```bash
python3 new-tr.py <problem-id> <language-code> <username>
```

- `<language-code>` should be a valid [IETF language tag](https://www.wikiwand.com/en/IETF_language_tag), with `-` replaced by `_` (as in `en_US`, `ko_KR`).

A file will be generated as `src/<problem-id>/<language-code>-<username>.html`,
and The file `index` will be updated accordingly.

You can translate the generated file, push to your repository, and send a pull request.

## Translation Rules

- No new sections can be used now.
- **No XSS (or any malicious HTML injection) is allowed.**
- You can rearrange paragraphs, rewrite sentences, or change character names **if you keep the shown and unshown.**
- If the problem has defects that should be resolved, you can warn in translation but please **write together that the warning is inserted by the translator.**
- Regarding formats, please refer to [formatting guide.](https://github.com/kiwiyou/boj-user-translation/blob/main/formatting.md)
- Under constraints above, translate freely.
- For languages not in my fluent zone, approval for pull requests can be delayed.
