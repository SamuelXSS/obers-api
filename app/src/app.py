from flask import Flask, request, json
import datetime
from CpfValidation import ValidateCpf

app = Flask(__name__)

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
def store():
    cpfNumber = request.get_json('cpf')
    cpf = ValidateCpf(cpfNumber)

    if cpf.validate:
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



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9095)