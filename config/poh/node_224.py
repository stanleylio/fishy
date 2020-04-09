# -*- coding: utf-8 -*-
name = 'Salinity (TBD)'
location = 'TBD, Paepae O He`eia Fishpond'
note = 'Aanderaa conductivity sensor 4319. Hardware v5.4. Renamed from node-182.'
#latitude = 21.439722
#longitude = -157.809722

conf = [
    {
        'dbtag':'sn',
        'unit':'-',
        'description':'Sensor serial number',
        'interval':5*60,
    },
    {
        'dbtag':'ec',
        'unit':'mS/cm',
        'description':'Electrical Conductivity',
        'lb':0,
        'interval':5*60,
    },
    {
        'dbtag':'t',
        'unit':'\u2103',
        'description':'Water temperature',
        'lb':-10,
        'ub':50,
        'interval':5*60,
    },
    {
        'dbtag':'sal',
        'unit':'PSU',
        'description':'Salinity',
        'lb':0,
        'interval':5*60,
    },
    {
        'dbtag':'sg',
        'unit':'kg/m^3',
        'description':'Density',
        'lb':900,
        'ub':1100,
        'interval':5*60,
    },
    {
        'dbtag':'sv',
        'unit':'Sound speed',
        'description':'m/s',
        'lb':1000,
        'ub':2000,
        'interval':5*60,
    },
    {
        'dbtag':'Vb',
        'description':'Battery voltage',
        'unit':'V',
        'lb':3.0,
        'ub':4.3,
        'interval':5*60,
    },
    {
        'dbtag':'Vs',
        'description':'Solar panel voltage (after rectifier)',
        'unit':'V',
        'lb':0,
        'ub':7.5,
        'interval':5*60,
    },
    {
        'dbtag':'idx',
        'description':'Sample index',
        'lb':24*60*60/(5*60),
        'interval':5*60,
    },
    {
        'dbtag':'c',
        'description':'1Hz ticker',
        'lb':24*60*60,
        'interval':5*60,
    },
]


if '__main__' == __name__:
    for c in conf:
        print('- - -')
        for k, v in c.items():
            print(k, ':', v)

    import sys
    sys.path.append('../..')
    from os.path import basename
    from storage.storage2 import create_table
    create_table(conf, basename(__file__).split('.')[0].replace('_', '-'))
