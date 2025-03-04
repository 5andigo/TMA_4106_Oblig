import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('Front_suspension_decomp.xlsx')
k = 150
m = 383 * (3040-912)/3040/2 * 1.5
force = 400 * (3040-912)/3040/2 * 1.6 *9.81
#force = 393 *9.81/2

z = df['z'].values
spring_length = df['spring_lenght'].values
alpha = df['alpha'].values

for j in range(len(z)):
    spring_length[j] = spring_length[j] - 65

i = 0
while True:
    i += 1
    force_spring = k * ((spring_length[0]-20) - (spring_length[i]-20))
    force_decomp_spring = force/np.cos((90-alpha[i])*np.pi/180)
    force_decomp_y = force_decomp_spring * np.cos(alpha[i]*np.pi/180)

    if force_spring > force_decomp_spring:
        break

c_crit = 2*np.sqrt(k*1000*m)

print(f'This is max dampening for the car: {z[i]}mm')
print(f'Force in lower wishbone: {round(force_decomp_y)}N')
print(f'Spring lenght for no forces: {round(spring_length[0])}mm')
print(f'Force in spring: {round(force_spring)}N')
print(f'Critical dampening: {round(c_crit)}Ns/m')

print(np.sqrt(350/3*25000))
print(393 * (3040-912)/3040/2 *9.81)


