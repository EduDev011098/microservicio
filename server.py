from flask import Flask,make_response,request,Response
from datetime import datetime
from pytz import timezone
import re


app = Flask(__name__)



now = datetime.now(timezone('America/mexico_city'))


@app.route('/',methods=['GET'])
def home():
    return make_response('haz un post ----> ip/animals, debe ser un animal que empiece con q, termine con s y conste de 15 letras. EJEMPLO ENVIO: {"name": "q...z"}',200)

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



@app.route('/animals',methods=['POST'])
def day_hou():
    data = request.get_json()

    pattern = '^q.............s$'
    test_string = data['name']
    if test_string == 'quebrantahuesos':

        result = re.match(pattern, test_string)

        if result:
            return make_response('Tienes grandes conocimientos en animales',200)
        else:
            return make_response('Ups! ERROR sigue participando',400)

    else:
        return make_response('ERROR',400)

    



if __name__ == '__main__':
    
    app.run(debug=True, port=5000, host='0.0.0.0')