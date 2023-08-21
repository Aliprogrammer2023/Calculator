from tkinter import *
import tkinter.messagebox
#settings
root=Tk()
root.title("Calculator")
root.geometry('400x200')
root.resizable(width=False,height=False)
color='gray'
root.configure(bg=color)

# variables
number1=StringVar()
number2=StringVar()
res=StringVar()

#frame
top_first=Frame(root,width=400,height=50, bg=color)
top_first.pack(side=TOP)

top_second=Frame(root,width=400,height=50, bg=color)
top_second.pack(side=TOP)

top_third=Frame(root,width=400,height=50,bg=color)
top_third.pack(side=TOP)

top_fourth=Frame(root,width=400,height=50,bg=color)
top_fourth.pack(side=TOP)

#functions
def errorMsg(ms):
    if ms=='error':
        tkinter.messagebox.showerror('Error','Something went wrong!')
    elif ms=='Division':
        tkinter.messagebox.showerror('Division Error','Can not division by 0!')

def plus():
    try:
        value=float(number1.get())+float(number2.get())
        res.set(value)
    except:
        errorMsg('error')

def minus():
    try:
        value=float(number1.get())-float(number2.get())
        res.set(value)
    except:
        errorMsg('error')

def mul():
    try:
        value=float(number1.get())*float(number2.get())
        res.set(value)
    except:
        errorMsg('error')

def div():
    
    if number2=='0':
        errorMsg('Division')
    elif number2!='0':
        try:
            value=float(number1.get())/float(number2.get())
            res.set(value)
        except:
            errorMsg('error')

#buttons
PlusBtn=Button(top_third,text='+',width=10,highlightbackground=color, command= lambda: plus())
PlusBtn.pack(side=LEFT,padx=10,pady=10)

MinusBtn=Button(top_third,text='-',width=10,highlightbackground=color, command= lambda: minus())
MinusBtn.pack(side=LEFT,padx=10,pady=10)

MulBtn=Button(top_third,text='*',width=10,highlightbackground=color,command= lambda:mul())
MulBtn.pack(side=LEFT,padx=10,pady=10)

DivBtn=Button(top_third,text='/',width=10,highlightbackground=color,command= lambda: div())
DivBtn.pack(side=LEFT,padx=10,pady=10)

#entries and labels
FirstLabel=Label(top_first,text='Enter first number: ',bg=color)
FirstLabel.pack(side=LEFT, padx=10,pady=10)

FitrstEntry=Entry(top_first,highlightbackground=color, textvariable=number1)
FitrstEntry.pack(side=LEFT)

SecondLabel=Label(top_second,text='Enter first number: ',bg=color)
SecondLabel.pack(side=LEFT, padx=10,pady=10)

SecondEntry=Entry(top_second,highlightbackground=color, textvariable=number2)
SecondEntry.pack(side=LEFT)

result=Label(top_fourth,text='The result is:  ',bg=color)
result.pack(side=LEFT, padx=10,pady=10)

resultEntry=Entry(top_fourth,highlightbackground=color, textvariable=res)
resultEntry.pack(side=LEFT)

root.mainloop()