# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""
"""
A Lot of this methodology was "borrowed" from
    - https://github.com/jgehrcke/python-cmdline-bootstrap/blob/master/bootstrap/bootstrap.py
"""

import re
from setuptools import setup

install_requires = [
    'argparse', 'numpy', 'networkx'
]

version = re.search(
      '^__version__\s*=\s*"(.*)"',
      open('rivernetworkengine.__version__.py').read(),
      re.M
).group(1)

with open("README.md", "rb") as f:
      long_descr = f.read().decode("utf-8")

setup(
      name='rivernetworktools',
      description='A tool for river networks',
      url='https://github.com/NorthArrowResearch/rivernetworkengine',
      author='Matt Reimer',
      author_email='matt@northarrowresearch.com',
      license='MIT',
      packages=['rivernetworktools'],
      zip_safe=False,
      install_requires=install_requires,
      entry_points={
            "console_scripts": ['networkprofiler = rivernetworkengine.profiler.console:main']
      },
      version=version,
      long_description=long_descr,
)