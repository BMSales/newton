import numpy as np
import math

def Function(m, x, e):
    return m + x - e * np.sin(x)

def Derivative(x, e):
    return 1 - e * np.cos(x)

def Newton(m, eA, e):
    while Function(m, eA, e) > 0.0000000001 or Function(m, eA, e) < -0.0000000001:
        eA = eA - Function(m, eA, e)/Derivative(eA, e)
    else:
        return eA

def PositionOrbit(time, radSpeed, eccentricity, a, guess):
    m = radSpeed * time
    eA = Newton(m, guess, eccentricity)
    trueAnomaly = math.sqrt((1 + eA)/(1 - eA)) * np.tan(eA/2)
    trueAnomaly = np.arctan(trueAnomaly)*2
    r = a*(1 - eccentricity**2)/(1 + eccentricity * np.cos(trueAnomaly))

    return (r, trueAnomaly)


time = 600 # 10 minutos
radSpeed = math.pi/3600
a = 25
eccentricity = 0.6
guess = 20

print(PositionOrbit(time, radSpeed, eccentricity, a, guess))
