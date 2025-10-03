import numpy as np 
import matplotlib.pyplot as plt 
data={
    "P_b":[10,20,30,40,50],
    "P_c":[0.1,0.1,0.1,0.1],
    "h1":[2800,3200,3500,3700,3900],
    "h2":[2100,2300,2400,2500,2600],
    "h3":[200,200,200,200,200],
    "h4":[210,212,215,218,220]
    }
P=np.array(data["P_b"])
h1=np.array(data["h1"])
h2=np.array(data["h2"])
h3=np.array(data["h3"])
h4=np.array(data["h4"])
W_T=h1-h2
W_P=h4-h3
Q_in=h1-h4
Q_out=h2-h3
W_net=W_T-W_P
eff=W_net/Q_in
SSC=3600/W_net
print("boiler pressures:",P)
print("efficiency:",np.round(eff,2))
print("ssc:",np.round(SSC,2))
plt.plot(P,eff*100,label="efficiency",marker='o',color='blue')
plt.plot(P,SSC,label="specific steam consumption",marker='o',color='black')
plt.xlabel("boiler pressures(bar)---->")
plt.ylabel("efficiency(%)--->\nSSC(kg/Kwh)---->")
plt.grid()
plt.legend()
plt.show()