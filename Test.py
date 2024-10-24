import ACLib as AC
import math
import random

#This first section analyzes all the posibilities for things that can go wrong with capacitor impedance.
#There are only 2 ways it can go wrong: division by 0, or the function spitting out the wrong values:
print "-------------------------------------------------------"
#If capacitance and frequency are 0, the result of the function should be 0
Result_1 = AC.ReactRes(0,0)
if Result_1 == 0:
    print "-Reactive Resistance 0,0 (div by 0): Pass"
else:
    print "-Reactive Resistance 0,0 (div by 0): Fail"

#setting up random values for c and f that will be helpfull later
c=random.randint(1,10)
f=random.randint(1,10)
#For any given value of capacitance, if frequency is 0, then the function should also return 0
Result_2 = AC.ReactRes (c,0)

if Result_2 == 0:
    print "-Reactive Resistance c,0 (div by 0): Pass"
else:
    print "Reactive Resistance c,0 (div by 0): Fail"

#For any given value of frequency, if capacitance is 0, then the function should also return 0
Result_3 = AC.ReactRes (0,f)
if Result_3 == 0:
    print "-Reactive Resistance 0,f (div by 0): Pass"
else:
    print "-Reactive Resistance 0,f (div by 0): Fail"


#With the formula for capacitor impedance, 1/(2*pi*f*c), we can check that for 2 random values of C and f, the result is the same as the ones the formulas indicate
Result_4 = AC.ReactRes(c,f)
Expected_Result_4 = (1/(2*math.pi*c*f))

if Expected_Result_4 == Result_4:
    print "-Reactive Resistance c,f (result is accurate): Pass"
else:
    print "-Reactive Resistance c,f (result is accurate): Fail, (Rerun if test and library results are the same on console)"


#For inductive impedance, since its a multiplication, it just needs to check that any given values match that of the formula, 2*pi*f*L
print "-------------------------------------------------------"
L=random.uniform(0.0,10000.0)
Result_5 = AC.InductRes(L,f)
Expected_Result_5 = 2*math.pi*f*L
if Result_5 == Expected_Result_5:
    print "-Inductive Resistance L,f (result is accurate): Pass"
else:
    print "-Inductive Resistance L,f (result is accurate): Fail"

#For the total circuit impedance, since both terms in the root are squared, there is no concern with a root of a negative
#However, we must still check that the values match
print "-------------------------------------------------------"
Xc=random.uniform(0.0,10000.0)
XL=random.uniform(0.0,10000.0)
R=random.uniform(0.0,10000.0)
Result_6 = AC.Impedence(Xc,XL,R)
Expected_Result_6 = math.sqrt(R**2+(XL-Xc)**2)

if Result_6 == Expected_Result_6:
    print "-Total circuit impedance Xc,XL,R (result is accurate): Pass"
else:
    print "-Total circuit impedance Xc,XL,R (result is accurate): Fail"

print"-------------------------------------------------------"  

#Here we check for the error message when there are no inputs on the current function  
Result_7 = AC.CurrentCalc(0,0)
if Result_7 == "Not enough inputs":
    print "-Current 0,0 (div by 0): Pass"
else:
    print "-Current 0,0 (div by 0): Fail"

Z=random.uniform(0.0,10000.0)
V=random.uniform(0.0,10000.0)

#Again, the same thing except we are looking for the same error message without an impedance input
Result_8 = AC.CurrentCalc(V,0)
if Result_8 == "Not enough inputs":
    print "-Current V,0 (No current without voltage): Pass"
else:
    print "-Current V,0 (No current without voltage): Fail"

#Same as before, except this time, without a voltage input
Result_9 = AC.CurrentCalc(0,Z)
if Result_9 == "Not enough inputs":
    print "-Current 0,Z (div by 0): Pass"
else:
    print "-Current 0,Z (div by 0): Fail"

#This is just an accuracy check for the mathematical formulas
Result_10 = AC.CurrentCalc(V,Z)
Expected_Result_10 = float(V/Z)

if Result_10 == Expected_Result_10:
    print "-Current V,Z (result is accurate): Pass"
else:
    print "-Current V,Z (result is accurate): Fail"

print"-------------------------------------------------------"  

#Without components, there is no phase angle. No need for error message since it is possible to build a circuit like this
Result_11 = AC.PhaseAng(0,0,0)
if Result_11 == 0:
    print "-Phase Angle 0,0,0 (No phase angle without compnents): Pass"
else:
    print "-Phase Angle 0,0,0 (No phase angle without compnents): Fail"

#Accuracy for the formulas in a Resistor-less circuit
Result_12 = AC.PhaseAng(Xc,XL,0)
Expected_Result_12 = math.pi/2

if Xc != XL:
    if Result_12 == Expected_Result_12:
        print "-Phase Angle Xc,XL,0 (accuracy without resistor): Pass"
    else:
        print "-Phase Angle Xc,XL,0 (accuracy without resistor): Fail"
else: 
    print "RANDOM XC CAME OUT EQUAL TO RANDOM XL. RUN TEST AGAIN."#Impossibly low chance of this happening

#When Both Xc and XL are the same, the circuit is in resonance, and the phase angle should be 90 degrees
Result_13 = AC.PhaseAng(XL,XL,0)
if Result_13 == 0:
    print "-Phase Angle X,X,0 (circuit in phase without resistor): Pass"
else:
    print"-Phase Angle X,X,0 (circuit in phase without resistor): Fail"

#Same as before, except now the circuit also has a resistor, which should have no effect on a resonant phase angle
Result_14 = AC.PhaseAng(XL,XL,R)
if Result_13 == 0:
    print "-Phase Angle X,X,R (circuit in phase with resistor): Pass"
else:
    print"-Phase Angle X,X,R (circuit in phase with resistor): Fail"

#A simple accuracy check for the formulas
Result_15 = AC.PhaseAng (Xc,XL,R)
Expected_Result_15 = float(math.atan((XL-Xc)/R))

if Xc != XL:
    if Result_15 == Expected_Result_15:
        print "-Phase Angle Xc,XL,R (result is accurate): Pass"
    else:
        print "-Phase Angle Xc,XL,R (result is accurate): Fail"
else: 
    print "RANDOM XC CAME OUT EQUAL TO RANDOM XL. RUN TEST AGAIN."#Impossibly low chance of this happening

print"-------------------------------------------------------"  
I_NoInput="Not enough inputs"
#This is the result that should come from running the function AC.CurrentCalc without either a 
#voltage, impedance, or both. We chose to write it in this manner instead of obtaining it from
#the function itself because, in case the function fails, this check is exclusively for 
# the power functions, so if the power funcitons fail, we shall know that it isnt
#due to the current function failing.

#Without a current, there cannot be any reactive power, therefore, we check for the correct error message
Result_16=AC.ReactivePwr(XL,Xc,I_NoInput)

if Result_16 == "Not enough inputs":
    print "-Reactive Power XL,Xc,No Input (Correct Error Message): Pass"
else:
    print "-Reactive Power XL,Xc,No Input (Correct Error Message): Fail"

#Again, a stable value for current that doesn't depend on the function, so that we
#may exclusively test the power functions
    
I=random.randint(0,10000)

#Mathematical formula accuracy check
Result_17 = AC.ReactivePwr(XL,Xc,I)
Expected_Result_17 = (I**2)*(XL-Xc)

if Result_17 == Expected_Result_17:
    print "-Reactive Power XL, Xc, I (Accuracy): Pass"
else:
    print "-Reactive Power XL, Xc, I (Accuracy): Fail"

print"-------------------------------------------------------"  
#The above process is repeated for all power functions
Result_18 = AC.ApparentPwr(I_NoInput,Z)

if Result_18 == "Not enough inputs":
    print "-Apparent Power XL,Xc,No Input (Correct Error Message): Pass"
else:
    print "-Appparent Power XL,Xc,No Input (Correct Error Message): Fail"
    
Result_19 = AC.ApparentPwr(I,Z)
Expected_Result_19 = (I**2)*(Z)


if Result_19 == Expected_Result_19:
    print "-Apparent Power XL, Xc, I (Accuracy): Pass"
else:
    print "-Reactive Power XL, Xc, I (Accuracy): Fail"

print"-------------------------------------------------------"  
R=random.randint(0,10000)
Result_20 = AC.TruePwr(I_NoInput,R)

if Result_20 == "Not enough inputs":
    print "-True Power XL,Xc,No Input (Correct Error Message): Pass"
else:
    print "-True Power XL,Xc,No Input (Correct Error Message): Fail"

Result_21 = AC.TruePwr(I,R)
Expected_Result_21 = (I**2)*(R)


if Result_21 == Expected_Result_21:
    print "-True Power XL, Xc, I (Accuracy): Pass"
else:
    print "-True Power XL, Xc, I (Accuracy): Fail"

print"-------------------------------------------------------"  

raw_input("Press Enter to Exit: ")
