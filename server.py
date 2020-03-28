from flask import Flask, request
from helpers import add_transaction

app = Flask(__name__)

@app.route("/addTransaction", methods=['GET', 'POST'])
def new_transaction_handler():
    if request.method == 'POST':
        tran_data = request.get_json()
        tran_type = tran_data['tran_type']
        amount = tran_data['amount']
        category = tran_data['category']
        vendor = tran_data['vendor']
        lat = tran_data['lat']
        lon = tran_data['long']
        add_transaction(tran_type, amount, category, vendor, lat, lon)
    return 'SUCC'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
    
