-- Insert sample students
INSERT INTO students (name, course, semester)
VALUES
('Rahul Sharma', 'BCA', 3),
('Anita Verma', 'BCA', 2),
('Vikram Singh', 'BCA', 1);

-- Insert sample marks
INSERT INTO marks (student_id, subject, marks)
VALUES
(1, 'DBMS', 85),
(1, 'Python', 90),
(2, 'DBMS', 78),
(2, 'Python', 82),
(3, 'DBMS', 92),
(3, 'Python', 88);
