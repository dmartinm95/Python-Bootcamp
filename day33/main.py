# Day 33: API Endpoints & API Parameters
# API: Application Programming Interface

from tkinter import *
import requests
from datetime import datetime
import smtplib

MY_LAT = 49.282730
MY_LONG = -123.120735


# Response codes:
# 404 - Thing you are looking for, doesn't exist
# 1XX - Hold on, something is happening
# 2XX - Here you go, everything was successfull
# 3XX - Go away, you don't have permission
# 4XX - You screwed up
# 5XX - The server / website screwed up


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (latitude, longitude)

    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG - 5 <= longitude <= MY_LONG + 5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data["results"])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset or time_now <= sunrise:
        return True


if is_iss_overhead() and is_night():
    # Send an email notification
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login("Username", "Password")
    connection.sendmail(from_addr="EMAIL", to_addrs="EMAIL",
                        msg="Subject:Look Up 👆\n\nThe ISS is above you in the sky.")


# def get_quote():
#     response = requests.get(url="https://api.kanye.rest/")
#     response.raise_for_status()
#     quote = response.json()["quote"]
#     canvas.itemconfig(quote_text, text=quote)


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="day33\\background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=(
#     "Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="day33\\kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)


# window.mainloop()
