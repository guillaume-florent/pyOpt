#!/usr/bin/env python
# coding: utf-8

r"""pyMIDACO setup"""

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
    config = Configuration('pyMIDACO', parent_package, top_path)

    config.add_library('midaco',
                       sources=[os.path.join('source', '*.f')])
    config.add_extension('midaco',
                         sources=['source/f2py/midaco.pyf'],
                         libraries=['midaco'])
    config.add_data_files('LICENSE', 'README')

    return config


if __name__ == '__main__':
    setup(**configuration(top_path='').todict())
