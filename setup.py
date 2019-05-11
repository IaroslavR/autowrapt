from distutils.sysconfig import get_python_lib
from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup_kwargs = dict(
    name='decimal-monkeypatch',
    version='0.4.3',
    description='Python 2 performance patches: decimal to cdecimal, json to ujson for psycopg2',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Iaroslav Russkykh',
    author_email='iarrus@ya.ru',
    license='BSD',
    url='https://github.com/IaroslavR/decimal-monkeypatch',
    packages=['decimal_monkeypatch'],
    package_dir={'decimal_monkeypatch': 'src'},
    package_data={'decimal_monkeypatch': ['__startup__/sitecustomize.py']},
    data_files=[(get_python_lib(prefix=''), ['autowrapt-init.pth'])],
    entry_points={
        'decimal': ['decimal = decimal_monkeypatch.patch:autowrapt_decimal'],
        'psycopg2': [
            'psycopg2._json = decimal_monkeypatch.patch:autowrapt_psycopg2',
        ],
        'dynamodb': ['boto.dynamodb2.items = decimal_monkeypatch.patch:autowrapt_dynamodb', ]
    },
    install_requires=['wrapt>=1.10.4', 'm3-cdecimal==2.3', 'ujson==1.35'],
)

setup(**setup_kwargs)
