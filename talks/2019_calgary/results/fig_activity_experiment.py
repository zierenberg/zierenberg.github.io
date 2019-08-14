#!/usr/bin/python

import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.ticker as ticker

#plt.style.use('./prx.mplstyle')
matplotlib.rcParams['text.latex.preview'] = True
params = {'text.latex.preamble' : [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
fig=plt.figure(figsize=(4.75, 1.00*2))
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
        "vitro2":'#9900DD',\
        "vivo1" :'#CC7700',\
        "vivo2" :'#CC7700'}
#CC0000

for i,exp in enumerate(experiments):
    ######################################## activity
    col=1
    if exp=="vivo2":
        col=0
    data=numpy.loadtxt(activity[exp], usecols=(col,),unpack=True)
    time=numpy.arange(len(data))*dt[exp]
    #convert to rate/neuron
    data=data/dt[exp]/num_electrodes[exp]
    if i<2:
        p_activity=plt.axes([0.08+0.32*(i),0.1/2.+0.55,0.26,0.75/2.])
    else:
        p_activity=plt.axes([0.08+0.32*(i-2),0.1/2.-0.05,0.26,0.75/2.])
    p_activity.plot(time,data,color[exp],lw=0.5)
    #p_activity.plot(numpy.arange(25,30,1e-3), numpy.ones(int(5./1e-3))*(-4), color=color[i], linestyle='-', lw=1.0, solid_capstyle='butt')
    #p_activity.text(27,-10.,'5s',size='x-small')
    p_activity.set_ylim([0,150])
    p_activity.xaxis.set_ticks_position('bottom')
    p_activity.yaxis.set_ticks_position('left')
    p_activity.xaxis.set_tick_params(direction='out',length=3, pad=-1)
    p_activity.yaxis.set_tick_params(direction='out',length=3, pad=-1)
    p_activity.spines['top'].set_visible(False)
    p_activity.spines['right'].set_visible(False)
    p_activity.spines['left'].set_linewidth(0.5)
    p_activity.spines['bottom'].set_linewidth(0.5)
    plt.setp(p_activity,xticks=[], yticks=[])
    if i==0 or i==2:
        p_activity.set_xticks([0,15,30])
        p_activity.set_yticks([0,100])
    else:
        p_activity.set_xticks([0,15,30])
        p_activity.set_yticks([0,100])
        plt.setp(p_activity.get_yticklabels()[:], visible=False)
    #p_activity.annotate(r'time (s)', xy=(0.65,-0.1), xytext=(5,matplotlib.rcParams['ytick.major.pad']), ha='left', va='top', xycoords='axes fraction', textcoords='offset points')
    p_activity.set_xlabel(r'time (s)', labelpad=-1.7)
    #exp label
    p_activity.text(10,110,name[exp])
    #p_activity.set_xlabel(r'$r\approx %s$\,Hz'%rate[exp], labelpad=0.5)

#additional labels
plt.figtext(0,0.92, r'{spiking activity}',rotation=90)
plt.figtext(0,0.30, r'{spiking activity}',rotation=90)

#plt.show()
plt.savefig("fig_activity_experiment.pdf", transparent=True)
