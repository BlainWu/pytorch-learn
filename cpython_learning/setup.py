#cython的初始化方法有很多，但是推荐使用的是setup.py
#详细信息http://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html#compilation
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("helloworld.pyx")
)