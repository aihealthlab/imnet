from __future__ import print_function
from setuptools import setup
from distutils.extension import Extension
import warnings
import os
import sys


use_cython = True

try:
    from Cython.Build import cythonize
except ImportError:
    use_cython = False
    warnings.warn('No cython found -- install will use pre-generated C files')


def create_ext_modules():
    """
    Build commands require preinstalled numpy to compile the c extensions. A global "import numpy"
    here would break tox and also if installed as a dependency from another python package.
    So we only require numpy for the cases where its header files are actually needed.
    """

    build_commands = ('build', 'build_ext', 'build_py',
                    'build_clib', 'build_scripts', 'bdist_wheel', 'bdist_rpm',
                    'bdist_wininst', 'bdist_msi', 'bdist_mpkg', 'build_sphinx')

    ext_modules = []
    for command in build_commands:
        if command in sys.argv[1:]:
            try:
                import numpy
            except ImportError:
                raise Exception(
                    "please install numpy, need numpy header files to compile c extensions")
            ext_modules = [Extension("imnet3.process_strings_cy",
                                    sources=["imnet3/process_strings_cy.pyx"],
                                    include_dirs=[numpy.get_include()])]
            if use_cython:
                print('Using cython')
                ext_modules = cythonize(ext_modules)

            break
    return ext_modules



currdir = os.getcwd()


setup(name="imnet3",
      author="Rok Roskar & Erand Smakaj",
      version='0.3.alpha1',
      author_email="erand.smakaj@fhnw.ch",
      url="https://github.com/aihealthlab/imnet",
      package_dir={'imnet3/': ''},
      packages=['imnet3'],
      ext_modules=create_ext_modules(),
      scripts=['scripts/imnet3-analyze'],
      install_requires=['click', 'python-Levenshtein', 'scipy', 'networkx', 'pandas'],
      keywords=['genomics', 'bioinformatics']
      )
