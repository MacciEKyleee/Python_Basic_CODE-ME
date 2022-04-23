import requests
import json
from datetime import datetime
from fpdf import FPDF

def main():
    key = "d7d33bcda62df8c3afe884bbb7c390a7"

    gdansk = (54.372158, 18.638306)

    url = f'https://api.openweathermap.org/data/2.5/onecall?lat=' \
          f'{gdansk[0]}&lon={gdansk[1]}&exclude=current,minutely,hourly,alerts&appid={key}&units=metric'

    response = requests.get(url)

    data = json.loads(response.text)

    days = []
    day_temp = {
        "date": "",
        "sunrise": "",
        "sunset": "",
        "tmin": 0,
        "tmax": 0,
        "tday": 0,
        "tnight": 0,
        "pressure": 0,
        "humidity": 0,
        "wind_speed": 0,
        "weather": "",
        "cloudiness": 0
    }

    for day in data["daily"]:
        day_temp["date"] = datetime.utcfromtimestamp(day["dt"]).strftime('%Y-%m-%d')
        day_temp["sunrise"] = datetime.utcfromtimestamp(day["sunrise"]).strftime('%H:%M:%S')
        day_temp["sunset"] = datetime.utcfromtimestamp(day["sunset"]).strftime('%H:%M:%S')
        day_temp["tmin"] = day["temp"]["min"]
        day_temp["tmax"] = day["temp"]["max"]
        day_temp["tday"] = day["temp"]["day"]
        day_temp["tnight"] = day["temp"]["night"]
        day_temp["pressure"] = day["pressure"]
        day_temp["humidity"] = day["humidity"]
        day_temp["wind_speed"] = day["wind_speed"]
        day_temp["weather"] = day["weather"][0]['main']
        day_temp["cloudiness"] = day["clouds"]
        days.append(day_temp.copy())

    #print("7 days forecast for Gdansk:\n")
    #selected_day = int(input('Podaj szukany dzień'))
    #print_day(selected_day)

    pdf_file = FPDF()
    for day in days:
        print_day(pdf_file,day)
    pdf_file.output(f'Weather_data.pdf', 'F')

def print_day(pdf, day):
    pdf.add_page()
    pdf.set_font('Arial','B',16)

    pdf.cell(60,20,f"Date: {day['date']}",0,1,'C')
    pdf.cell(40,10, f"\tsunrise: {day['sunrise']}",0,1)
    pdf.cell(40,10,f"\tsunset: {day['sunset']}",0,1)
    pdf.cell(40,10,f"\tminimal temperature: {day['tmin']}",0,1)
    pdf.cell(40,10,f"\tmaximal temperature: {day['tmax']}",0,1)
    pdf.cell(40,10,f"\ttemperature during the day: {day['tday']}",0,1)
    pdf.cell(40,10,f"\ttemperature at night: {day['tnight']}",0,1)
    pdf.cell(40,10,f"\tweather: {day['weather']}",0,1)
    pdf.cell(40,10,f"\tpressure: {day['pressure']}",0,1)
    pdf.cell(40,10,f"\thumidity: {day['humidity']}",0,1)
    pdf.cell(40,10,f"\twind speed: {day['wind_speed']}",0,1)
    pdf.cell(40,10,f"\tcloudiness: {day['cloudiness']}",0,1)

if __name__ == "__main__":
    main()