import numpy as np
import matplotlib.pyplot as plt

stressYield = 250e6 # Pa
elasticModulus = 200e9

interp = lambda y1, m, x1, x : y1 + m*(x-x1)

yieldingX = np.concatenate((np.arange(0,stressYield/elasticModulus,0.0001),np.linspace(stressYield/elasticModulus,0.00200,100)))
nonyieldingX = np.linspace(0,0.00200,100)

yieldingY = np.concatenate((interp(0,elasticModulus,0,np.arange(0,stressYield/elasticModulus,0.0001)),interp(stressYield,elasticModulus/10,stressYield/elasticModulus,np.linspace(stressYield/elasticModulus,0.00200,100))))
nonyieldingY = interp(0,elasticModulus,0,np.linspace(0,0.00200,100))


plt.figure(1)
plt.plot(yieldingX,yieldingY,'b',label="Yielding")
plt.plot(nonyieldingX,nonyieldingY,'g',label="NonYielding")
plt.plot(1.3954e-3,271.177e6,'ro',label="FEA Simulation")
plt.xlim([0,0.00200])
# plt.ylim([0,1400])
plt.title("Stress vs Strain")
plt.ylabel("Stress (Pa)")
plt.xlabel("Strain (m/m)")
plt.legend()
plt.show()