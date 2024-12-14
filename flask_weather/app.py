from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def weather():
    try:
        if request.method == 'POST':
            city = request.form['city']
        else:
            # 默认城市
            city = 'chengdu'

        # API 密钥
        api = "22c7e660f74765485cb007e80e941a62"

        # 获取天气数据
        source = urllib.request.urlopen(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
        ).read()

        # 将 JSON 数据转换为字典
        list_of_data = json.loads(source)

        # 数据处理
        temp_kelvin = list_of_data['main']['temp']
        temp_celsius = temp_kelvin - 273.15  # 开尔文转换为摄氏温度
        data = {
            "cityname": city.title(),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
            "temp": f"{temp_kelvin:.2f} K",
            "temp_cel": f"{temp_celsius:.2f} °C",
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "description": str(list_of_data['weather'][0]['description']).capitalize(),
        }
    except Exception as e:
        # 异常处理：如果 API 返回错误或城市名无效
        data = {
            "error": f"Unable to retrieve weather data for the city '{city}'. Please check the city name and try again.",
            "cityname": city.title(),
        }

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)