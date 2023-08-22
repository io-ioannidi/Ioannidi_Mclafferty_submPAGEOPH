'''
Script for loading sweepFiles and producing Fig.9
Ioannidi. McLafferty, Reber, Morra, Weatherley 2023 - PAGEOPH

Copyright P.I. Ioannidi
'''

import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from IwantHue import I_want_hue

plt.rcParams.update({'font.size': 16})

dir = '/path/to/mass/txt/files/'


fname = 'massStart.txt'
g = open(dir+fname)
grainFile = g.readlines()
g.close()
     
grainMass = np.zeros(len(grainFile))
ID = np.zeros(len(grainFile))

for i in range (len(grainFile)): 
    ID[i] = (float(grainFile[i].split()[0]))
    grainMass[i] = (float(grainFile[i].split()[1]))


df_t0=pd.DataFrame({'IDs':ID, 'grainMasses':grainMass})
clean_df_t0 = df_t0[df_t0.filter(like="grainMasses").apply(lambda x: all (1e+06<i for i in x), axis=1)]
singleGrains_df_t0 = df_t0[df_t0.filter(like="grainMasses").apply(lambda x: all (1e+06>i for i in x), axis=1)]
duplicated = clean_df_t0.duplicated()
duplicated.all()

'''
Plotting histograms for all normal roce models
'''
# Fn 0
fname = 'massEnd_0.txt'

g = open(dir+fname)
grainFile = g.readlines()
g.close()
     
grainMass = np.zeros(len(grainFile))
ID = np.zeros(len(grainFile))

for i in range (len(grainFile)): 
    ID[i] = (float(grainFile[i].split()[0]))
    grainMass[i] = (float(grainFile[i].split()[1]))

df0=pd.DataFrame({'IDs':ID, 'grainMasses':grainMass})
cond = df0['grainMasses'].isin(singleGrains_df_t0['grainMasses'])
df0.drop(df0[cond].index, inplace=True)

# Fn 1
fname = 'massEnd_1.txt'

g = open(dir+fname)
grainFile = g.readlines()
g.close()
     
grainMass = np.zeros(len(grainFile))
ID = np.zeros(len(grainFile))

for i in range (len(grainFile)): 
    ID[i] = (float(grainFile[i].split()[0]))
    grainMass[i] = (float(grainFile[i].split()[1]))

df1=pd.DataFrame({'IDs':ID, 'grainMasses':grainMass})
cond = df1['grainMasses'].isin(singleGrains_df_t0['grainMasses'])
df1.drop(df1[cond].index, inplace=True)

# Fn 2
fname = 'massEnd_2.txt'

g = open(dir+fname)
grainFile = g.readlines()
g.close()
     
grainMass = np.zeros(len(grainFile))
ID = np.zeros(len(grainFile))

for i in range (len(grainFile)): 
    ID[i] = (float(grainFile[i].split()[0]))
    grainMass[i] = (float(grainFile[i].split()[1]))

df2=pd.DataFrame({'IDs':ID, 'grainMasses':grainMass})
cond = df2['grainMasses'].isin(singleGrains_df_t0['grainMasses'])
df2.drop(df2[cond].index, inplace=True)

# Fn 3
fname = 'massEnd_3.txt'

g = open(dir+fname)
grainFile = g.readlines()
g.close()
     
grainMass = np.zeros(len(grainFile))
ID = np.zeros(len(grainFile))

for i in range (len(grainFile)): 
    ID[i] = (float(grainFile[i].split()[0]))
    grainMass[i] = (float(grainFile[i].split()[1]))

df3=pd.DataFrame({'IDs':ID, 'grainMasses':grainMass})
cond = df3['grainMasses'].isin(singleGrains_df_t0['grainMasses'])
df3.drop(df3[cond].index, inplace=True)

# Fn 4
fname = 'massEnd_4.txt'

g = open(dir+fname)
grainFile = g.readlines()
g.close()
     
grainMass = np.zeros(len(grainFile))
ID = np.zeros(len(grainFile))

for i in range (len(grainFile)): 
    ID[i] = (float(grainFile[i].split()[0]))
    grainMass[i] = (float(grainFile[i].split()[1]))

df4=pd.DataFrame({'IDs':ID, 'grainMasses':grainMass})
cond = df4['grainMasses'].isin(singleGrains_df_t0['grainMasses'])
df4.drop(df4[cond].index, inplace=True)

# Fn 5
fname = 'massEnd_5.txt'

g = open(dir+fname)
grainFile = g.readlines()
g.close()
     
grainMass = np.zeros(len(grainFile))
ID = np.zeros(len(grainFile))

for i in range (len(grainFile)): 
    ID[i] = (float(grainFile[i].split()[0]))
    grainMass[i] = (float(grainFile[i].split()[1]))

df5=pd.DataFrame({'IDs':ID, 'grainMasses':grainMass})
cond = df5['grainMasses'].isin(singleGrains_df_t0['grainMasses'])
df5.drop(df5[cond].index, inplace=True)

# Fn 6
fname = 'massEnd_6.txt'

g = open(dir+fname)
grainFile = g.readlines()
g.close()
     
grainMass = np.zeros(len(grainFile))
ID = np.zeros(len(grainFile))

for i in range (len(grainFile)): 
    ID[i] = (float(grainFile[i].split()[0]))
    grainMass[i] = (float(grainFile[i].split()[1]))

df6=pd.DataFrame({'IDs':ID, 'grainMasses':grainMass})
cond = df6['grainMasses'].isin(singleGrains_df_t0['grainMasses'])
df6.drop(df6[cond].index, inplace=True)

# Fn 7
fname = 'massEnd_7.txt'

g = open(dir+fname)
grainFile = g.readlines()
g.close()
     
grainMass = np.zeros(len(grainFile))
ID = np.zeros(len(grainFile))

for i in range (len(grainFile)): 
    ID[i] = (float(grainFile[i].split()[0]))
    grainMass[i] = (float(grainFile[i].split()[1]))

df7=pd.DataFrame({'IDs':ID, 'grainMasses':grainMass})
cond = df7['grainMasses'].isin(singleGrains_df_t0['grainMasses'])
df7.drop(df7[cond].index, inplace=True)

Fn_legend = ([str(item) for item in range(8, 8*7, 6)])
Fn_legend.insert(0, 'Initial')

plt.figure(dpi=299, figsize=(8,6))
(n, bins_initial, pathces) = plt.hist(clean_df_t0['grainMasses']/1e6, color='k', ec='black', bins=1, label='x', alpha=0.9, histtype='stepfilled')

newbins = [ bins_initial[0] - 0.1 * bins_initial[0], bins_initial[1]]   # arbitrarily considering grains
                                                                        # broken once they have lost 10% of their mass
                                                                        # otherwise even one single DE particle chipping off
                                                                        # would create 2 (!!!) new grains

(n0, bins0, pathces0) = plt.hist(df0['grainMasses']/1e6, color=I_want_hue[0], ec='black', bins=newbins, label='y', alpha=0.5, histtype='stepfilled')
(n1, bins1, pathces1) = plt.hist(df1['grainMasses']/1e6, color=I_want_hue[1], ec='black', bins=newbins, label='y', alpha=0.5, histtype='stepfilled')
(n2, bins2, pathces2) = plt.hist(df2['grainMasses']/1e6, color=I_want_hue[2], ec='black', bins=newbins, label='y', alpha=0.4, histtype='stepfilled')
(n3, bins3, pathces3) = plt.hist(df3['grainMasses']/1e6, color=I_want_hue[3], ec='black', bins=newbins, label='y', alpha=0.4, histtype='stepfilled')
(n4, bins4, pathces4) = plt.hist(df4['grainMasses']/1e6, color=I_want_hue[4], ec='black', bins=newbins, label='y', alpha=0.3, histtype='stepfilled')
(n5, bins5, pathces5) = plt.hist(df5['grainMasses']/1e6, color=I_want_hue[5], ec='black', bins=newbins, label='y', alpha=0.3, histtype='stepfilled')
(n6, bins6, pathces6) = plt.hist(df6['grainMasses']/1e6, color=I_want_hue[6], ec='black', bins=newbins, label='y', alpha=0.2, histtype='stepfilled')
(n7, bins7, pathces7) = plt.hist(df7['grainMasses']/1e6, color=I_want_hue[7], ec='black', bins=newbins, label='y', alpha=0.1, histtype='stepfilled')
# plt.legend((Fn_legend), title='Normal force (N)' , loc="upper right", frameon=False, ncol=1)
# plt.yscale('log'); #plt.xscale('log')
# plt.ylim([0, 200]); plt.xlim([2.5e6, 2.8e6])
plt.show()


### just for fun plotting the distribution of grains-masses (divided by 1e6 to make the values more reasonable)
### Figure not in paper
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(8,10), dpi=299)
fig.tight_layout()
# fig.suptitle('Grain size distributions')
(n, bins_initial, pathces) = ax1.hist(clean_df_t0['grainMasses']/1e6, color='k', ec='black', bins=1, label='x', alpha=0.9, histtype='stepfilled')

(n0, bins0, pathces0) = ax1.hist(df0['grainMasses']/1e6, color=I_want_hue[0], ec='black', bins=10, label='y', alpha=0.5, histtype='stepfilled')
(n1, bins1, pathces1) = ax1.hist(df1['grainMasses']/1e6, color=I_want_hue[1], ec='black', bins=10, label='y', alpha=0.5, histtype='stepfilled')
(n2, bins2, pathces2) = ax1.hist(df2['grainMasses']/1e6, color=I_want_hue[2], ec='black', bins=10, label='y', alpha=0.4, histtype='stepfilled')
(n3, bins3, pathces3) = ax1.hist(df3['grainMasses']/1e6, color=I_want_hue[3], ec='black', bins=10, label='y', alpha=0.4, histtype='stepfilled')
(n4, bins4, pathces4) = ax1.hist(df4['grainMasses']/1e6, color=I_want_hue[4], ec='black', bins=10, label='y', alpha=0.3, histtype='stepfilled')
(n5, bins5, pathces5) = ax1.hist(df5['grainMasses']/1e6, color=I_want_hue[5], ec='black', bins=10, label='y', alpha=0.3, histtype='stepfilled')
(n6, bins6, pathces6) = ax1.hist(df6['grainMasses']/1e6, color=I_want_hue[6], ec='black', bins=10, label='y', alpha=0.2, histtype='stepfilled')
(n7, bins7, pathces7) = ax1.hist(df7['grainMasses']/1e6, color=I_want_hue[7], ec='black', bins=10, label='y', alpha=0.1, histtype='stepfilled')
ax1.set_xlabel('Grain mass'); ax1.set_ylabel('Log(number of grains)'); 
ax1.legend((Fn_legend), title='Normal force (N)' , loc="upper right", frameon=False, ncol=1)
ax1.set_yscale('log'); #plt.xscale('log')
ax1.set_ylim([0, 12000]); ax1.set_xlim([0, 3.0])

(n, bins_initial, pathces) = ax2.hist(clean_df_t0['grainMasses']/1e6, color='k', ec='black', bins=1, label='x', alpha=0.9, histtype='stepfilled')

(n0, bins0, pathces0) = ax2.hist(df0['grainMasses']/1e6, color=I_want_hue[0], ec='black', bins=10, label='y', alpha=0.5, histtype='stepfilled')
(n1, bins1, pathces1) = ax2.hist(df1['grainMasses']/1e6, color=I_want_hue[1], ec='black', bins=10, label='y', alpha=0.5, histtype='stepfilled')
(n2, bins2, pathces2) = ax2.hist(df2['grainMasses']/1e6, color=I_want_hue[2], ec='black', bins=10, label='y', alpha=0.4, histtype='stepfilled')
(n3, bins3, pathces3) = ax2.hist(df3['grainMasses']/1e6, color=I_want_hue[3], ec='black', bins=10, label='y', alpha=0.4, histtype='stepfilled')
(n4, bins4, pathces4) = ax2.hist(df4['grainMasses']/1e6, color=I_want_hue[4], ec='black', bins=10, label='y', alpha=0.3, histtype='stepfilled')
(n5, bins5, pathces5) = ax2.hist(df5['grainMasses']/1e6, color=I_want_hue[5], ec='black', bins=10, label='y', alpha=0.3, histtype='stepfilled')
(n6, bins6, pathces6) = ax2.hist(df6['grainMasses']/1e6, color=I_want_hue[6], ec='black', bins=10, label='y', alpha=0.2, histtype='stepfilled')
(n7, bins7, pathces7) = ax2.hist(df7['grainMasses']/1e6, color=I_want_hue[7], ec='black', bins=10, label='y', alpha=0.1, histtype='stepfilled')
ax2.set_ylim([0, 125]); ax2.set_xlim([2.0, 3.0])
ax2.set_xlabel('Grain mass'); ax2.set_ylabel('Number of grains'); 

#fig.savefig(dir+'grainSizeDistribution.png',dpi=299, bbox_inches='tight')

'''
After getting the bin sizes from the plot, calculate the percentage of broken grains
'''

brokenGrains = [n0[9], n1[9], n2[9], n3[9], n4[9], n5[9], n6[9], n7[9]]

pcent_DE = []
for i in range(len(brokenGrains)):
        pcent_DE.append(((1-brokenGrains[i]/n)*100))
print(pcent_DE)

'''
Figure 9
Fractured grains in numerical vs. analog models
'''

pcent_DI = np.array([0, 16.2, 18.9])
pcent_T = np.array([6.4, 2.7])
pcent_Lg = np.array([21.1])

normalForce_DI = np.array([18., 46., 48.])
normalForce_T = np.array([60., 49.])
normalForce_LG = np.array([20.])

### cohesion_0 in normal force sweep models
normalForceDE = np.array([8, 14, 20, 26, 32, 38, 44, 50])

a, b = np.polyfit(normalForceDE,pcent_DE,1)

plt.figure(dpi = 299, figsize=(8,6))
plt.plot(normalForce_DI,pcent_DI, 's', color=I_want_hue[0], markersize=14);
plt.plot(normalForce_T,pcent_T, 's', color=I_want_hue[1], markersize=14);
plt.plot(normalForce_LG,pcent_Lg, 's', color=I_want_hue[2], markersize=14);

plt.plot(normalForceDE,pcent_DE, 'o', color=I_want_hue[3], markersize=13);
plt.plot(normalForceDE,a*normalForceDE+b,'k--')

text = 'y = '+str((a)[0])[0:4]+'*x + b'

plt.annotate(text, xy=(24., 8.2), xytext=(30., 5.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlabel('Normal force (N)')
plt.ylabel('% of broken grains')
plt.legend(['DI', 'Tap', 'Lg','DE'], loc='upper left')
plt.xlim([0., 62.])
plt.ylim([-1., 25.])

plt.savefig(dir+'Fig9.png')
plt.show()

