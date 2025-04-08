from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('cves.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/cve/<cve_id>')
def get_cve_by_id(cve_id):
    conn = get_db_connection()
    cve = conn.execute('SELECT * FROM cves WHERE id = ?', (cve_id,)).fetchone()
    conn.close()

    if cve:
        return dict(cve)
    else:
        return {"error": "CVE not found"}, 404

@app.route('/cves/modified')
def get_recent_cves():
    days = int(request.args.get('days', 7))
    since = datetime.now() - timedelta(days=days)
    since_str = since.strftime('%Y-%m-%d')

    conn = get_db_connection()
    cves = conn.execute('SELECT * FROM cves WHERE last_modified >= ?', (since_str,)).fetchall()
    conn.close()

    return jsonify([dict(cve) for cve in cves])

if __name__ == '__main__':
    app.run(debug=True)
