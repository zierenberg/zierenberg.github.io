#!/usr/bin/python

import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.ticker as ticker

#plt.style.use('./prx.mplstyle')
matplotlib.rcParams['text.latex.preview'] = True
params = {'text.latex.preamble' : [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
fig=plt.figure(figsize=(4.75, 2.70))
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
    p_activity=plt.axes([0.09+0.31*i,0.58,0.26,0.28])
    p_activity.plot(time,data,color[i],lw=0.5)
    p_activity.plot(numpy.arange(25,30,1e-3), numpy.ones(int(5./1e-3))*(-4), color=color[i], linestyle='-', lw=1.0, solid_capstyle='butt')
    p_activity.text(27,-10.,'5s',size='x-small')
    p_activity.set_ylim([-7,40])
    p_activity.spines['bottom'].set_visible(False)
    p_activity.spines['right'].set_visible(False)
    p_activity.spines['top'].set_visible(False)
    p_activity.spines['left'].set_linewidth(0.5)
    plt.setp(p_activity,xticks=[], yticks=[])
    p_activity.set_yticks([0,20,40])
    p_activity.yaxis.set_ticks_position('left')
    plt.setp(p_activity.get_yticklabels()[-1:], visible=False)
    p_activity.annotate(r'$a_t$ (Hz)', xy=(0,1), xytext=(-matplotlib.rcParams['ytick.major.pad']*2,8), ha='left', va='top', xycoords='axes fraction', textcoords='offset points')
    ######################################## avalanche size distribution
    #S,PS,Err=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/result_avg_distribution_avalanche_full_size_BN_MF_T1e7_h%.0e.dat"%h, usecols=(0,1,2), unpack=True)
    s,Ps,err=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/result_avg_distribution_avalanche_sub_size_BN_MF_T1e7_h%.0e.dat"%h, usecols=(0,1,2), unpack=True)
    #p_avalanche=plt.axes([0.60, 0.20*i+0.05, 0.38, 0.12])
    p_avalanche=plt.axes([0.09+0.31*i,0.15,0.26,0.28])
    p_avalanche.errorbar(s[::1],Ps[::1],yerr=err[::1],fmt='^', color=color[i], lw=0.1, markersize=2, capsize=1, mec=color[i], mfc='none', label=r'$P_\mathrm{sub}$')
    log_x=numpy.logspace(0,6,100)
    #p_avalanche.plot(log_x,0.5*numpy.power(log_x,-3/2.),color='black',lw=0.5)
    p_avalanche.plot(log_x[log_x>2e0],2*numpy.power(log_x[log_x>2e0],-3/2.),color='black',lw=0.5)
    p_avalanche.text(1e1,1e-1,r'$\sim s^{-3/2}$',size='x-small')
    p_avalanche.spines['bottom'].set_linewidth(0.5)
    p_avalanche.spines['right'].set_visible(False)
    p_avalanche.spines['top'].set_visible(False)
    p_avalanche.spines['left'].set_linewidth(0.5)
    p_avalanche.set_xscale('log')
    p_avalanche.set_yscale('log')
    p_avalanche.set_xlim([1,1e4])
    p_avalanche.set_xlabel(r'{avalanche size $s$}')
    p_avalanche.xaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    p_avalanche.xaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    p_avalanche.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    p_avalanche.yaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    p_avalanche.yaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    p_avalanche.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    if i==0:
        plt.setp(p_avalanche.get_xticklabels()[::2], visible=False)
        plt.setp(p_avalanche.get_yticklabels()[::2], visible=False)
    else:
        plt.setp(p_avalanche.get_xticklabels()[::2], visible=False)
        plt.setp(p_avalanche.get_yticklabels()[:], visible=False)
    p_avalanche.set_ylim([1e-9,1])
    p_avalanche.tick_params(top=False)
    if i==2:
        #x_ana,y_ana=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/calculations/result_numeric_evaluation_shriki-priesemann_avalanche-size-dist_poisson_H10.0.dat", unpack=True)
        #p_avalanche.plot(x_ana[x_ana>20],y_ana[x_ana>20],color='black', ls='--', dashes=(2,3))
        x_ana,y_ana=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/calculations/result_numeric_evaluation_shriki-priesemann_avalanche-size-dist_poisson_H00.1.dat", unpack=True)
        p_avalanche.plot(x_ana,y_ana,color='black', ls='--', dashes=(2,1))
        #Trick 17 - to specifically set the ticks I want to ...?
        #p_avalanche.set_yticks(list(p_avalanche.get_yticks()) + [1e-8,1e-6,1e-4,1e-2])
        #plt.setp(p_avalanche.get_yticklabels()[:-4], visible=False)
        #p_avalanche.set_xticks([1e0,1e2,1e4,1e6])
        #p_avalanche.set_yticks([1e-8,1e-6,1e-4,1e-2])
        #p_avalanche.annotate(r'$P_\mathrm{sub}(s)$', xy=(0,1), xytext=(-matplotlib.rcParams['ytick.major.pad'],8), ha='left', va='top', xycoords='axes fraction', textcoords='offset points')
    p_avalanche.legend(loc=(0.6,0.6), frameon=False, markerfirst=True, markerscale=1, numpoints=1,fontsize='x-small', handletextpad=-0.5)

#additional labels
plt.figtext(0,0.90, r'{spiking activity}',rotation=90)
plt.figtext(0,0.41, r'{avalanche-size}',rotation=90)
plt.figtext(0.02,0.36, r'{distribution}',rotation=90)

#input legend
#ax.annotate('', xy=(1.00,0.08), xycoords='axes fraction', xytext=(1.00,0.95), arrowprops=dict(arrowstyle='->', color='black'))
#plt.figtext(0.97,0.96,r'$h/r^\ast$')
#plt.figtext(1.02,0.10,r'$1$')
plt.figtext(0.12+0*0.19,0.98,r'{$h/r^\ast=10^{-4}$}',color=color[0])
#plt.figtext(0.12+1*0.19,0.98,r'{$h/r^\ast=10^{-3}$}',color=color[1])
plt.figtext(0.12+2*0.18,0.98,r'{$h/r^\ast=10^{-2}$}',color=color[1])
#plt.figtext(0.12+3*0.19,0.98,r'{$h/r^\ast=10^{-1}$}',color=color[3])
plt.figtext(0.12+4*0.18,0.98,r'{$h/r^\ast=10^{0} $}',color=color[2])

#plt.show()
plt.savefig("fig_overview_simulation_mf.pdf", transparent=True)
