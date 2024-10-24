# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from __future__ import division
import Tkinter
import tkMessageBox
import tkFont
from Tkinter import *
import math
import ACLib as AC
import Pmw # http://pmw.sourceforge.net/ .baloon function used. (Library reference) 

  
#Visual element
root = Tkinter.Tk()
root.resizable(width=False, height=False)

#Live font update declaration and initialization
ft = ['Calibri','Comic Sans MS']
fnt = Tkinter.StringVar(root)
fnt.set(ft[0])
#List of text elements and procedure to configure these element's font properties
lbllist = []
def callback(*args):
    for i in range(0,len(lbllist)):
        lbllist[i].config(font=(fnt.get(),scalefont.get()))

#Theme Colour (Will be expanded):

background = 'white'
graphcolour='grey'
root.configure(bg=background)


######################################################### LEFT GRİDS START


#Children - Canvases for Circuit and input section
cframe = Tkinter.LabelFrame(root, text = 'Circuit diagram', bg=background)
cframe.grid(column = 1, row=3,padx=10,pady=5)
circuit = Tkinter.Canvas(cframe, bg=background,height=265, width=300)
circuit.grid(padx=0,pady=5)

inputgrid = Tkinter.LabelFrame(root, text='Input data')
inputgrid.grid(column=1,row=1)

optionsgrid = Tkinter.LabelFrame(root,text='Options')
optionsgrid.grid(column=1,row=2,padx=10,pady=10)

######################################################### LEFT GRİDS (CIRCUIT IMAGE) START

#Elements For the Circuit Image

#Top line encompassing the resistor
circuit.create_line(50,50,250,50)
resistor = circuit.create_rectangle(100,25,200,75,state=HIDDEN,fill=background)
#Bottom line encompassing the capacitor
circuit.create_line(50,200,250,200)
capacitor = circuit.create_rectangle(140,175,160,225,state=HIDDEN)
capmask = circuit.create_rectangle(141,175,159,225,fill=background,outline=background,state=HIDDEN)
#Right line encompassing the capacitor
circuit.create_line(250,50,250,200)
#List holding the capacitor's elements
capelements=[circuit.create_oval(230,65,270,95,state=HIDDEN),circuit.create_oval(230,95,270,125,state=HIDDEN),circuit.create_oval(230,125,270,155,state=HIDDEN),circuit.create_oval(230,155,270,185,state=HIDDEN),circuit.create_oval(230,155,270,185,state=HIDDEN),circuit.create_rectangle(230,65,250,185,fill=background,outline=background,state=HIDDEN)]
#Left line encompassing the power source
circuit.create_line(50,50,50,200)
circuit.create_oval(25,100,75,150,fill=background)



#END
############################## INPUT GUI Starts

isres = IntVar()
isind = IntVar()
iscap = IntVar()

def getRes(): # opens resistance entry when checkbox variable is ticked
    entryres.delete(0,END)
    entryres.insert(0,0)
    if isres.get() == 1:
        circuit.itemconfig(resistor,state=NORMAL)
        entryres.grid(column=2, row=1)
        unitres.grid(column=3, row=1)
    else:
        circuit.itemconfig(resistor,state=HIDDEN)
        unitres.grid_forget()
        entryres.grid_forget()

def getInd():  # opens inductance entry when checkbox variable is ticked
    entryind.delete(0,END)
    entryind.insert(0,0)
    if isind.get() == 1:
        for i in range(0,6):
            circuit.itemconfig(capelements[i],state=NORMAL)
        entryind.grid(column=2, row=2)
        unitind.grid(column=3, row=2)
    else:
        for i in range(0,6):
            circuit.itemconfig(capelements[i],state=HIDDEN)
        unitind.grid_forget()
        entryind.grid_forget()

def getCap():# opens capacitance entry when checkbox variable is ticked
    entrycap.delete(0,END)
    entrycap.insert(0,0)
    if iscap.get() == 1:
        circuit.itemconfig(capmask,state=NORMAL)
        circuit.itemconfig(capacitor,state=NORMAL)
        entrycap.grid(column=2, row=3)
        unitcap.grid(column=3, row=3)
    else:
        circuit.itemconfig(capmask,state=HIDDEN)
        circuit.itemconfig(capacitor,state=HIDDEN)
        unitcap.grid_forget()
        entrycap.grid_forget()

def buildCircuit(): # makes build circuit button open info page, will refres vector and sine graphs
    infoWindow()
    buildImpedenceVector()
    buildCircuitVector()
    PhasorResonanceData()
    

def helpData():
    helpWindow()
    
Vo= 0
Cu = 0
In = 0
Cap = 0
Freq = 0
Res = 0

def refreshInput(): # gives AC library values the entry values
    global Vo
    global Cu
    global In
    global Cap
    global Freq
    global Res

    try:
        if isres.get() == 1 and float(entryres.get()) >= 0 and type(float(entryres.get())).__name__ == 'float':
            Res = float(entryres.get())
        elif isres.get() == 0:
            Res=0
        else:
            tkMessageBox.showinfo('Error','Input is negative in Resistance')
    except:
        tkMessageBox.showinfo('Error','Input is alphaumeric or empty in Resistance ')

    try:
        if isind.get() == 1 and float(entryind.get()) >= 0 and type(float(entryind.get())).__name__ == 'float':
            In = float(entryind.get())
        elif isind.get() == 0:
            In=0
        else:
            tkMessageBox.showinfo('Error','Input is negative in inductance')
    except:
            tkMessageBox.showinfo('Error','Input is alphaumeric or empty in inductance')

    try:
        if iscap.get() == 1 and float(entrycap.get()) >= 0 and type(float(entrycap.get())).__name__ == 'float':
            Cap = float(entrycap.get())
        elif iscap.get() == 0:
            Cap = 0
        else:
            tkMessageBox.showinfo('Error','Input is negative in capacitance')
    except:
            tkMessageBox.showinfo('Error','Input is alphaumeric or empty in capacitance')

    try:
        if type(float(entryvolt.get())).__name__ == 'float' and float(entryvolt.get()) >= 0:
            Vo = float(entryvolt.get())
        else:
            tkMessageBox.showinfo('Error','Input is negative in voltage')
            Vo=0
    except:
            tkMessageBox.showinfo('Error','Input is alphaumeric or empty in voltage')

    try:
        if type(float(entryfreq.get())).__name__ == 'float' and float(entryfreq.get()) >= 0:
            Freq = float(entryfreq.get())
        else:
            tkMessageBox.showinfo('Error','Input is negative in frequency')
            Freq=0
    except:
            tkMessageBox.showinfo('Error','Input is alphaumeric or empty in frequency')

    curvoltwave.delete("all")
    indsinwave.delete("all")


padval=9

checkres = Tkinter.Checkbutton(inputgrid, text = 'Resistance = ', variable=isres, command = getRes, offvalue = 0)
checkres.grid(column=1,row=1,sticky=W,pady=padval)
entryres = Tkinter.Entry(inputgrid)
unitres = Tkinter.Label(inputgrid,text='Ω')
lbllist.append(unitres)
lbllist.append(checkres)

checkind = Tkinter.Checkbutton(inputgrid, text = 'Inductor =', variable=isind, command = getInd, offvalue = 0)
checkind.grid(column=1,row=2,sticky=W,pady=padval)
entryind = Tkinter.Entry(inputgrid)
unitind = Tkinter.Label(inputgrid,text='H')
lbllist.append(unitind)
lbllist.append(checkind)

checkcap = Tkinter.Checkbutton(inputgrid, text = 'Capacitor = ', variable=iscap, command = getCap, offvalue = 0)
checkcap.grid(column=1,row=3,sticky=W,pady=padval)
entrycap  = Tkinter.Entry(inputgrid)
unitcap = Tkinter.Label(inputgrid,text='F')
lbllist.append(unitcap)
lbllist.append(checkcap)

labelvolt = Tkinter.Label(inputgrid, text = 'Volt = ')
labelvolt.grid(column=1, row=4,sticky=E,pady=padval,padx=0)
entryvolt = Tkinter.Entry(inputgrid)
entryvolt.grid(column=2, row=4)
entryvolt.insert(0,0)
unitvolt = Tkinter.Label(inputgrid,text='V')
unitvolt.grid(column=3,row=4)
lbllist.append(unitvolt)
lbllist.append(labelvolt)

labelfreq = Tkinter.Label(inputgrid, text = 'Frequency =')
labelfreq.grid(column=1, row=5,sticky=E,pady=padval)
entryfreq = Tkinter.Entry(inputgrid)
entryfreq.grid(column=2, row=5)
entryfreq.insert(0,0)
unitfreq = Tkinter.Label(inputgrid,text='Hz')
unitfreq.grid(column=3,row=5)
lbllist.append(unitfreq)
lbllist.append(labelfreq)

menufont = Tkinter.OptionMenu(optionsgrid, fnt, 'Comic Sans MS','Calibri') #Font type drop down menu
menufont.grid(column=1,row=1,padx=17)
lbllist.append(menufont)

scalefont = Tkinter.Scale(optionsgrid, from_=12, to=15, orient=Tkinter.HORIZONTAL,command=callback) #Font scale bar
scalefont.set(12)
scalefont.grid(column=2,row=1,padx=17)

buttonrefresh = Tkinter.Button(inputgrid, text = 'Set Values', command = refreshInput, font=(fnt.get(),scalefont.get())) # For registering the input valus to library
buttonrefresh.grid(column=1, row=6,pady=padval,padx=27)
lbllist.append(buttonrefresh)

buttonbuild = Tkinter.Button(inputgrid, text = 'Build Circuit', command = buildCircuit, font=(fnt.get(),scalefont.get())) # For use to draw graphs and update the info page
buttonbuild.grid(column=2, row=6,pady=padval,padx=27)
lbllist.append(buttonbuild)

helpbutton = Tkinter.Button(optionsgrid, text = 'Terms & Explanations',font=(fnt.get(),scalefont.get()), command = helpData,height=1, width=25) # For registering the input values to library
helpbutton.grid(column=1, row=2,columnspan=2,padx=45,pady=15)
lbllist.append(helpbutton)

entryres.delete(0,END)
entryres.insert(0,0)
entryind.delete(0,END)
entryind.insert(0,0)
entrycap.delete(0,END)
entrycap.insert(0,0)


############################################# ENTRY GET AND INFO PAGE LAUNCH FUNCTIONS END

################################## INFO WINDOW STARTS

#Instantiation of Results menu
infowindow= Toplevel(root)
infoballoon = Pmw.Balloon(infowindow)
infowindow.resizable(width=False, height=False)
infowindow.title("Information Page")
infowindow.protocol("WM_DELETE_WINDOW", infowindow.withdraw)


#Labels of Titles
Volt= Tkinter.Label(infowindow, text="Voltage:",cursor='question_arrow')
Volt.grid(row=2, column=1,sticky=W,pady=10)
lbllist.append(Volt)
infoballoon.bind(Volt,'Voltage is the difference in the electrical potential \n between the two terminals of the power source')

Current= Tkinter.Label(infowindow, text="Current:",cursor='question_arrow')
Current.grid(row=3, column=1,sticky=W,pady=10)
lbllist.append(Current)
infoballoon.bind(Current,'Current is the rate of the flow of electrically charged particles')

Impedence = Tkinter.Label(infowindow, text="Impedance:",cursor='question_arrow')
Impedence.grid(row=4, column=1,sticky=W,pady=10)
lbllist.append(Impedence)
infoballoon.bind(Impedence,'Impedance is effectively the resistance to alternating current in a circuit')

CR= Tkinter.Label(infowindow, text="Capactive Reactance (XC):",cursor='question_arrow')
CR.grid(row=5, column=1,sticky=W,pady=10)
lbllist.append(CR)
infoballoon.bind(CR,'Capacitve Reactance is a measure of the opposition to voltage across the capacitor')

IR= Tkinter.Label(infowindow, text="Inductive Reactance (XL):",cursor='question_arrow')
IR.grid(row=6, column=1,sticky=W,pady=10)
lbllist.append(IR)
infoballoon.bind(IR,'Inductive Reactance is a measure of the opposition to a change in direction of alteranting current')

PhaseAngle= Tkinter.Label(infowindow, text="Phase Angle:",cursor='question_arrow')
PhaseAngle.grid(row=8, column=1,sticky=W,pady=10)
lbllist.append(PhaseAngle)
infoballoon.bind(PhaseAngle,'The phase angle is the time difference between when circuit current and circuit voltage to reach their maximum values')

PhaseofCoil= Tkinter.Label(infowindow, text="Phase of Coil:",cursor='question_arrow')
PhaseofCoil.grid(row=9, column=1,sticky=W,pady=10)
lbllist.append(PhaseofCoil)
infoballoon.bind(PhaseofCoil,'The phase of the coil is the time difference between when coil current and coil voltage to reach their maximum values')

ApparentPower= Tkinter.Label(infowindow, text="Apparent Power:", cursor='question_arrow')
ApparentPower.grid(row=10, column=1,sticky=W,pady=10)
lbllist.append(ApparentPower)
infoballoon.bind(ApparentPower,'The apparent power is the power dissapated in the whole circuit')

TruePower= Tkinter.Label(infowindow, text="True Power:",cursor='question_arrow')
TruePower.grid(row=11, column=1,sticky=W,pady=10)
lbllist.append(TruePower)
infoballoon.bind(TruePower,'The true power is the power dissapated in the resistor')

ReactivePower= Tkinter.Label(infowindow, text="Reactive Power:",cursor='question_arrow')
ReactivePower.grid(row=12, column=1,sticky=W,pady=10)
lbllist.append(ReactivePower)
infoballoon.bind(ReactivePower,'Power dissapated in reactive components these being the inductor and the capacitor')

#Declaration and partial initialization of the results
VoltDisplay= Tkinter.Label(infowindow, text="0 V")
VoltDisplay.grid(row=2, column=2,sticky=W)
lbllist.append(VoltDisplay)

CurrentDisplay= Tkinter.Label(infowindow, text ="0 A")
CurrentDisplay.grid(row=3, column=2,sticky=W)
lbllist.append(CurrentDisplay)

ImpedenceDisplay= Tkinter.Label(infowindow, text="0 Ω")
ImpedenceDisplay.grid(row=4, column=2,sticky=W)
lbllist.append(ImpedenceDisplay)

ReactiveDisplay= Tkinter.Label(infowindow, text="0 Ω")
ReactiveDisplay.grid(row=5, column=2,sticky=W)
lbllist.append(ReactiveDisplay)

InductiveDisplay= Tkinter.Label(infowindow, text="0 Ω")
InductiveDisplay.grid(row=6, column=2,sticky=W)
lbllist.append(InductiveDisplay)

PhaseAngleDisplay= Tkinter.Label(infowindow, text="0 Radians")
PhaseAngleDisplay.grid(row=8, column=2,sticky=W)
lbllist.append(PhaseAngleDisplay)

PhaseCoilDisplay= Tkinter.Label(infowindow, text= "0 Radians")
PhaseCoilDisplay.grid(row=9, column=2,sticky=W)
lbllist.append(PhaseCoilDisplay)

ApparentPDisplay= Tkinter.Label(infowindow, text= "0 Volt-Ampere")
ApparentPDisplay.grid(row=10, column=2,sticky=W)
lbllist.append(ApparentPDisplay)

TruePDisplay= Tkinter.Label(infowindow, text= "0 Watts")
TruePDisplay.grid(row=11, column=2, sticky=W)
lbllist.append(TruePDisplay)

ReactivePDisplay= Tkinter.Label(infowindow, text= "0 VAr")
ReactivePDisplay.grid(row=12, column=2,sticky=W)
lbllist.append(ReactivePDisplay)

def infoWindow(): # Infowindow top page creation

    infowindow.deiconify()

    #Labels of Titles



#Test Variables

    Xc= AC.ReactRes(Cap,Freq)
    Xl= AC.InductRes(In,Freq)
    Z= AC.Impedence (Xc,Xl,Res)
    Cur= AC.CurrentCalc(Vo,Z)

#Labels of Answers


    VoltDisplay= Tkinter.Label(infowindow, text=str(Vo) + " Volts", font=(fnt.get(),scalefont.get()))
    VoltDisplay.grid(row=2, column=2,sticky=W)
    lbllist.append(VoltDisplay)

    Ccheck=False

    for i in str(AC.CurrentCalc(Vo,Z)):
                 if i =="e":
                     Ccheck= True

    if Cur==  "Not enough inputs":
        CurrentDisplay= Tkinter.Label(infowindow, text= str(AC.CurrentCalc(Vo,Z)), font=(fnt.get(),scalefont.get()))
        CurrentDisplay.grid(row=3, column=2)
        lbllist.append(CurrentDisplay)
    elif Ccheck==True:
        CurrentDisplay= Tkinter.Label(infowindow, text= str(AC.CurrentCalc(Vo,Z))+ " Amperes", font=(fnt.get(),scalefont.get()))
        CurrentDisplay.grid(row=3, column=2,sticky=W)
        lbllist.append(CurrentDisplay)
    else:
        CurrentDisplay= Tkinter.Label(infowindow, text= str(AC.CurrentCalc(Vo,Z))[:7]+ " Amperes", font=(fnt.get(),scalefont.get()))
        CurrentDisplay.grid(row=3, column=2,sticky=W)
        lbllist.append(CurrentDisplay)


    Impcheck=False
    for i in str(AC.Impedence(Xc,Xl,Res)):
                 if i =="e":
                     Impcheck= True
    if Impcheck== True:
        ImpedenceDisplay= Tkinter.Label(infowindow, text= str(AC.Impedence(Xc,Xl,Res))+ " Ohms", font=(fnt.get(),scalefont.get()))
        ImpedenceDisplay.grid(row=4, column=2,sticky=W)
        lbllist.append(ImpedenceDisplay)
    else:
        ImpedenceDisplay= Tkinter.Label(infowindow, text= str(AC.Impedence(Xc,Xl,Res))[0:7]+ " Ohms", font=(fnt.get(),scalefont.get()))
        ImpedenceDisplay.grid(row=4, column=2,sticky=W)
        lbllist.append(ImpedenceDisplay)

    Reacheck=False
    for i in str(AC.ReactRes(Cap,Freq)):
                 if i =="e":
                     Reacheck= True
    if  Reacheck==True:
        ReactiveDisplay= Tkinter.Label(infowindow, text= str(AC.ReactRes(Cap,Freq))+ " Ohms", font=(fnt.get(),scalefont.get()))
        ReactiveDisplay.grid(row=5, column=2,sticky=W,)
        lbllist.append(ReactiveDisplay)
    else:
        ReactiveDisplay= Tkinter.Label(infowindow, text= str(AC.ReactRes(Cap,Freq))[0:7]+ " Ohms", font=(fnt.get(),scalefont.get()))
        ReactiveDisplay.grid(row=5, column=2,sticky=W,)
        lbllist.append(ReactiveDisplay)


    Inductcheck=False
    for i in str(AC.InductRes(In,Freq)):
                 if i =="e":
                     Inductcheck= True
    if  Inductcheck== True:
        InductiveDisplay= Tkinter.Label(infowindow, text= str(AC.InductRes(In,Freq))+ " Ohms", font=(fnt.get(),scalefont.get()))
        InductiveDisplay.grid(row=6, column=2,sticky=W,)
        lbllist.append(InductiveDisplay)
    else:
        InductiveDisplay= Tkinter.Label(infowindow, text= str(AC.InductRes(In,Freq))[0:7]+ " Ohms", font=(fnt.get(),scalefont.get()))
        InductiveDisplay.grid(row=6, column=2,sticky=W,)
        lbllist.append(InductiveDisplay)

    PAncheck=False
    for i in str(AC.PhaseAng(Xc,Xl,Res)):
                 if i =="e":
                     PAncheck= True

    if PAncheck==True:
        PhaseAngleDisplay= Tkinter.Label(infowindow, text= str(AC.PhaseAng(Xc,Xl,Res))+ " Radians", font=(fnt.get(),scalefont.get()))
        PhaseAngleDisplay.grid(row=8, column=2,sticky=W,)
        lbllist.append(PhaseAngleDisplay)
    else:
        PhaseAngleDisplay= Tkinter.Label(infowindow, text= str(AC.PhaseAng(Xc,Xl,Res))[0:7]+ " Radians", font=(fnt.get(),scalefont.get()))
        PhaseAngleDisplay.grid(row=8, column=2,sticky=W,)
        lbllist.append(PhaseAngleDisplay)

    POCncheck=False
    for i in str(AC.PhaseNoC(Xl,Res)):
                 if i =="e":
                     POCncheck= True
    if POCncheck==True:
        PhaseCoilDisplay= Tkinter.Label(infowindow, text= str(AC.PhaseNoC(Xl,Res))+ "   Radians", font=(fnt.get(),scalefont.get()))
        PhaseCoilDisplay.grid(row=9, column=2,sticky=W,)
        lbllist.append(PhaseCoilDisplay)
    else:
        PhaseCoilDisplay= Tkinter.Label(infowindow, text= str(AC.PhaseNoC(Xl,Res))[0:7]+ "   Radians", font=(fnt.get(),scalefont.get()))
        PhaseCoilDisplay.grid(row=9, column=2,sticky=W,)
        lbllist.append(PhaseCoilDisplay)

    APcheck=False

    for i in str(AC.ApparentPwr(Cur,Z)):
                 if i =="e":
                     APcheck= True

    if AC.ApparentPwr(Cur,Z) == "Not enough inputs":
        ApparentPDisplay= Tkinter.Label(infowindow, text= str(AC.ApparentPwr(Cur,Z)), font=(fnt.get(),scalefont.get()))
        ApparentPDisplay.grid(row=10, column=2,)
        lbllist.append(ApparentPDisplay)
    elif APcheck==True:
        ApparentPDisplay= Tkinter.Label(infowindow, text= str(AC.ApparentPwr(Cur,Z))+ "   Volt-Ampere", font=(fnt.get(),scalefont.get()))
        ApparentPDisplay.grid(row=10, column=2,sticky=W,)
        lbllist.append(ApparentPDisplay)
    else:
        ApparentPDisplay= Tkinter.Label(infowindow, text= str(AC.ApparentPwr(Cur,Z))[0:7]+ "   Volt-Ampere", font=(fnt.get(),scalefont.get()))
        ApparentPDisplay.grid(row=10, column=2,sticky=W,)
        lbllist.append(ApparentPDisplay)

    TPheck=False

    for i in str(AC.TruePwr(Cur,Res)):
                 if i =="e":
                     TPheck= True

    if AC.TruePwr(Cur,Res) == "Not enough inputs":
        TruePDisplay= Tkinter.Label(infowindow, text= str(AC.TruePwr(Cur,Res)), font=(fnt.get(),scalefont.get()))
        TruePDisplay.grid(row=11, column=2,)
        lbllist.append(TruePDisplay)
    elif  TPheck== True:
        TruePDisplay= Tkinter.Label(infowindow, text= str(AC.TruePwr(Cur,Res))+ "   Watt", font=(fnt.get(),scalefont.get()))
        TruePDisplay.grid(row=11, column=2,sticky=W,)
        lbllist.append(TruePDisplay)
    else:
        TruePDisplay= Tkinter.Label(infowindow, text= str(AC.TruePwr(Cur,Res))[0:7]+ "   Watt", font=(fnt.get(),scalefont.get()))
        TruePDisplay.grid(row=11, column=2,sticky=W,)
        lbllist.append(TruePDisplay)

    RPheck=False

    for i in str(AC.ReactivePwr(Xl,Xc,Cur)):
                 if i =="e":
                     RPheck= True

    if AC.ReactivePwr(Xl,Xc,Cur) == "Not enough inputs":
        ReactivePDisplay= Tkinter.Label(infowindow, text= str(AC.ReactivePwr(Xl,Xc,Cur)), font=(fnt.get(),scalefont.get()))
        ReactivePDisplay.grid(row=12, column=2,)
        lbllist.append(ReactivePDisplay)
    elif RPheck== True:
        ReactivePDisplay= Tkinter.Label(infowindow, text= str(AC.ReactivePwr(Xl,Xc,Cur))+ "   Volt-Ampere Reactive", font=(fnt.get(),scalefont.get()))
        ReactivePDisplay.grid(row=12, column=2,sticky=W,)
        lbllist.append(ReactivePDisplay)
    else:
        ReactivePDisplay= Tkinter.Label(infowindow, text= str(AC.ReactivePwr(Xl,Xc,Cur))[0:7]+ "   Volt-Ampere Reactive", font=(fnt.get(),scalefont.get()))
        ReactivePDisplay.grid(row=12, column=2,sticky=W,)
        lbllist.append(ReactivePDisplay)
    #print Cur
        
    if Cur != 'Not enough inputs':
        curvoltGraph(AC.PhaseAng(Xc,Xl,Res),AC.CurrentCalc(Vo,Z))
        impedGraph(AC.ReactRes(Cap,Freq),AC.InductRes(In,Freq),AC.CurrentCalc(Vo,Z),AC.PhaseAng(Xc,Xl,Res))



############################## INFO WINDOW ENDS

##################################HELP WINDOW STARTS


helpwindow= Toplevel(root)
helpwindow.title("Help Window")
helpwindow.resizable(width=True, height=False)
helpwindow.protocol("WM_DELETE_WINDOW", helpwindow.withdraw)


ishelplaunched=False

def helpWindow():

    helpwindow.deiconify()

    global ishelplaunched

    
    if ishelplaunched==False:

        ishelplaunched=True

        containcanvas = Tkinter.Canvas(helpwindow,height=500,width=1275)
        scrollbarvertical = Tkinter.Scrollbar(helpwindow, orient="vertical", command=containcanvas.yview)

        frameoflabels = Tkinter.Frame(containcanvas)

        label= Label(frameoflabels, text="  ") #White space right
        label.grid(row=1,column=3)

        #list of labels


        Titlemain=Tkinter.Label(frameoflabels, text=" == Terms & Explanations == ",font=('Calibri',15,'bold'))
        Titlemain.grid(row=1, column=1, columnspan=2,padx=10,pady=10)
        #lbllist.append(Titlemain)

        ACtitle= Tkinter.Label(frameoflabels, text="Alternating Current (AC):", font=(fnt.get(),scalefont.get()))
        ACtitle.grid(row=2, column=1, sticky=W,)
        lbllist.append(ACtitle)

        Restitle= Tkinter.Label(frameoflabels, text=" Resistance: ", font=(fnt.get(),scalefont.get()))
        Restitle.grid(row=3, column=1, sticky=W)
        lbllist.append(Restitle)

        Inducttitle = Tkinter.Label(frameoflabels, text="Inductor and Inductance (L):", font=(fnt.get(),scalefont.get()))
        Inducttitle.grid(row=4, column=1, sticky=W)
        lbllist.append(Inducttitle)

        Captitle= Tkinter.Label(frameoflabels, text="Capacitor and Capacitance (C):", font=(fnt.get(),scalefont.get()))
        Captitle.grid(row=5, column=1, sticky=W)
        lbllist.append(Captitle)
            
        Suptitle= Tkinter.Label(frameoflabels, text="Supply (f-V):", font=(fnt.get(),scalefont.get()))
        Suptitle.grid(row=6, column=1, sticky=W)
        lbllist.append(Suptitle)

        Infotitle= Tkinter.Label(frameoflabels, text="Info Window:", font=(fnt.get(),scalefont.get()))
        Infotitle.grid(row=7, column=1, sticky=W)
        lbllist.append(Infotitle)

        PhaseAngle= Tkinter.Label(frameoflabels, text="Phase Angle:", font=(fnt.get(),scalefont.get()))
        PhaseAngle.grid(row=8, column=1, sticky=W)
        lbllist.append(PhaseAngle)

        Reacttitle= Tkinter.Label(frameoflabels, text="Reactance (XL & XC):", font=(fnt.get(),scalefont.get()))
        Reacttitle.grid(row=9, column=1, sticky=W)
        lbllist.append(Reacttitle)

        Imptitle= Tkinter.Label(frameoflabels, text="Impedance:", font=(fnt.get(),scalefont.get()))
        Imptitle.grid(row=10, column=1, sticky=W)
        lbllist.append(Imptitle)

        Resotitle= Tkinter.Label(frameoflabels, text="Resonance:", font=(fnt.get(),scalefont.get()))
        Resotitle.grid(row=11, column=1, sticky=W)
        lbllist.append(Resotitle)

        Vectitle= Tkinter.Label(frameoflabels, text="Vector Graphs:", font=(fnt.get(),scalefont.get()))
        Vectitle.grid(row=12, column=1, sticky=W)
        lbllist.append(Vectitle)

        Scaletitle= Tkinter.Label(frameoflabels, text="Scaling and Scaled Phase:", font=(fnt.get(),scalefont.get()))
        Scaletitle.grid(row=13, column=1, sticky=W)
        lbllist.append(Scaletitle)

        Sintitle= Tkinter.Label(frameoflabels, text="Sinus Graphs:", font=(fnt.get(),scalefont.get()))
        Sintitle.grid(row=14, column=1, sticky=W)
        lbllist.append(Sintitle)

        #Explanation:


        ACexp= Tkinter.Label(frameoflabels, text=" AC is an electric current that changes it's direction in fixed time periods.\n This program demonstrates different attributes of AC componenets in a circuit.",justify=LEFT, font=(fnt.get(),scalefont.get()))
        ACexp.grid(row=2, column=2, sticky=W)
        lbllist.append(ACexp)
        
        Resexp= Tkinter.Label(frameoflabels, text=" Resistance is a value that identifies how easy electric current can travel trough a material. It is measured in Ohms.",justify=LEFT, font=(fnt.get(),scalefont.get()))
        Resexp.grid(row=3, column=2, sticky=W,pady=15)
        lbllist.append(Resexp)

        Indexp = Tkinter.Label(frameoflabels, text=" Inductors are components which can produce electric charges using magnetic field changes.\n They can be visualised as coils of wire in circuit diagrams.\n Inductance identifies a materials ability to store energy in the magnetic field which can be converted to electric current.\n It is measured in Henrys",justify=LEFT,font=(fnt.get(),scalefont.get()))
        Indexp.grid(row=4, column=2, sticky=W)
        lbllist.append(Indexp)

        Capexp= Tkinter.Label(frameoflabels, text=" Capacitors are components that have the ability to store charges in electric fields.\n They achieve this using two paralel plates that creates the said field.\n Because of this reason they are represented with two paralel lines in a circuit diagram.\n Capacitance identifies a capacitors ability to store electric charges in electric fields.\n It is measured in Farads",justify=LEFT, font=(fnt.get(),scalefont.get()))
        Capexp.grid(row=5, column=2, sticky=W,pady=15)
        lbllist.append(Capexp)

        Supexp= Tkinter.Label(frameoflabels, text=" The supply has the ability to convert other type of energy to electrical. \n In AC circuits they have voltages as well frequencies to describe the time it takes for direction of current to shift.",justify=LEFT ,font=(fnt.get(),scalefont.get()))
        Supexp.grid(row=6, column=2, sticky=W,pady=15)
        lbllist.append(Supexp)

        Infex= Tkinter.Label(frameoflabels, text=" You can use the InfoWindow to find related calculations about power, phase and impedence. ", font=(fnt.get(),scalefont.get()))
        Infex.grid(row=7, column=2, sticky=W,pady=15)
        lbllist.append(Infex)

        PhaseAngle= Tkinter.Label(frameoflabels, text=" Is the time difference between the circuit components reaching their maximum voltage values.\n This is a challenging concept to visualize please refer to sinus and vector graphs. ",justify=LEFT, font=(fnt.get(),scalefont.get()))
        PhaseAngle.grid(row=8, column=2, sticky=W,pady=15)
        lbllist.append(PhaseAngle)

        Reactexp= Tkinter.Label(frameoflabels, text=" Reactance ,like resistance, is the opposition to electrical current, but it is caused by inductance or capacitance.\n For basic AC circuits it can be treated similar to resistance.",justify=LEFT, font=(fnt.get(),scalefont.get()))
        Reactexp.grid(row=9, column=2, sticky=W,pady=15)
        lbllist.append(Reactexp)

        Impex= Tkinter.Label(frameoflabels, text=" Impedance is the total opposition to electrical current.\n But because AC current is subject to phase for different components, it is a trigonometric operation rather than a simple summation.",justify=LEFT, font=(fnt.get(),scalefont.get()))
        Impex.grid(row=10, column=2, sticky=W,pady=15)
        lbllist.append(Impex)

        Resoexp= Tkinter.Label(frameoflabels, text=" Resonance is phenomenon that takes place when values of reactance for impedence and capacitance are the same.\n If a circuit is resonating impedence is equal to resistance and phase angle is zero. ",justify=LEFT, font=(fnt.get(),scalefont.get()))
        Resoexp.grid(row=11, column=2, sticky=W,pady=15)
        lbllist.append(Resoexp)

        Vecexp= Tkinter.Label(frameoflabels, text=" It is possible to conceptualize maximum voltage or current values as lines of a certain lenght spining around a fixed point.\n Vector graphs is a way to visualise this concept to show phase angle between different values.\n In a basic sense these lines or phasors can be moved from their fixed origin point and treated as vectors.\n You can observe voltage and reactance values and their phase behavior with the `Current-Voltage Vector` and `Impedence Vector`",justify=LEFT, font=(fnt.get(),scalefont.get()))
        Vecexp.grid(row=12, column=2, sticky=W,pady=15)
        lbllist.append(Vecexp)

        Scaexp= Tkinter.Label(frameoflabels, text="Because this program uses fixed windows for graphing, it is important to scale down values to make them visible when they exceed the window space.\n Program shows scaled phase and scaling factor to illustrate which values are scaled up or down and any difference in the phase angle cause by this.",justify=LEFT, font=(fnt.get(),scalefont.get()))
        Scaexp.grid(row=13, column=2, sticky=W,pady=15)
        lbllist.append(Scaexp)

        Sinexp= Tkinter.Label(frameoflabels, text=" Sinus function is a very illustrative way to visualise AC current and voltage.\n As mentioned before maximum values of voltages can be thought as phasor lines.\n Graphing their y-magnitude over time leads to a sinus graph.\n Using this graph it is possible to observe the voltage or current value of a component in a given time.\n It is also very useful for understanding phase angle. In basic terms phase angle is time difference between peak values of current-voltage or resistance-impedence.  ",justify=LEFT, font=(fnt.get(),scalefont.get()))
        Sinexp.grid(row=14, column=2, sticky=W,pady=15)
        lbllist.append(Sinexp)


        
        
        containcanvas.create_window(0, 0, anchor='nw', window=frameoflabels) #creates window in canvas and attribuites to the frameoflabels
        
        containcanvas.update_idletasks() # completes any geometry left pending. So when scroll region scrolls canvas new frames in the canvas are updated.

        containcanvas.configure(scrollregion=containcanvas.bbox('all'), yscrollcommand=scrollbarvertical.set) #configures canvas to have a scrollable region equal to everything inside it.
                         
        containcanvas.pack(fill='both', expand=True, side='left')
        scrollbarvertical.pack(fill='y', side='right')

    elif ishelplaunched==True:

        return None

##################################HELP WINDOW END
        
######################################################### MID GRIDS START


# Main LabelFrames

circuit_diagram_frame= LabelFrame(root, text= "Current-Voltage Vector",padx=5,pady=5)
circuit_diagram_frame.grid(column = 2, row=1,padx=5,pady=5)

data_diagram_frame= LabelFrame(root, text= "Resonance Data",padx=5,pady=5)
data_diagram_frame.grid(column = 2, row=2,)

impedence_diagram_frame= LabelFrame(root, text= "Impedance Vector",padx=5,pady=5)
impedence_diagram_frame.grid(column = 2, row=3,padx=5,pady=5)


# Canvases For Diagrams

circuitdiagram=Tkinter.Canvas(circuit_diagram_frame,bg=graphcolour,height=265, width=375)
circuitdiagram.grid(column=1,row=1)

legendimpedenceC=Tkinter.Canvas(circuit_diagram_frame,bg="light grey", height=265, width=65)
legendimpedenceC.grid(column=2,row=1)

diagramdata=Tkinter.Canvas(data_diagram_frame,bg=graphcolour,height=75,width=375+55)
diagramdata.grid(column=1,row=1)

impedencediagram=Tkinter.Canvas(impedence_diagram_frame,bg=graphcolour, height=265, width=375)
impedencediagram.grid(column=1,row=1)

legendimpedenceI=Tkinter.Canvas(impedence_diagram_frame,bg="light grey", height=265, width=65)
legendimpedenceI.grid(column=2,row=1)

# Legend texts:


#1#

Title= legendimpedenceC.create_text(33,20, text="Legend",font=('Calibri', 11, 'bold'))
R_line_text=legendimpedenceC.create_text(33,70, text="V(R)",font=('Calibri', 11, 'bold'))
XL_line_text=legendimpedenceC.create_text(33,110, text="V(L)",font=('Calibri', 11, 'bold'))
XC_line_text=legendimpedenceC.create_text(33,150, text="V(C)",font=('Calibri', 11, 'bold'))
Z_line_text=legendimpedenceC.create_text(33,190, text="V",font=('Calibri', 11, 'bold'))

R_line=legendimpedenceC.create_line(23,90,46,90,width=5,fill="blue")
XL_line=legendimpedenceC.create_line(23,130,46,130,width=5,fill="white")
XC_line=legendimpedenceC.create_line(23,170,46,170,width=5,fill="orange")
Z_line=legendimpedenceC.create_line(23,210,46,210,width=5,fill="peachpuff")

#2#
Title= legendimpedenceI.create_text(33,20, text="Legend",font=('Calibri', 11, 'bold'))
R_line_text=legendimpedenceI.create_text(33,70, text="R",font=('Calibri', 11, 'bold'))
XL_line_text=legendimpedenceI.create_text(33,110, text="XL",font=('Calibri', 11, 'bold'))
XC_line_text=legendimpedenceI.create_text(33,150, text="XC",font=('Calibri', 11, 'bold'))
Z_line_text=legendimpedenceI.create_text(33,190, text="Z",font=('Calibri', 11, 'bold'))

R_line=legendimpedenceI.create_line(23,90,46,90,width=5,fill="blue")
XL_line=legendimpedenceI.create_line(23,130,46,130,width=5,fill="white")
XC_line=legendimpedenceI.create_line(23,170,46,170,width=5,fill="orange")
Z_line=legendimpedenceI.create_line(23,210,46,210,width=5,fill="peachpuff")



# Diagram Functions: #

def buildCircuitVector():

    circuitdiagram.delete(Tkinter.ALL)

    global Res

    x1=0  # Starting Coordinates
    x2=0
    y1=265
    y2=150




    RMod= Res # Lenght Modifiers
    XcMod= AC.ReactRes(Cap,Freq)
    XlMod= AC.InductRes(In,Freq)
    ZMod= AC.Impedence (XcMod,XlMod,Res)
    CurMod= AC.CurrentCalc(Vo,ZMod)

    IModifier=AC.CurrentCalc(Vo,ZMod)

    if  CurMod != "Not enough inputs":
        RMod= RMod*IModifier
        XcMod= XcMod*IModifier
        XlMod=XlMod*IModifier
        ZMod= ZMod*IModifier
    else:
        RMod= 0
        XcMod= 0
        XlMod=0
        ZMod= 0

    #print RMod,XcMod,XlMod,ZMod,IModifier



    Ilegendcheck=False

    if RMod==0: # 0. MAIN CONDITION

        if XlMod>XcMod:

            Ilegendcheck=True

            if XlMod>=265 or XcMod>=265:
                ScaleMultiplier=0
                while XlMod>=265 or XcMod>=265:
                    ScaleMultiplier=ScaleMultiplier+1
                    XlMod=XlMod/(3)
                    XcMod=XcMod/(3)
                ScaleFactor= 3**(ScaleMultiplier)
                ScaleFactor= str(ScaleFactor)
                Scale_info=circuitdiagram.create_text(200,8, text="Vl/Vc: Scaled down by a factor of "+ ScaleFactor)


            elif (XlMod<=10 or XcMod<=10):
                ScaleMultiplier2=0
                if XlMod<132:
                    while XlMod<132:
                        ScaleMultiplier2=ScaleMultiplier2+1
                        XlMod=XlMod*(20)
                        XcMod=XcMod*(20)
                if XlMod>132:
                        ScaleMultiplier2=ScaleMultiplier2-1
                        XlMod=XlMod/(20)
                        XcMod=XcMod/(20)
                ScaleFactor2= 20**(ScaleMultiplier2)
                ScaleFactor2= str(ScaleFactor2)
                Scale_info=circuitdiagram.create_text(200,8, text="Xl and Xc: Scaled up by a factor of "+ ScaleFactor2)

            I=circuitdiagram.create_line(x1+125,y1,150+125,y1,width=3,fill="red") #I
            XL=circuitdiagram.create_line(x1+125,y1,x1+125,y1-XlMod,fill="white",width=3) #XL
            XC=circuitdiagram.create_line(x1+125+3,y1-XlMod,x1+125+3,y1-XlMod+XcMod,fill="orange",width=3) #XC
            Z=circuitdiagram.create_line(x1+125+5,y1,x1+125+5,y1-XlMod+XcMod,fill="peachpuff",width=3)#Z


        elif XcMod>XlMod:

            Ilegendcheck=True

            if XlMod>=150 or XcMod>=115:
                ScaleMultiplier=0
                while XlMod>=265 or XcMod>=115:
                    ScaleMultiplier=ScaleMultiplier+1
                    XlMod=XlMod/(3)
                    XcMod=XcMod/(3)
                ScaleFactor= 3**(ScaleMultiplier)
                ScaleFactor= str(ScaleFactor)
                Scale_info=circuitdiagram.create_text(200,8, text="Vl/Vc: Scaled down by a factor of "+ ScaleFactor)


            elif (XlMod<=10 or XcMod<=10):
                ScaleMultiplier2=0
                if XcMod<75:
                    while XcMod<75:
                        ScaleMultiplier2=ScaleMultiplier2+1
                        XlMod=XlMod*(3)
                        XcMod=XcMod*(3)
                if XcMod>75:
                        ScaleMultiplier2=ScaleMultiplier2-1
                        XlMod=XlMod/(3)
                        XcMod=XcMod/(3)
                ScaleFactor2= (3)**(ScaleMultiplier2)
                ScaleFactor2= str(ScaleFactor2)
                Scale_info=circuitdiagram.create_text(200,8, text="Xl and Xc: Scaled up by a factor of "+ ScaleFactor2)



            I=circuitdiagram.create_line(x2+125,y2,x2+275,y2,width=3,fill="red") #I
            XL=circuitdiagram.create_line(x2+125,y2,x2+125,y2-XlMod,fill="white",width=3) #XL
            XC=circuitdiagram.create_line(x2+125+3,y2-XlMod,x2+125+3,y2-XlMod+XcMod,fill="orange",width=3) #XC
            Z=circuitdiagram.create_line(x2+125+5,y2,x2+125+5,y2-XlMod+XcMod,fill="peachpuff",width=3)#Z

        if Ilegendcheck== True:
            I_line_text=legendimpedenceC.create_text(33,230, text="I")
            I_line=legendimpedenceC.create_line(23,250,46,250,width=5,fill="red")



    elif XlMod>XcMod: #FIRST MAIN CONDITION



    #Scaling Conditionals

        if XlMod>=265 or XcMod>=265:
            ScaleMultiplier=0
            while XlMod>=265 or XcMod>=265:
                ScaleMultiplier=ScaleMultiplier+1
                XlMod=XlMod/(3)
                XcMod=XcMod/(3)
            ScaleFactor= 3**(ScaleMultiplier)
            ScaleFactor= str(ScaleFactor)
            Scale_info=circuitdiagram.create_text(200,8, text="Vl/Vc: Scaled down by a factor of "+ ScaleFactor)

        elif (XlMod<=10 or XcMod<=10):
            ScaleMultiplier2=0
            if XlMod<132:
                while XlMod<132:
                    ScaleMultiplier2=ScaleMultiplier2+1
                    XlMod=XlMod*(20)
                    XcMod=XcMod*(20)
            if XlMod>132:
                    ScaleMultiplier2=ScaleMultiplier2-1
                    XlMod=XlMod/(20)
                    XcMod=XcMod/(20)
            ScaleFactor2= 20**(ScaleMultiplier2)
            ScaleFactor2= str(ScaleFactor2)
            Scale_info=circuitdiagram.create_text(200,8, text="Xl and Xc: Scaled up by a factor of "+ ScaleFactor2)


        if RMod>=300:
            ScaleMultiplier3=0
            while  RMod>300:
               ScaleMultiplier3=ScaleMultiplier3+1
               RMod=RMod/5
            ScaleFactor3= 5**(ScaleMultiplier3)
            ScaleFactor3= str(ScaleFactor3)
            Scale_info=circuitdiagram.create_text(200,20, text="R: Scaled down by a factor of "+ScaleFactor3)

        elif RMod<=10:
             ScaleMultiplier4=0
             while  RMod<=10:
                ScaleMultiplier4=ScaleMultiplier4+1
                RMod=RMod*30
             ScaleFactor4= 30**(ScaleMultiplier4)
             ScaleFactor4= str(ScaleFactor4)
             Scale_info=circuitdiagram.create_text(200,20, text="R: Scaled UP by a factor of "+ ScaleFactor4)

    # Relative Phase Angle Display

        R= Res
        Xc= AC.ReactRes(Cap,Freq)
        Xl= AC.InductRes(In,Freq)
        Z= AC.Impedence (XcMod,XlMod,RMod)


        NormalPhase=AC.PhaseAng(Xc,Xl,R)
        RelativePhase=0
        Displayphase=0
        if Z!=0:
            DisplayPhase=math.atan(XlMod-XcMod)/Z
            RelativePhase= NormalPhase-DisplayPhase


        if RelativePhase!=0 and DisplayPhase>NormalPhase:
            Scale_info=circuitdiagram.create_text(200,33, text="Scaled phase is: "+str(RelativePhase)+" radians bigger.")
        elif RelativePhase!=0 and DisplayPhase<NormalPhase:
            Scale_info=circuitdiagram.create_text(200,33, text="Scaled phase is: "+str(RelativePhase)+" radians smaller.")

    # Vector Diagram

        R=circuitdiagram.create_line(x1,y1,x1+RMod,y1,width=3,fill="blue") #R
        XL=circuitdiagram.create_line(x1+RMod,y1,x1+RMod,y1-XlMod,fill="white",width=3) #XL
        XC=circuitdiagram.create_line(x1+RMod+3,y1-XlMod,x1+RMod+3,y1-XlMod+XcMod,fill="orange",width=3) #XC
        Z=circuitdiagram.create_line(x1,y1,x1+RMod,y1-XlMod+XcMod,fill="peachpuff",width=3)#Z




    elif XcMod>XlMod: #SECOND MAIN CONDITION



    #Scaling Conditionals

        if XlMod>=150 or XcMod>=115:
            ScaleMultiplier=0
            while XlMod>=265 or XcMod>=115:
                ScaleMultiplier=ScaleMultiplier+1
                XlMod=XlMod/(3)
                XcMod=XcMod/(3)
            ScaleFactor= 3**(ScaleMultiplier)
            ScaleFactor= str(ScaleFactor)
            Scale_info=circuitdiagram.create_text(200,8, text="Vl/Vc: Scaled down by a factor of "+ ScaleFactor)

        elif (XlMod<=10 or XcMod<=10):
            ScaleMultiplier2=0
            if XcMod<75:
                while XcMod<75:
                    ScaleMultiplier2=ScaleMultiplier2+1
                    XlMod=XlMod*(3)
                    XcMod=XcMod*(3)
            if XcMod>75:
                    ScaleMultiplier2=ScaleMultiplier2-1
                    XlMod=XlMod/(3)
                    XcMod=XcMod/(3)
            ScaleFactor2= (3)**(ScaleMultiplier2)
            ScaleFactor2= str(ScaleFactor2)
            Scale_info=circuitdiagram.create_text(200,8, text="Xl and Xc: Scaled up by a factor of "+ ScaleFactor2)


        if RMod>=300:
            ScaleMultiplier3=0
            while  RMod>300:
               ScaleMultiplier3=ScaleMultiplier3+1
               RMod=RMod/5
            ScaleFactor3= 5**(ScaleMultiplier3)
            ScaleFactor3= str(ScaleFactor3)
            Scale_info=circuitdiagram.create_text(200,20, text="R: Scaled down by a factor of "+ScaleFactor3)

        elif RMod<=10:
             ScaleMultiplier3=0
             while  RMod<=10:
                ScaleMultiplier3=ScaleMultiplier3+1
                RMod=RMod*30
             ScaleFactor3= 30**(ScaleMultiplier3)
             ScaleFactor3= str(ScaleFactor3)
             Scale_info=circuitdiagram.create_text(200,20, text="R: Scaled UP by a factor of "+ ScaleFactor3)


    # Relative Phase Angle Display
        R= Res
        Xc= AC.ReactRes(Cap,Freq)
        Xl= AC.InductRes(In,Freq)
        Z= AC.Impedence (XcMod,XlMod,RMod)


        NormalPhase=AC.PhaseAng(Xc,Xl,R)
        RelativePhase=0
        Displayphase=0
        if Z!=0:
            DisplayPhase=math.atan(XlMod-XcMod)/Z
            RelativePhase= NormalPhase-DisplayPhase


        if RelativePhase!=0 and DisplayPhase>NormalPhase:
            Scale_info=circuitdiagram.create_text(200,33, text="Scaled phase is: "+str(RelativePhase)+" radians bigger.")
        elif RelativePhase!=0 and DisplayPhase<NormalPhase:
            Scale_info=circuitdiagram.create_text(200,33, text="Scaled phase is: "+str(RelativePhase)+" radians smaller.")

    # Vector Diagram

        R=circuitdiagram.create_line(x2,y2,x2+RMod,y2,width=3,fill="blue") #R
        XL=circuitdiagram.create_line(x2+RMod,y2,x2+RMod,y2-XlMod,fill="white",width=3) #XL
        XC=circuitdiagram.create_line(x2+RMod+3,y2-XlMod,x2+RMod+3,y2-XlMod+XcMod,fill="orange",width=3) #XC
        Z=circuitdiagram.create_line(x2,y2,x2+RMod,y2-XlMod+XcMod,fill="peachpuff",width=3)#Z



    elif (XlMod==0 and XcMod==0) and RMod!=0: # THIRD CONDITION

        if RMod>=300:
            ScaleMultiplier3=0
            while  RMod>300:
               ScaleMultiplier3=ScaleMultiplier3+1
               RMod=RMod/5
            ScaleFactor3= 5**(ScaleMultiplier3)
            ScaleFactor3= str(ScaleFactor3)
            Scale_info=circuitdiagram.create_text(200,20, text="R: Scaled down by a factor of "+ScaleFactor3)

        R=circuitdiagram.create_line(x2,y2,x2+RMod,y2,width=3,fill="peachpuff")
        R=circuitdiagram.create_line(x2,y2+5,x2+RMod,y2+5,width=3,fill="blue")




#Seperation#




def buildImpedenceVector():

    impedencediagram.delete(Tkinter.ALL)

    global Res

    x1=0  # Starting Coordinates
    x2=0
    y1=265
    y2=150


    RMod= Res  # Lenght Modifiers
    XcMod= AC.ReactRes(Cap,Freq)
    XlMod= AC.InductRes(In,Freq)
    ZMod= AC.Impedence (XcMod,XlMod,Res)
    CurMod= AC.CurrentCalc(Vo,ZMod)


    Ilegendcheck=False

    if RMod==0: #0. MAIN CONDITIONAL

        if XlMod>XcMod:

            Ilegendcheck=True

            if XlMod>=265 or XcMod>=265:
                ScaleMultiplier=0
                while XlMod>=265 or XcMod>=265:
                    ScaleMultiplier=ScaleMultiplier+1
                    XlMod=XlMod/(3)
                    XcMod=XcMod/(3)
                ScaleFactor= 3**(ScaleMultiplier)
                ScaleFactor= str(ScaleFactor)
                Scale_info=impedencediagram.create_text(200,8, text="Xl/Xc: Scaled down by a factor of "+ ScaleFactor)

            elif (XlMod<=10 or XcMod<=10):
                ScaleMultiplier2=0
                if XlMod<132:
                    while XlMod<132:
                        ScaleMultiplier2=ScaleMultiplier2+1
                        XlMod=XlMod*(20)
                        XcMod=XcMod*(20)
                if XlMod>132:
                        ScaleMultiplier2=ScaleMultiplier2-1
                        XlMod=XlMod/(20)
                        XcMod=XcMod/(20)
                ScaleFactor2= 20**(ScaleMultiplier2)
                ScaleFactor2= str(ScaleFactor2)
                Scale_info=impedencediagram.create_text(200,8, text="Xl and Xc: Scaled up by a factor of "+ ScaleFactor2)

            I=impedencediagram.create_line(x1+125,y1,150+125,y1,width=3,fill="red") #I
            XL=impedencediagram.create_line(x1+125,y1,x1+125,y1-XlMod,fill="white",width=3) #XL
            XC=impedencediagram.create_line(x1+125+3,y1-XlMod,x1+125+3,y1-XlMod+XcMod,fill="orange",width=3) #XC
            Z=impedencediagram.create_line(x1+125+5,y1,x1+125+5,y1-XlMod+XcMod,fill="peachpuff",width=3)#Z


        elif XcMod>XlMod:

            Ilegendcheck=True

            if XlMod>=150 or XcMod>=115:
                ScaleMultiplier=0
                while XlMod>=265 or XcMod>=115:
                    ScaleMultiplier=ScaleMultiplier+1
                    XlMod=XlMod/(3)
                    XcMod=XcMod/(3)
                ScaleFactor= 3**(ScaleMultiplier)
                ScaleFactor= str(ScaleFactor)
                Scale_info=impedencediagram.create_text(200,8, text="Xl/Xc: Scaled down by a factor of "+ ScaleFactor)


            elif (XlMod<=10 or XcMod<=10):
                ScaleMultiplier2=0
                if XcMod<75:
                    while XcMod<75:
                        ScaleMultiplier2=ScaleMultiplier2+1
                        XlMod=XlMod*(3)
                        XcMod=XcMod*(3)
                if XcMod>75:
                        ScaleMultiplier2=ScaleMultiplier2-1
                        XlMod=XlMod/(3)
                        XcMod=XcMod/(3)
                ScaleFactor2= (3)**(ScaleMultiplier2)
                ScaleFactor2= str(ScaleFactor2)
                Scale_info=impedencediagram.create_text(200,8, text="Xl and Xc: Scaled up by a factor of "+ ScaleFactor2)

            I=impedencediagram.create_line(x2+125,y2,x2+275,y2,width=3,fill="red") #I
            XL=impedencediagram.create_line(x2+125,y2,x2+125,y2-XlMod,fill="white",width=3) #XL
            XC=impedencediagram.create_line(x2+125+3,y2-XlMod,x2+125+3,y2-XlMod+XcMod,fill="orange",width=3) #XC
            Z=impedencediagram.create_line(x2+125+5,y2,x2+125+5,y2-XlMod+XcMod,fill="peachpuff",width=3)#Z

        if Ilegendcheck== True:
            I_line_text=legendimpedenceI.create_text(33,230, text="I")
            I_line=legendimpedenceI.create_line(23,250,46,250,width=5,fill="red")



    elif XlMod>XcMod: #FIRST MAIN CONDITION

        

    #Scaling Conditionals

        if XlMod>=265 or XcMod>=265:
            ScaleMultiplier=0
            while XlMod>=265 or XcMod>=265:
                ScaleMultiplier=ScaleMultiplier+1
                XlMod=XlMod/(3)
                XcMod=XcMod/(3)
            ScaleFactor= 3**(ScaleMultiplier)
            ScaleFactor= str(ScaleFactor)
            Scale_info=impedencediagram.create_text(200,8, text="Xl and Xc: Scaled down by a factor of "+ ScaleFactor)
####



        elif (XlMod<=10 or XcMod<=10):
            ScaleMultiplier2=0
            if XlMod<132:
                while XlMod<132:
                    ScaleMultiplier2=ScaleMultiplier2+1
                    XlMod=XlMod*(20)
                    XcMod=XcMod*(20)
            if XlMod>132:
                    ScaleMultiplier2=ScaleMultiplier2-1
                    XlMod=XlMod/(20)
                    XcMod=XcMod/(20)
            ScaleFactor2= 20**(ScaleMultiplier2)
            ScaleFactor2= str(ScaleFactor2)
            Scale_info=impedencediagram.create_text(200,8, text="Xl and Xc: Scaled up by a factor of "+ ScaleFactor2)

        

####

        if RMod>=300:
            ScaleMultiplier3=0
            while  RMod>300:
               ScaleMultiplier3=ScaleMultiplier3+1
               RMod=RMod/5
            ScaleFactor3= 5**(ScaleMultiplier3)
            ScaleFactor3= str(ScaleFactor3)
            Scale_info=impedencediagram.create_text(200,20, text="R: Scaled down by a factor of "+ScaleFactor3)

        elif RMod<=10:
             ScaleMultiplier4=0
             while  RMod<=10:
                ScaleMultiplier4=ScaleMultiplier4+1
                RMod=RMod*30
             ScaleFactor4= 30**(ScaleMultiplier4)
             ScaleFactor4= str(ScaleFactor4)
             Scale_info=impedencediagram.create_text(200,20, text="R: Scaled UP by a factor of "+ ScaleFactor4)

    # Relative Phase Angle Display
        R= Res
        Xc= AC.ReactRes(Cap,Freq)
        Xl= AC.InductRes(In,Freq)
        Z= AC.Impedence (XcMod,XlMod,RMod)

        
        
        NormalPhase=AC.PhaseAng(Xc,Xl,R)
        RelativePhase=0
        Displayphase=0
        if Z!=0:
            DisplayPhase=math.atan(XlMod-XcMod)/Z
            RelativePhase= NormalPhase-DisplayPhase



        if RelativePhase!=0 and DisplayPhase>NormalPhase:
            Scale_info=impedencediagram.create_text(200,33, text="Scaled phase is: "+str(RelativePhase)+" radians bigger.")
        elif RelativePhase!=0 and DisplayPhase<NormalPhase:
            Scale_info=impedencediagram.create_text(200,33, text="Scaled phase is: "+str(RelativePhase)+" radians smaller.")

    # Vector Diagram

        if RMod!=0:

            R=impedencediagram.create_line(x1,y1,x1+RMod,y1,width=3,fill="blue") #R
            XL=impedencediagram.create_line(x1+RMod,y1,x1+RMod,y1-XlMod,fill="white",width=3) #XL
            XC=impedencediagram.create_line(x1+RMod+3,y1-XlMod,x1+RMod+3,y1-XlMod+XcMod,fill="orange",width=3) #XC
            Z=impedencediagram.create_line(x1,y1,x1+RMod,y1-XlMod+XcMod,fill="peachpuff",width=3)#Z



    elif XcMod>XlMod: #SECOND MAIN CONDITION



    #Scaling Conditionals

        if XlMod>=150 or XcMod>=115:
            ScaleMultiplier=0
            while XlMod>=265 or XcMod>=115:
                ScaleMultiplier=ScaleMultiplier+1
                XlMod=XlMod/(3)
                XcMod=XcMod/(3)
            ScaleFactor= 3**(ScaleMultiplier)
            ScaleFactor= str(ScaleFactor)
            Scale_info=impedencediagram.create_text(200,8, text="Xl/Xc: Scaled down by a factor of "+ ScaleFactor)


        elif (XlMod<=10 or XcMod<=10):
            ScaleMultiplier2=0
            if XcMod<75:
                while XcMod<75:
                    ScaleMultiplier2=ScaleMultiplier2+1
                    XlMod=XlMod*(3)
                    XcMod=XcMod*(3)
            if XcMod>75:
                    ScaleMultiplier2=ScaleMultiplier2-1
                    XlMod=XlMod/(3)
                    XcMod=XcMod/(3)
            ScaleFactor2= (3)**(ScaleMultiplier2)
            ScaleFactor2= str(ScaleFactor2)
            Scale_info=impedencediagram.create_text(200,8, text="Xl and Xc: Scaled up by a factor of "+ ScaleFactor2)


        if RMod>=300:
            ScaleMultiplier3=0
            while  RMod>300:
               ScaleMultiplier3=ScaleMultiplier3+1
               RMod=RMod/5
            ScaleFactor3= 5**(ScaleMultiplier3)
            ScaleFactor3= str(ScaleFactor3)
            Scale_info=impedencediagram.create_text(200,20, text="R: Scaled down by a factor of "+ScaleFactor3)

        elif RMod<=10:
             ScaleMultiplier4=0
             while  RMod<=10:
                ScaleMultiplier4=ScaleMultiplier4+1
                RMod=RMod*30
             ScaleFactor4= 30**(ScaleMultiplier4)
             ScaleFactor4= str(ScaleFactor4)
             Scale_info=impedencediagram.create_text(200,20, text="R: Scaled UP by a factor of "+ ScaleFactor4)


    # Relative Phase Angle Display

        R= Res
        Xc= AC.ReactRes(Cap,Freq)
        Xl= AC.InductRes(In,Freq)
        Z= AC.Impedence (XcMod,XlMod,RMod)


        NormalPhase=AC.PhaseAng(Xc,Xl,R)
        RelativePhase=0
        Displayphase=0
        if Z!=0:
            DisplayPhase=math.atan(XlMod-XcMod)/Z
            RelativePhase= NormalPhase-DisplayPhase


        if RelativePhase!=0 and DisplayPhase>NormalPhase:
            Scale_info=impedencediagram.create_text(200,33, text="Scaled phase is: "+str(RelativePhase)+" radians bigger.")
        elif RelativePhase!=0 and DisplayPhase<NormalPhase:
            Scale_info=impedencediagram.create_text(200,33, text="Scaled phase is: "+str(RelativePhase)+" radians smaller.")

    # Vector Diagram

        R=impedencediagram.create_line(x2,y2,x2+RMod,y2,width=3,fill="blue") #R
        XL=impedencediagram.create_line(x2+RMod,y2,x2+RMod,y2-XlMod,fill="white",width=3) #XL
        XC=impedencediagram.create_line(x2+RMod+3,y2-XlMod,x2+RMod+3,y2-XlMod+XcMod,fill="orange",width=3) #XC
        Z=impedencediagram.create_line(x2,y2,x2+RMod,y2-XlMod+XcMod,fill="peachpuff",width=3)#Z



    elif (XlMod==0 and XcMod==0) and RMod!=0: # THIRD MAIN CONDITION

        if RMod>=300:
            ScaleMultiplier=0
            while  RMod>300:
               ScaleMultiplier=ScaleMultiplier+1
               RMod=RMod/5
            ScaleFactor= 5**(ScaleMultiplier)
            ScaleFactor= str(ScaleFactor)
            Scale_info=impedencediagram.create_text(200,20, text="R: Scaled down by a factor of " +ScaleFactor)

        elif RMod<=10:
             ScaleMultiplier4=0
             while  RMod<=10:
                ScaleMultiplier4=ScaleMultiplier4+1
                RMod=RMod*30
             ScaleFactor4= 30**(ScaleMultiplier4)
             ScaleFactor4= str(ScaleFactor4)
             Scale_info=impedencediagram.create_text(200,20, text="R: Scaled UP by a factor of "+ ScaleFactor4)

        R=impedencediagram.create_line(x2,y2,x2+RMod,y2,width=3,fill="peachpuff")
        R=impedencediagram.create_line(x2,y2+5,x2+RMod,y2+5,width=3,fill="blue")


    #elif XcMod=XlMod and Freq=0:

# Data Text and Function

ComponentCheck=diagramdata.create_text(135,15, text=" Do the circuit have the needed components (LCR): ")
ResonanceCheck=diagramdata.create_text(70,43, text=" Is the Circuit Resonating: ")
Toresonance=diagramdata.create_text(45,65, text=" Until Resonance:")

def PhasorResonanceData():

    diagramdata.delete(Tkinter.ALL)

    ComponentCheck=diagramdata.create_text(135,15, text=" Do the circuit have the needed components (LCR): ")
    ResonanceCheck=diagramdata.create_text(70,43, text=" Is the Circuit Resonating: ")
    Toresonance=diagramdata.create_text(45,65, text=" Until Resonance:")

    CompCheck=False
    if In !=0 and Cap !=0 and Res !=0 and Vo!=0 and Freq != 0:
        ComponentCheck=diagramdata.create_text(285,15, text="YES", fill="darkgreen")
    else:
        CompCheck=True
        ComponentCheck=diagramdata.create_text(305,15, text="     Circuit Needs", fill="red")
        if In ==0:
            ComponentCheck=diagramdata.create_text(55,28, text="Inductance,", fill="red")
        if Cap ==0:
            ComponentCheck=diagramdata.create_text(135,28, text="Capacitance,", fill="red")
        if Res ==0 :
            ComponentCheck=diagramdata.create_text(215,28, text="Resistance,", fill="red")
        if (Vo ==0 or Freq==0):
            ComponentCheck=diagramdata.create_text(290,28, text="Supply.", fill="red")

    R= Res
    Xc= AC.ReactRes(Cap,Freq)
    Xl= AC.InductRes(In,Freq)

    PhaseData=float(AC.PhaseAng(Xc,Xl,R))
    ToResData= (PhaseData*180)/math.pi

    #print PhaseData>-0.00872664626, PhaseData<0

    if PhaseData>0:
        if (PhaseData< 0.00872664626):
            ResonanceCheck=diagramdata.create_text(175,43, text="= RESONANCE =", fill ="darkgreen")
        elif PhaseData<0.15:
            ResonanceCheck=diagramdata.create_text(225,43, text="=  VERY CLOSE TO RESONANCE =", fill ="darkgreen")
        else:
            ResonanceCheck=diagramdata.create_text(195,43, text="= NO RESONANCE =", fill ="red")

    elif PhaseData<0:
          if (PhaseData> -0.00872664626):
            ResonanceCheck=diagramdata.create_text(175,43, text="= RESONANCE =", fill ="darkgreen")
          elif PhaseData>-0.15:
            ResonanceCheck=diagramdata.create_text(225,43, text="=  VERY CLOSE TO RESONANCE =", fill ="darkgreen")
          else:
            ResonanceCheck=diagramdata.create_text(195,43, text="= NO RESONANCE =", fill ="red")
    elif PhaseData ==0 and (In !=0 and Cap !=0 and Res !=0 and Vo!=0 and Freq != 0) :
            ResonanceCheck=diagramdata.create_text(225,43, text="= TRUE RESONANCE =", fill ="darkgreen")
    elif CompCheck==True:
            ResonanceCheck=diagramdata.create_text(195,43, text="= NO RESONANCE =", fill ="red")


    Toresonance=diagramdata.create_text(185,65, text= str(ToResData)+" Degrees")






######################################################### MID GRIDS (PHASOR DIAGRAMS) END


######################################################### RIGHT GRIDS (SİNE GRAPHS) START

# Main LabelFrames

curvoltwave_frame= LabelFrame(root, text= "Current-Voltage Graph",padx=5,pady=5)
curvoltwave_frame.grid(column = 3, row=1,padx=5,pady=5)

options_diagram_frame= LabelFrame(root, text= "SineGraph Data",padx=5,pady=5)
options_diagram_frame.grid(column = 3, row=2)

indsinwave_frame= LabelFrame(root, text= "Component Voltage Graph",padx=5,pady=5)
indsinwave_frame.grid(column = 3, row=3,padx=5,pady=5)


#Canvases For Graphs

curvoltwave=Tkinter.Canvas(curvoltwave_frame,bg=graphcolour,width=360,height=245)
curvoltwave.grid(column=1,row=1,pady=10)


options=Tkinter.Canvas(options_diagram_frame,bg=graphcolour,height=75,width=375+55)
options.grid(column=1,row=1)

indsinwave=Tkinter.Canvas(indsinwave_frame,bg=graphcolour,width=375,height=265)
indsinwave.grid(column=1,row=1)

legendcircuitwave=Tkinter.Canvas(curvoltwave_frame,bg="light grey", height=245, width=65)
legendcircuitwave.grid(column=2,row=1)

legendimpedencewave=Tkinter.Canvas(indsinwave_frame,bg="light grey", height=265, width=65)
legendimpedencewave.grid(column=2,row=1)

# Legend texts:

#1# Circuit-Voltage Legend

Title= legendcircuitwave.create_text(33,20, text="Legend",font=('Calibri', 11, 'bold'))
V_line_text=legendcircuitwave.create_text(33,70, text="V",font=('Calibri', 11, 'bold'))
I_line_text=legendcircuitwave.create_text(33,150, text="I",font=('Calibri', 11, 'bold'))


V_line=legendcircuitwave.create_line(23,90,46,90,width=5,fill="blue")
I_line=legendcircuitwave.create_line(23,170,46,170,width=5,fill="green")


#2# Component Legend:

Title= legendimpedencewave.create_text(33,20, text="Legend",font=('Calibri', 11, 'bold'))
VR_line_text=legendimpedencewave.create_text(33,90, text="V(R)",font=('Calibri', 11, 'bold'))
VL_line_text=legendimpedencewave.create_text(33,130, text="V(L)",font=('Calibri', 11, 'bold'))
VC_line_text=legendimpedencewave.create_text(33,170, text="V(C)",font=('Calibri', 11, 'bold'))

VR_line=legendimpedencewave.create_line(23,90+20,46,90+20,width=5,fill="blue")
VL_line=legendimpedencewave.create_line(23,130+20,46,130+20,width=5,fill="red")
VC_line=legendimpedencewave.create_line(23,170+20,46,170+20,width=5,fill="green")


#optionslabels

firstamplitude=options.create_text(35,15, text=" Amplitude:")
firstfrequency=options.create_text(280,15, text="Frequency:")

##firstfrequency=options.create_text(180,15, text=" Is Frequncy Scaled:")
##firstamplitude=options.create_text(320,15, text=" Is Amplitude Scaled:")
Toresonance=options.create_text(35,45, text=" Amplitude:")
firstfrequency=options.create_text(280,45, text="Frequency:")

##ResonanceCheck=options.create_text(180,45, text=" Is Frequncy Scaled:")
##ResonanceCheck=options.create_text(320,45, text=" Is Amplitude Scaled:")


def buildGraph(can,col):
    #Horizontal
    can.create_line(0, 100, 450, 100,fill=col)
    can.create_line(0, 50, 450, 50,fill=col)
    can.create_line(0, 150, 450, 150,fill=col)
    can.create_line(0, 25, 450, 25,fill=col)
    can.create_line(0, 75, 450, 75,fill=col)
    can.create_line(0, 125, 450, 125,fill=col)
    can.create_line(0, 175, 450, 175,fill=col)
    #Vertical
    can.create_line(91, 0, 91, 201,fill=col)
    can.create_line(181, 0, 181, 201,fill=col)
    can.create_line(271, 0, 271, 201,fill=col)
    can.create_line(91, 0, 91, 201,fill=col)
    can.create_line(181, 0, 181, 201,fill=col)
    can.create_line(271, 0, 271, 201,fill=col)

#valu[] is array which holds and sorts values using a bubble sort
def bubbleSort(value):
    n = len(value)
    for i in range(0,n-1):
        for x in range(0, n-i-1):
            if value[x] < value[x+1] :
                minsel = value[x+1]
                maxsel = value[x]
                value[x] = minsel
                value[x+1] = maxsel
    return value

#Allows integers to fit into absolute constraints by making magnitude relative


def relativeScale(maxmag,minmag,val):
        #first values
        fvalue = bubbleSort(val)
        leng = len(fvalue)
        #altered values
        avalue=[]
        if fvalue[0] > maxmag or fvalue[leng-1] < minmag:
            sectors= float((maxmag-minmag)/leng)
            for i in range(0,leng):
                avalue.append(fvalue[i])
            if fvalue[0] > maxmag:
                avalue[0] = maxmag
                for i in range(1,leng):
                    scale = fvalue[i]/fvalue[0]
                    if scale <= 0.5:
                        scale = -scale
                    avalue[i] = ((leng-i)*sectors)+(scale*(sectors))
                    if avalue[i] < minmag:
                        avalue[i] = minmag + (leng-i)
            else:
                avalue[leng-1] = minmag
                for i in range(leng-1,-1,-1):
                        scale = (fvalue[i]/fvalue[0])
                        if scale <= 0.5:
                            scale = -scale
                        avalue[i] = ((leng-i)*sectors)+(scale*(sectors))
                        if avalue[i] > maxmag:
                            avalue[i] = avalue[i+1] + minmag
            return avalue
        else:
            return fvalue

#cap V-I graph
#451 pixels is approx 4pi
def curvoltGraph(ang,cur):
    options.delete("all")
    curvoltwave.delete("all")
#scaling for frequency
    freq=Freq
    if freq > 100:
        freq = 100
    elif freq < 10:
        freq = 10
#add check for when currennt  = 0

    val=[Vo,cur]
    amp = [0,0]
    amp = relativeScale(60,4,val)
    
    if Vo >= cur:
        vamp = amp[0]
        camp = amp[1]
    else:
        camp = amp[0]
        vamp = amp[1]

    #CURRENT
    for i in range(1,451):
        prei = i - 1
        prey = camp*math.sin(float(prei*(2*3.14*freq)+ang))
        y = camp*math.sin(float(i*(2*3.14*freq)+ang))
        curvoltwave.create_line(prei, prey+100, i, y+100,fill='green')
    #VOLTAGE
    for i in range(1,451):
        prei = i - 1
        prey = vamp*math.sin(float(prei*(2*3.14*freq)))
        y = vamp*math.sin(float(i*(2*3.14*freq)))
        curvoltwave.create_line(prei, prey+100, i, y+100,fill='blue')

    buildGraph(curvoltwave,'#bebebe')

    firstamplitude=options.create_text(35,15, text=" Amplitude:")
    firstfrequency=options.create_text(280,15, text="Frequency:")

    Toresonance=options.create_text(35,45, text=" Amplitude:")
    firstfrequency=options.create_text(280,45, text="Frequency:")

    vampdis=options.create_text(95,15, text=" V is "+str(vamp))
    campdis=options.create_text(185,15, text=" I is "+str(camp))

    freqdis=options.create_text(365,15, text=str(freq)+" Hertz")

def impedGraph(cap,ind,cur,ang):
        freq=Freq
        if freq > 100:
            freq = 100
        elif freq < 10:
            freq = 10
        indsinwave.delete("all")
        res = float(entryres.get())
        #figure phase difference
        #Res
        ramp = res*cur
        camp = cap*cur
        iamp = ind*cur
        val=[ramp,camp,iamp]
        val = relativeScale(75,2,val)
        if res >= ind and ind >= cap:
            ramp = val[0]
            iamp = val[1]
            camp = val[2]
        elif res >= cap and cap >= ind:
            ramp = val[0]
            camp = val[1]
            iamp = val[2]
        elif cap >= res and res >= ind:
            camp = val[0]
            ramp = val[1]
            iamp = val[2]
        elif ind >= cap and cap >= res:
            iamp = val[0]
            camp = val[1]
            ramp = val[2]
        elif cap >= ind and ind >= res:
            camp = val[0]
            iamp = val[1]
            ramp = val[2]
        elif ind >= res and res >= cap:
            iamp = val[0]
            ramp = val[1]
            camp = val[2]
        #Resistance should be in phase with current
        #Res
        for i in range(1,451):
            if isres.get() == 1 and float(entryres.get()) > 0:
                prei = i - 1
                prey = ramp*math.sin(prei*(2*3.14*freq)+ang)
                y = ramp*math.sin(i*(2*3.14*freq)+ang)
                indsinwave.create_line(prei, prey+100, i, y+100,fill='blue')
        #+90 from current
        #Cap
        for i in range(1,451):
            if iscap.get() == 1 and float(entrycap.get()) > 0: 
                prei = i - 1
                prey = camp*math.sin(prei*(2*3.14*freq)+(ang+1.57))
                y = camp*math.sin(i*(2*3.14*freq)+(ang+1.57))
                indsinwave.create_line(prei, prey+100, i, y+100,fill='green')
        #-90 from current
        #Ind
        for i in range(1,451):
            if isind.get() == 1 and float(entryind.get()) > 0:
                prei = i - 1
                prey = iamp*math.sin(prei*(2*3.14*freq)+(ang-1.57))
                y = iamp*math.sin(i*(2*3.14*freq)+(ang-1.57))
                indsinwave.create_line(prei, prey+100, i, y+100,fill='red')

        Rampdis=options.create_text(55,65, text=" VR is "+str(ramp))
        capampdis=options.create_text(155,45, text=" VC is "+str(camp))
        indampdis=options.create_text(155,65, text=" VL is "+str(iamp))


        freqdis=options.create_text(365,45, text=str(freq)+" Hertz")     

#voltage through each of the components and respective phase

######################################################### RİGHT GRIDS (SİNE GRAPHS) END
fnt.trace('w',callback)
root.mainloop() #Functional element
