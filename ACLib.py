import math

#Test Variables

def ReactRes(C,f):# Calculates Reactive Ressistance
    if C != 0 and f !=0:
        Xc= (1/(2*math.pi*f*C))
    else:
        Xc=0
    return Xc
    
def InductRes(L,f):# Calculates Inductive Ressistance
    Xl= (2*math.pi*f*L)
    return Xl

def Impedence(Xc,Xl,R):# Calculates Impedence
    Z= math.sqrt((R**2)+((Xl-Xc)**2))
    return Z

def CurrentCalc(V,Z): # Calculates Current
    if Z ==0 or V ==0:
        I= "Not enough inputs"
    if Z!=0 and V!=0:
        I = V/Z
    return I

#Calculates Phase Angle
def PhaseAng(Xc,Xl,R):
    if R != 0:
        Phase_c=float(math.atan((Xl-Xc)/R))
    elif R ==0 and Xl-Xc !=0:
        Phase_c= math.pi/2
    else:
        Phase_c=0
    return Phase_c
#Phase Angle Without Capacitor
def PhaseNoC(Xl,R):
    if R !=0:
        Phase_noC=float(math.atan((Xl)/R))
    else:
        Phase_noC=0
    return Phase_noC
#Calculates Phase of Coil

#Calculates Apparent Power
def ApparentPwr(I,Z):
    if type(I) != str:
        Apparent_P=(I**2)*(Z)
    else:
        Apparent_P="Not enough inputs"
    return Apparent_P
#Calculates True Power
def TruePwr(I,R):
    if type(I) != str:
        True_P=(I**2)*(R)
    else:
        True_P="Not enough inputs"
    return True_P

#Calculates Reactive Power
def ReactivePwr(Xl,Xc,I):
    if type(I) != str:
        Reactive_P_C=(I**2)*(Xl-Xc)
    else:
        Reactive_P_C="Not enough inputs"
    return Reactive_P_C
#Reactive Power Without Capacitor

#Calculates Sinus Coordinates

#Info Page Radians and Degrees Caalculation

##def turn_to_radians(DEG):
##    Rad=(DEG*math.pi)/180
##    return Rad
    


#Sinus Graphs Period Calculation

#Cosinus coordinates

