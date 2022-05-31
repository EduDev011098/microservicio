from flask import Flask,make_response
from datetime import datetime
from pytz import timezone


app = Flask(__name__)



now = datetime.now(timezone('America/mexico_city'))



@app.route('/dayhour',methods=['GET'])
def day_hour():
    
    year = now.year
    month = now.month
    day = now.day

    hour = now.hour
    minutes = now.minute

    info = f'hora actual: {hour}:{minutes} fecha actual: {year}-{month}-{day}'

    print(info)
    return make_response(f'{info}',200)



if __name__ == '__main__':
    
    app.run(debug=True, port=5000, host='0.0.0.0')