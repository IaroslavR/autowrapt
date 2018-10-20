import sys
import os

from distutils.sysconfig import get_python_lib
from setuptools import setup

setup_kwargs = dict(
    name='decimal-monkeypatch',
    version='0.1',
    description='Monkey patches Python 2 decimal to cdecimal',
    author='Iaroslav Russkykh',
    author_email='iarrus@ya.ru',
    license='BSD',
    url='https://github.com/IaroslavR/decimal-monkeypatch',
    packages=['decimal-monkeypatch'],
    package_dir={'decimal-monkeypatch': 'src'},
    package_data={'decimal-monkeypatch': ['__startup__/sitecustomize.py']},
    data_files=[(get_python_lib(prefix=''), ['autowrapt-init.pth'])],
    entry_points={
        'console_scripts': ['decimal-monkeypatch = decimal-monkeypatch.main:main'],
        'decimal-monkeypatch.patches': ['decimal = decimal-monkeypatch.patches:autowrapt_decimal']},
    install_requires=['wrapt>=1.10.4', 'm3-cdecimal==2.3'],
)

setup(**setup_kwargs)
