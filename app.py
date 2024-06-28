from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Carregar os dados do JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Criar endpoints dinamicamente com base nos objetos do JSON
for key, value in data.items():
    def create_endpoint(key):
        def endpoint_func():
            print({key: data[key]})
            return jsonify({key: data[key]})
        return endpoint_func

    app.add_url_rule(f'/{key}', key, create_endpoint(key))

if __name__ == '__main__':
    app.run(debug=True)
