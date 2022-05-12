import urllib.request
import json
from prettytable import PrettyTable



def process_input(place):
    first_letter_encountered = ""
    for char in place:
        if char.isalpha():
            first_letter_encountered = char.upper()
            place = place.replace(char, "", 1)
        break;


    filtered_input = first_letter_encountered + place.lower()
    filtered_input = filtered_input.replace(" ", "%20")

    return filtered_input

def generate_temp_from_place(place):



    try:
        get_url = urllib.request.urlopen('https://geocode.xyz/'+process_input(place)+'?json=1')
    except:
        exception_string = "Please use only valid characters and enter a valid city name!"
        print(exception_string)
        print()
        print("examples: London, Paris, Amsterdam, Berlin")
        return exception_string
    timetemp = dict()


    info_dict = json.loads((get_url.read()))

    if "error" in info_dict:
        error_string = "Please enter a valid city name!"
        print(error_string)
        print()
        print("examples: London, Paris, Amsterdam, Berlin")
        return error_string

    if len(info_dict['alt']) != 0 and type(info_dict['alt']['loc'])==list:
        lat = info_dict['alt']['loc'][0]['latt']
        long = info_dict['alt']['loc'][0]['longt']
    else:
        lat = info_dict['latt']
        long = info_dict['longt']
    mateoapistr = "https://api.open-meteo.com/v1/forecast?latitude="+lat+"&longitude="+long+"&hourly=temperature_2m"
    get_url_mateo = urllib.request.urlopen(mateoapistr)
    mateo_dict = json.loads((get_url_mateo.read()))

    for i in range(len(mateo_dict['hourly']['temperature_2m'])):
        timetemp[mateo_dict['hourly']['time'][i]] = mateo_dict['hourly']['temperature_2m'][i]

    table = PrettyTable()
    table.field_names = ["time","temperature"]
    if "standard" in info_dict and "city" in info_dict["standard"]:
        table.title = info_dict["standard"]["city"]
    else:
        table.title = place
    for item in timetemp.items():
        table.add_row([item[0],item[1]])

    print(table)
    return table

def main():
    while True:
        place = input("Please enter the name of a city: ")
        generate_temp_from_place(place)

if __name__ == "__main__":
    main()


