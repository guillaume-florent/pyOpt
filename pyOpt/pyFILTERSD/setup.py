#!/usr/bin/env python
# coding: utf-8

r"""pyFILTERSD setup"""

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
    config = Configuration('pyFILTERSD', parent_package, top_path)

    config.add_library('filtersd',
                       sources=[os.path.join('source', '*.f')])
    config.add_extension('filtersd',
                         sources=['source/f2py/filtersd.pyf'],
                         libraries=['filtersd'])
    config.add_data_files('LICENSE', 'README')

    return config


if __name__ == '__main__':
    setup(**configuration(top_path='').todict())
