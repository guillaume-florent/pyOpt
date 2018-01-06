#!/usr/bin/env python
# coding: utf-8

r"""pyNLPQLP setup"""

import os

from numpy.distutils.misc_util import Configuration
from numpy.distutils.core import setup


def configuration(parent_package='', top_path=None):
    r"""
    
    Parameters
    ----------
    parent_package
    top_path

    Returns
    -------
    Configuration

    """
    config = Configuration('pyNLPQLP', parent_package, top_path)

    config.add_library('nlpqlp',
                       sources=[os.path.join('source', '*.for')])
    config.add_extension('nlpqlp',
                         sources=['source/f2py/nlpqlp.pyf'],
                         libraries=['nlpqlp'])
    config.add_data_files('LICENSE', 'README')

    return config


if __name__ == '__main__':
    setup(**configuration(top_path='').todict())
