# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# root path
ROOT = os.path.dirname(os.path.realpath(__file__))

# README
with open(os.path.join(ROOT, 'README.rst'), encoding='utf-8') as file:
    long_desc = file.read()

# version string
__version__ = '0.0.0.dev0'

# set-up script for pip distribution
setup(
    name='python-babel',
    version=__version__,
    author='Jarry Shaw',
    author_email='jarryshaw@icloud.com',
    url='https://github.com/JarryShaw/babel',
    license='MIT License',
    keywords=['back-port compiler'],
    description='The compiler for next generation Python.',
    long_description=long_desc,
    long_description_content_type='text/x-rst; charset=UTF-8',
    # python_requires='>=3.3',
    zip_safe=True,
    py_modules=['babel'],
    # entry_points={
    #     'console_scripts': [
    #         'babel = babel:main',
    #     ]
    # },
    package_data={
        '': [
            'LICENSE',
            'README.rst',
            'CHANGELOG.md',
        ],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
        # 'Programming Language :: Python :: 3.7',
        # 'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ]
)
