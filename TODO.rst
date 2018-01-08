
Python 2 and 3 compatibility

******** Import system is a bit weird (using __all_ defined in subpackage to append to pyOpt __all_) -> confusing -> simplify

Doc
---

Infos about the algorithms

Tests
-----

Proper tests suite


Code
----

Documentation last updated by -> delete

Should there be a README in each subpackage? in the source directories?

Machine precision code duplication in subpackages

Miscellaneous
-------------

Docker -> install from Miniconda ?

Licensed software -> how to get the code
    FSQP
    GCMMA
    MIDACO
    MMA
    NLPQL
    NLPQLP
    SNOPT

Notes
-----

sudo chown -R guillaume:guillaume anaconda2
conda install -c anaconda mpi4py
or
conda3 (defined in .bashrc for example to point to the conda of an anaconda3 install)

'python3 setup.py inplace' to develop under Python3