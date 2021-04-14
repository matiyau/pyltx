#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:07:40 2021

@author: n7
"""

import os
from . import text as tx
from . import utils as ut


def _get_tabular(tab, col_style=None):
    """
    Generate LaTeX tabular environment code for a DataFrame.

    Parameters
    ----------
    tab : pandas.DataFrame
        DataFrame for which the LaTeX tabularenvironment will be created.
    col_style : str or None, optional
        LaTeX column formatting for the table. If None, |c|c|---|c| will be
        used. The default is None.

    Returns
    -------
    ltx : str
        LaTeX code for the tabular environment.

    """
    if col_style is None:
        col_style = "|"
        for col in tab.columns:
            col_style += "c|"

    header = [tx.bf(col) for col in tab.columns]

    ltx = tab.to_latex(header=header, index=False,
                       column_format=col_style, escape=False)

    ltx = ltx.replace(r"\toprule",
                      r"\hline").replace(r"\midrule" + os.linesep,
                                         "").replace(r"\bottomrule" +
                                                     os.linesep,
                                                     "").replace(r"\\",
                                                                 r"\\ \hline")
    return ltx


def get_latex(tab, pos="h!", caption=None, col_style=None, ref=None):
    """
    Convert a DataFrame to a LaTeX Table

    Parameters
    ----------
    tab : pandas.DataFrame
        DataFrame for which the LaTeX table will be created.
    pos : str, optional
        LaTeX positioning scheme. The default is "h!".
    caption : str or None, optional
        Caption for the table. If None, the caption will not be added to the
        LaTeX table code. The default is None.
    col_style : str or None, optional
        LaTeX column formatting for the table. The default is None.
    ref : str or None, optional
        Tag for adding a reference label to the table. If None, no label is
        added. The default is None.

    Returns
    -------
    ltx : str
        LaTeX code for the table.

    """
    pos = "[" + pos + "]"
    ltx = _get_tabular(tab, col_style)

    # Encapsulate in "table" tags
    ltx = ut.encapsln("table", ltx, pos, True, caption, "top", ref)

    return ltx
