# -*- coding: utf-8 -*-
# kph2
name = 'Coco'
location = 'Site #4, Kāneʻohe Bay'
note = 'SeaFET pH Sensor; pole on a pole on a reef'

#interval = 15*60   # second
#plot_range = 24*7  # hour
#data_source = '/home/nuc/node/www/poh/storage/sensor_data.db'


conf = [
    {
        'dbtag':'ticker',
        'dbtype':'INTEGER',
        'comtag':None,
        'unit':None,
        'description':'Voltage report sequence number',
        'lb':0,
    },
    {
        'dbtag':'Vbatt',
        'dbtype':'REAL',
        'comtag':None,
        'unit':'V',
        'description':'Relay dongle battery voltage',
        'lb':2.5,
        'ub':5.2,
    },
    {
        'dbtag':'DATE',
        'dbtype':'INTEGER',
        'comtag':'DATE',
        'unit':None,
        'description':'Sample Date (UTC) in format, YYYYDDD',
        'plot':False,
    },
    {
        'dbtag':'TIME',
        'dbtype':'REAL',
        'comtag':'TIME',
        'unit':None,
        'description':'Sample Time (UTC) in format, DESCIMALHOUR',
        'plot':False,
    },
    {
        'dbtag':'PH_INT',
        'dbtype':'REAL',
        'comtag':'PH_INT',
        'unit':None,
        'description':'FET|INT calculated pH in total scale',
        'lb':7,
        'ub':8.5,
    },
    {
        'dbtag':'PH_EXT',
        'dbtype':'REAL',
        'comtag':'PH_EXT',
        'unit':None,
        'description':'FET|EXT calculated pH in total scale',
        'lb':7,
        'ub':8.5,
    },
    {
        'dbtag':'TEMP',
        'dbtype':'REAL',
        'comtag':'TEMP',
        'unit':'Deg.C',
        'description':'ISFET Thermistor temperature',
    },
    {
        'dbtag':'TEMP_CTD',
        'dbtype':'REAL',
        'comtag':'TEMP_CTD',
        'unit':'Deg.C',
        'description':'CTD temperature',
    },
    {
        'dbtag':'S_CTD',
        'dbtype':'REAL',
        'comtag':'S_CTD',
        'unit':'psu',
        'description':'CTD salinity',
    },
    {
        'dbtag':'O_CTD',
        'dbtype':'REAL',
        'comtag':'O_CTD',
        'unit':'ml/L',
        'description':'CTD oxygen concentration',
    },
    {
        'dbtag':'P_CTD',
        'dbtype':'REAL',
        'comtag':'P_CTD',
        'unit':'dbar',
        'description':'CTD pressure',
        'plot':False,
    },
    {
        'dbtag':'Vrs_FET_INT',
        'dbtype':'REAL',
        'comtag':'Vrs(FET|INT)',
        'unit':'V',
        'description':'FET|INT voltage',
        'plot':False,
    },
    {
        'dbtag':'Vrs_FET_EXT',
        'dbtype':'REAL',
        'comtag':'Vrs(FET|EXT)',
        'unit':'V',
        'description':'FET|EXT voltage',
        'plot':False,
    },
    {
        'dbtag':'V_THERM',
        'dbtype':'REAL',
        'comtag':'V_THERM',
        'unit':'V',
        'description':'Thermistor voltage',
        'plot':False,
    },
    {
        'dbtag':'V_SUPPLY',
        'dbtype':'REAL',
        'comtag':'V_SUPPLY',
        'unit':'V',
        'description':'Supply voltage',
        'plot':False,
    },
    {
        'dbtag':'I_SUPPLY',
        'dbtype':'REAL',
        'comtag':'I_SUPPLY',
        'unit':'mA',
        'description':'Supply current',
        'plot':False,
    },
    {
        'dbtag':'HUMIDITY',
        'dbtype':'REAL',
        'comtag':'HUMIDITY',
        'unit':'%',
        'description':'Electronics compartment relative humidity',
    },
    {
        'dbtag':'V_5V',
        'dbtype':'REAL',
        'comtag':'V_5V',
        'unit':'V',
        'description':'Internal 5V supply voltage',
        'plot':False,
    },
    {
        'dbtag':'V_MBATT',
        'dbtype':'REAL',
        'comtag':'V_MBATT',
        'unit':'V',
        'description':'Main battery pack voltage',
    },
    {
        'dbtag':'V_ISO',
        'dbtype':'REAL',
        'comtag':'V_ISO',
        'unit':'V',
        'description':'Internal isolated supply voltage',
        'plot':False,
    },
    {
        'dbtag':'V_ISOBATT',
        'dbtype':'REAL',
        'comtag':'V_ISOBATT',
        'unit':'V',
        'description':'Isolated battery pack voltage',
    },
    {
        'dbtag':'I_B',
        'dbtype':'REAL',
        'comtag':'I_B',
        'unit':'nA',
        'description':'Substrate leakage current',
        'plot':False,
    },
    {
        'dbtag':'I_K',
        'dbtype':'REAL',
        'comtag':'I_K',
        'unit':'nA',
        'description':'Counter electrode leakage current',
        'plot':False,
    },
    {
        'dbtag':'V_K',
        'dbtype':'REAL',
        'comtag':'V_K',
        'unit':'V',
        'description':'Counter electrode voltage',
        'plot':False,
    },
    {
        'dbtag':'STATUS',
        'dbtype':'TEXT',
        'comtag':'STATUS',
        'unit':None,
        'description':'Status word',
        'plot':False,
    },
]


if '__main__' == __name__:
    for c in conf:
        print '- - -'
        for k,v in c.iteritems():
            print k, ':' ,v

    import sys
    sys.path.append('../..')
    from storage.storage2 import create_table
    create_table(conf,__file__.split('.')[0].replace('_','-'))
    
