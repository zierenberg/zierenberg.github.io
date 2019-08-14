#!/usr/bin/python

import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.ticker as ticker

params = {'text.latex.preamble' : [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}

def x_from_tau(tau):
    return 1-numpy.exp(-1/tau)

#THEORY
x_MF=numpy.logspace(-7,2,100)
tau_MF=numpy.ones(len(x_MF))*0.5
mask = x_MF < x_from_tau(0.5)
tau_MF[mask] = -1./numpy.log(1-x_MF[mask])



simulations=("ER1","ER2")

name={  "MF" :r"AA $\overline{k}\approx 10^4$",\
        "ER1":r"$P(r^\ast)=\delta(r^\ast-1)$",\
        "ER2":r"$P(r^\ast)=\frac{1}{r^\ast\sqrt{2\pi}}e^{-\frac{(\ln r^\ast - 0.5)^2}{2}}$",\
        "SC" :r"SC $\overline{k}\approx 25$"}

filename={ "MF" :"../../../paper/2018_homplast_dynamic-states/data/result_avg_tau_BN_MF_T1e7.dat",\
           "ER1":"../../../paper/2018_homplast_dynamic-states/data/result_avg_tau_BN_ER_p1e-1_T1e7.dat",\
           "ER2":"../../../paper/2018_homplast_dynamic-states/data/result_avg_tau_log-normal_ER_p1e-1.dat",\
           "SC" :"../../../paper/2018_homplast_dynamic-states/data/result_avg_tau_metric.dat"}
symbol={ "MF" : 's',\
         "ER1": 'o',\
         "ER2": '^',\
         "SC" : 'v'}

rtarget={"ER1":1e-3, "ER2":numpy.exp(1)*1e-3}

#color-brewer http://colorbrewer2.org/#type=diverging&scheme=RdGy&n=4 (qualitative)
#color={ "MF" :'#a6cee3',\
#        "ER1":'#1f78b4',\
#        "ER2":'#b2df8a',\
#        "SC" :'#33a02c'}

#color from gnuplot
color={ "MF" :'#9400d3',\
        "ER1":'#009e73',\
        "ER2":'#56b4e9',\
        "SC" :'#e69f00'}

#color-brewer http://colorbrewer2.org/#type=diverging&scheme=RdGy&n=4 (diverging)
#color={ "MF" :'#a6611a',\
#        "ER1":'#dfc27d',\
#        "ER2":'#80cdc1',\
#        "SC" :'#018571'}


x_MF=numpy.logspace(-7,2,100)
m_MF=(1-x_MF)
m_MF[m_MF<0]=0
matplotlib.rcParams['text.latex.preview'] = True
###############################################################figure
for i in [1,2]:
    fig=plt.figure(figsize=(3.375, 2.30))
    plt.rcParams.update({'axes.titlesize': 10})
    plt.rcParams.update({'axes.labelsize':   12})
    plt.rcParams.update({'font.size':        12})
    plt.rcParams.update({'legend.fontsize':  10})
    plt.rcParams.update({'xtick.labelsize':  10})
    plt.rcParams.update({'ytick.labelsize':  10})
    plt.rcParams.update({'text.usetex':  True})
    plt.rcParams.update({'savefig.bbox':  'tight'})
    ax1=fig.add_subplot(111)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_linewidth(0.5)
    ax1.spines['bottom'].set_linewidth(0.5)
    # plot all data
    if i>1:
        plt.setp(ax1,xticks=[], yticks=[])
        for sim in simulations:
            x_sim,m_sim,err_sim = numpy.loadtxt(filename[sim],usecols=(0,1,2),unpack=True)
            x_sim /= rtarget[sim]
            ax1.errorbar(x_sim,m_sim, yerr=err_sim, fmt=symbol[sim], label=r'\makebox[3.3cm][l]{%s}'%name[sim], color=color[sim], mec=color[sim], markersize=3, capsize=2)
        ax1.legend(loc='upper right', frameon=False, markerfirst=True, markerscale=1, numpoints=1) 
    # plot all predictions
    ax1.plot(x_MF,tau_MF,'black',lw=0.5)
    if i>1:
        for j, k in enumerate([1e3]):
            x_NE   = x_MF
            tau_NE = numpy.ones(len(x_NE))*1e6/k 
            mask  = x_NE < x_from_tau(1e6/k)*2
            ax1.plot(x_NE[mask], tau_NE[mask], ls='dashed', lw=1.0, dashes=(2,2), color=color[simulations[j]])
    
    #plotstyle
    ax1.set_xlim([8e-7,10])
    ax1.set_ylim([1e-1,1e6])
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax1.set_xlabel(r'input rate $h$ / avg. target firing rate $r^\ast$')
    ax1.set_ylabel(r'autocorrelation time $\tau$ (ms)')
    ax1.xaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    ax1.xaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    ax1.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax1.yaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    ax1.yaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    ax1.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    ax1.tick_params(direction='out',top='off', right='off', which='both')
    plt.setp(ax1.get_xticklabels()[1::2], visible=False)
    plt.setp(ax1.get_yticklabels()[1::2], visible=False)
    #this may induce problems on laptop...
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')
    ax1.tick_params(which='both', direction='out')
    ####################################
    if i==2:
        plt.savefig("fig_log-norm_tau.pdf", transparent=True)
    if i==1:
        plt.savefig("fig_log-norm_tau_empty.pdf", transparent=True)
