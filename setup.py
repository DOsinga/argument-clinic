#!/usr/bin/env python
# Learn more: https://github.com/kennethreitz/setup.py
import os
import sys

from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()


about = {}
with open(os.path.join(here, 'argument', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'argument': 'argument'},
    include_package_data=True,
    python_requires=">=3.6",
    packages=['argument'],
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    install_requires=['docstring-parser'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
