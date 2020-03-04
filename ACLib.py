import math

#Test Variables
V=150
I= 30
f=10
L=10
C=10
R=10
DEG=10


def ReactRes(C):# Calculates Reactive Ressistance
    Xc= (1/(2*math.pi*f*C))
    return Xc
    
def InductRes(L):# Calculates Inductive Ressistance
    Xl= (2*math.pi*f*L)
    return Xl

def Impedence(Xc,Xl,R):# Calculates Impedence
    print Xl
    print Xc
    if Xl>Xc:
        Z= math.sqrt((R**2)+((Xl-Xc)**2))
    elif Xc>Xl:
        Z= math.sqrt((R**2)+((Xc-Xl)**2))
    elif Xc==Xl:
        Z=R
    return Z

#Calculates Phase Angle

#Calculates Phase of Coil

#Calculates Apparent Power

#Calculates True Power

#Calculates Reactive Power

#Calculates Sinus Coordinates

#Info Page Radians and Degrees Caalculation

def turn_to_radians(DEG):
    Rad=(DEG*math.pi)/180
    return Rad
    


#Sinus Graphs Period Calculation

#Cosinus coordinates

print ReactRes(C)
