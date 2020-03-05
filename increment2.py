import Tkinter
import tkMessageBox
from Tkinter import *

#Visual element
root = Tkinter.Tk()

#no division by 0
#no alphanumeric
#has to be a float
#if component has a value of 0 then there it is considered not be on the circuit 
#
    
#Left section
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

def getVone():
    entryres.delete(0,END)
    entryres.insert(0,0)
    if var1.get() == 1:
        entryres.grid(column=2, row=1)
    else:
        entryres.grid_forget()
        
def getVtwo():
    entryind.delete(0,END)
    entryind.insert(0,0)
    if var2.get() == 1:
        entryind.grid(column=2, row=2)
    else:
        entryind.grid_forget()

def getVthree():
    entrycap.delete(0,END)
    entrycap.insert(0,0)
    if var3.get() == 1:
        entrycap.grid(column=2, row=3)
    else:
        entrycap.grid_forget()
        
def buildCircuit():
    circuitParameters = [0,0,0,0,0]
    if var1.get() == 1 and entryres != 0:
        circuitParameters[0] = int(entryres.get())
    if var2.get() == 1 and entryind != 0:
        circuitParameters[1] = int(entryind.get())
    if var3.get() == 1 and entrycap != 0:
        circuitParameters[2] = int(entrycap.get())
    circuitParameters[3] = int(entryvolt.get())
    circuitParameters[4] = int(entryfreq.get())

    return circuitParameters


        
checkres = Tkinter.Checkbutton(root, text = 'Resistance = ', variable=var1, command = getVone) 
checkres.grid(column=1,row=1)
entryres = Tkinter.Entry(root)

checkind = Tkinter.Checkbutton(root, text = 'Inductor =', variable=var2, command = getVtwo)
checkind.grid(column=1,row=2)
entryind = Tkinter.Entry(root)

checkcap = Tkinter.Checkbutton(root, text = 'Capacitor = ', variable=var3, command = getVthree)
checkcap.grid(column=1,row=3)
entrycap  = Tkinter.Entry(root)

labelvolt = Tkinter.Label(root, text = 'Volt = ')
labelvolt.grid(column=1, row=4)
entryvolt = Tkinter.Entry(root)
entryvolt.grid(column=2, row=4)
entryvolt.insert(0,0)

labelfreq = Tkinter.Label(root, text = 'Frequency =')
labelfreq.grid(column=1, row=5)
entryfreq = Tkinter.Entry(root)
entryfreq.grid(column=2, row=5)
entryfreq.insert(0,0)

buttonbuild = Tkinter.Button(root, text = 'Build Circuit', command = buildCircuit)
buttonbuild.grid(column=2, row=6)

root.mainloop()
#Functional element

