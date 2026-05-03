import db


def get_all_classes():
    sql = "SELECT title, value FROM classes ORDER BY id"
    result = db.query(sql)

    classes = {}
    for title, value in result:
        classes[title] = []
    for title, value in result:
        classes[title].append(value)

    return classes


def add_workout(title, description, user_id, classes):

    sql = """INSERT INTO workouts (title, description, user_id)
    VALUES (?, ?, ?)"""
    db.execute(sql, [title, description, user_id])

    workout_id = db.last_insert_id()

    sql = "INSERT INTO workout_classes (workout_id, title, value) VALUES (?,?,?)"
    for class_title, class_value in classes:
        db.execute(sql, [workout_id, class_title, class_value])

    return workout_id


def get_workouts():
    sql = """SELECT w.id, w.title, u.id user_id, u.username, COUNT(r.id) rating_count
    FROM workouts w
    JOIN users u ON w.user_id = u.id
    LEFT JOIN ratings r ON w.id = r.workout_id
    GROUP BY w.id
    ORDER BY w.id DESC"""
    return db.query(sql)


def get_classes(workout_id):
    sql = "SELECT title, value FROM workout_classes WHERE workout_id = ?"
    return db.query(sql, [workout_id])


def get_workout(workout_id):
    sql = """SELECT
    w.id,
    w.title,
    w.description,
    u.username,
    u.id AS user_id
    FROM workouts AS w
    LEFT JOIN users AS u ON w.user_id  = u.id
    WHERE w.id = ?"""
    result = db.query(sql, [workout_id])
    return result[0] if result else None


def update_workout(workout_id, title, description, classes):
    sql = """UPDATE workouts SET
    title=?,
    description=?
    WHERE id = ?"""
    db.execute(sql, [title, description, workout_id])

    sql = "DELETE FROM workout_classes WHERE workout_id = ?"
    db.execute(sql, [workout_id])

    sql = "INSERT INTO workout_classes (workout_id, title, value) VALUES (?,?,?)"
    for class_title, class_value in classes:
        db.execute(sql, [workout_id, class_title, class_value])


def remove_workout(workout_id):
    sql = "DELETE FROM workout_classes WHERE workout_id = ?"
    db.execute(sql, [workout_id])
    sql = "DELETE FROM ratings WHERE workout_id = ?"
    db.execute(sql, [workout_id])
    sql = "DELETE FROM workouts WHERE id = ?"
    db.execute(sql, [workout_id])


def find_workout(query):
    sql = """SELECT DISTINCT w.id, w.title
    FROM workouts w
    JOIN workout_classes classes ON classes.workout_id=w.id
    WHERE w.title LIKE ? OR w.description LIKE ? OR classes.title LIKE ? OR classes.value LIKE ?
    ORDER BY w.id DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like, like])


def rate_workout(user_id, workout_id, rating, comment):
    sql = """INSERT INTO ratings
    (user_id, workout_id, rating, comment, sent_at)
    VALUES (?, ?, ?, ?, datetime('now'))"""
    db.execute(sql, [user_id, workout_id, rating, comment])


def get_ratings(workout_id):
    sql = """SELECT r.id, r.rating, r.comment, r.sent_at, u.username
    FROM ratings r
    LEFT JOIN users u ON r.user_id = u.id
    WHERE r.workout_id = ?"""
    return db.query(sql, [workout_id])


def get_user_ratings(user_id):
    sql = """SELECT r.id, r.rating, r.comment, r.sent_at, r.workout_id, u.username, w.title
    FROM ratings r
    LEFT JOIN users u ON r.user_id = u.id
    LEFT JOIN workouts w ON r.workout_id = w.id
    WHERE r.user_id = ?"""
    return db.query(sql, [user_id])
