#!/usr/bin/python

import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.ticker as ticker

#plt.style.use('./prx.mplstyle')
matplotlib.rcParams['text.latex.preview'] = True
params = {'text.latex.preamble' : [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
fig=plt.figure(figsize=(4.75, 1.00))
plt.rcParams.update(params)
plt.rcParams.update({'axes.titlesize':  8})
plt.rcParams.update({'axes.labelsize':  8})
plt.rcParams.update({'font.size':       8})
plt.rcParams.update({'legend.fontsize': 8})
plt.rcParams.update({'xtick.labelsize': 8})
plt.rcParams.update({'ytick.labelsize': 8})
plt.rcParams.update({'text.usetex':  True})
plt.rcParams.update({'savefig.bbox':  'tight'})
#sadly this is needed to fix the figure size to the predifined height and width from the style file
ax = plt.axes([0., 0., 1., 1.], frameon=False, xticks=[],yticks=[])

h_list=(1e-7,1e-5,1e-3)
dt=1e-3

color=('#9900DD', '#CC7700', '#009900')

for i,h in enumerate(h_list):
    ######################################## activity
    data=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/processed/BN_driven_homeostatic_N010000_h%.2e_i0_T1.00e+08_seed1000_time_series_cut-1e7+30000.dat"%h, usecols=(0,),unpack=True)
    time=numpy.arange(len(data))*dt
    #convert to rate/neuron
    data = data/dt/1e4
    p_activity=plt.axes([0.08+0.32*i,0.1,0.26,0.75])
    p_activity.plot(time,data,color[i],lw=0.5)
    #p_activity.plot(numpy.arange(25,30,1e-3), numpy.ones(int(5./1e-3))*(-4), color=color[i], linestyle='-', lw=1.0, solid_capstyle='butt')
    #p_activity.text(27,-10.,'5s',size='x-small')
    p_activity.set_ylim([0,40])
    p_activity.xaxis.set_ticks_position('bottom')
    p_activity.yaxis.set_ticks_position('left')
    p_activity.xaxis.set_tick_params(direction='out',length=3, pad=-1)
    p_activity.yaxis.set_tick_params(direction='out',length=3, pad=-1)
    p_activity.spines['top'].set_visible(False)
    p_activity.spines['right'].set_visible(False)
    p_activity.spines['left'].set_linewidth(0.5)
    p_activity.spines['bottom'].set_linewidth(0.5)
    plt.setp(p_activity,xticks=[], yticks=[])
    if i==0:
        p_activity.set_xticks([0,15,30])
        p_activity.set_yticks([0,20])
    else:
        p_activity.set_xticks([0,15,30])
        p_activity.set_yticks([0,20])
        plt.setp(p_activity.get_yticklabels()[:], visible=False)
    #p_activity.annotate(r'time (s)', xy=(0.65,-0.1), xytext=(5,matplotlib.rcParams['ytick.major.pad']), ha='left', va='top', xycoords='axes fraction', textcoords='offset points')
    p_activity.set_xlabel(r'time (s)', labelpad=-1.7)

#additional labels
plt.figtext(0,0.75, r'{spiking activity}',rotation=90)

#input legend
#ax.annotate('', xy=(1.00,0.08), xycoords='axes fraction', xytext=(1.00,0.95), arrowprops=dict(arrowstyle='->', color='black'))
#plt.figtext(0.97,0.96,r'$h/r^\ast$')
#plt.figtext(1.02,0.10,r'$1$')
plt.figtext(0.15,0.98,r'{$h/r^\ast=10^{-4}$}',color=color[0])
#plt.figtext(0.12+1*0.19,0.98,r'{$h/r^\ast=10^{-3}$}',color=color[1])
plt.figtext(0.47,0.98,r'{$h/r^\ast=10^{-2}$}',color=color[1])
#plt.figtext(0.12+3*0.19,0.98,r'{$h/r^\ast=10^{-1}$}',color=color[3])
plt.figtext(0.80,0.98,r'{$h/r^\ast=10^{0} $}',color=color[2])

#make arrow directly here
plt.figtext(0.4,1.2,r'increasing input strength')
#ax.arrow(0,1,1,1, head_width=0.1, head_length=0.1)
ax.annotate('', xy=(0.05,1.15), xycoords='axes fraction', xytext=(0.98,1.15), arrowprops=dict(arrowstyle='<-', color='black'))

#plt.show()
plt.savefig("fig_activity_simulation_mf.png", transparent=True, dpi=300)
