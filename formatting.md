# Problem Formatting Guidelines

This guideline is largely based on [BOJ formatting guide.](https://stack.acmicpc.net/guide/problem)
This guideline may be **different** from the document.

- Don't use `<br>`. Use `<p>` to divide paragraphs.
- Don't use empty lines.
- Recommend using mathjax for math expressions.
- Don't change font size. Headings `<h1>` to `<h6>` is OK, only if the original document used them.
- Don't change font family. Monospaced tags `<pre>` and `<code>` is OK.
- Don't use CSS styles `margin` and `padding`
- Don't use `l` as a symbol. Use `ℓ` (mathjax `\ell`).
- Don't write listings as `1.`, or `- `. Use `<ul>` and `<ol>`.
- Use `<pre>` (block) and `<code>` (inline) for texts directly related to input and output formats.
  e.g. Don't use `Print "a"` but `Print "<code>a</code>"`.
- Don't insert whitespaces right after opening parentheses and before closing parentheses. e.g. Don't use `( 1 ≤ N )` but `(1 ≤ N)`.
- Insert a space before a parenthesis for a range of some values. e.g. Don't use `N(1 ≤ N ≤ 100)` but `N (1 ≤ N ≤ 100)`.
- Use proper digit group separators. If the number has four digits, you don't need to use them. From five digits, you must use them. Over eleven digits, consider exponential notation. As to what character to use, refer to the following rules.

## If you use HTML math expression

- Don't use symbols like `<=`, `>=`, `*`, `!=`, etc.
  Use mathematical symbols like `≤`, `≥`, `×`, `≠`, etc. [Refer to Unicode Table.](#unicode-table)
- Use digit group separator `,`. Don't use `1 000 000` or `1.000.000` but `1,000,000`.
- Don't use `^` and `_` for superscript and subscript, respectively. Use `<sup>` and `<sub>`. e.g. Don't use `10^3` but `10<sup>3</sup>`.
- Insert whitespaces before and after mathematical symbols. e.g. Don't use `a+b` but `a + b`.

## If you use mathjax

- Use digit group separator `\,`. Don't use `1 000 000`, `1.000.000`, or `1,000,000` but `1\,000\,000`.
- Don't include parentheses for a range of some values in mathjax. e.g. Don't use `$N (1 \le N \le 100)$` but `$N$ ($1 \le N \le 100$)`.

## Unicode Table

|              Do               |  Don't   |
| :---------------------------: | :------: |
|       &minus; `&minus;`       |   `-`    |
|       &times; `&times;`       | `*`, `x` |
|    &setminus; `&setminus;`    |   `\`    |
| &mldr; `&hellip;` or `&mldr;` |  `...`   |
|          &le; `&le;`          |   `<=`   |
|          &ge; `&ge;`          |   `>=`   |
|          &ne; `&ne;`          |   `!=`   |
|  &rightarrow; `&rightarrow;`  |   `->`   |
|  &Rightarrow; `&Rightarrow;`  |   `=>`   |
|   &leftarrow; `&leftarrow;`   |   `<-`   |
|   &Leftarrow; `&Leftarrow;`   |   `<=`   |
|       &equiv; `&equiv;`       |  `===`   |
|         &sim; `&sim;`         |   `~`    |
|      &colone; `&colone;`      |   `:=`   |
|         &and; `&and;`         |   `&&`   |
|          &or; `&or;`          |  `\|\|`  |
|         &not; `&not;`         | `!`, `~` |
|         &cap; `&cap;`         |          |
|         &cup; `&cup;`         |          |
|       &empty; `&empty;`       |   `0`    |
|         &deg; `&deg;`         |   `°`    |