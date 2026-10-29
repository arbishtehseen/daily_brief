import sqlite3

def init_db():
    conn = sqlite3.connect('news_history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sent_headlines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            headline TEXT UNIQUE,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def is_headline_sent(headline):
    conn = sqlite3.connect('news_history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM sent_headlines WHERE headline = ?', (headline,))
    result = cursor.fetchone()
    conn.close()
    return result is not None 

def save_headline(headline):
    conn = sqlite3.connect('news_history.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO sent_headlines (headline) VALUES (?)', (headline,))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  
    conn.close()