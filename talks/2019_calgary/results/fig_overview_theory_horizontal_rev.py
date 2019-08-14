#!/usr/bin/python

import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.ticker as ticker


matplotlib.rcParams['text.latex.preview'] = True

params = {'text.latex.preamble' : [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
fig=plt.figure(figsize=(6.75, 2.00))
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

h_list=(1e-7,1e-6,1e-5,1e-4,1e-3)
dt=1e-3

color=('#9900DD', '#CC0000', '#CC7700', '#CCBB00', '#009900')

for i,h in enumerate(h_list):
    ######################################## activity
    data=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/processed/BN_driven_homeostatic_N010000_h%.2e_i0_T1.00e+08_seed1000_time_series_cut-1e7+30000.dat"%h, usecols=(0,),unpack=True)
    time=numpy.arange(len(data))*dt
    #convert to rate/neuron
    data = data/dt/1e4
    p_activity=plt.axes([0.09+0.20*i,0.58,0.14,0.28])
    p_activity.plot(time,data,color[i],lw=0.5)
    p_activity.plot(numpy.arange(25,30,1e-3), numpy.ones(int(5./1e-3))*(-4), color=color[i], linestyle='-', lw=1.0, solid_capstyle='butt')
#    p_activity.axvline(x=26, c='black', lw=0.5)
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
    p_activity.annotate(r'$r_t$ (Hz)', xy=(0,1), xytext=(-matplotlib.rcParams['ytick.major.pad']*2,8), ha='left', va='top', xycoords='axes fraction', textcoords='offset points')
    ######################################## avalanche size distribution
    S,PS,Err=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/result_avg_distribution_avalanche_full_size_BN_MF_T1e7_h%.0e.dat"%h, usecols=(0,1,2), unpack=True)
    s,Ps,err=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/result_avg_distribution_avalanche_sub_size_BN_MF_T1e7_h%.0e.dat"%h, usecols=(0,1,2), unpack=True)
    #p_avalanche=plt.axes([0.60, 0.20*i+0.05, 0.38, 0.12])
    p_avalanche=plt.axes([0.09+0.20*i,0.15,0.14,0.28])
    p_avalanche.errorbar(S[::1],PS[::1],yerr=Err[::1],fmt='o', color=color[i], lw=0.5, markersize=2, capsize=1, mec=color[i], label=r'$P_{\phantom{\mathrm{sub}}}$')
    p_avalanche.errorbar(s[::1],Ps[::1],yerr=err[::1],fmt='o', color=color[i], lw=0.5, markersize=2, capsize=1, mec=color[i], mfc='none', label=r'$P_\mathrm{sub}$')
    #p_avalanche.plot(S[PS>1e-9],PS[PS>1e-9],'-', color=color[i], lw=0.5)
    #p_avalanche.plot(s[Ps>1e-9],Ps[Ps>1e-9],'-', color=color[i], lw=0.5)
    #p_avalanche.fill_between(S,PS-Err,PS+Err, facecolor=color[i], alpha=0.5, lw=0)
    #p_avalanche.fill_between(s,Ps-err,Ps+err, facecolor=color[i], alpha=0.5, lw=0)
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
    p_avalanche.set_xlim([1,1e7])
    p_avalanche.set_xlabel(r'{avalanche size $s$}')
    p_avalanche.xaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    p_avalanche.xaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    p_avalanche.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    p_avalanche.yaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    p_avalanche.yaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    p_avalanche.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    plt.setp(p_avalanche.get_xticklabels()[::2], visible=False)
    plt.setp(p_avalanche.get_yticklabels()[::2], visible=False)
    p_avalanche.set_ylim([1e-9,1])
    if i==4:
        x_ana,y_ana=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/calculations/result_numeric_evaluation_shriki-priesemann_avalanche-size-dist_poisson_H10.0.dat", unpack=True)
        p_avalanche.plot(x_ana[x_ana>20],y_ana[x_ana>20],color='black', ls='--', dashes=(2,3))
        x_ana,y_ana=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/calculations/result_numeric_evaluation_shriki-priesemann_avalanche-size-dist_poisson_H00.1.dat", unpack=True)
        p_avalanche.plot(x_ana,y_ana,color='black', ls='--', dashes=(2,1))
    p_avalanche.legend(loc=(0.6,0.5), frameon=False, markerfirst=True, markerscale=1, numpoints=1,fontsize='x-small', handletextpad=-0.5)

#additional labels
plt.figtext(0,0.90, r'{neural activity}',rotation=90)
plt.figtext(0,0.41, r'{avalanche-size}',rotation=90)
plt.figtext(0.02,0.36, r'{distribution}',rotation=90)

#plt.figtext(0.4,1.1, r'{incerasing input strength}')
#ax.arrow(0.5,0.7,0.5,0.6, head_width=0.05, head_length=0.1, fc='k', ec='k')


#input legend
#ax.annotate('', xy=(1.00,0.08), xycoords='axes fraction', xytext=(1.00,0.95), arrowprops=dict(arrowstyle='->', color='black'))
#plt.figtext(0.97,0.96,r'$h/r^\ast$')
#plt.figtext(1.02,0.10,r'$1$')
plt.figtext(0.12+0*0.19,0.98,r'{$h/r^\ast=10^{-4}$}',color=color[0])
plt.figtext(0.12+1*0.19,0.98,r'{$h/r^\ast=10^{-3}$}',color=color[1])
plt.figtext(0.12+2*0.19,0.98,r'{$h/r^\ast=10^{-2}$}',color=color[2])
plt.figtext(0.12+3*0.19,0.98,r'{$h/r^\ast=10^{-1}$}',color=color[3])
plt.figtext(0.12+4*0.19,0.98,r'{$h/r^\ast=10^{0} $}',color=color[4])

#plt.show()
plt.savefig("fig_overview_theory_horizontal_rev.pdf", transparent=True)
