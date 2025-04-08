import sqlite3

def create_db():
    conn = sqlite3.connect("cves.db")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS cves (
            id TEXT PRIMARY KEY,
            description TEXT,
            last_modified TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_cve(cve_id, description, last_modified):
    conn = sqlite3.connect("cves.db")
    cur = conn.cursor()

    cur.execute('''
        INSERT OR REPLACE INTO cves (id, description, last_modified)
        VALUES (?, ?, ?)
    ''', (cve_id, description, last_modified))

    conn.commit()
    conn.close()
