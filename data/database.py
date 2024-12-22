import sqlite3

def create_data():
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT,
        status TEXT CHECK(status IN ('todo', 'in-progress', 'done')) NOT NULL,
        createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
        updatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    conn.close()


def add_data(name, id, status, createdAt, updatedAt):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    cursor.execute(f"""
    INSERT INTO tasks (id, name, status, createdAt, updatedAt)
    VALUES ('{id}', '{name}', '{status}', '{createdAt}', '{updatedAt}');
    """)


    conn.commit()
    conn.close()



def update_data(new_name, id, updatedAt):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET name = ?, updatedAt = ?
    WHERE id = ?
    """, (new_name, updatedAt, id))

    conn.commit()
    conn.close()


def delete_data(id: int):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = ?;", (id))
    have_id = cursor.fetchall()


    if have_id:
        cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?;
        """, (id))
        conn.commit()
        conn.close()

        return True
    else:
        return False

def mark_progress(status: str, id: int,):
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tasks
        SET status = ?
        WHERE id = ?
    """, (status, id))

    conn.commit()

    conn.close()




def get_tasks(mark: str) -> list:
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    if mark == "done":
        cursor.execute("SELECT * FROM tasks WHERE status = 'done';")
        records = cursor.fetchall()
    elif mark == "in-progress":
        cursor.execute("SELECT * FROM tasks WHERE status = 'in-progress';")
        records = cursor.fetchall()
    elif mark == "todo":
        cursor.execute("SELECT * FROM tasks WHERE status = 'todo';")
        records = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM tasks")
        records = cursor.fetchall()

    conn.commit()
    conn.close()

    return records


def get_id():
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(id) FROM tasks")
    max_id = cursor.fetchone()[0]
    new_id = (max_id + 1) if max_id is not None else 1


    conn.commit()
    conn.close()

    return new_id
