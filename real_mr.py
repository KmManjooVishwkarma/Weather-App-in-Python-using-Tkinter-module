import json
import requests
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox

# Required Details
root = Tk()
root.geometry("550x550")
root.resizable(False,False)
root.title("Weather App")
root.configure(bg='white')

# for images

img = ImageTk.PhotoImage(Image.open('hello.jpg'))
panel = Label(root,image=img)
panel.place(x=0,y=0)

lable_0 = Label(root,text="WEATHER APP",width = 20,bg='green2',font=("bold",20),fg='red')
lable_0.place(x=75,y=50)

lbl=Label(root,text="ENTER CITY NAME ",bg="deep sky blue",bd=5,font=("bold",10) )
lbl.place(x=95,y=100)

city_names = StringVar()
entry_1 = Entry(root,textvariable=city_names,bd=5)
city_names.set(" ")
entry_1.place(x=250,y=100)



Temperature_lable = Label(root,text="TEMPERATURE :-",width = 15,bg='cyan',font=("bold",10),fg='blue',bd=7,borderwidth=5,relief="raised")
Temperature_lable.place(x=85,y=200)

Pressure_label = Label(root,text="PRESSURE :- ",width = 15,bg='cyan',font=("bold",10),fg='blue',bd=7,borderwidth=5,relief="raised")
Pressure_label.place(x=85,y=250)


Humidity_label=Label(root,text="HUMIDITY :- ",width = 15,bg='cyan',font=("bold",10),fg='blue',bd=7,borderwidth=5,relief="raised")
Humidity_label.place(x=85,y=300)

Description_lable = Label(root,text="DESCRIPTION :- ",width = 15,bg='cyan',font=("bold",10),fg='blue',bd=7,borderwidth=5,relief="raised")
Description_lable.place(x=85,y=350)


lable_temp = Label(root,text=" ",width = 20,bg='white',font=("bold",10),fg='blue',bd=7)
lable_temp.place(x=275,y=200)

lable_pres = Label(root,text=" ",width = 20,bg='white',font=("bold",10),fg='blue',bd=7)
lable_pres.place(x=275,y=250)

label_humidity=Label(root,text=" ",width = 20,bg='white',font=("bold",10),fg='blue',bd=7)
label_humidity.place(x=275,y=300)


lable_desc = Label(root,text=" ",width = 20,bg='white',font=("bold",10),fg='blue',bd=7)
lable_desc.place(x=275,y=350)




# api config
def getTemp():

    api_key = "cca1563a45fe1cbbf8c15e4496a4cb3c"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = entry_1.get()
    complete_url = base_url+"appid="+api_key+"&q="+city_name

# module response get

    response = requests.get(complete_url)
    x=response.json()

    if["cod"] !='404':
        y = x["main"]
        current_temprature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity=y["humidity"]

        z = x["weather"]
        weather_description = z[0]["description"]

        lable_pres.configure(text=current_pressure)
        lable_temp.configure(text=current_temprature)
        label_humidity.configure(text=current_humidity)
        lable_desc.configure(text=weather_description)
        
    else:
        lable_pres.configure(text="Err")
        lable_temp.configure(text="Err")
        label_humidity.configure(text="Err")
        lable_desc.configure(text="Err")
       # tkinter.messagebox.showinfo("Error","City not found")
        
# for button
btn=Button(root,text="SUBMIT",width=15,bg='red',fg='white',command=getTemp,bd=7,relief=SUNKEN,borderwidth=5)
btn.place(x=175,y=150)

lable_unit = Label(root,text="TEMPERATURE in Kelvin \n  PRESSURE in mb",width = 35,bg='white',font=("bold",10),fg='blue2')
lable_unit.place(x=115,y=400)

lable_unit = Label(root,text="developed by Manjoo",width = 50,bg='white',font=("bold",10),fg='blue2')
lable_unit.place(x=80,y=450)

 
root.mainloop()
