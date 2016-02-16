#!/usr/bin/env python

#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Author: Evan Hubinger
License: Apache 2.0
Description: Syntax highlighting for Coconut code.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#----------------------------------------------------------------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

from .command import *
from pygments.lexers import Python3Lexer, PythonConsoleLexer
from pygments.token import Text, Comment, Operator, Keyword, Name, String, Number, Punctuation, Generic, Other, Error
from pygments.lexer import words

#-----------------------------------------------------------------------------------------------------------------------
# LEXERS:
#-----------------------------------------------------------------------------------------------------------------------

class pylexer(Python3Lexer):
    """Coconut-style Python syntax highlighter."""
    name = "coc_python"
    aliases = ["coc_python", "coc_py", "coc_python3", "coc_py3"]
    filenames = []

    def __init__(self, stripnl=False, stripall=False, ensurenl=True, tabsize=tablen, encoding=encoding):
        """Initialize the Python syntax highlighter."""
        super(pylexer, self).__init__(stripnl=stripnl, stripall=stripall, ensurenl=ensurenl, tabsize=tabsize, encoding=encoding)

class pyconlexer(PythonConsoleLexer):
    """Coconut-style Python console syntax highlighter."""
    name = "coc_pycon"
    aliases = ["coc_pycon", "coc_pycon3"]
    filenames = []

    def __init__(self, stripnl=False, stripall=False, ensurenl=True, tabsize=tablen, encoding=encoding, python3=True):
        """Initialize the Python console syntax highlighter."""
        super(pyconlexer, self).__init__(stripnl=stripnl, stripall=stripall, ensurenl=ensurenl, tabsize=tabsize, encoding=encoding, python3=python3)

class coclexer(Python3Lexer):
    """Coconut syntax highlighter."""
    name = "coconut"
    aliases = ["coconut", "coc", "coconutcon"]
    filenames = ["*"+code_ext]

    tokens = Python3Lexer.tokens.copy()
    tokens["keywords"] = [
        (words(keywords + reserved_vars, suffix=r"\b"), Keyword),
        (words(const_vars, suffix=r"\b"), Keyword.Constant)
    ]
    tokens["backtick"] = [
        (r"`.*?`", String.Backtick)
    ]
    tokens["root"] = [
        (r"\$|::", Operator)
    ] + tokens["root"]
    tokens["builtins"] = tokens["builtins"] + [
        (words((
            "reduce",
            "takewhile",
            "dropwhile",
            "tee",
            "recursive",
            "datamaker",
            "consume"
            ), prefix=r"(?<!\.)", suffix=r"\b"), Name.Builtin),
        (r"(?<!\.)MatchError\b", Name.Exception)
    ]
    magicvars = [
        (r"(?<!\.)__coconut_version__\b", Name.Variable.Magic)
    ]
    if "magicvars" in tokens:
        tokens["magicvars"] = tokens["magicvars"] + magicvars
    elif "magicfuncs" in tokens:
        tokens["magicfuncs"] = tokens["magicfuncs"] + magicvars
    else:
        tokens["builtins"] = tokens["builtins"] + magicvars
    tokens["numbers"] = [
        (r"\d[\d_]*(\.\d[\d_]*)?", Number.Integer),
        (r"0b[01_]+", Number.Integer),
        (r"0o[0-7_]+", Number.Integer),
        (r"0x[\da-fA-F_]+", Number.Integer)
    ] + tokens["numbers"]

    def __init__(self, stripnl=False, stripall=False, ensurenl=True, tabsize=tablen, encoding=encoding):
        """Initialize the Python syntax highlighter."""
        super(coclexer, self).__init__(stripnl=stripnl, stripall=stripall, ensurenl=ensurenl, tabsize=tabsize, encoding=encoding)