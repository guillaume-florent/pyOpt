#!/usr/bin/env python
# coding: utf-8

r"""pySDPEN setup"""

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
    config = Configuration('pySDPEN', parent_package, top_path)

    config.add_library('sdpen',
                       sources=[os.path.join('source', '*.f90')])
    config.add_extension('sdpen',
                         sources=['source/f2py/sdpen.pyf'],
                         libraries=['sdpen'])
    config.add_data_files('LICENSE', 'README')

    return config


if __name__ == '__main__':
    setup(**configuration(top_path='').todict())
