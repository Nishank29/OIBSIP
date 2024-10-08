import requests
from tkinter import *

def forecast():
    window = Toplevel(root)
    window.geometry('400x400')
    url = "https://api.weatherstack.com/current"
    
    
    with open("api_key.txt", "r") as file:
        access_key = file.read().strip()
    
    query = query_value.get() or query_zip.get()
    params = {'access_key': access_key, 'query': query}
    result = requests.get(url, params=params)

    
    if result.status_code != 200:
        Label(window, text="Error fetching data").grid(row=0, column=0)
        return

    response = result.json()

    
    if 'current' not in response or 'location' not in response:
        Label(window, text="Invalid location").grid(row=0, column=0)
        return

    current_weather = response['current']
    current_location = response['location']
    
    
    current_temperature = current_weather['temperature']
    current_humidity = current_weather['humidity']
    weather_description = current_weather['weather_descriptions'][0]

    
    Label(window, text=f"Location: {current_location['name']}, {current_location['country']}").grid(row=0, column=0)
    Label(window, text=f"Temperature: {current_temperature}°C").grid(row=1, column=0)
    Label(window, text=f"Humidity: {current_humidity}%").grid(row=2, column=0)
    Label(window, text=f"Weather: {weather_description}").grid(row=3, column=0)

# Main application window
root = Tk()
root.title('Weather App')
root.geometry('400x500')

Label(root, text='Location:').grid(row=0, column=0)
Label(root, text='or').grid(row=1, column=1)
Label(root, text='Postal or Zip Code(for US and Uk only):').grid(row=2, column=0)

query_value = StringVar()
query_zip =StringVar()
query_entry = Entry(root, textvariable=query_value)
zip_entry = Entry(root, textvariable=query_zip)

zip_entry.grid(row=2, column=1)
query_entry.grid(row=0, column=1)

Submit_button = Button(root, text="Submit", command=forecast)
Submit_button.grid(row=3, column=1)

mainloop()