#!/usr/bin/python
#
# Stanley Lio, hlio@usc.edu
# All Rights Reserved. February 2015
import matplotlib,numpy,traceback
matplotlib.use('Agg')
import sys,logging
from os.path import expanduser
sys.path.append(expanduser('~'))
from node.helper import ts2dt
import matplotlib.pyplot as plt
from datetime import datetime,timedelta
from matplotlib.dates import DateFormatter,HourLocator
#from config.config_support import *


def auto_tick(ax):
    x = ax.get_lines()[0].get_xdata()
    y = ax.get_lines()[0].get_ydata()

    # major tick labels
    # Not x[0] and x[-1] because x is not always sorted in ascending order.
    #
    # ... ORDER BY ... DESC... because otherwise sqlite will return the first
    # N readings - so if the latest N readings are wanted, they should be at
    # the first N readings (even though they are sorted in descending order)
    # For plotting the order doesn't matter because the samples are timestamped.

    # "locate the earliest timestamp at which time the sample is not an NaN"
    # nan in numpy.float64 is not float('nan')... and
    # certainly not None, and "is not" won't work either
    nonnull = [z[0] for z in zip(x,y) if not numpy.isnan(z[1])]
    if len(nonnull) <= 0:
        logging.debug('no data or all NaNs')
        return
    begin = min(nonnull)
    end = max(x)
    # why not?
    #end = max([z[0] for z in zip(x,y) if not numpy.isnan(z[1])])

    # show/hide the date in the time axis labels
    if begin.date() == end.date():
        ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    else:
        ax.xaxis.set_major_formatter(DateFormatter('%b %d %H:%M'))
    plt.gcf().autofmt_xdate()

    # set minor tick density
    ax.yaxis.get_major_formatter().set_useOffset(False)
    timespan = end - begin
    if timespan <= timedelta(days=2):
        ax.xaxis.set_minor_locator(HourLocator(interval=1))
    elif timespan <= timedelta(days=7):
        ax.xaxis.set_minor_locator(HourLocator(interval=3))
    elif timespan <= timedelta(days=14):
        ax.xaxis.set_minor_locator(HourLocator(interval=6))
    elif timespan <= timedelta(days=21):
        ax.xaxis.set_minor_locator(HourLocator(interval=12))
    plt.tight_layout()


def plot_multi_time_series(data,plotfilename,title='',xlabel='',ylabel='',loc='best'):
    plt.figure()

    for d in data:
        # maybe use python's own kargs instead? TODO
        x = d['x']
        y = d['y']
        label = d.get('linelabel',None)
        color = d.get('color',None)
        linestyle = d.get('linestyle','')
        marker = d.get('marker','.')
        markersize = d.get('markersize',1)

        #print x[0]
        #print type(x[0])

        if type(x[0]) is not datetime:
            x = [ts2dt(tmp) for tmp in x]
        
        #print(color,linestyle,marker,markersize)

        plt.plot_date(x,y,
                      linestyle=linestyle,
                      label=label,
                      color=color,
                      marker=marker,
                      markersize=markersize)

        #import matplotlib.patches as mpatches
        #red_patch = mpatches.Patch()
        #plt.legend(handles=[red_patch])

        #import matplotlib.lines as mlines
        #blue_line = mlines.Line2D([], [], marker='.',
                          #markersize=15, label='stuff')
        #plt.legend(handles=[blue_line])

    plt.legend(loc=loc,framealpha=0.5)
    plt.title(title)
    plt.grid(True)

    auto_tick(plt.gca())
    
    if '' == xlabel:
        #auto_xlabel(plt.gca())
        #begin = data[0]['x'][0]
        begin = x[0]
        end = begin
        for d in data:
            #x,y = d['x'],d['y']
            b = min([z[0] for z in zip(x,y) if not numpy.isnan(z[1])])
            if b < begin:
                begin = b
            e = max([z[0] for z in zip(x,y) if not numpy.isnan(z[1])])
            if e > end:
                end = e
        plt.gca().set_xlabel('UTC Time ({} to {})'.\
                             format(begin.strftime('%Y-%m-%d'),\
                                    end.strftime('%Y-%m-%d')))
    else:
        plt.gca().set_xlabel(xlabel)
        
    plt.gca().set_ylabel(ylabel)

    # make the markers in the legend bigger in order to show the color
    try:
        tmp = plt.gca().get_legend()
        if tmp is not None:
            for h in tmp.legendHandles:
                h.set_marker('.')
                #h.set_color('red')
                h.set_markersize(8)
    except:
        traceback.print_exc()

    plt.savefig(plotfilename,bbox_inches='tight',dpi=600)
    plt.cla()
    plt.clf()
    plt.close()


def plot_time_series(x,y,plotfilename,title='',xlabel='',ylabel='',linelabel=None,color='#1f77b4',linestyle='-',marker='.',markersize=1):
    assert len(x) == len(y)
    assert len(x) > 0
    assert len(plotfilename) > 0

    # replace any None with float('nan')
    y = [yy if yy is not None else float('nan') for yy in y]

    # locate the start and end dates on which the data is not float('nan')
    if '' == xlabel:
        z = zip(x,y)
        z = [zz[0] for zz in z]
        begin = min(z)
        end = max(z)
        if type(begin) is float:
            begin = ts2dt(begin)
        if type(end) is float:
            end = ts2dt(end)
        if begin.date() == end.date():
            xlabel = 'UTC Time ({})'.format(begin.strftime('%Y-%m-%d'))
        else:
            xlabel = 'UTC Time ({} to {})'.\
                     format(begin.strftime('%Y-%m-%d'),\
                            end.strftime('%Y-%m-%d'))

    data = [{'x':x,'y':y,'linelabel':linelabel,'color':color,'linestyle':linestyle,'marker':marker,'markersize':markersize}]
    
    plot_multi_time_series(data,plotfilename,
                           title=title,
                           xlabel=xlabel,
                           ylabel=ylabel)

