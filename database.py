import sqlite3
from datetime import datetime

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = BASE_DIR / "sacred_life_studio.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            product_type TEXT,
            score INTEGER,
            recommendation TEXT,
            status TEXT DEFAULT 'Research',
            created_at TEXT
        )
        """
    )

    conn.commit()
    conn.close()


def save_project(name, product_type, score, recommendation, status="Research"):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO projects (name, product_type, score, recommendation, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            product_type,
            score,
            recommendation,
            status,
            datetime.now().strftime("%Y-%m-%d %H:%M"),
        ),
    )

    conn.commit()
    conn.close()


def get_projects():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, name, product_type, score, recommendation, status, created_at
        FROM projects
        ORDER BY id DESC
        """
    )

    rows = cur.fetchall()
    conn.close()

    return rows