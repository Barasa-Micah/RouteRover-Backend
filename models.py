from flask import Flask, jsonify, request
from models import db, TransportType, Route, Schedule, PaymentMethod, Payment

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Keithp8608@localhost/transport_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return jsonify({
        "message": "Welcome to the Transport API. Use /bus, /taxi, or /train to get specific routes and times."
    })

@app.route('/bus')
def bus():
    return get_transport_data(1)  # 1 for bus

@app.route('/taxi')
def taxi():
    return get_transport_data(2)  # 2 for taxi

@app.route('/train')
def train():
    return get_transport_data(3)  # 3 for train

def get_transport_data(transport_type_id):
    transport_type = TransportType.query.get(transport_type_id)
    if not transport_type:
        return jsonify({'error': 'Transport type not found'}), 404

    routes_data = []
    for route in transport_type.routes:
        schedules = [schedule.departure_time for schedule in route.schedules]
        routes_data.append({'route': route.name, 'times': schedules})

    return jsonify({
        'transport': transport_type.name,
        'routes': routes_data
    })

@app.route('/payments', methods=['POST'])
def create_payment():
    user_id = request.json.get('user_id')
    payment_method_id = request.json.get('payment_method_id')
    amount = request.json.get('amount')

    payment = Payment(user_id=user_id, payment_method_id=payment_method_id, amount=amount)
    db.session.add(payment)
    db.session.commit()

    return jsonify({'message': 'Payment recorded successfully'}), 201

@app.route('/payment-methods', methods=['GET'])
def get_payment_methods():
    methods = PaymentMethod.query.all()
    methods_data = [{'id': method.id, 'name': method.name} for method in methods]
    return jsonify(methods_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)
