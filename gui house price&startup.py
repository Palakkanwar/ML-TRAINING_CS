import tkinter as ttk
import pandas as pd

model =pd. read_pickle('housePrice.pickle')

app=ttk.Tk()
app.configure(background='purple')
app.geometry('600x600')
app.title('House Price Predictor')

income=ttk.Variable(app)
ttk.Label(app,text='Income',padx=15,pady=15,background='white').grid(row=0,column=0)  ## padx,pady= for spacing 
ttk.Entry(app, textvariable=income,width=10).grid(row=0,column=1)

house_age=ttk.Variable(app)
ttk.Label(app,text='house age',padx=15,pady=15,background='white').grid(row=1,column=0)  ## padx,pady= for spacing 
ttk.Entry(app, textvariable=house_age,width=10).grid(row=1,column=1)

num_rooms=ttk.Variable(app)
ttk.Label(app,text='number of rooms',padx=15,pady=15,background='white').grid(row=2,column=0)  ## padx,pady= for spacing 
ttk.Entry(app, textvariable=num_rooms,width=10).grid(row=2,column=1)

population=ttk.Variable(app)
ttk.Label(app,text='population',padx=15,pady=15,background='white').grid(row=3,column=0)  ## padx,pady= for spacing 
ttk.Entry(app, textvariable=population,width=10).grid(row=3,column=1)


def prediction():
    global model
    query_data= {'Avg. Area Income':[eval(income.get())],'Avg. Area House Age':[eval(house_age.get())],'Avg. Area Number of Rooms':[eval(num_rooms.get())],'Area Population':[eval(population.get())]}
    price=model.predict(pd.DataFrame(query_data))
    result.set(round(price[0],2))
    pass
ttk.Button(app,text='Predict', command=prediction).grid(row=4,column=0)

result=ttk.Variable(app)
result.set('0')
ttk.Label(app, textvariable=result,pady=15,font=('Arial,20')).grid(row=5,column=0,columnspan=2)


app.mainloop()