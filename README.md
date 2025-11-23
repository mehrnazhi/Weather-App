# Weather App (Python + Tkinter)

A desktop weather application built with **Python**, **Tkinter**, and the **OpenWeatherMap API**.
The app lets users search any city and displays its **local time**, **temperature**, **weather condition**, and additional details such as wind speed, humidity, and pressure.

---

## Features

* Search weather by city name using OpenWeatherMap API
* Automatic geolocation using `geopy`
* Detects local timezone with `timezonefinder`
* Shows local time using `pytz`
* GUI built with Tkinter
* Displays:

  * Temperature (°C)
  * Weather condition + description
  * Wind speed
  * Humidity
  * Pressure

---

## Technologies Used

* Python
* Tkinter (GUI)
* Geopy
* TimezoneFinder
* Requests
* OpenWeatherMap API
* Pytz

---

## How to Run

### 1. Install dependencies

```bash
pip install geopy timezonefinder requests pytz
```

### 2. Add your OpenWeatherMap API Key

Inside the script:

```python
api_key = "YOUR_API_KEY"
```

### 3. Make sure image assets exist

Place these files in the project folder:

```
search.png
search_icon.png
logo.png
box.png
```

### 4. Run the application

```bash
python main.py
```

---

## Project Structure

```
weather-app/
│── main.py
│── search.png
│── search_icon.png
│── logo.png
│── box.png
└── README.md
```

---

## Screenshots

(Add your screenshot here)

```
![App Screenshot](screenshot.png)
```

---

## Notes

* API temperature is returned in Kelvin; the app converts it to Celsius.
* Ensure stable internet connection for API/geolocation.

---

## License

This project is open-source and available under the MIT License.
