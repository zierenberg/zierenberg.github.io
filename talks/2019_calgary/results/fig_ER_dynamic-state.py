#!/usr/bin/python

import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.ticker as ticker

params = {'text.latex.preamble' : [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}

x_MF=numpy.logspace(-7,2,100)
m_MF=(1-x_MF)
m_MF[m_MF<0]=0

simulations=("MF","ER1","ER2", "SC")

name={  "MF" :r"$\overline{k}\approx 10^4$",\
        "ER1":r"$\overline{k}\approx 10^3$",\
        "ER2":r"$\overline{k}\approx 10^2$",\
        "SC" :r"$\overline{k}\approx 25$"}

filename={ "MF" :"../../../paper/2018_homplast_dynamic-states/data/result_avg_dynamic-state_BN_MF_T1.00e+07.dat",\
           "ER1":"../../../paper/2018_homplast_dynamic-states/data/result_avg_dynamic-state_BN_ER_p1e-1_T1e7.dat",\
           "ER2":"../../../paper/2018_homplast_dynamic-states/data/result_avg_dynamic-state_BN_ER_p1e-2_T3e7.dat",\
           "SC" :"../../../paper/2018_homplast_dynamic-states/data/result_avg_dynamic-state_metric_equilibrium.dat"}
symbol={ "MF" : 's',\
         "ER1": 'o',\
         "ER2": '^',\
         "SC" : 'v'}

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

color_tau=('#9400d3','#009e73','#56b4e9')

#color-brewer http://colorbrewer2.org/#type=diverging&scheme=RdGy&n=4 (diverging)
#color={ "MF" :'#a6611a',\
#        "ER1":'#dfc27d',\
#        "ER2":'#80cdc1',\
#        "SC" :'#018571'}

#non-equilibrium approx
NE_file={ "tau1e3":"../../../paper/2018_homplast_dynamic-states/data/calculations/result_numeric_evaluation_avg-m_BN_A1.00e+01_tau1.00e+03.dat",\
          "tau1e4":"../../../paper/2018_homplast_dynamic-states/data/calculations/result_numeric_evaluation_avg-m_BN_A1.00e+01_tau1.00e+04.dat",\
          "tau1e5":"../../../paper/2018_homplast_dynamic-states/data/calculations/result_numeric_evaluation_avg-m_BN_A1.00e+01_tau1.00e+05.dat"}

NE_bound={  "tau1e3":1e-4,\
            "tau1e4":1e-5,\
            "tau1e5":2e-6}

NE_label={  "tau1e3":r'$\tau^{\prime}=10^2${ms}',\
            "tau1e4":r'$\tau^{\prime}=10^3${ms}',\
            "tau1e5":r'$\tau^{\prime}=10^4${ms}'} 


matplotlib.rcParams['text.latex.preview'] = True
###############################################################figure
for i in [1,2,3,4,5,6]:
    fig=plt.figure(figsize=(3.375, 2.30))
    plt.rcParams.update({'axes.titlesize':  12})
    plt.rcParams.update({'axes.labelsize':  12})
    plt.rcParams.update({'font.size':       12})
    plt.rcParams.update({'legend.fontsize': 10})
    plt.rcParams.update({'xtick.labelsize': 10})
    plt.rcParams.update({'ytick.labelsize': 10})
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
        for k,sim in enumerate(simulations):
            if i+k > 3:
                x_sim,m_sim,err_sim = numpy.loadtxt(filename[sim],usecols=(0,1,2),unpack=True)
                x_sim /= 1e-3
                ax1.errorbar(x_sim,m_sim, yerr=err_sim, fmt=symbol[sim], label=r'\makebox[1.5cm][l]{%s}'%name[sim], color=color[sim], mec=color[sim], markersize=3, capsize=2)
        ax1.legend(loc='upper right', frameon=False, markerscale=1, numpoints=1) 
    
    # plot all predictions
    ax1.plot(x_MF,m_MF,'black',lw=0.5)
    if i>5:
        for j, tau in enumerate(['tau1e3','tau1e4','tau1e5']):
            x_NE,m_NE = numpy.loadtxt(NE_file[tau], usecols=(0,1), unpack=True)
            x_NE /= 10
            mask  = x_NE<NE_bound[tau]
            ax1.plot(x_NE[mask], m_NE[mask], ls='dashed', dashes=(3,1), lw=0.5, color=color_tau[j], label=NE_label[tau])
            #ax1.legend(loc='lower left', frameon=False, markerfirst=False, markerscale=1, numpoints=1)
    
    #plotstyle
    ax1.set_xlim([8e-7,10])
    ax1.set_ylim([0,2])
    ax1.set_xscale('log')
    ax1.set_xlabel(r'input rate $h$ / target firing rate $r^\ast$')
    ax1.set_ylabel(r'branching parameter $m$')
    ax1.set_yticks([0,1,2])
    #ax1.xaxis.set_ticks_position('bottom')
    #ax1.yaxis.set_ticks_position('left')
    ax1.xaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    ax1.xaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    ax1.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    plt.setp(ax1.get_xticklabels()[1::2], visible=False)
    #this may induce problems on laptop...
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')
    ax1.tick_params(which='both', direction='out')
    ####################################
    if i==6: 
        plt.savefig("fig_ER_dynamic-state.png", transparent=True, dpi=300)
    if i==5: 
        plt.savefig("fig_ER_dynamic-state_data.png", transparent=True, dpi=300)
    if i==4: 
        plt.savefig("fig_ER_dynamic-state_data3.png", transparent=True, dpi=300)
    if i==3: 
        plt.savefig("fig_ER_dynamic-state_data2.png", transparent=True, dpi=300)
    if i==2: 
        plt.savefig("fig_ER_dynamic-state_data1.png", transparent=True, dpi=300)
    if i==1: 
        plt.savefig("fig_ER_dynamic-state_empty.png", transparent=True, dpi=300)
