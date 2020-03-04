import Tkinter
import tkMessageBox
import math
import ACLib as AC

infowindow= Tkinter.Tk()

#Page Title
Titlemain=Tkinter.Label(infowindow, text="Information Page Layout (0.1)")
Titlemain.grid(row=1, column=3)

#Radians Switch

var1 = Tkinter.IntVar()
c1 = Tkinter.Checkbutton(infowindow, text='Radians',variable=var1, onvalue=1, offvalue=0, command=AC.turn_to_radians(AC.DEG))
c1.grid(row=17,column=3)

#Labels of Titles
Volt= Tkinter.Label(infowindow, text="Voltage:")
Volt.grid(row=2, column=1)
Current= Tkinter.Label(infowindow, text="Current:")
Current.grid(row=3, column=1)
Impedence= Tkinter.Label(infowindow, text="Impedence:")
Impedence.grid(row=4, column=1)
RR= Tkinter.Label(infowindow, text="Reactive Ressistance (XC):")
RR.grid(row=5, column=2)
IR= Tkinter.Label(infowindow, text="Inductive Ressistance (XL):")
IR.grid(row=6, column=2)
PhaseAngle= Tkinter.Label(infowindow, text="Phase Angle:")
PhaseAngle.grid(row=8, column=1)
PhaseofCoil= Tkinter.Label(infowindow, text="Phase of Coil:")
PhaseofCoil.grid(row=9, column=1)
ApparentPower= Tkinter.Label(infowindow, text="Apparent Power:")
ApparentPower.grid(row=10, column=1)
TruePower= Tkinter.Label(infowindow, text="True Power:")
TruePower.grid(row=11, column=1)
ReactivePower= Tkinter.Label(infowindow, text="Reactive Power:")
ReactivePower.grid(row=12, column=1)

#Test Variables
##V=150
##I= 30
##f=10
##L=10
##C=10
R=10
Xc=AC.ReactRes(AC.C)
Xl=AC.InductRes(AC.L)

#Labels of Answers
VoltDisplay= Tkinter.Label(infowindow, text=AC.V)
VoltDisplay.grid(row=2, column=2,)
CurrentDisplay= Tkinter.Label(infowindow, text=AC.I)
CurrentDisplay.grid(row=3, column=2,)
ImpedenceDisplay= Tkinter.Label(infowindow, text= AC.Impedence(Xc,Xl,R))
ImpedenceDisplay.grid(row=4, column=2,)
ReactiveDisplay= Tkinter.Label(infowindow, text= AC.ReactRes(AC.C))
ReactiveDisplay.grid(row=5, column=3,)
InductiveDisplay= Tkinter.Label(infowindow, text= AC.InductRes(AC.L))
InductiveDisplay.grid(row=6, column=3,)


infowindow.mainloop()
