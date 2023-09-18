#MODULES
from tkinter import*
from tkinter import messagebox
import math

#GUI

root=Tk()
root.title("Scientific Calculator")
root.resizable("False","False")
root.geometry("500x600+0+0")
root.configure(bg="#000000")

#LABEL

Label_result=Label(root,width=20,height=1,text="",font=("TIMES",25),bg="#000000",fg="#FFFFFF")
Label_result.place(x="60",y="10")


#VARIABLES

equation = ""
x=""
trigo=""
value=""

#FUNCTIONS

def show(value):                                                    #Function for all the integer and DMAS operations

    global equation
    global x
    x=str(equation)+str(value)
    equation=str(equation)+value
    Label_result.config(text=equation)

def exponent(value):                                               #Function for exponents

    global equation
    equation+=value
    result=equation
    Label_result.config(text=result)

def sqroot(value):                                                 #Function for roots

    global equation
    global trigo
    global x
    equation=str(equation)+value
    trigo=equation
    y=equation

    try:

        x=eval(str(equation))

        Label_result.config(text=str(round(float(x),2)))

    except SyntaxError:

        Label_result.config(text="Error")

    equation=str(round(x,2))


def clear():                                                   #Function for clearing the Label

    global equation
    equation=""
    Label_result.config(text=equation)

def sin():                                                     #Sine function

    global equation
    global x
    global trigo

    trigo='sin'+str(equation)

    y=round(math.sin(math.radians(float(eval(str(equation))))),2**32)
    
    x=str(eval(str(y)))

    Label_result.config(text=str(eval(str(y))))
    equation=x

def cos():                                                    #Cosine function

    global equation
    global x
    global trigo

    trigo="cos"+str(equation)
    
    y=round(math.cos(math.radians(float(eval(str(equation))))),2**32)
    
    x=str(eval(str(y)))
    
    Label_result.config(text=x)
    equation=x
     
    
def tan():                                                    #Tan function

    global equation
    global x
    global trigo
    
    trigo="tan"+str(equation)
    
    y=round(math.tan(math.radians(float(eval(str(equation))))),2**32)
    
    x=str(eval(str(y)))
    
    if float(x)==1.633123935319537e+16:

        x="Infinity"
    
    Label_result.config(text=x)
    equation=x
     
def backspace():                                             #Backspace function

    global equation
    
    equation=(str(equation)[:-1])
    
    Label_result.config(text=equation)


def ln():                                                    #Log to the base e

    global x
    global equation
    global trigo
    
    trigo="ln"+str(equation)

    try:
    
        y=math.log(float(eval(str(equation))))
        
        x=str(eval(str(y)))
    
    except ValueError:

        x="Undefined"
    
    Label_result.config(text=x)
    equation=x


def log():                                                 #Log to the base 10

    global x
    global equation
    global trigo
    
    trigo="log"+str(equation)
    
    try:
        y=math.log10(float(eval(str(equation))))
        
        x=str(eval(str(y)))
    
    except ValueError:
        
        x="Undefined"
    
    Label_result.config(text=x)
    equation=x
    
def cosec():                                               #Cosecant function

    global x
    global equation
    global trigo
    
    trigo="cosec"+str(equation)
    
    y=0
    
    try:

        y=(math.sin(math.radians(float(eval(str(equation))))**(-1)))
        x=str(eval(str(round(y,6))))

    except ZeroDivisionError:

        x="Infinity"

    Label_result.config(text=x)
    
    equation=x

def sec():                                                #Secant function

    global x
    global equation
    global trigo
    
    trigo="sec"+str(equation)

    y=0
    
    try:
        y=(math.cos(math.radians(float(eval(str(equation))))**(-1)))
        
        x=str(eval(str(round(y,6))))
    
    except ZeroDivisionError:

        x="Infinity"
    
    Label_result.config(text=x)
    equation=x

def asin():                                            #Arcsin function

    global equation
    global x
    global trigo

    trigo='arcsin'+str(equation)

    try:

        y=round(math.asin(float(equation))*57.2958)
        
        x=str(y)

        Label_result.config(text=x+"°")

    except ValueError:

        Label_result.config(text="Domain Error")
    equation=x

def acos():                                           #Arccos function

    global equation
    global x
    global trigo

    trigo='arccos'+str(equation)
    
    try:

        y=round(math.acos(float(equation))*57.2958)

        x=str(y)

        Label_result.config(text=x+"°")

    except ValueError:

        Label_result.config(text="Domain Error")

    equation=x

def atan():                                          #Arctan function

    global equation
    global x
    global trigo

    trigo="arctan"+str(equation)

    try:

        y=round(math.atan(float(equation))*57.2958)
        x=str(y)
        Label_result.config(text=x+"°")

    except ValueError:

        Label_result.config(text="Domain Error")

    equation=x

def acosec():                                       #ArcCosec function

    global equation
    global x
    global trigo

    trigo="arccsc"+ str(equation)

    try:

        y=float(str(equation))

        try:

            z=math.asin(1/y)

            x=str(round(z*57.2958))

        except ZeroDivisionError:

            x="Domain Error"

        Label_result.config(text=x+"°")

    except ValueError:

        Label_result.config(text="Domain Error")

def asec():                                       #ArcSecant function

    global equation
    global x
    global trigo

    trigo="arcsec"+ str(equation)

    try:

        y=float(str(equation))

        try:

            z=math.acos(1/y)

            x=str(round(z*57.2958))

        except ZeroDivisionError:

            x="Domain Error"

        Label_result.config(text=x+"°")

    except ValueError:

        Label_result.config(text="Domain Error")

def save():                                      #Save function

    global equation
    global x
    global trigo
    global value

    f=open("history.txt","a")
    f.seek(0,2)

    f.write("\n")

    try:


        try:

            if str(equation)==str(eval(str(equation))) or str(equation)==x or "**" in str(x):

                if trigo!="":

                    f.write(trigo)
                    f.write('=')
                    f.write(str(x))
                
                elif "**" in trigo:
                    f.write(str(x))
                    f.write("=")
                    f.write(str(eval(str(equation))))

                else:

                    f.write(str(x))
                    f.write("=")
                    f.write(str(eval(str(equation))))

                messagebox.showinfo("Reminder!","Data Saved in history.txt")

        except NameError:

            f.write(trigo)
            f.write("=")
            f.write(x)
            messagebox.showinfo("Reminder!","Data Saved in history.txt")
            
            
    except SyntaxError:

        Label_result.config(text="PLEASE ENTER DATA")
    
    equation=""

    Label_result.config(text="")
    f.close()
    trigo=""


def calculate():                                 #Calculate function

    global equation
    global x
    result=""

    if equation !="":

        if "/0" in equation:

            result="Undefined"

        else:

            try:

                result=eval(equation)

            except:

                result="Error"
                equation=""

    Label_result.config(text=result)
    x=equation
    equation=result

#BUTTONS

Button(root,width=8,height=3,text="x^n",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF", command=lambda: show("**")).place(x=10,y=75)            

Button(root,width=8,height=3,text="√",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: sqroot("**(1/2)")).place(x=110,y=75)       

Button(root,width=8,height=3,text="3√",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: sqroot("**(1/3)")).place(x=210,y=75)
        
Button(root,width=8,height=3,text="ln",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: ln()).place(x=310,y=75)

Button(root,width=8,height=3,text="log",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: log()).place(x=410,y=75)

Button(root,width=8,height=3,text="csc",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: cosec()).place(x=310,y=150)

Button(root,width=8,height=3,text="sec",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: sec()).place(x=410,y=150)

Button(root,width=8,height=3,text="⌫",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: backspace()).place(x=310,y=300)

Button(root,width=8,height=3,text="AC",font=("TIMES",12,"bold"),bg="#000080",fg="#FFFFFF",command=lambda: clear()).place(x=410,y=300)

Button(root,width=8,height=3,text="x",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: show("*")).place(x=310,y=375)

Button(root,width=8,height=3,text="÷",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: show("/")).place(x=410,y=375)

Button(root,width=8,height=3,text="3",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("3")).place(x=210,y=450)

Button(root,width=8,height=3,text="sin",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: sin()).place(x=10,y=150)

Button(root,width=8,height=3,text="cos",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: cos()).place(x=110,y=150)

Button(root,width=8,height=3,text="tan",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: tan()).place(x=210,y=150)

Button(root,width=8,height=3,text="7",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("7")).place(x=10,y=300)

Button(root,width=8,height=3,text="8",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("8")).place(x=110,y=300)

Button(root,width=8,height=3,text="9",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("9")).place(x=210,y=300)
        
Button(root,width=8,height=3,text="4",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("4")).place(x=10,y=375)

Button(root,width=8,height=3,text="5",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("5")).place(x=110,y=375)

Button(root,width=8,height=3,text="6",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("6")).place(x=210,y=375)

Button(root,width=8,height=3,text="1",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("1")).place(x=10,y=450)

Button(root,width=8,height=3,text="2",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("2")).place(x=110,y=450)

Button(root,width=8,height=3,text="+",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: show("+")).place(x=310,y=450)

Button(root,width=8,height=3,text="-",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: show("-")).place(x=410,y=450)

Button(root,width=8,height=3,text="0",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show("0")).place(x=10,y=525)

Button(root,width=8,height=3,text=".",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show(".")).place(x=110,y=525)

Button(root,width=8,height=3,text="π",font=("TIMES",12,"bold"),bg="#000000",fg="#FFFFFF",command=lambda: show(str(math.pi))).place(x=210,y=525)

Button(root,width=8,height=3,text="SAVE\nDATA",font=("TIMES",12,"bold"),bg="#023020",fg="#FFFFFF",command=lambda: save()).place(x=310,y=525)

Button(root,width=8,height=3,text="arcsin",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: asin()).place(x=10,y=225)

Button(root,width=8,height=3,text="arccos",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: acos()).place(x=110,y=225)

Button(root,width=8,height=3,text="arctan",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: atan()).place(x=210,y=225)

Button(root,width=8,height=3,text="arccsc",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: acosec()).place(x=310,y=225)

Button(root,width=8,height=3,text="arcsec",font=("TIMES",12,"bold"),bg="#000020",fg="#FFFFFF",command=lambda: asec()).place(x=410,y=225)

Button(root,width=8,height=3,text="=",font=("TIMES",12,"bold"),bg="#fe9037",fg="#FFFFFF",command=lambda: calculate()).place(x=410,y=525)




root.mainloop()