from loader import con


def db_init():
    cur = con.cursor()

    cur.execute("CREATE TABLE users(user_id bigint primary key, email varchar(255), auth_code varchar(255))")

    cur.close()
    con.commit()


def insert_user(user_id):
    cur = con.cursor()

    cur.execute(f"insert into users(user_id) values ({user_id})")

    cur.close()
    con.commit()


def add_email(user_id, email : str):
    cur = con.cursor()

    cur.execute(f"update users set email = '{email}' where user_id = {user_id}")

    cur.close()
    con.commit()


def add_auth_code(user_id, auth_code : str):
    cur = con.cursor()

    cur.execute(f"update users set auth_code = '{auth_code}' where user_id = {user_id}")

    cur.close()
    con.commit()


def get_auth_code(user_id) -> str:
    cur = con.cursor()

    auth_code = cur.execute(f"select auth_code from users where user_id = {user_id}").fetchone()[0]

    return auth_code



