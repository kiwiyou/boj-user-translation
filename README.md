<div align="center">
    <h1>boj-user-translation</h1>
    <p>English / <a href="https://github.com/kiwiyou/boj-user-translation/blob/main/README-ko.md">한국어</a></p>
</div>

User translation repository for Baekjoon Online Judge.
To view translations on the problem page, see [o-ey.](https://github.com/kiwiyou/o-ey)

## How to Contribute

Requires git and python 3.

### Setting Up Environment

Fork and clone the repository, and type the following command to move to the repository directory.

```bash
cd <location of cloned repository>
```

### Adding a Translation

Move to the your repository directory, and type the following command to create new translation files.

```bash
python3 new-tr.py <problem-id> <language-code> <username>
```

- `<language-code>` should be a valid [IETF language tag](https://www.wikiwand.com/en/IETF_language_tag), with `-` replaced by `_` (as in `en_US`, `ko_KR`).

A file will be generated as `src/<problem-id>/<language-code>-<username>.html`,
and The file `index` will be updated accordingly.
After translating the content of generated file, type the following command
to upload your translation to GitHub.

```bash
git add .
git commit -m "작업 내용"
git push
```

### Testing Your Translation

Click the button of `o-ey` extension, and enter the URL of your translation repository.
Uploaded change will be applied in a few minutes, which you can view on BOJ.

### Creating a Pull Request

Create a Pull Request from your forked repository into the base repository.
The maintainer will soon review your request and merge it.

## Translation Rules

- No new sections can be used now.
- **No XSS (or any malicious HTML injection) is allowed.**
- You can rearrange paragraphs, rewrite sentences, or change character names
  **if you follow the problemsetter's intention.**
- If the problem has defects that should be resolved, you can warn in translation
  but please **write together that the warning is inserted by the translator.**
- Regarding formats, please refer to [formatting guide.](https://github.com/kiwiyou/boj-user-translation/blob/main/formatting.md)
- Under constraints above, translate freely.
- For languages not in my fluent zone, approval for pull requests can be delayed.
- Before sending pull requests, please review the local changes via `o-ey`.
  You can see the local changes by adding your repository to the repository list of `o-ey`.
