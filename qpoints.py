import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

def vis(klist):
    #Visualization
    fig, ax=plt.subplots()
    ax.scatter(klist[:,0],klist[:,1],s=10)
    plt.show()


m = 20 #取点数
axis = np.array([[1,0,0],[-1/2,3**0.5/2,0],[0,0,20]])
kpoints = np.zeros((m**2,3))
anticlockwise_120 = np.array([[-1/2,-3**0.5/2,0],[3**0.5/2,-1/2,0],[0,0,1]])
clockwise_120 = np.array([[-1/2,3**0.5/2,0],[-3**0.5/2,-1/2,0],[0,0,1]])
for i in range(m):
    for j in range(m):
        kpoints[i*m+j][0] = (1/m)*i
        kpoints[i*m+j][1] = (1/m)*j
k_cartesian = np.dot(kpoints,axis)
k1 = np.transpose(np.dot(anticlockwise_120,np.transpose(k_cartesian)))
k2 = np.transpose(np.dot(clockwise_120,np.transpose(k_cartesian)))
k_all = np.concatenate((k_cartesian,k1,k2))
k_all = np.unique(k_all,axis=0)
k_all_crystal = np.dot(k_all,inv(axis))
# vis(k_all)
q = len(k_all_crystal)
weight = np.ones(q)
qpts = np.insert(k_all_crystal,3,values=weight,axis=1)
np.savetxt('qpoints_hex.txt',qpts)
ff = open('qpoints_hex.txt','r')
ctt = ff.readlines()
ff.close()
ww = open('qpoints_hex.txt','w')
ww.writelines(str(len(k_all)) + '\tcrystal\n')
ww.writelines(ctt[:])
ww.close()