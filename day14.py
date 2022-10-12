# GUI -graphical user interface
# libraries
##############
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app = ttk.Tk()
app.title('My App')
app.geometry('600x400')

msg = ttk.Variable(app)
# print(msg.get())
#msg.set('Empty')
#print(msg.get())

ttk.Label(app, text='A simple text label').place(x=50,y=30)
ttk.Label(app,textvariable=msg).place(x=100,y=10)




def abc():
    print('good night')
    msg.set('jo tera mann ho')

#ttk.Button(app, text= 'Isko click krdo',command= abc).place(x=100,y=100)
#ttk.Button(app, text='Or this', command= lambda:msg.set('get lost')).place(x=200,y=300)pipp

f1= ttk.Variable(app)
f1.set('0')
f2= ttk.Variable(app)
f2.set('0')
result= ttk.Variable(app)

ttk.Entry(app, textvariable=f1,width=4, font=('Arial',22)).place(x=50,y=250)
ttk.Entry(app, textvariable=f2,width=4, font=('Arial',22)).place(x=150,y=250)
ttk.Label(app, text='Result',font=('Arial',22)).place(x=300,y=30)
ttk.Label(app, textvariable=result , font=('Arial',22)).place(x=300,y=70)
def calci(op):
    print('Calclute')
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app, text='+',command= lambda:calci('+'), font=('Arial',25)).place(x=50,y=300)
ttk.Button(app, text='-',command= lambda:calci('-'), font=('Arial',25)).place(x=100,y=300)
ttk.Button(app, text='*',command= lambda:calci('*'), font=('Arial',25)).place(x=150,y=300)
ttk.Button(app, text='/',command=lambda: calci('/'), font=('Arial',25)).place(x=200,y=300)

box=ttk.Listbox(app,height=5,fg='purple', activestyle='dotbox')
box.insert(1,'bts')
box.insert(2,'jin')
box.insert(3,'jk')
box.place(x=50,y=30)

def show():
    print(box.get(box.curselection()))

ttk.Button(app,text='show', command=show).place(x=350,y=250) 






app.mainloop() 

