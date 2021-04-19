# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:26:11 2019

@author: stefano
"""

import numpy as np
import matplotlib.pyplot as plt


#p=100 #popolazione massima
a= 0.5#percentuale nascite
b=0.25 #percentuale morte
c=0.25
lam=[a]
mu=[b]
cu=[c]
p01=1.0
p10=1.0
p00=1.0



T=100
x= np.zeros(T)
x[0]=2
x[:25]

for t in range (T-1):
    if 0< x[t]:
       
        prob=np.random.multinomial(1, [a/(a+b+c),b/(a+b+c), c/(a+b+c)], size=None)
        #probabilità random di nascita
        nascita=prob[0]
        #è una morte
        morte=prob[1]
        
        #aggiorno la taglia della popolazione
        x[t+1]= x[t]+nascita- morte
        a=a*t+1 #tassi lineari
        b=b*t+1
        c=c*t+1
        #p01=a*x[t]      #P_i_i+1(h)= lambda*X[t]*h   h=1
        #p10=b*x[t]       #P_i_i-1(h)= mu*X[t]*h
        #p00=c*x[t] 
             
        
        
        #aa=a/(a+b+c) #normalizzati a 1 P(i,i+1)
        #bb=b/(b+a+c)  #P(i,i-1)
        #cc=c/(a+b+c)  #P(i,i)
       
        lam.append(a)
        mu.append(b)
        cu.append(c)
       
        #else:
        #   x[t+1]=x[t]
    elif x[t]<=0:
         x[t+1]=0         #se la popolazione arriva a 0 si estingue
            
         a=0 
         b=0
         lam.append(a)
         mu.append(b)



#E_i indica il tempo che ci vuole per passare dallo stato i al successivo
E= np.zeros(T)
#E[0]=(1/lam[0])
time_0_100=0
for l in range (T):
    if 0< lam[l] and mu[l]:
        E[l]=(1/lam[l])+E[l-1]*(mu[l]/lam[l])
        time_0_100=E[l]+time_0_100
    elif (lam[l] or mu[0])<=0:
         E[l]=0 





plt.subplot(311)
plt.plot(x)
plt.xlabel("tempo")
plt.ylabel("taglia popolazione")

plt.subplot(312)
plt.plot(E)
plt.ylabel("E(T_i)")
print("attesa tempo da stato 0 a 100:", time_0_100)



plt.show()

