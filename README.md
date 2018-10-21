#### decimal-monkeypatch

A Python module based on [autowrapt](https://github.com/GrahamDumpleton/autowrapt)
for monkeypatching slow `decimal` module to [cdecimal](http://www.bytereef.org/mpdecimal/index.html) on Python 2 with preservation of the functionality of the `boto` lib
##### Usage
1. `pip install decimal-monkeypatch`  
2. set `AUTOWRAPT_BOOTSTRAP=decimal` env variable for patch activation
##### Additional reading
* [Swapping decimal for cdecimal on Python 2](https://adamj.eu/tech/2015/06/06/swapping-decimal-for-cdecimal-on-python-2/)
* [Automatic patching of Python applications](https://github.com/openstack/deb-python-wrapt/blob/master/blog/14-automatic-patching-of-python-applications.md)
###### WARNING
Tested on only this configuration:  
Python 2.7.12+  
`boto` 2.48.0   
`m3-cdecimal` 2.3  
