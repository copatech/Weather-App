from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


main = Tk()
main.title("Weather App")
main.geometry("900x500+300+200")
main.resizable(False, False)

# Top window pane icon
image_icon = PhotoImage(file="logo.png")
main.iconphoto(False, image_icon)

def get_weather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Weather API
        api = (
            "https://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&appid=3af5b8038d2bba6c74977113680191f2"
        )

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Location!!!")


# Search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(
    main,
    justify="center",
    width=17,
    font=("poppins", 25, "bold"),
    bg="#404040",
    border=0,
    fg="white",
)
textfield.place(x=50, y=40)
textfield.focus()
textfield.bind("<Return>", get_weather)

search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(
    image=search_icon,
    borderwidth=0,
    cursor="hand2",
    bg="#404040",
    command=get_weather,
)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=130)

# Bottom Box
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# time
name = Label(main, font=("arial", 15, "bold"))
name.place(x=40, y=100)
clock = Label(main, font=("Helvetica", 20))
clock.place(x=40, y=130)

# Label
label1 = Label(
    main, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label1.place(x=120, y=400)

label2 = Label(
    main, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label2.place(x=250, y=400)

label3 = Label(
    main, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label3.place(x=430, y=400)

label4 = Label(
    main, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef"
)
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=230)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=200)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=430, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=680, y=430)

main.mainloop()
