import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

appliedStress = 1e6 # Pa
ratios = np.array([0.05,.1,.15,.2,.25,.3,.35,.4,.45,.5,.55,.6,.65,.7,.75,.8])
ratioStresses = 1e6*np.array([1.8086,1.8634,2.5541,2.9519,3.2942,3.3876,3.4115,3.6597,4.0372,4.3855,4.7864,5.1957,5.9162,7.0512,8.369,10.027])
stressConcFact1 = ratioStresses*(1 - ratios)/appliedStress
slope,intercept,r,p,std_error = stats.linregress(ratios[3:],stressConcFact1[3:])
print(slope,intercept)
fitLine = lambda slope,intercept,ratio : slope*ratio+intercept
plt.figure(1)
plt.scatter(ratios,stressConcFact1,label='Data',color='r')
plt.plot(ratios,fitLine(slope,intercept,ratios),'b',label='Best fit line')
plt.xlabel('Hole Ratio (d/w)')
plt.ylabel('Stress Concentration Factor')
plt.title('Stress Concentration Factor vs Hole Ratio')
plt.xlim([0,1])
plt.ylim([1,2.5])
plt.legend()

# plt.show()