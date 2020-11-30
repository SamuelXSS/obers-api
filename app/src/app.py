from flask import Flask, request, json
from flask_cors import CORS, cross_origin
import datetime
from validate_docbr import CPF
from validate_docbr import CNPJ

app = Flask(__name__)

app.debug = True

cors = CORS(app)

@app.route('/health')
def index():
    health = {
        "status": 200,
        "message": "All right with the service",
        "code": "success",
        "data": {
            "environment": "Development",
            "datatime_server": datetime.datetime.now(),
            "version": "1-0-2"
        }
    }
    return health

@app.route('/validator/Cpf', methods=['POST'])
def checkCpf():
    data = request.get_json()
    cpfNumber = data.get('cpf')
    cpf = CPF()

    if cpf.validate(cpfNumber):
        return {
            "status": 200,
            "cpf": cpfNumber,
            "code": "success",
            "data": "CPF is valid"
        }
    else:
        return {
            "status": 406,
            "cpf": cpfNumber,
            "code": "error",
            "data": "CPF is not valid"
        }

@app.route('/validator/Cnpj', methods=['POST'])
def checkCnpj():
    data = request.get_json()
    cnpjNumber = data.get('cnpj')
    cnpj = CNPJ()

    if cnpj.validate(cnpjNumber):
        return {
            "status": 200,
            "cpf": cnpjNumber,
            "code": "success",
            "data": "CNPJ is valid"
        }
    else:
        return {
            "status": 406,
            "cpf": cnpjNumber,
            "code": "error",
            "data": "CNPJ is not valid"
        }



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9095)