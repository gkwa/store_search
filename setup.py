import setuptools
from setuptools import setup

setup(
    version="0.0.1",
    name="store_search-mtmonacelli",
    py_modules=["grocer"],
    packages=setuptools.find_packages(),
    install_requires=["Click",],
    entry_points="""
        [console_scripts]
        grocer=grocer:cli
    """,
)
