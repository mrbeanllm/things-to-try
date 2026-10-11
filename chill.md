<div class="markdown-content prose prose-sm max-w-none min-w-0 [&amp;_p]:whitespace-pre-line coding-question-description-markdown"><p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">You are building a simplified code editor similar to VS Code. The editor stores source code as a list of lines and supports collapsing and expanding indentation-based code blocks.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">A line starts a foldable block if the next line is more indented than the current line. The block contains all following lines whose indentation is strictly greater than the block-starting line’s indentation. The block ends right before the first later line whose indentation is less than or equal to the block-starting line’s indentation.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">For example:</p>
<pre><figure class="not-prose my-4 max-w-full overflow-hidden rounded-xl border border-slate-200/70 bg-slate-50/70 shadow-none dark:border-slate-700/75 dark:bg-slate-950/55"><div class="max-w-full overflow-x-auto"><div class="block dark:hidden"><div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>1   a = 1
</span>2   for i in range(10):
3       print(i)
4       print(i ** 2)
5   b = 10</code></div></div><div class="hidden dark:block"><div style="background: transparent; color: rgb(171, 178, 191); text-shadow: rgba(0, 0, 0, 0.3) 0px 1px; font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>1   a = 1
</span>2   for i in range(10):
3       print(i)
4       print(i ** 2)
5   b = 10</code></div></div></div></figure></pre>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Line <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">2</code> is foldable because line <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">3</code> is more indented. If line <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">2</code> is collapsed, lines <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">3</code> and <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">4</code> should be hidden:</p>
<pre><figure class="not-prose my-4 max-w-full overflow-hidden rounded-xl border border-slate-200/70 bg-slate-50/70 shadow-none dark:border-slate-700/75 dark:bg-slate-950/55"><div class="max-w-full overflow-x-auto"><div class="block dark:hidden"><div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>1   a = 1
</span>2 + for i in range(10):
5   b = 10</code></div></div><div class="hidden dark:block"><div style="background: transparent; color: rgb(171, 178, 191); text-shadow: rgba(0, 0, 0, 0.3) 0px 1px; font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>1   a = 1
</span>2 + for i in range(10):
5   b = 10</code></div></div></div></figure></pre>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Implement a <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">FoldableCodeEditor</code> class:</p>
<pre><figure class="not-prose my-4 max-w-full overflow-hidden rounded-xl border border-slate-200/70 bg-slate-50/70 shadow-none dark:border-slate-700/75 dark:bg-slate-950/55"><div class="max-w-full overflow-x-auto"><div class="block dark:hidden"><div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>class FoldableCodeEditor:
</span>    def __init__(self, lines: list[str]):
        ...

    def shrink_block(self, line_number: int) -&gt; bool:
        ...

    def expand_block(self, line_number: int) -&gt; bool:
        ...

    def render(self) -&gt; list[str]:
        ...</code></div></div><div class="hidden dark:block"><div style="background: transparent; color: rgb(171, 178, 191); text-shadow: rgba(0, 0, 0, 0.3) 0px 1px; font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>class FoldableCodeEditor:
</span>    def __init__(self, lines: list[str]):
        ...

    def shrink_block(self, line_number: int) -&gt; bool:
        ...

    def expand_block(self, line_number: int) -&gt; bool:
        ...

    def render(self) -&gt; list[str]:
        ...</code></div></div></div></figure></pre></div>

        <code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>Input:
</span>editor = FoldableCodeEditor([
    "a = 1",
    "for i in range(10):",
    "    print(i)",
    "    print(i ** 2)",
    "b = 10"
])
editor.shrink_block(2)
editor.render()

Output:
[
    "1   a = 1",
    "2 + for i in range(10):",
    "5   b = 10"
]

Explanation:
Line 2 owns the indented block containing lines 3 and 4.
After shrinking line 2, those lines are hidden.</code>

from typing import Any

class FoldableCodeEditor:
    def __init__(self, lines: Any) -> None:
        # TODO: initialize the instance.
        pass

    def shrink_block(self, line_number: Any) -> Any:
        raise NotImplementedError

    def expand_block(self, line_number: Any) -> Any:
        raise NotImplementedError

    def render(self) -> Any:
        raise NotImplementedError

    def _indent_count(self, line: Any) -> Any:
        raise NotImplementedError

    def _compute_block_ends(self) -> Any:
        raise NotImplementedError

    def _is_valid_fold_line(self, index: Any) -> Any:
        raise NotImplementedError

    def _format_line(self, index: Any) -> Any:
        raise NotImplementedError

# Add your own calls below.

<div class="markdown-content prose prose-sm max-w-none min-w-0 [&amp;_p]:whitespace-pre-line coding-question-description-markdown"><p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">You are designing a two-player board game similar to Connect Four, but the board is infinite. The board has infinitely many columns horizontally, and each column can grow upward without limit. Columns are indexed by integers, so valid columns can be negative, zero, or positive.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Players take turns inserting tokens into a column. Because of gravity, when a token is inserted into column <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">col</code>, it lands on top of the existing stack in that column. For example, if column <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">3</code> already contains two tokens, the next token inserted into column <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">3</code> lands at row <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">2</code>.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">A player wins immediately after placing a token if they have <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">N</code> consecutive tokens in any of these directions:</p>
<pre><figure class="not-prose my-4 max-w-full overflow-hidden rounded-xl border border-slate-200/70 bg-slate-50/70 shadow-none dark:border-slate-700/75 dark:bg-slate-950/55"><div class="max-w-full overflow-x-auto"><div class="block dark:hidden"><div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>horizontal
</span>vertical
diagonal up-right
diagonal up-left</code></div></div><div class="hidden dark:block"><div style="background: transparent; color: rgb(171, 178, 191); text-shadow: rgba(0, 0, 0, 0.3) 0px 1px; font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>horizontal
</span>vertical
diagonal up-right
diagonal up-left</code></div></div></div></figure></pre>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Implement:</p>
<pre><figure class="not-prose my-4 max-w-full overflow-hidden rounded-xl border border-slate-200/70 bg-slate-50/70 shadow-none dark:border-slate-700/75 dark:bg-slate-950/55"><div class="max-w-full overflow-x-auto"><div class="block dark:hidden"><div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>class InfiniteConnectNGame:
</span>    def __init__(self, n: int):
        ...</code></div></div><div class="hidden dark:block"><div style="background: transparent; color: rgb(171, 178, 191); text-shadow: rgba(0, 0, 0, 0.3) 0px 1px; font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>class InfiniteConnectNGame:
</span>    def __init__(self, n: int):
        ...</code></div></div></div></figure></pre></div>

from typing import Any

class InfiniteConnectNGame:
    def __init__(self, n: Any) -> None:
        # TODO: initialize the instance.
        pass

    def insert(self, col: Any, player: Any) -> Any:
        raise NotImplementedError

    def _wins_from(self, position: Any, player: Any) -> Any:
        raise NotImplementedError

    def _count_direction(self, position: Any, player: Any, dr: Any, dc: Any) -> Any:
        raise NotImplementedError

# Add your own calls below.

<div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>Input:
</span>game = InfiniteConnectNGame(4)
game.insert(0, "A")
game.insert(0, "B")
game.insert(1, "A")
game.insert(1, "B")
game.insert(2, "A")
game.insert(2, "B")
game.insert(3, "A")

Output:
"PENDING"
"PENDING"
"PENDING"
"PENDING"
"PENDING"
"PENDING"
"A"

Explanation:
Player A forms a horizontal line at row 0 across columns 0, 1, 2, and 3.</code></div>

<div class="markdown-content prose prose-sm max-w-none min-w-0 [&amp;_p]:whitespace-pre-line coding-question-description-markdown"><p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">A code review tool compares two versions of a text file. Each file is represented as a list of lines. The tool wants to find one line that can safely be used as an anchor between the two versions. A line is considered a reliable matching line only if:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">it appears exactly once in the first file</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">it appears exactly once in the second file</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">it appears in both files</li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">If a line appears multiple times in either file, it cannot be used as a reliable match.</p>
<hr class="my-4 border-gray-200 dark:border-gray-700">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">You are given:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">oldFile</code>: lines from the old version</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">newFile</code>: lines from the new version</li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Return a pair: <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">[i, j]</code>, where:</p></div>

<div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>Input:
</span>oldFile = ["init app", "load config", "connect db", "start"]
newFile = ["connect db", "connect db", "load config", "shutdown"]

Output:
[1, 2]</code></div>

from typing import Any

class Solution:
    def findReliableMatch(self, oldFile: Any, newFile: Any) -> Any:
        raise NotImplementedError

# Add your own calls below.

<div class="markdown-content prose prose-sm max-w-none min-w-0 [&amp;_p]:whitespace-pre-line coding-question-description-markdown"><p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">You are building a two-player token game on an infinite board. The board has infinitely many columns, indexed by integers: <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">..., -2, -1, 0, 1, 2, ...</code></p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">The lowest row is height <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">0</code>. The board can grow upward, but never downward. There are two players:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">"B"</code></li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">"R"</code></li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">When a player places a token in a column, the token is inserted at the bottom of that column. This means every existing token in that column is pushed up by one height.</p>
<hr class="my-4 border-gray-200 dark:border-gray-700">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">A player wins if they have <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">k</code> consecutive tokens in a straight line. The line may be:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">vertical</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">horizontal</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">diagonal up-right</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">diagonal up-left</li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Because inserting a token at the bottom may push existing tokens upward, it is possible for either player to create a winning line after a move. If both players win after the same move, return <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">"DRAW"</code>.</p>
<hr class="my-4 border-gray-200 dark:border-gray-700">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Implement the <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">StackingConnectK</code> class:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">StackingConnectK(int k)</code> initializes the game with win condition <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">k</code>.</li>
</ul></div>

<div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>Input:
</span>["StackingConnectK", "move", "move", "move", "move", "move", "printBoard"]
[[3], ["B", 0], ["R", 1], ["B", 0], ["R", 1], ["B", 0], []]

Output:
[null, "NO WINNER", "NO WINNER", "NO WINNER", "NO WINNER", "B WINS", "BR\nBR\nBR"]</code></div>

from typing import Any

class StackingConnectK:
    def __init__(self, k: Any) -> None:
        # TODO: initialize the instance.
        pass

    def move(self, player: Any, column: Any) -> Any:
        raise NotImplementedError

    def printBoard(self) -> Any:
        raise NotImplementedError

    def _checkVertical(self, player: Any, column: Any) -> Any:
        raise NotImplementedError

    def _checkAnyHorizontal(self, player: Any, column: Any) -> Any:
        raise NotImplementedError

    def _checkHorizontal(self, player: Any, centerColumn: Any, height: Any) -> Any:
        raise NotImplementedError

    def _checkAnyDiagonal(self, player: Any, column: Any) -> Any:
        raise NotImplementedError

    def _checkDiagonal(self, player: Any, centerColumn: Any, height: Any, heightDirection: Any) -> Any:
        raise NotImplementedError

    def _getPiece(self, column: Any, height: Any) -> Any:
        raise NotImplementedError

# Add your own calls below.

<div class="markdown-content prose prose-sm max-w-none min-w-0 [&amp;_p]:whitespace-pre-line coding-question-description-markdown"><p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">A monitoring system receives live sensor readings one record at a time. Each record contains:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">a timestamp</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">a sensor code</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">a reading value</li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">The system needs to convert this stream into table rows. Each row represents one timestamp, and each column represents one registered sensor code. Sensor codes are already provided in sorted order. Their order decides the column order.</p>
<hr class="my-4 border-gray-200 dark:border-gray-700">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">You are given:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">sensorCodes</code>: a sorted list of distinct sensor codes</li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Each output row should look like: <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">[timestamp, value0, value1, ..., valueM-1]</code></p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">where:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">value0</code> is the reading for <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">sensorCodes[0]</code></li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">value1</code> is the reading for <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">sensorCodes[1]</code></li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">and so on</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">if a sensor has no reading for that timestamp, use <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">-1</code></li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Records arrive sorted by timestamp. When a new timestamp appears, it means the previous timestamp is complete and should be returned. At the end of the stream, <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">flush()</code> returns the final pending row.</p>
<hr class="my-4 border-gray-200 dark:border-gray-700">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Implement the <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">SensorStreamTransformer</code> class:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">SensorStreamTransformer(List&lt;String&gt; sensorCodes)</code> initializes the transformer with known sensor codes.</li>
</ul></div>


<div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>Input:
</span>["SensorStreamTransformer", "processReading", "processReading", "processReading", "processReading", "flush"]
[["A", "B", "C"], [10, "A", 5], [10, "C", 9], [11, "B", 7], [11, "C", 8], []]

Output:
[null, [], [], [10, 5, -1, 9], [], [11, -1, 7, 8]]</code></div>

from typing import Any

class SensorStreamTransformer:
    def __init__(self, sensorCodes: Any) -> None:
        # TODO: initialize the instance.
        pass

    def processReading(self, timestamp: Any, sensorCode: Any, value: Any) -> Any:
        raise NotImplementedError

    def flush(self) -> Any:
        raise NotImplementedError

    def _buildRow(self, timestamp: Any, values: Any) -> Any:
        raise NotImplementedError

# Add your own calls below.

<div class="markdown-content prose prose-sm max-w-none min-w-0 [&amp;_p]:whitespace-pre-line coding-question-description-markdown"><p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">A low-level programming tool needs to describe how a structured object is stored in memory. The object is made of fields. Each field has:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">a unique name</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">a byte size</li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Fields are packed one after another starting from byte offset <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">0</code>. There are no gaps between fields. For example, if the fields are:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">name</code>: 4 bytes</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">age</code>: 2 bytes</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">score</code>: 8 bytes</li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Then the layout is:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">name</code> starts at offset <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">0</code></li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">age</code> starts at offset <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">4</code></li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">score</code> starts at offset <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">6</code></li>
</ul>
<hr class="my-4 border-gray-200 dark:border-gray-700">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">You need to design a manager that can quickly return the starting byte offset of any field. The manager should also support inserting a new field into the field order. When a new field is inserted, every field after it shifts right by the inserted field’s size.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Implement the <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">StructLayoutManager</code> class:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">StructLayoutManager(List&lt;String&gt; fieldNames, List&lt;Integer&gt; fieldSizes)</code> initializes the object layout using the given fields in order.</li>
</ul></div>

<div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>Input:
</span>["StructLayoutManager", "getOffset", "getOffset", "insertField", "getOffset", "getOffset", "getOffset"]
[[["name", "age", "score"], [4, 2, 8]], ["name"], ["score"], ["id", 3, 1], ["name"], ["id"], ["score"]]

Output:
[null, 0, 6, null, 0, 4, 9]</code></div>

from typing import Any

class StructLayoutManager:
    def __init__(self, fieldNames: Any, fieldSizes: Any) -> None:
        # TODO: initialize the instance.
        pass

    def _initializeOffsets(self, fieldNames: Any, fieldSizes: Any) -> Any:
        raise NotImplementedError

    def getOffset(self, fieldName: Any) -> Any:
        raise NotImplementedError

    def insertField(self, fieldName: Any, size: Any, index: Any) -> Any:
        raise NotImplementedError

# Add your own calls below.

<div class="markdown-content prose prose-sm max-w-none min-w-0 [&amp;_p]:whitespace-pre-line coding-question-description-markdown"><p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">A logging system stores recent message bytes inside a fixed-size circular buffer. The buffer has a fixed capacity. It uses two independent pointers:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">writeIndex</code>: where the next write starts</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">readIndex</code>: where the next read starts</li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">When writing reaches the end of the buffer, it wraps around to the beginning.
When reading reaches the end of the buffer, it also wraps around to the beginning.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">The buffer does not track message boundaries. It simply stores characters in fixed positions. If new data is written into a position that already contains old data, the old data is overwritten. Initially, every position stores the special null character <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">"\0"</code>.</p>
<hr class="my-4 border-gray-200 dark:border-gray-700">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Implement the <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">CircularMessageBuffer</code> class:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">CircularMessageBuffer(int capacity)</code> initializes a buffer with fixed size <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">capacity</code>.</li>
</ul></div>

<code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>Input:
</span>["CircularMessageBuffer", "write", "write", "write", "read", "read"]
[[10], ["hello"], ["world"], ["abc"], [5], [5]]

Output:
[null, null, null, null, "abclo", "world"]</code>


from typing import Any

class CircularMessageBuffer:
    def __init__(self, capacity: Any) -> None:
        # TODO: initialize the instance.
        pass

    def write(self, message: Any) -> Any:
        raise NotImplementedError

    def read(self, length: Any) -> Any:
        raise NotImplementedError

# Add your own calls below.

<div class="markdown-content prose prose-sm max-w-none min-w-0 [&amp;_p]:whitespace-pre-line coding-question-description-markdown"><p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">You are designing a two-player board game. The board has: 6 rows * 7 columns</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Two players, <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">"A"</code> and <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">"B"</code>, take turns dropping tokens into columns.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">When a player drops a token into a column, the token falls to the lowest empty cell in that column.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">A player wins if, after their move, they have 4 tokens in a row in any direction:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">horizontally</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">vertically</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">diagonally down-right</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">diagonally down-left</li>
</ul>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">If the board becomes full and nobody has won, the game ends in a draw.</p>
<hr class="my-4 border-gray-200 dark:border-gray-700">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Implement the <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">ConnectFourGame</code> class:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">ConnectFourGame()</code> initializes an empty 6 × 7 board.</p>
</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">String move(int column, String player)</code> drops <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">player</code>'s token into <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">column</code>.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Returns:</p>
</li>
</ul></div>

<div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>Input:
</span>["ConnectFourGame", "move", "move", "move", "move", "move", "move", "move", "printBoard"]
[[], [0, "A"], [1, "B"], [0, "A"], [1, "B"], [0, "A"], [1, "B"], [0, "A"], []]

Output:
[null, "PENDING", "PENDING", "PENDING", "PENDING", "PENDING", "PENDING", "A",
"| | | | | | | |
| | | | | | | |
|A| | | | | | |
|A|B| | | | | |
|A|B| | | | | |
|A|B| | | | | |"]</code></div>

from typing import Any

class ConnectFourGame:
    def __init__(self) -> None:
        # TODO: initialize the instance.
        pass

    def move(self, column: Any, player: Any) -> Any:
        raise NotImplementedError

    def _hasWon(self, row: Any, col: Any, player: Any) -> Any:
        raise NotImplementedError

    def _countDirection(self, row: Any, col: Any, dr: Any, dc: Any, player: Any) -> Any:
        raise NotImplementedError

    def printBoard(self) -> Any:
        raise NotImplementedError

# Add your own calls below.

<div class="markdown-content prose prose-sm max-w-none min-w-0 [&amp;_p]:whitespace-pre-line coding-question-description-markdown"><p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">An online marketplace has many product listings. Each listing belongs to a seller, has a product name, a price, and may or may not already be sold. A buyer can place an order for a product and specify the highest price they are willing to pay. The marketplace should always try to match the buyer with the cheapest currently available listing for that product.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">You are given an initial list of listings. Each listing is represented as: <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">[productName, sellerName, price, buyerName]</code></p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">buyerName == ""</code> means the listing is still available</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">non-empty <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">buyerName</code> means the listing has already been sold</li>
</ul>
<hr class="my-4 border-gray-200 dark:border-gray-700">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Implement the <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">Marketplace</code> class:</p>
<ul class="list-disc list-outside pl-6 text-gray-700 dark:text-gray-300 mb-3 space-y-1 marker:text-gray-500 dark:marker:text-gray-400 [&amp;_ul]:mt-1 [&amp;_ul]:mb-1 [&amp;_ol]:mt-1 [&amp;_ol]:mb-1">
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">Marketplace(List&lt;List&lt;String&gt;&gt; listings)</code> initializes the marketplace with the given product listings.</p>
</li>
<li class="text-gray-700 dark:text-gray-300 pl-1 leading-relaxed [&amp;&gt;p]:mb-0">
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0"><code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">List&lt;String&gt; processOrders(List&lt;List&lt;String&gt;&gt; orders)</code> processes a batch of buy orders.</p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">Each order is represented as: <code class="coding-question-inline-code !inline max-w-full whitespace-pre-wrap break-words !border-0 !bg-transparent !p-0 !shadow-none !outline-0 text-[#0D9488] dark:text-teal-300 text-sm font-mono" node="[object Object]">[buyerName, productName, maxPrice]</code></p>
<p class="text-gray-700 dark:text-gray-300 leading-relaxed mb-3 last:mb-0">For each order:</p>
</li>
</ul></div>

<div style="background: transparent; color: rgb(56, 58, 66); font-family: &quot;Fira Code&quot;, &quot;Fira Mono&quot;, Menlo, Consolas, &quot;DejaVu Sans Mono&quot;, monospace; direction: ltr; text-align: left; white-space: pre; word-spacing: normal; word-break: normal; line-height: 1.62; tab-size: 2; hyphens: none; padding: 1rem 1.05rem; margin: 0px; overflow: auto; border-radius: 0px; font-size: 0.82rem; width: 100%; max-width: 100%; box-sizing: border-box;"><code style="white-space: pre; font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, &quot;Liberation Mono&quot;, &quot;Courier New&quot;, monospace;"><span>Input:
</span>listings = [
  ["book", "Alice", "100", ""],
  ["book", "Bob", "120", ""],
  ["pen", "Carol", "50", ""],
  ["book", "David", "90", ""]
]

orders = [
  ["Charlie", "book", "110"],
  ["Eve", "pen", "40"]
]

Output:
["book:90"]

Final listings:
[
  ["book", "Alice", "100", ""],
  ["book", "Bob", "120", ""],
  ["pen", "Carol", "50", ""],
  ["book", "David", "90", "Charlie"]
]</code></div>

from typing import Any

class Listing:
    def __init__(self, productName: Any, sellerName: Any, price: Any, buyerName: Any) -> None:
        # TODO: initialize the instance.
        pass

class Marketplace:
    def __init__(self, listings: Any) -> None:
        # TODO: initialize the instance.
        pass

    def _buildHeaps(self) -> Any:
        raise NotImplementedError

    def processOrders(self, orders: Any) -> Any:
        raise NotImplementedError

    def getListings(self) -> Any:
        raise NotImplementedError

# Add your own calls below.
