'''
Script for loading sweepFiles and producing Fig.6-8
Ioannidi. McLafferty, Reber, Morra, Weatherley 2023 - PAGEOPH

Copyright P.I. Ioannidi
'''

import glob
import numpy as np
import matplotlib.pyplot as plt
from IwantHue import I_want_hue
import statistics

plt.rcParams.update({'font.size': 18})

def rateBreakingBonds(x, y):
    xvals = np.linspace(0, np.max(x), int(max(x))*10)
    yinterp = np.interp(xvals, x, y)
    return xvals, yinterp


'''
Load files
'''
path = '/path/to/npy/files/'

data = {}
for np_name in glob.glob(path+'*.np[y]'):
    data[np_name] = np.load(np_name, allow_pickle=True)
    
names = list(data.keys())
values = list(data.values())

varname = []
for i in range(len(names)):
    varname.append(names[i].split('/')[-1].split('.')[0])

timestep = np.arange(len(values[0][0])) * 1e-03

for k in range(len(data)):
     exec(f'{varname[k]} = np.array(values[k])')
     

with open(path+"Fname.txt", "r") as file:
    fnames=file.read().splitlines()
       
colors = plt.cm.cividis(np.linspace(0,1,len(names)))
style = ['-','--','-.',':','-','--','-.',':']

Fn_legend = ([item for item in range(8, 8*7, 6)])
sn_legend = [ 360,  625,  890, 1160, 1430, 1700, 1960, 2230]



'''''''''''''''''''''
FIGURES
'''''''''''''''''''''

'''
Figure 6a
Nbonds - LOG-LIN
'''
plt.figure(dpi=299, figsize=(8,6))
for i in range(len(Nbonds)):
    plt.plot(timestep, (-Nbonds[i]+max(Nbonds[i])), color=I_want_hue[i])

plt.axvline(250,c='k',linestyle='dotted');plt.axvline(350,c='k',linestyle='dotted')
plt.xticks(np.arange(min(timestep), max(timestep)+1, 100))
plt.xlabel('Time (s)'); plt.ylabel('Number broken bonds')
plt.yscale('log');
plt.xticks([0, 200, 400, 600, 800, 1000])
plt.yticks([0.1, 10, 100, 1000, 10000, 100000])
plt.legend((Fn_legend), title='Normal force (N)' , loc="lower right", frameon=False, ncol=2)
plt.savefig(path+'6a.png')
plt.show()

'''
Figure 6b
Rate of bond breaking with shear strain
'''
plt.figure(dpi=299, figsize=(8,6))
for i in range(len(Nbonds)):
    x, y = rateBreakingBonds(-ShearStrain[i], -Nbonds[i])
    plt.plot(x[1:len(x)],np.diff(y), color=I_want_hue[i])
plt.xlabel('Shear strain'); plt.ylabel('Rate of breaking bonds')
plt.ylim([0,1300])
plt.xlim([0, 27.5])
plt.legend((Fn_legend), title='Normal force (N)' , loc="upper right", frameon=False, ncol=2)
plt.savefig(path+'6b.png', bbox_inches='tight')
plt.show()


'''
Figure 7a
Horizontal force
'''
plt.rcParams['legend.title_fontsize'] = 'small'

plt.figure(dpi=299, figsize=(8,6))
for i in range(len(Fn)):
    plt.plot(timestep, -Fn[i], color=I_want_hue[i]);
plt.axvline(250,c='k',linestyle='dotted');plt.axvline(350,c='k',linestyle='dotted')
plt.xticks(np.arange(min(timestep), max(timestep)+1, 100))
plt.xlabel('Time (s)'); plt.ylabel('Horizontal force (N)')
plt.xticks([0, 200, 400, 600, 800, 1000])
plt.legend((Fn_legend), title='Normal force (N)' , loc="upper left", frameon=False, ncol=1)
plt.savefig(path+'7a.png')
plt.show()

'''
Figure 7b
Variance
'''
Fn_cut0 = []
Fn_cut1 = []
var0 = []
var1 = []
for i in range(len(Fn)):
    Fn_cut0.append(Fn[i][250001:len(Fn[0])])
    Fn_cut1.append(Fn[i][350001:len(Fn[0])])

for i in range(len(Fn)):
    var0.append(statistics.variance(Fn_cut0[i]))
    var1.append(statistics.variance(Fn_cut1[i]))


from matplotlib.lines import Line2D
legend_elements =  [Line2D([0], [0], marker='s', color='w', label='From onset of shearing',
                          markeredgecolor='k', markersize=15),
                    Line2D([0], [0], marker='o', color='w', label='After max. shearing velocity reached',
                         markeredgecolor='k', markersize=15)]

plt.figure(dpi=299, figsize=(8,6))      
for i in range(len(Fn)):
   plt.plot(str(Fn_legend[i]), var0[i], color=I_want_hue[i], marker='s',  markeredgecolor='k', markersize=15)
   plt.plot(str(Fn_legend[i]), var1[i], color=I_want_hue[i], marker='o', markeredgecolor='k', markersize=15)
plt.xlabel('Normal force (N)'); plt.ylabel('Variance')
plt.legend(handles=legend_elements, loc='upper left', frameon=False)
plt.savefig(path+'7b.png')
plt.show()  


'''
Figure 8
Max horizontal force and max broken bonds vs. normal stress
'''
from matplotlib.lines import Line2D
legend_elements0 =  [Line2D([0], [0], marker='o', color='w', label='Percentage of broken bonds',
                          markerfacecolor='k', markersize=15),
                    Line2D([0], [0], marker='o', color='w', label='Max. horizontal force (N)',
                         markerfacecolor='c', markersize=15)]

fig,ax = plt.subplots(dpi=299, figsize=(8,6))
for i in range(len(Fn)):
    ax.plot(Fn_legend[i],np.max(-Nbonds[i]+max(Nbonds[i]))/max(Nbonds[0])*100,'ko',
            markersize=17);
ax.set_xlabel('Normal force (N)')
ax.set_ylabel('% of broken bonds')

ax2 = ax.twinx()
for i in range(len(Fn)):
    ax2.plot(Fn_legend[i],np.max(-Fn[i]),'co',
    markersize=17)
ax2.set_ylabel('Max. horizontal force (N)')
ax2.set_ylim([0, 10])
plt.legend(handles=legend_elements0, loc='upper left', frameon=False)
plt.savefig(path+'8.png')
plt.show()
