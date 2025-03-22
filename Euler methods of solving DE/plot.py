import numpy as np
import matplotlib.pyplot as plt

V = 10.0  
dt = 0.001  

def squarewave(t, T, alpha):
    return V if (t % T) < (alpha * T) else 0

def euler(R, L, alpha, T, duration):
    steps = int(duration / dt)
    i = 0.0
    tau = L / R
    time, currents = [], []

    for n in range(steps):
        t = n * dt
        v = squarewave(t, T, alpha)
        di = (v - R * i) / L
        i += dt * di
        time.append(t)
        currents.append(i)
    print(max(currents))
    return time, currents

def backeuler(R, L, alpha, T, duration):
    steps = int(duration / dt)
    i = 0.0
    tau = L / R
    time, currents = [], []

    for n in range(steps):
        t = n * dt
        v = squarewave(t, T, alpha)
        if v == V:
            i = (i + (dt * v / L)) / (1 + (dt * R / L))
        else:
            i *= np.exp(-dt / tau)
        time.append(t)
        currents.append(i)
    print(max(currents))
    return time, currents

R = 1.0
L = 1.0
alpha = 0.5
T = 2.0
duration = 20.0  

timeeuler, currentseuler = euler(R, L, alpha, T, duration)
timebackeuler, currentsbackeuler = backeuler(R, L, alpha, T, duration)

plt.plot(timeeuler, currentseuler, label='Euler Method')
plt.plot(timebackeuler, currentsbackeuler, '--', label='Backward Euler Method')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.title('RL Circuit Response to Square Wave')
plt.legend()
plt.grid(True)
plt.savefig(f"fig{alpha}.png")
plt.show()

