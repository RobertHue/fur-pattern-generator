"""Used solely for building the .pyd/.so files (Cython)"""

from setuptools import setup
from Cython.Build import cythonize

extensions = cythonize(["fpg/generator/_helpers.pyx"])


setup(
    name="fpg",
    version="0.3.0",
    packages=["fpg", "fpg.generator"],
    ext_modules=extensions,
)
