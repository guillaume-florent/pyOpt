#!/usr/bin/env python
# coding: utf-8

r"""pyGCMMA setup"""

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
    config = Configuration('pyGCMMA', parent_package, top_path)

    config.add_library('gcmma',
                       sources=[os.path.join('source', '*.f')])
    config.add_extension('gcmma',
                         sources=['source/f2py/gcmma.pyf'],
                         libraries=['gcmma'])
    config.add_data_files('LICENSE', 'README')

    return config


if __name__ == '__main__':
    setup(**configuration(top_path='').todict())
