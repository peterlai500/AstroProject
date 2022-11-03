#!/usr/bin/env python
# coding: utf-8

# In[3]:


from matplotlib import pyplot as plt
import numpy as np
PI = np.pi

#ALMA -23.0231838862327, -67.75156299046668
#Sgr A* RA = 17h 45m 40.0409s;Dec = −29° 0′ 28.118″

#LST = np.linspace(0,24,21600)*15                #local sidereal time, LST
dec = (-29-28.118/3600)*PI/180                   #declination of Sgr A*
ra = (17*15+45*15/60+40.0409/3600)*PI/180        #ascension of Sgr A*
#H = LST-dec*PI/180                              #H:Local hour angle H = LST-a 
phi = -23.0231838862327*PI/180                   #observation latitude
 
for l in range(0,24):
    LST = l*15*PI/180
    H = LST-dec*PI/180                           #H:Local hour angle H = LST-a
    z = np.sin(phi)*np.sin(dec)+np.cos(phi)*np.cos(dec)*np.cos(H)
    x = -np.cos(phi)*np.sin(dec)+np.cos(phi)*np.cos(dec)*np.cos(H)
    y = np.cos(dec)*np.sin(H)
    a = np.arcsin(z)                             #a is altitude
    eta = PI-a
    p = eta*(180/PI)
    t = H*(12/PI)
    plt.scatter(t,p)
    #plt.scatter(H*(12/PI),a*(180/PI))
plt.title('The parallatic angle change among time')
plt.xlabel('time (hour)')
plt.ylabel('Parallactic angle (degree)')
plt.pause(0.05)
plt.show()


# In[ ]:




