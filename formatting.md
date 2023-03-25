# Problem Formatting Guidelines

This guideline is largely based on [BOJ formatting guide.](https://stack.acmicpc.net/guide/problem)

- Don't use `<br>`. Use `<p>` to divide paragraphs.
- Don't use empty lines.
- Don't change font size. Headings `<h1>` to `<h6>` is OK, only if the original document used them.
- Don't change font family. Monospaced tags `<pre>` and `<code>` is OK.
- Don't use CSS styles `margin` and `padding`
- Don't use `^` and `_` for superscript and subscript, respectively. Use `<sup>` and `<sub>`. e.g. Don't use `10^3` but `10<sup>3</sup>`.
- Don't use `l` as a symbol. Use `ℓ` (LaTeX `\ell`).
- Don't write listings as `1.`, or `- `. Use `<ul>` and `<ol>`.
- Use `<pre>` (block) and `<code>` (inline) for texts directly related to input and output formats.
  e.g. Don't use `Print "a"` but `Print "<code>a</code>"`.
- Don't insert whitespaces right after opening parentheses and before closing parentheses. e.g. Don't use `( 1 ≤ N )` but `(1 ≤ N)`.
- **If you don't use LaTeX,** insert whitespaces before and after mathematical symbols. e.g. Don't use `a+b` but `a + b`.
- Don't use symbols like `<=`, `>=`, `*`, `!=`, etc. Use mathematical symbols like `≤` (LaTeX `\le`), `≥` (LaTeX `\ge`), `×` (LaTeX `\times`), and `≠` (LaTeX `\ne`), etc.
- Use digit group separator, depending on your target language. On LaTeX, you can use `\,` as a digit separator.
  e.g. Don't use `1000000` or `1 000 000` but `1,000,000`, `1.000.000`, or `$1\,000\,000$` (depending on your target language).
