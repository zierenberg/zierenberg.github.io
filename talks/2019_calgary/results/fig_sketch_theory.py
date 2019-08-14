#!/usr/bin/python

import numpy
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.collections as collections
import matplotlib.ticker as ticker

#
#set term epslatex size 8.6cm,6cm standalone color solid 8 
#set output "fig_sketch_theory.tex"


#tau_x, tau_val, tau_err = numpy.loadtxt("../data/result_avg_tau_BN_MF_T1e7.dat",usecols=(0,1,2), unpack=True)
#tau_x/=1e-3
#m_x, m_val, m_err = numpy.loadtxt("../data/result_avg_dynamic-state_BN_MF_T1.00e+07.dat",usecols=(0,1,2), unpack=True)
#m_x/=1e-3

tau_x, tau_val, tau_err = numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/result_avg_tau_BN_ER_p1e-1_T1e7.dat",usecols=(0,1,2), unpack=True)
tau_x/=1e-3
m_x, m_val, m_err = numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/result_avg_dynamic-state_BN_ER_p1e-1_T1e7.dat",usecols=(0,1,2), unpack=True)
m_x/=1e-3

#tau_x, tau_val, tau_err = numpy.loadtxt("../data/result_avg_tau_BP_T1e7.dat",usecols=(0,1,2), unpack=True)
#tau_x/=10
#m_x, m_val, m_err = numpy.loadtxt("../data/result_avg_dynamic-state_BP_T1.00e+07.dat",usecols=(0,1,2), unpack=True)
#m_x/=10

x=numpy.logspace(-7,0,1000)

mean_field=(1-x)
mean_field[mean_field<0]=0
#non_equil=numpy.loadtxt('../data/calculations/result_numeric_evaluation_avg-m_BN_A1.00e+01_tau1.00e+03.dat', usecols=(0,1), unpack=True)
non_equil=numpy.loadtxt('../../../paper/2018_homplast_dynamic-states/data/calculations/result_numeric_evaluation_avg-m_BN_A1.00e+01_tau1.00e+04.dat', usecols=(0,1), unpack=True)
non_equil[0]/=10
mask_non_equil=non_equil[0]<3e-5

plt.style.use('./prx.mplstyle')
fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
#different regimes
ax2=ax1.twiny()
ax2.spines['top'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_xticks([])
color_map = numpy.ones((100,100,3),dtype=numpy.uint8)*255
for ix in range(color_map.shape[1]):
    if ix < 30:
        color_map[:,ix,0]=153.
        color_map[:,ix,1]=0.
        color_map[:,ix,2]=221.
    if 37 <ix < 66:
        color_map[:,ix,0]=204
        color_map[:,ix,1]=119
        color_map[:,ix,2]=0  
    if 72< ix :
        color_map[:,ix,0]=0
        color_map[:,ix,1]=153
        color_map[:,ix,2]=0
    #multiply Gaussian filters

ax2.imshow(color_map,extent=(-1,2,0,2),origin='lower',alpha=0.2, interpolation='gaussian')


# first plot at index 
ax1.plot(x,mean_field,'black',linewidth=0.5)
ax1.plot(non_equil[0][mask_non_equil],non_equil[1][mask_non_equil], 'black',linewidth=0.5, ls='dashed', dashes=(2,1))
ax1.errorbar(m_x, m_val, yerr=m_err, color='black', fmt='o', markersize=3, capsize=2)
ax1.set_ylim([0,2])
ax1.set_xscale('log')
ax1.set_xlabel(r'external input rate $h$ / target neural firing rate $r^\ast$')
#ax1.set_ylabel(r'branching parameter $m$')
ax1.set_ylabel(r'branching parameter $m$')
ax1.set_yticks([0,1,2])
#ax1.xaxis.set_ticks_position('bottom')
#ax1.yaxis.set_ticks_position('left')

ax3=ax1.twinx()
ax3.spines['top'].set_visible(False)
ax3.spines['bottom'].set_linewidth(0.5)

color_tau='#708090'
tau=1/(-numpy.log(1-x))
#tau[x<1e-5]='Nan'
#tau[tau<0.5]=0.5
#tau[x>1]=0.5
tauprime=numpy.ones(len(x))*1e3/1e-3/1e4/0.1
ax3.plot(x,tau,color_tau,linewidth=0.5, alpha=1)
ax3.plot(x[x<1e-2],tauprime[x<1e-2],color_tau,linewidth=0.5,ls='dashed', alpha=1, dashes=(2,1))
ax3.errorbar(tau_x, tau_val, yerr=tau_err, color=color_tau, fmt='o',markersize=3, mec=color_tau, capsize=2)
ax3.set_ylim([1e-1,1e12])
ax3.set_yscale('log')

ax3.yaxis.set_ticks_position('right')
ax3.set_ylabel(r'autocorrelation time $\tau$ (ms)')
#ax3.minorticks_off()
ax3.spines['right'].set_color(color_tau)
ax3.yaxis.label.set_color(color_tau)
ax3.tick_params(axis='y', which='both', colors=color_tau)

color=['#9900DD','#CC7700','#009900']


ax1.spines['left'].set_linewidth(0.5)
ax1.spines['bottom'].set_linewidth(0.5)
ax2.spines['left'].set_linewidth(0.5)
ax2.spines['bottom'].set_linewidth(0.5)
ax3.spines['left'].set_linewidth(0.5)
ax3.spines['bottom'].set_linewidth(0.5)
ax3.yaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
ax3.yaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
ax3.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax3.set_yticks([1e0,1e1,1e2,1e3,1e4])
plt.setp(ax3.get_yticklabels()[1::2], visible=False)
ax1.set_xlim([8e-7,40])
ax1.xaxis.set_major_locator(matplotlib.ticker.LogLocator(base=10.0, subs=(1.0,), numticks=100) )
ax1.xaxis.set_minor_locator(ticker.LogLocator(base=10., subs=numpy.arange(2,10)*.1, numticks=100))
ax1.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
plt.setp(ax1.get_xticklabels()[1::2], visible=False)

#additional labels
plt.figtext(0.18,0.91,'bursting')
plt.figtext(0.45,0.91,'fluctuating')
plt.figtext(0.71,0.91,'input-driven')

#insets
x =[0.16,0.45,0.73]
hx=[1e-5,1e-2,5e0]
for i,h in enumerate([1e-7,1e-5,1e-3]):
    data=numpy.loadtxt("../../../paper/2018_homplast_dynamic-states/data/processed/BN_driven_homeostatic_ER_N010000_p1.00e-01_h%.2e_i0_T1.00e+07_seed1000_time_series_cut-5e6+30000.dat"%h, usecols=(0,),unpack=True)
    time=numpy.arange(len(data))/1000.
    inset1=plt.axes([x[i],0.70,0.15,0.15])
    inset1.plot(time,data,color[i],lw=0.5)
    inset1.plot(numpy.arange(25,30,1e-3), numpy.ones(int(5./1e-3))*(-20), color=color[i], linestyle='-', lw=1.0, solid_capstyle='butt')
    inset1.text(25,-70.,'5s',size='x-small')
    inset1.set_ylim([-50,200])
    inset1.spines['bottom'].set_visible(False)
    inset1.spines['right'].set_visible(False)
    inset1.spines['top'].set_visible(False)
    inset1.spines['left'].set_linewidth(0.5)
    plt.setp(inset1,xticks=[], yticks=[])
    index=numpy.where(m_x==h/1e-3)
    ax1.plot([m_x[index],m_x[index]],[1.5,m_val[index]], 'k-', ls='dashed', lw=1.0, dashes=(1,3), color=color[i])

#plt.show()
plt.savefig("fig_sketch_theory.png", transparent=True, dpi=300)
