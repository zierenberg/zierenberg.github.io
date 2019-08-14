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
    s,Ps,err=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/result_avg_distribution_avalanche_sub_size_BN_MF_T1e7_h%.0e.dat"%h, usecols=(0,1,2), unpack=True)
    p_avalanche=plt.axes([0.13+0.30*i,0.1,0.24,0.75])
    p_avalanche.errorbar(s[::1],Ps[::1],yerr=err[::1],fmt='^', color=color[i], lw=0.1, markersize=2, capsize=1, mec=color[i], mfc='none', label=r'$P_\mathrm{sub}$')
    log_x=numpy.logspace(0,6,100)
    p_avalanche.plot(log_x[log_x>2e0],2*numpy.power(log_x[log_x>2e0],-3/2.),color='black',lw=0.5)
    p_avalanche.text(1e1,1e-1,r'$\sim s^{-3/2}$',size='x-small')
    p_avalanche.spines['bottom'].set_linewidth(0.5)
    p_avalanche.spines['right'].set_visible(False)
    p_avalanche.spines['top'].set_visible(False)
    p_avalanche.spines['left'].set_linewidth(0.5)
    p_avalanche.set_xscale('log')
    p_avalanche.set_yscale('log')
    p_avalanche.set_xlim([1,2e4])
    p_avalanche.set_xlabel(r'{avalanche size $s$}')
    p_avalanche.xaxis.set_ticks_position('bottom')
    p_avalanche.yaxis.set_ticks_position('left')
    p_avalanche.xaxis.set_tick_params(which='both', direction='out')
    p_avalanche.yaxis.set_tick_params(which='both', direction='out')
    p_avalanche.xaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    p_avalanche.xaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    p_avalanche.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    p_avalanche.yaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    p_avalanche.yaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    p_avalanche.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    p_avalanche.set_ylim([1e-9,1])
    plt.setp(p_avalanche.get_xticklabels()[::2], visible=False)
    if i==0:
        plt.setp(p_avalanche.get_yticklabels()[::2], visible=False)
    else:
        plt.setp(p_avalanche.get_yticklabels()[:], visible=False)

#additional labels
plt.figtext(0,0.70, r'{avalanche-size}',rotation=90)
plt.figtext(0.025,0.60, r'{distribution}',rotation=90)

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
plt.savefig("fig_avalanches_simulation_mf.png", transparent=True, dpi=300)
