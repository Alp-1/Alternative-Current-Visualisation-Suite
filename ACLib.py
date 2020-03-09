import math

#Test Variables
V=230
I=9.13
f=100
L=0.15
C=0.0001
R=20
DEG=10



def ReactRes(C):# Calculates Reactive 
    if C != 0:
        Xc= (1/(2*math.pi*f*C))
        return Xc
    else:
        Xc=0
        return Xc
    
def InductRes(L):# Calculates Inductive Ressistance
    Xl= (2*math.pi*f*L)
    return Xl

def Impedence(Xc,Xl,R):# Calculates Impedence
    print Xl
    print Xc
    if Xl>Xc:
        Z= math.sqrt((R**2)+((Xl-Xc)**2))
    elif Xc==Xl:
        Z=R
    return Z

Z= Impedence(ReactRes(C),InductRes(L),R)

#Calculates Phase Angle
def PhaseAng(Xc,Xl,R):
    if R != 0:
        Phase_c=float(math.atan((Xl-Xc)/R))
        return Phase_c
    else:
        Phase_c=float(90.0)
        return Phase_c
    
#Phase Angle Without Capacitor
def PhaseNoC(Xl,R):
    Phase_noC=float(math.atan((Xl)/R))
    return Phase_noC
#Calculates Phase of Coil

#Calculates Apparent Power
def ApparentPwr(I,Z):
    Apparent_P=(I**2)*(Z)
    return Apparent_P
#Calculates True Power
def TruePwr(I,R):
    True_P=(I**2)*(R)
    return True_P
#Calculates Reactive Power
def ReactivePwr(Xl,Xc,I):
    Reactive_P_C=(I**2)*(Xl-Xc)
    print Xc,Xl,R
    return Reactive_P_C
#Reactive Power Without Capacitor
def ReactivePwrNoC(I,Xl):
    Reactive_P_noC=I*(Xl)**2
    return Reactive_P_noC
#Calculates Sinus Coordinates

#Info Page Radians and Degrees Caalculation

def turn_to_radians(DEG):
    Rad=(DEG*math.pi)/180
    return Rad
    


#Sinus Graphs Period Calculation

#Cosinus coordinates

print ReactRes(C) 
