#### decimal-monkeypatch

A Python module based on [autowrapt](https://github.com/GrahamDumpleton/autowrapt)
for: 
- Interpreter-wide monkey patching slow `decimal` module to [cdecimal](http://www.bytereef.org/mpdecimal/index.html) on Python 2 with preservation of the functionality of the `boto` lib.
- `psycopg2` `json` to `ujson` replacement
- Custom `deepcopy` for boto.dynamodb2.items. This patch can give huge performance benefits if you know expected data structure.
##### Usage
`pip install decimal-monkeypatch`  
- set `AUTOWRAPT_BOOTSTRAP=decimal` env variable for `decimal` patch activation
- set `AUTOWRAPT_BOOTSTRAP=psycopg2` env variable for `psycopg2` patch activation
- set `AUTOWRAPT_BOOTSTRAP=dynamodb` env variable for `dynamodb` patch activation
- set `AUTOWRAPT_BOOTSTRAP=decimal,psycopg2,dynamodb` for all at once
##### Additional reading
* [Swapping decimal for cdecimal on Python 2](https://adamj.eu/tech/2015/06/06/swapping-decimal-for-cdecimal-on-python-2/)
* [Automatic patching of Python applications](https://github.com/openstack/deb-python-wrapt/blob/master/blog/14-automatic-patching-of-python-applications.md)
* [Discussion about json module selection in psycopg2](https://github.com/psycopg/psycopg2/issues/284)
* [SO deepcopy question](https://stackoverflow.com/a/45858907/4249707)
###### WARNING
Tested on only this configuration:  
Python 2.7.12+  
`boto` 2.48.0   
`m3-cdecimal` 2.3  
`psycopg2-binary` 2.7.4  
`ujson` 1.35
