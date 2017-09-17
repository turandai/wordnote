import numpy as np

def update(old_rate,speed):
    #standard: yes+2,no-1
    old_e_x=old_rate/104
    old_x=np.log((1+old_e_x)/(1-old_e_x))/2
    new_x=old_x+speed/100
    new_e_x=(np.exp(new_x)-np.exp(-new_x))/(np.exp(new_x)+np.exp(-new_x))
    new_rate=104*new_e_x
    if new_rate<0:
        new_rate=0
    elif new_rate>100:
        new_rate=100
    return new_rate

def fade(old_rate,dif_day):
    new_rate=old_rate-dif_day/5
    return new_rate
