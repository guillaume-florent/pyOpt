#!/usr/bin/env python
# coding: utf-8

r"""pyCOBYLA setup"""

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
    config = Configuration('pyCOBYLA', parent_package, top_path)

    config.add_library('cobyla',
                       sources=[os.path.join('source', '*.f')])
    config.add_extension('cobyla',
                         sources=['source/f2py/cobyla.pyf'],
                         libraries=['cobyla'])
    config.add_data_files('LICENSE', 'README')

    return config


if __name__ == '__main__':
    setup(**configuration(top_path='').todict())
