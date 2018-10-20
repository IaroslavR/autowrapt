import sys
import os

from distutils.sysconfig import get_python_lib
from setuptools import setup

setup_kwargs = dict(
    name='decimal-monkeypatch',
    version='0.2',
    description='Monkey patches Python 2 decimal to cdecimal',
    author='Iaroslav Russkykh',
    author_email='iarrus@ya.ru',
    license='BSD',
    url='https://github.com/IaroslavR/decimal-monkeypatch',
    packages=['decimal_monkeypatch'],
    package_dir={'decimal_monkeypatch': 'src'},
    package_data={'decimal_monkeypatch': ['__startup__/sitecustomize.py']},
    data_files=[(get_python_lib(prefix=''), ['autowrapt-init.pth'])],
    entry_points={
        'console_scripts': ['decimal_monkeypatch = decimal_monkeypatch.main:main'],
        'decimal_monkeypatch.patches': ['decimal = decimal_monkeypatch.patches:autowrapt_decimal']},
    install_requires=['wrapt>=1.10.4', 'm3-cdecimal==2.3', ],
)

setup(**setup_kwargs)
