from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()
    user_id = "shravani_mane_08072004"
    email = "ss9676@srmist.edu.in"
    roll_number = "RA2111003011223"

    raw_data = data.get('data', [])
    numbers = [item for item in raw_data if item.isdigit()]
    alphabets = [item for item in raw_data if item.isalpha()]

    highest_alphabet = max(alphabets, key=str.upper) if alphabets else None

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": [highest_alphabet] if highest_alphabet else []
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
