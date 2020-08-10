#!/usr/bin/python3

# BUG: mistune_contrib.math cannot support inline
# Using self-modified code instead of default
# AND I'VE TRIED BUT FINALLY EXHAUSTED MODIFING THEM.
# I'M TRIED AND DO NOT WANT TO TRY AGAIN TO MODIFY THEM.
from mistune_contrib_math import MathInlineMixin, MathBlockMixin, MathRendererMixin
# from mistune_contrib.math import MathInlineMixin, MathBlockMixin, MathRendererMixin

from mistune import InlineLexer, BlockLexer, Renderer, Markdown

import yaml
import re


class MathBlockLexer(MathBlockMixin, BlockLexer):
    def __init__(self, *args, **kwargs):
        super(MathBlockLexer, self).__init__(*args, **kwargs)
        self.enable_math()


class MathInlineLexer(InlineLexer, MathInlineMixin):
    def __init__(self, *args, **kwargs):
        super(MathInlineLexer, self).__init__(*args, **kwargs)
        self.enable_math()


class MathRenderer(Renderer, MathRendererMixin):
    pass


renderer = MathRenderer()
inline = MathInlineLexer(renderer)
block = MathBlockLexer()
markdown = Markdown(renderer, inline=inline, block=block)


def parse(text):
    text = markdown(text.strip())

    # For LOJ
    text = re.sub(r'<pre>([\s\S]*?)</pre>',
                  r'<div class="ui existing segment"><pre style="margin-top: 0; margin-bottom: 0; ">\1</pre></div>', text)
    text = re.sub(r'<blockquote>([\s\S]*?)</blockquote>',
                  r'<div class="ui message">\1</div>', text)
    text = re.sub(r'<table>([\s\S]*?)</table>',
                  r'<table class="ui structured celled table">\1</table>', text)
    return text


def split_meta(text):
    text = text.strip()

    # TODO: Better meta information support
    if text[:3] == '---':
        pos = text.find('---', 3)
        if pos == -1:
            raise SyntaxError('meta information is not completed')
        meta = yaml.load(text[3:pos].strip(), Loader=yaml.SafeLoader)
        text = text[pos + 3:].strip()
    else:
        meta = dict()

    return (meta, text)


if __name__ == '__main__':
    TEST_TEXT = """
Here is a example.

$$\\text{block latex with } a_{\\text{sub}}^{\\text{sup}}$$

$$


\\begin{aligned}
    & \\text{multi-line latex with } a_{\\text{sub}}^{\\text{sup}} \\\\



    =&\\sum_{i = 1}^n \\varphi(i) \\\\
    =&\\text{should be escaped.} \\\\
\\end{aligned}


$$

And


$$
\\begin{aligned}
    & \\text{multi-line latex with } a_{\\text{sub}}^{\\text{sup}} \\\\
    =&\\sum_{i = 1}^n \\varphi(i) \\\\
    =&\\text{should be escaped (this version excludes linewrap).} \\\\
\\end{aligned}
$$

Or $\\text{Also inline math with } a_{\\text{sub}}^{\\text{sup}}$

and `$not parsed latex in code$`

and \\$escaped **dollar** mark\\$

as so.
"""
    print(parse(TEST_TEXT))
