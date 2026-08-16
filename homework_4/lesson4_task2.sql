CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);
ALTER TABLE Employees
ADD COLUMN Email VARCHAR(100);
UPDATE Employees
SET Email = CASE EmployeeID
    WHEN 1 THEN 'alice.smith@example.com'
    WHEN 2 THEN 'bob.johnson@example.com'
    WHEN 3 THEN 'charlie.brown@example.com'
    WHEN 4 THEN 'diana.prince@example.com'
    WHEN 6 THEN 'frank.miller@example.com'
    WHEN 7 THEN 'grace.wilson@example.com'
END;
ALTER TABLE Employees
ADD CONSTRAINT employees_email_unique UNIQUE (Email);
ALTER TABLE Departments
RENAME COLUMN Location TO OfficeLocation;
SELECT * FROM Employees;

SELECT * FROM Departments;