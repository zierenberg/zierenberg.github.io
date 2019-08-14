#!/usr/bin/python

import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.ticker as ticker

#plt.style.use('./prx2.mplstyle')

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

#experiments=("vitro1","vitro2","vivo1","vivo2")
experiments=("vitro1","vitro2","vivo1","vivo2")

name={  "vitro1":r"exp 1",\
        "vitro2":r"exp 2",\
        "vivo1" :r"rat CA1",\
        "vivo2" :r"cat V1 "}

dt={ "vitro1":4e-3,\
     "vitro2":4e-3,\
     "vivo1" :4e-3,\
     "vivo2" :4e-3}

rate={  "vitro1":9,\
        "vitro2":5,\
        "vivo1" :11,\
        "vivo2" :7}

num_electrodes={ "vitro1":58,\
                 "vitro2":58,\
                 "vivo1" :31,\
                 "vivo2" :50} 

activity={ "vitro1":"../../../paper/2018_homplast_dynamic-states/data/Exp_Wagenaar2005_rat_dense/result_8-2-34_populationActivity_cut_1000-1030.dat",\
           "vitro2":"../../../paper/2018_homplast_dynamic-states/data/Exp_Wagenaar2005_rat_dense/result_7-2-35_populationActivity_cut_1000-1030.dat",\
           "vivo1" :"../../../paper/2018_homplast_dynamic-states/data/Exp_Rat_Miszukeki_Hippocampus/result_ec013.527_populationActivity_cut_1000-1030.dat",\
           "vivo2" :"../../../paper/2018_homplast_dynamic-states/data/Exp_Blanche2009_cat/Cactivity.txt"}
avalanche={"vitro1":"../../../paper/2018_homplast_dynamic-states/data/Exp_Wagenaar2005_rat_dense/result_8-2-34_avalancheSize.dat",\
           "vitro2":"../../../paper/2018_homplast_dynamic-states/data/Exp_Wagenaar2005_rat_dense/result_7-2-35_avalancheSize.dat",\
           "vivo1" :"../../../paper/2018_homplast_dynamic-states/data/Exp_Rat_Miszukeki_Hippocampus/result_ec013.527_avalancheSize.dat",\
           "vivo2" :"../../../paper/2018_homplast_dynamic-states/data/Exp_Blanche2009_cat/avalanches.txt"}

color={ "vitro1":'#9900DD',\
        "vitro2":'#CC0000',\
        "vivo1" :'#CC7700',\
        "vivo2" :'#CC7700'}

for i,exp in enumerate(experiments):
    ######################################## activity
    col=1
    if exp=="vivo2":
        col=0
    data=numpy.loadtxt(activity[exp], usecols=(col,),unpack=True)
    time=numpy.arange(len(data))*4e-3
    #convert to rate=spikes/dt/channel
    data=data/dt[exp]/num_electrodes[exp]
    p_activity=plt.axes([0.09+0.24*i,0.58,0.16,0.28])
    p_activity.plot(time,data,color[exp],lw=0.5)
    p_activity.plot(numpy.arange(25,30,4e-3), numpy.ones(int(5./4e-3))*(-10), color=color[exp], linestyle='-', lw=1.0, solid_capstyle='butt')
    p_activity.text(27,-35.,'5s',size='x-small')
    p_activity.set_ylim([-20,150])
    p_activity.spines['bottom'].set_visible(False)
    p_activity.spines['right'].set_visible(False)
    p_activity.spines['top'].set_visible(False)
    p_activity.spines['left'].set_linewidth(0.5)
    plt.setp(p_activity,xticks=[], yticks=[])
    p_activity.set_yticks([0,100])
    p_activity.yaxis.set_ticks_position('left')
    p_activity.annotate(r'$a_t$ (Hz)', xy=(0,1), xytext=(-matplotlib.rcParams['ytick.major.pad']*2,8), ha='left', va='top', xycoords='axes fraction', textcoords='offset points')
    # exp label
    p_activity.text(10,110,name[exp])
    p_activity.set_xlabel(r'$r\approx %s$\,Hz'%rate[exp], labelpad=0.5)
#    p_activity.text(ccccc,,transform=p_activity.transAxes, va='bottom', ha='right')
    ######################################## avalanche size distribution
    s,Ps=numpy.loadtxt(avalanche[exp], usecols=(0,1), unpack=True)
    p_avalanche=plt.axes([0.09+0.24*i,0.15,0.16,0.28])
    p_avalanche.plot(s,Ps,'o', color=color[exp], lw=0.5, markersize=2, mec=color[exp], mfc='none')
    log_x=numpy.logspace(0,4,100)
    p_avalanche.plot(log_x[log_x>2e0],2*numpy.power(log_x[log_x>2e0],-3/2.),color='black',lw=0.5)
    p_avalanche.text(1e3,1e-4,r'$\sim s^{-3/2}$',size='small')
    if exp=="vivo2":
        BN_x,BN_y=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/result_avg_distribution_avalanche_cat_sub_size_BN_MF.dat", unpack=True)
        p_avalanche.plot(BN_x,BN_y,color='black',ls='dashed', lw=1, dashes=(2,1))
        p_avalanche.text(1e3,2e-8,r'matched',size='small')
    if exp=="vivo1":
        BN_x,BN_y=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/result_avg_distribution_avalanche_rat_sub_size_BN_MF.dat", unpack=True)
        p_avalanche.plot(BN_x,BN_y,color='black',ls='dashed', lw=1, dashes=(2,1))
        p_avalanche.text(1e3,2e-8,r'matched',size='small')
    p_avalanche.spines['bottom'].set_linewidth(0.5)
    p_avalanche.spines['right'].set_visible(False)
    p_avalanche.spines['top'].set_visible(False)
    p_avalanche.spines['left'].set_linewidth(0.5)
    p_avalanche.xaxis.set_ticks_position('bottom')
    p_avalanche.yaxis.set_ticks_position('left')
    p_avalanche.set_xscale('log')
    p_avalanche.set_yscale('log')
    p_avalanche.set_xlim([1,2e4])
    p_avalanche.set_xlabel(r'{avalanche size $s$}')
    p_avalanche.xaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    p_avalanche.xaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    p_avalanche.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    p_avalanche.yaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
    p_avalanche.yaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
    p_avalanche.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    p_avalanche.annotate(r'$P_\mathrm{sub}$', xy=(0,1), xytext=(-matplotlib.rcParams['ytick.major.pad']*1.5,8), ha='left', va='top', xycoords='axes fraction', textcoords='offset points')
    plt.setp(p_avalanche.get_xticklabels()[::2], visible=False)
    plt.setp(p_avalanche.get_yticklabels()[::2], visible=False)
    p_avalanche.set_ylim([1e-9,1])

#additional labels
plt.figtext(0.26,1.00,r' \textit{cultures}', size='large')
plt.figtext(0.73,1.00,r' \textit{brain}',    size='large')
plt.figtext(0,0.90, r'{spiking activity}',rotation=90)
plt.figtext(0,0.41, r'{avalanche-size}',rotation=90)
plt.figtext(0.02,0.36, r'{distribution}',rotation=90)

#plt.show()
plt.savefig("fig_overview_experiment.png", transparent=True, dpi=300)
