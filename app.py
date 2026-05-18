from flask import Flask, render_template, request, abort
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('business_permits.db')
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

@app.route('/verify/<business_no>')
def verify_permit(business_no):
    conn = get_db_connection()
    # Search for the business record based on the URL parameter
    permit = conn.execute('SELECT * FROM permits WHERE business_no = ?', (business_no,)).fetchone()
    conn.close()

    if permit is None:
        return "Permit not found", 404

    return render_template('index.html', permit=permit)

if __name__ == '__main__':
    app.run(debug=True)