from apscheduler.schedulers.blocking import BlockingScheduler
import psycopg2, random, os, time

USER_2FA = os.environ.get('USER_2FA')
PASSWORD_2FA = os.environ.get('PASSWORD_2FA')
DB_2FA = os.environ.get('DB_2FA')

DATABASE_URL = f"postgresql://{USER_2FA}:{PASSWORD_2FA}@db:5432/{DB_2FA}"

def task():
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users")
            ids = cur.fetchall()
            for id in ids:
                tempPass = f"{random.randint(0, 999999):06d}"
                cur.execute("UPDATE users SET lastChange = %s, tempPass = %s WHERE id = %s", (int(time.time()), tempPass, id))
            conn.commit()
            
scheduler = BlockingScheduler()
scheduler.add_job(task, 'interval', seconds=30)

scheduler.start()