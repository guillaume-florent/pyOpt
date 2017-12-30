#!/usr/bin/env python
# coding: utf-8

r"""pyALGENCAN setup"""

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
    config = Configuration('pyALGENCAN', parent_package, top_path)

    config.add_library('algencan',
                       sources=[os.path.join('source', '*.f')],
                       include_dirs=['source'])
    config.add_extension('algencan',
                         sources=['source/f2py/algencan.pyf'],
                         libraries=['algencan'])
    config.add_data_files('LICENSE', 'README')

    return config


if __name__ == '__main__':
    setup(**configuration(top_path='').todict())
