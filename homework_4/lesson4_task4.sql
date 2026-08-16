UPDATE public.employees
SET salary = salary * 1.10
WHERE department = 'HR';
UPDATE public.employees
SET department = 'Senior IT'
WHERE firstname = 'Bob'
  AND lastname = 'Johnson'
  AND salary > 70000.00;
DELETE FROM public.employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM public.employeeprojects ep
    WHERE ep.employeeid = e.employeeid
);
BEGIN;

INSERT INTO public.projects
(ProjectName, Budget, StartDate, EndDate)
VALUES
('New Internal Project', 100000.00, CURRENT_DATE, NULL)
RETURNING ProjectID;
INSERT INTO public.employeeprojects
(EmployeeID, ProjectID, HoursWorked)
VALUES
(1, 4, 60),
(4, 4, 40);
SELECT *
FROM public.projects
WHERE projectid = 4;

SELECT *
FROM public.employeeprojects
WHERE projectid = 4;
COMMIT;