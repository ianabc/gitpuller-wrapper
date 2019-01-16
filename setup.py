from setuptools import setup, find_packages
from distutils.util import convert_path

import os

# Imports __version__, reference: https://stackoverflow.com/a/24517154/2220152
ns = {}
ver_path = convert_path('gitpuller-wrapper/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), ns)
__version__ = ns['__version__']


setup(
    name="gitpuller-wrapper",
    version='0.1.0',
    url="https://github.com/callysto/gitpuller-wrapper",
    author="Alex Tennant",
    author_email="alex.tennant@cybera.ca"
    description="Cute little wrapper for nbgitpuller so you can just paste URLs and get stuff on your hub",
    packages=find_packages(),
    install_requires=[
        'notebook>=5.5.0',
        'nbgitpuller>=0.6.1',
    ],
    data_files=[
        (
            'share/jupyter/nbextensions/gitpuller-wrapper',
             ['gitpuller-wrapper/static/main.js',
              'gitpuller-wrapper/static/main.js',
              'gitpuller-wrapper/static/parse-git.js'
             ]
        ),
        (
            'etc/jupyter/jupyter_notebook_config.d', 
            ['gitpuller-wrapper/etc/serverextension.json']
        ),
        (
            'etc/jupyter/nbconfig/notebook.d', 
            ['gitpuller-wrapper/etc/nbextension.json']
        )
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta'
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
