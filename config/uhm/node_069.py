# -*- coding: utf-8 -*-
name = "Moli'i cellular Water Level"
location = "Moli'i"
note = 'Cellular ultrasonic tide gauge. Each sample is average of 60 measurements taken every second. One transmission every 10 samples. Firmware p5d, hardware v0.2.'
google_earth_link = 'https://goo.gl/maps/C7bPidpD5Km'

coreid = '4d0057001851353338363036'


conf = [
    {
        'dbtag':'Timestamp',
        'description':'Sample time (device clock)',
    },
    {
        'dbtag':'d2w',
        'unit':'mm',
        'description':'Distance from sensor to water surface',
        'lb':300,
        'ub':5000,
    },
    {
        'dbtag':'VbattV',
        'unit':'V',
        'description':'Battery voltage',
        'lb':3.7,
        'ub':5.5,
    },
    {
        'dbtag':'SoC',
        'unit':'%',
        'description':'State of Charge',
        'lb':30,    # the meaning has changed: it was a "boundary of sane readings", now it's "warning level"
        'ub':100,
    },
    {
        'dbtag':'sample_size',
        'description':'Number of valid readings in the 60 measurements',
        'lb':0,
        'ub':60,
    },
]


if '__main__' == __name__:
    for c in conf:
        print('- - -')
        for k,v in c.iteritems():
            print(k,':',v)

    import sys
    sys.path.append('../..')
    from os.path import basename
    from storage.storage2 import create_table
    create_table(conf,basename(__file__).split('.')[0].replace('_','-'))
