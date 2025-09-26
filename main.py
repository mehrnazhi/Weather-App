import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def get_weather():
    try:
        city = textfile.get()
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        print("Location:", location)  # برای debug

        if location is None:
            messagebox.showerror("Weather App", "City not found!")
            return

        lat = location.latitude
        lng = location.longitude

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=lng, lat=lat)
        print("Timezone:", result)  # برای debug

        if result:
            city_label.config(text=result.split("/")[-1])
        else:
            messagebox.showerror("Weather App", "Timezone not found!")
        # time
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M %p")
        clock.config(text=current_time)
        time_label.config(text="lOCAL TIME")

        # weather
        api_key = "d0292001bd1d229a8c1c027ea617404e"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"
        jason_data = requests.get(api).json()
        conditon = jason_data["weather"][0]["main"]
        description = jason_data["weather"][0]["description"]
        temp = int(jason_data["main"]["temp"] - 273.15)
        perussure = jason_data["main"]["pressure"]
        humidity = jason_data["main"]["humidity"]
        wind = jason_data["wind"]["speed"]

        temp_label.config(text=f"{temp} °")
        condition_label.config(text=f"{conditon} | FEELS LIKE{temp} °")
        wind_label.config(text=wind)
        description_label.config(text=description)
        humidity_label.config(text=humidity)
        pressure_label.config(text=perussure)

    except Exception as error:
        print("Error:", error)
        messagebox.showerror("Weather App", "Invalid entry!")


root = tk.Tk()
root.title(" Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)
# search box
search_image = tk.PhotoImage(file="search.png")
search_image_label = tk.Label(root, image=search_image)
search_image_label.pack(pady=20, side="top")

textfile = tk.Entry(root, justify="center", width=17, font=(
    " arial", 25, "bold"), bg="#404040", fg="white", border=0)
textfile.place(x=280, y=40)

# search icon

search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_button = tk.Button(
    root, image=search_icon, border=0, bg="#404040", cursor="hand2", command=get_weather)
search_icon_button.place(x=590, y=34)

# Logo

logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(side="top")

# bottom box

frame_image = tk.PhotoImage(file="box.png")
frame_label = tk.Label(root, image=frame_image)
frame_label.pack(pady=10, side="bottom")

# city name

city_label = tk.Label(root, font=("arial", 40, "bold"), fg="#e355cd")
city_label.place(x=120, y=160)


# time

time_label = tk.Label(root, font=("arial", 20, "bold"), fg="#4b4bcc")
time_label.place(x=120, y=230)

clock = tk.Label(root, font=("Helvetica", 20), fg="#4b4bcc")
clock.place(x=120, y=270)

# labels

label1 = tk.Label(root, text="WIND", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = tk.Label(root, text="HUMINIDY", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=280, y=400)

label3 = tk.Label(root, text="DESCRIPTION", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=450, y=400)

label4 = tk.Label(root, text="PRUSSURE", font=(
    "Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=670, y=400)

# Temperature

temp_label = tk.Label(root, font=("arial", 70, "bold"), fg="#e355cd")
temp_label.place(x=590, y=170)

condition_label = tk.Label(root, font=("arial", 15, "bold"), fg="#e355cd")
condition_label.place(x=590, y=270)

wind_label = tk.Label(root, text="....", font=(
    "arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
wind_label.place(x=120, y=430)

humidity_label = tk.Label(root, text="....", font=(
    "arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
humidity_label.place(x=280, y=430)

description_label = tk.Label(root, text="....", font=(
    "arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
description_label.place(x=450, y=430)

pressure_label = tk.Label(root, text="....", font=(
    "arial", 20, "bold"), fg="#404040", bg="#1ab5ef")
pressure_label.place(x=670, y=430)


root.mainloop()
