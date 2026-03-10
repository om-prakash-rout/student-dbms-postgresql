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

# Show all students
print("=== All Students ===")
cur.execute("SELECT student_id, name, semester, course,>
for row in cur.fetchall():
    print(row)
print("\n")

# Show marks for a student
student_id = "BCA-SF-25-001"
print(f"=== Marks for {student_id} ===")
cur.execute("""
SELECT s.name, sub.subject_name, m.marks
FROM students s
JOIN marks m ON s.student_id = m.student_id
JOIN subjects sub ON m.subject_id = sub.subject_id
WHERE s.student_id=%s
ORDER BY sub.subject_id;
""", (student_id,))
for row in cur.fetchall():
    print(row)
print("\n")

# Average marks per student
print("=== Average Marks per Student ===")
cur.execute("""
SELECT s.student_id, s.name, s.semester, ROUND(AVG(m.ma>
FROM students s
JOIN marks m ON s.student_id = m.student_id
GROUP BY s.student_id, s.name, s.semester
ORDER BY s.semester, avg_marks DESC;
""")
for row in cur.fetchall():
    print(row)
print("\n")

# Topper per semester
print("=== Topper per Semester ===")
cur.execute("""
SELECT s.semester, s.student_id, s.name, ROUND(AVG(m.ma>
FROM students s
JOIN marks m ON s.student_id = m.student_id
GROUP BY s.semester, s.student_id, s.name
HAVING AVG(m.marks) = (
    SELECT MAX(avg_sub)
    FROM (
        SELECT AVG(m2.marks) AS avg_sub
        FROM students s2
        JOIN marks m2 ON s2.student_id = m2.student_id
        WHERE s2.semester = s.semester
        GROUP BY s2.student_id
    ) AS t
)
ORDER BY s.semester;
""")
for row in cur.fetchall():
    print(row)
print("\n")


# Students below 75% average (fail alert)
print("=== Students Below 75% Average Marks ===")
cur.execute("""
SELECT s.student_id, s.name, s.semester, ROUND(AVG(m.ma>
FROM students s
JOIN marks m ON s.student_id = m.student_id
GROUP BY s.student_id, s.name, s.semester
HAVING AVG(m.marks) < 75
ORDER BY semester;
""")
for row in cur.fetchall():
    print(row)
print("\n")


# Attendance report
print("=== Attendance Report ===")
cur.execute("""
SELECT s.student_id, s.name, s.semester, a.attendance_p>
FROM students s
JOIN attendance a ON s.student_id = a.student_id
ORDER BY s.semester, s.student_id;
""")
for row in cur.fetchall():
    print(row)
print("\n")

# Close connection
cur.close()
conn.close()
