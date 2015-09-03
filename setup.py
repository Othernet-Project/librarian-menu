import os
from setuptools import setup, find_packages

import librarian_menu


def read(fname):
    """ Return content of specified file """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = librarian_menu.__version__

setup(
    name='librarian-menu',
    version=VERSION,
    license='BSD',
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=[
        'librarian_core',
    ],
    dependency_links=[
        'git+ssh://git@github.com/Outernet-Project/librarian-core.git#egg=librarian_core-0.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Applicaton',
        'Framework :: Bottle',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
