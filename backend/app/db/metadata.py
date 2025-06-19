import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "data" / "metadata.db"

def get_conn():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS file_metadata (
            drive_id TEXT PRIMARY KEY,
            file_name TEXT,
            modified_time TEXT,
            vector_id TEXT
        )
        """)
        conn.commit()

def get_all_metadata():
    with get_conn() as conn:
        return {row[0]: row for row in conn.execute("SELECT * FROM file_metadata")}

def upsert_metadata(drive_id, file_name, modified_time, vector_id):
    with get_conn() as conn:
        conn.execute("""
        INSERT OR REPLACE INTO file_metadata (drive_id, file_name, modified_time, vector_id)
        VALUES (?, ?, ?, ?)
        """, (drive_id, file_name, modified_time, vector_id))
        conn.commit()

def delete_metadata(drive_id):
    with get_conn() as conn:
        conn.execute("DELETE FROM file_metadata WHERE drive_id = ?", (drive_id,))
        conn.commit()