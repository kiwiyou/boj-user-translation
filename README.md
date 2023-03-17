# boj-user-translation

User translation repository for Baekjoon Online Judge.

## How to Contribute

Requires git and python 3.

Fork and clone the repository, and type the following commands
inside the repository directory.

```bash
python3 new-tr.py <problem-id> <language-code> <username>
```

- `<language-code>` should be a valid [IETF language tag](https://www.wikiwand.com/en/IETF_language_tag), with `-` replaced by `_` (as in `ko_KR`).

A file will be generated as `src/<problem-id>/<language-code>-<username>.json`.
You can translate the file and send a pull request.
