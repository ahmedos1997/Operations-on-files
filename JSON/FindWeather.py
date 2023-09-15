import requests, json

# section 3
api_key = 'e482751086410e8db70397689211a790'

base_url = 'https://api.openweathermap.org/data/2.5/weather?'


# section2
city_name = input('enter city name ')
# الفرق بين السطرين ادناه هو انني حويل unit الى metric
#complete_url = base_url +'q=' + city_name +'&appid=' + api_key
complete_url = base_url +'q=' + city_name + '&units=metric'+'&appid=' + api_key

#response object

response = requests.get(complete_url)
#print(response.text)

# نحول صيغة جيسونس لصيغة مفهومة اكثر

x = json.loads(response.text)
# cod في المثال يعني رقم الصفحة اذا كان 404 يعني انها غير موجودة غيره يعني ان الطلب وصل بنجاح
if x['cod'] != '404':

    y = x["main"]  # ال main هو عنوان لشي معين داخل جمل الجيسونس وهنا سنستخرج فقط بعض الجمل
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]

    z = x["weather"]
    weather_description = z[0]["description"]
    print('the current_temperature is ' + str(current_temperature) ,
          '\n and the current pressure is '  + str(current_pressure),
          '\n and the current humidity is '+ str(current_humidity),
          '\n and the description is ' + str(weather_description)
          )




else:
    print('city not found')