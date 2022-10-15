import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk
import warnings
warnings.filterwarnings('ignore')
import os
from PIL import Image,ImageTk
data=pd.read_csv('treadmil-users.csv')

app= ttk.Tk()
app.geometry('600x400')
app.title('Treadmil Users Analysis')


graphs=ttk.Variable(app)
values={'Pairplot':'sns.pairplot(data=data)',
       'Jointplot':"sns.jointplot(data=data,x='{col1}',y='{col2}')",'barplot':"sns.barplot(data=data,x='{col1}',y='{col2}')"
       ,'boxplot':"sns.boxplot(data=data,x='{col1}',y='{col2}')"}
graphs.set(values['Pairplot'])
y=10        
for key, value in values.items():
    ttk.Radiobutton(app,text=key,variable=graphs,value=value).place(x=10,y=y)
    y+=20
## option menu 1  
col1=ttk.Variable(app)  
values=['Select']+list(data.columns)
col1.set(values[0])
ttk.Label(app, text='column1').place(x=100,y=40)
ttk.OptionMenu(app, col1,*values).place(x=100,y=10)    

## option menu 2
col2=ttk.Variable(app)
col2.set(values[0])
ttk.Label(app, text='column2').place(x=100,y=140)
ttk.OptionMenu(app, col2,*values).place(x=100,y=110) 

# option menu 3
col3=ttk.Variable(app)
col3.set(values[0])
ttk.Label(app, text='column3').place(x=100,y=240)
ttk.OptionMenu(app, col3,*values).place(x=100,y=180)

# canvas
cnv=ttk.Canvas(app,width=250,height=200)
cnv.place(x=200,y=100)

# label
result=ttk.Variable(app)
ttk.Label(app,textvariable=result).place(x=300,y=300)
def show():
    global cnv
    global img
    column1=col1.get()
    column2=col2.get()
    column3=col3.get()
    g=graphs.get()
    if 'col1' in g:
        if column1=='Select':
            result.set('column1 must be selected')
            return
    if 'col2' in g:
        if column1=='Select':
            result.set('column2 must be selected')
            return
    if 'col3' in g:
        if column1=='Select':
            result.set('column3 must be selected')
            return

    fig=plt.figure(figsize=(5,2))
    eval(g.format(col1=column1,col2=column2,col3=column3))
    fig.savefig('graph.png')
    img=ImageTk.PhotoImage(Image.open("graph.png").resize((250,200)))
   
    cnv.create_image(0,0,anchor=ttk.NW, image=img) ##2nd quardant

    #plt.show()
    #print(graphs.get())
    #print(col1.get(),col2.get(),col3.get())
  

ttk.Button(app,text='Show',command=show).place(x=400,y=10)       

app.mainloop()