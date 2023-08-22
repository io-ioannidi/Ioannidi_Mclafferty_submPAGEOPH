import numpy as np
import os

def readFiles(dir):

    '''
    Load csv files for position, force(stress), kinEnergy, and number of bonds
    '''
    posnfile = open(dir+'/out_Position.csv','r')
    posn = posnfile.readlines()
    posnfile.close()
    
    forcefile = open(dir+'/out_Force.csv','r')
    force = forcefile.readlines()
    forcefile.close()
    
    length = len(force)
    if len(posn) < len(force):
        length = len(posn)
        
    stress = np.zeros(length)
    strain = np.zeros(length)
    shearStrain = np.zeros(length)
    
    forceBX = np.zeros(len(force))

    
    X_init = float(posn[0].split()[3])
    
    for i in range (length):
        Y_bottom = float(posn[i].split()[1])
        Y_top = float(posn[i].split()[4])
        X_top = float(posn[i].split()[3])
        X_bottom = float(posn[i].split()[0])
        shearStrain[i] = (X_init - X_top)/((Y_top - Y_bottom))
        F_bottom = float(force[i].split()[1])
        F_top = float(force[i].split()[4])
    	
        stress[i] = np.abs((F_bottom - F_top))/(0.140*0.08)
        strain[i] = 1 - (Y_top - Y_bottom)/140.0
        
    for i in range (length):    
        forceBX[i] = float(force[i].split()[0])

    
    ## kinetic energy
    ekinfile = open(dir+'/ekin.csv','r')
    ekin = ekinfile.readlines()
    ekinfile.close()
    
    sizeList=len(ekin)
    dataEkin=np.zeros(sizeList)
    for i in np.arange(sizeList):
        dataEkin[i]=float(ekin[i].split()[0])
    ekinfile.close()
    
    
    '''
    Number of bonds in gouge
    '''
    ## number of bonds in gouge
    Nbondsfile = open(dir+'/Nbonds.csv','r')
    Nbonds = Nbondsfile.readlines()
    Nbondsfile.close()
    
    sizeList=len(Nbonds)
    dataNb=np.zeros(sizeList)
    for i in np.arange(sizeList):
        dataNb[i]=float(Nbonds[i])
    
    
    '''
    Check that all variables have the same size
    '''
    maxS = min(len(dataNb),len(dataEkin),len(forceBX),len(stress),len(strain),len(shearStrain))
    minS = 0
    dataNb = dataNb[minS:maxS]
    dataEkin = dataEkin[minS:maxS]
    forceBX = forceBX[minS:maxS]
    stress = stress[minS:maxS]
    strain = strain[minS:maxS]
    shearStrain = shearStrain[minS:maxS]
    
    allData = np.stack((dataNb, dataEkin, forceBX, stress, strain, shearStrain))

    return dataNb, dataEkin, forceBX, stress, strain, shearStrain, allData


Fname = []

Nbonds = []
Ekin = []
Fn = []
Stress = []
AxStrain = []
ShearStrain = []

allData = []

rootdir = '/path/to/normal_force_*/directory/'


dirs = []

for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        dirs.append(d)


for i in dirs:
    print(i)
    dataNb, dataEkin, force, stress, strain, shearStrain, allDt = readFiles(i)
    
    Fname.append(i.rsplit('/',3)[2]+'_'+i.rsplit('/',3)[3])
    
    Nbonds.append(dataNb)
    Ekin.append(dataEkin)
    Fn.append(force)
    Stress.append(stress)        
    AxStrain.append(strain)
    ShearStrain.append(shearStrain)
    allData.append(allDt)
            

# make Fn, Nbonds same size for all models

maxx = len(allData[0][0])

for i in range(len(allData)):
    if maxx > len(allData[i][0]):
        maxx = len(allData[i][0])
        print(len(allData[i][0]), maxx)
            

NbondsN = []
EkinN = []
FnN = []
StressN = []
AxStrainN = []
ShearStrainN = []


for i in range(len(Nbonds)):
    
    NbondsN.append(np.resize(Nbonds[i][:], maxx))
    EkinN.append(np.resize(Ekin[i][:], maxx))
    FnN.append(np.resize(Fn[i][:], maxx))
    StressN.append(np.resize(Stress[i][:], maxx))
    AxStrainN.append(np.resize(AxStrain[i][:], maxx))
    ShearStrainN.append(np.resize(ShearStrain[i][:], maxx))
        

'''
Normalize normal force
'''

Norm_FnN = []

for i in range(len(FnN)):
    Norm_FnN.append(FnN[i]/np.linalg.norm(FnN[i]))

np.save(rootdir+'Nbonds', NbondsN)
np.save(rootdir+'Ekin', EkinN)
np.save(rootdir+'Fn', FnN)
np.save(rootdir+'Stress', StressN)
np.save(rootdir+'AxialStrain', AxStrainN)
np.save(rootdir+'ShearStrain', ShearStrainN)

np.savetxt(rootdir+'Fname.txt', Fname, fmt='%s')
