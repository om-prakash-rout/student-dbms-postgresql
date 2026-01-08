import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="studentdb",
    user="studentuser",
    password="password123",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Run a simple query
cur.execute("SELECT * FROM students;")
rows = cur.fetchall()

for row in rows:
    print(row)

# Close connection
cur.close()
conn.close()
