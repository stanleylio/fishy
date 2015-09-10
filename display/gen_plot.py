#!/usr/bin/python
#
# Stanley Lio, hlio@usc.edu
# All Rights Reserved. February 2015

import matplotlib
matplotlib.use('Agg')
import sys,re,json,time
sys.path.append('../storage')
import matplotlib.pyplot as plt
from datetime import timedelta
from matplotlib.dates import DateFormatter,HourLocator
from storage import storage
from config_support import *
from os.path import exists,join
from os import makedirs
#from scipy.signal import medfilt


def plot_time_series(x,y,plotfilename,title='',xlabel='',ylabel='',linelabel=None):
    plt.figure()
    plt.plot_date(x,y,linestyle='-',label=linelabel,color='r',marker=None)
    plt.legend(loc='best',framealpha=0.5)
    plt.title(title)
    plt.grid(True)

    # major tick labels
    begin = x[0]
    end = x[-1]
    timespan = end - begin
    if begin.date() == end.date():
        plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M'))
    else:
        plt.gca().xaxis.set_major_formatter(DateFormatter('%b %d %H:%M'))
    plt.gcf().autofmt_xdate()

    # minor tick density
    plt.gca().yaxis.get_major_formatter().set_useOffset(False)
    if timespan <= timedelta(days=2):
        plt.gca().xaxis.set_minor_locator(HourLocator(interval=1))
    elif timespan <= timedelta(days=7):
        plt.gca().xaxis.set_minor_locator(HourLocator(interval=3))
    elif timespan <= timedelta(days=14):
        plt.gca().xaxis.set_minor_locator(HourLocator(interval=6))
    elif timespan <= timedelta(days=21):
        plt.gca().xaxis.set_minor_locator(HourLocator(interval=12))
    plt.tight_layout()

    # auto xlabel (time)
    if '' == xlabel:
        if begin.date() == end.date():
            plt.gca().set_xlabel('UTC Time ({})'.format(begin.strftime('%Y-%m-%d')))
        else:
            plt.gca().set_xlabel('UTC Time ({} to {})'.format(\
                begin.strftime('%Y-%m-%d'),end.strftime('%Y-%m-%d')))
    else:
        plt.gca().set_xlabel(xlabel)
        
    plt.gca().set_ylabel(ylabel)
        
    plt.savefig(plotfilename,bbox_inches='tight',dpi=150)
    plt.cla()
    plt.clf()
    plt.close()


if '__main__' == __name__:
    import traceback,logging,logging.handlers,sqlite3

    # LOGGING
    '''DEBUG,INFO,WARNING,ERROR,CRITICAL'''
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    handler = logging.handlers.RotatingFileHandler('gen_plot.log',
                                         maxBytes=1e6,
                                         backupCount=10)
    logger.addHandler(handler)

    IDs = []
    time_col = None
    if is_base():
        IDs = get_list_of_nodes()
        time_col = 'ReceptionTime'
    elif is_node():
        IDs = [get_node_id()]
        time_col = 'Timestamp'

    assert time_col is not None

    for node_id in IDs:
        node_tag = 'node_{:03d}'.format(node_id)
        config_file = '../config/{}.ini'.format(node_tag)
        assert exists(config_file)
        #plot_range = 2  # days
        count = 500

        tags = get_tag(node_id)
        units = get_unit(node_id)
        mapping = dict(zip(tags,units))

        store = storage()
        
        config = read_ini(config_file)['display']
        plot_dir = config['plot_dir']
        if not exists(plot_dir):
            makedirs(plot_dir)

        variables = [c.strip() for c in config['variable'].split(',')]
        for var in variables:
            logger.info('Plotting {} of {}'.format(var,node_tag))
            unit = mapping[var]
            
            title = '{} of {}'.format(var,node_tag)
# better be sure the folder exists...
            plotfilename = '../www/{}/{}.png'.format(node_tag,var)

            try:
                tmp = store.read_latest(node_id,time_col,variables,count)
                x = tmp[time_col]
                y = [l if l is not None else float('NaN') for l in tmp[var]]

                plot_time_series(x,y,plotfilename,title,ylabel=unit,linelabel=var)

            except (TypeError,sqlite3.OperationalError) as e:
                #print traceback.print_exc()
                logger.warning('SQLite error (no record of {} for {}?)'.\
                               format(var,node_tag))

                
