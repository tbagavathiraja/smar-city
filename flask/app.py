from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample Data
bills = []
city_info = [
    {"title": "New Park Opening", "description": "A new park will open downtown next week."},
    {"title": "Road Maintenance", "description": "Road maintenance on Main Street will begin on Monday."}
]
messages = []
energy_data = {"usage": 10000, "renewable": 3000}
water_data = {"usage": 5000, "recycled": 2000}
industries = [
    {"name": "Industry A", "energy_consumption": 1000, "emissions": 500},
    {"name": "Industry B", "energy_consumption": 2000, "emissions": 1000}
]
solar_car_data = {"routes": 5, "co2_saved": 1000}

@app.route('/')
def home():
    return render_template('home.html', bills=bills, city_info=city_info, messages=messages, energy_data=energy_data, water_data=water_data, industries=industries, solar_car_data=solar_car_data)

# Bills Section
@app.route('/bills', methods=['GET', 'POST'])
def manage_bills():
    if request.method == 'POST':
        bill_name = request.form['bill_name']
        due_date = request.form['due_date']
        amount = request.form['amount']
        bills.append({"name": bill_name, "due_date": due_date, "amount": amount})
        return redirect(url_for('home'))
    return render_template('bills.html')

# City Information Section
@app.route('/city_info')
def view_city_info():
    return render_template('city_info.html', city_info=city_info)

# Communication Section
@app.route('/messages', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        sender = request.form['sender']
        message = request.form['message']
        messages.append({"sender": sender, "message": message})
        return redirect(url_for('home'))
    return render_template('messages.html')

# Energy Conservation Dashboard
@app.route('/energy')
def energy_dashboard():
    return render_template('energy.html', energy_data=energy_data)

# Water Recycling Management
@app.route('/water')
def water_dashboard():
    return render_template('water.html', water_data=water_data)

# Industrial Energy Monitoring
@app.route('/industry')
def industry_dashboard():
    return render_template('industry.html', industries=industries)

# Solar Car Integration
@app.route('/solar')
def solar_dashboard():
    return render_template('solar.html', solar_car_data=solar_car_data)

if __name__ == '__main__':
    app.run(debug=True)
