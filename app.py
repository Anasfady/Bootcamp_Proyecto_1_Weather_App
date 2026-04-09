# ... (your other imports at the top) ...

@app.route('/')
def index():
    return render_template('index.html')

# Ensure this part is kept from the 'Incoming' side:
@app.route('/add_data')
def add_data():
    return render_template('add_data.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)