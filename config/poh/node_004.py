# -*- coding: utf-8 -*-
name = 'Oxygen and Depth'
location = 'Mākāhā 1'
note = 'Beaglebone-based node measuring oxygen, temperature and water depth'

# node stuff
INTERVAL = 5*60
NGROUP = 5

LOGDIR = '/var/uhcm/log'
DBPATH = '/var/uhcm/storage/sensor_data.db'


from node.config.config_support import Range


conf = [
    {
        'dbtag':'Timestamp',
        'dbtype':'TIMESTAMP',
        'comtag':'ts',
        'unit':None,
        'description':'Time of sampling',
        'plot':False,
    },
    {
        'dbtag':'P_180',
        'dbtype':'REAL',
        'unit':'Pa',
        'description':'Barometric pressure (BMP180)',
        'plot':True,
        'range':Range(90e3,110e3),
    },
    {
        'dbtag':'T_180',
        'dbtype':'REAL',
        'unit':'Deg.C',
        'description':'Enclosure temperature (BMP180)',
        'plot':True,
        'range':Range(-10,80),
    },
    {
        'dbtag':'P_5803',
        'dbtype':'REAL',
        'unit':'kPa',
        'description':'Water pressure (MS5803-14BA)',
        'plot':True,
        'range':Range(80,150),
    },
    {
        'dbtag':'T_5803',
        'dbtype':'REAL',
        'unit':'Deg.C',
        'description':'Water temperature (MS5803-14BA)',
        'plot':True,
        'range':Range(-10,60),
    },
    {
        'dbtag':'O2Concentration',
        'dbtype':'REAL',
        'comtag':'O2',
        'unit':'uM',
        'description':'Oxygen concentration (4330F)',
        'plot':True,
        'range':Range(0,450),
    },
    {
        'dbtag':'AirSaturation',
        'dbtype':'REAL',
        'comtag':'Air',
        'unit':'%',
        'description':'Air saturation (4330F)',
        'plot':True,
        'range':Range(0,150),
    },
    {
        'dbtag':'Temperature',
        'dbtype':'REAL',
        'comtag':'T_4330f',
        'unit':'Deg.C',
        'description':'Water temperature (4330F)',
        'plot':True,
        'range':Range(-20,60),
    },
    {
        'dbtag':'CalPhase',
        'dbtype':'REAL',
        'unit':'Deg',
        'description':'CalPhase',
        'plot':False,
    },
    {
        'dbtag':'TCPhase',
        'dbtype':'REAL',
        'unit':'Deg',
        'description':'TCPhase',
        'plot':False,
    },
    {
        'dbtag':'C1RPh',
        'dbtype':'REAL',
        'unit':'Deg',
        'description':'C1RPh',
        'plot':False,
    },
    {
        'dbtag':'C2RPh',
        'dbtype':'REAL',
        'unit':'Deg',
        'description':'C2RPh',
        'plot':False,
    },
    {
        'dbtag':'C1Amp',
        'dbtype':'REAL',
        'unit':'mV',
        'description':'C1Amp',
        'plot':False,
    },
    {
        'dbtag':'C2Amp',
        'dbtype':'REAL',
        'unit':'mV',
        'description':'C2Amp',
        'plot':False,
    },
    {
        'dbtag':'RawTemp',
        'dbtype':'REAL',
        'unit':'mV',
        'description':'RawTemp',
        'plot':False,
    },
]


if '__main__' == __name__:
    for c in conf:
        print '- - -'
        for k,v in c.iteritems():
            print k, ':' ,v

