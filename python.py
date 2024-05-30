from flask import Flask, jsonify, request
import requests

app = Flask(_name_)

window_size = 10
number_store = []

@app.route('/numbers/<numberid>', methods=['GET'])
def get_numbers(numberid):
    global number_store
    # Fetch data from a third-party server (simulated here with a local list)
    response = requests.get(f'http://third-party-server/numbers/{numberid}')
    if response.status_code == 200:
        number = response.json().get('number')
        if number not in number_store:
            if len(number_store) >= window_size:
                number_store.pop(0)
            number_store.append(number)
        
        avg = sum(number_store) / len(number_store) if number_store else 0
        return jsonify({
            "windowPrevState": number_store[:-1],
            "windowCurrState": number_store,
            "numbers": [number],
            "avg": avg
        })
    else:
        return jsonify({"error": "Failed to fetch number"}), 500

if _name_ == '_main_':
    app.run(port=9876, debug=True)