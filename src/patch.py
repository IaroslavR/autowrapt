from __future__ import print_function, division


def autowrapt_decimal(_module):
    import sys
    import cdecimal

    sys.modules['decimal'] = cdecimal
    print('module decimal patched to {}'.format(sys.modules['decimal'].__name__))
    cdecimal.tmp_context = cdecimal.Context

    def patched(*args, **kwargs):
        if 'rounding' in kwargs and kwargs['rounding'] is None:
            kwargs['rounding'] = 6
        return cdecimal.tmp_context(*args, **kwargs)
    cdecimal.Context = patched

    print('cdecimal.Context monkey-patch for boto(if rounding=None, then 6 passed to Context instead) applied\n')


def autowrapt_psycopg2(module):
    import ujson
    module.json = ujson
    print('psycopg2._json.json monkey-patched to ujson instead of json\n')


def autowrapt_dynamodb(module):
    from decimal import Decimal
    from boto.dynamodb.types import Binary


    def deepcopy(data):
        """Expected dicts nesting level 1. Lists, sets, and nested dicts
         contains only simple types"""
        res = {}
        for k, v in data.items():
            if type(v) in [Decimal, Binary, str, int, unicode, long, bool]:
                res[k] = v
            elif type(v) in [set, dict, list]:
                res[k] = type(v)(v)
            elif v is None:
                res[k] = v
            else:
                raise ValueError('Unknown type: {}'.format(type(v)))
        return res

    module.deepcopy = deepcopy
    print('boto.dynamodb2.items.deepcopy monkey-patched\n')

