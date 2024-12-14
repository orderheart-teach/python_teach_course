from flask import Flask, render_template, request, session, redirect, url_for
import json
import urllib.request

app = Flask(__name__)
app.secret_key = 'yoursecretkey'  # 替换为更安全的随机字符串

@app.route('/', methods=['POST', 'GET'])
def weather():
    # 获取用户名
    username = session.get('username', 'Guest')
    if request.method == 'POST':
        city = request.form['city']
    else:
        # 默认城市
        city = 'chengdu'

    # API Key
    api = "22c7e660f74765485cb007e80e941a62"

    try:
        # 请求天气数据
        source = urllib.request.urlopen(
            f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
        ).read()
        list_of_data = json.loads(source)

        # 开尔文转摄氏温度
        temp_kelvin = float(list_of_data['main']['temp'])
        temp_celsius = temp_kelvin - 273.15

        # 天气描述及图标
        description = list_of_data['weather'][0]['description'].capitalize()
        weather_icon = list_of_data['weather'][0]['icon']  # 从API获取icon id

        data = {
            "cityname": city.title(),
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
            "temp": f"{temp_kelvin:.2f} K",
            "temp_cel": f"{temp_celsius:.2f} °C",
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "description": description,
            "icon": weather_icon
        }
    except Exception:
        # 当请求出错或城市名无效时
        data = None

    return render_template('index.html', data=data, username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 简单的登录示例，不做密码校验，只使用用户名
        username = request.form.get('username')
        if username:
            session['username'] = username
            return redirect(url_for('weather'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('weather'))

if __name__ == '__main__':
    app.run(debug=True)