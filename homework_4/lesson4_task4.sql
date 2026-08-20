UPDATE public.employees
SET salary = salary * 1.10
WHERE department = 'HR';
UPDATE public.employees
SET department = 'Senior IT'
WHERE salary > 70000;
DELETE FROM public.employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM public.employeeprojects ep
    WHERE ep.employeeid = e.employeeid
);
BEGIN;

WITH new_project AS (
    INSERT INTO public.projects
        (ProjectName, Budget, StartDate, EndDate)
    VALUES
        ('New Internal Project', 100000.00, CURRENT_DATE, NULL)
    RETURNING ProjectID
)
INSERT INTO public.employeeprojects
    (EmployeeID, ProjectID, HoursWorked)
SELECT 1, ProjectID, 60
FROM new_project
UNION ALL
SELECT 4, ProjectID, 40
FROM new_project;

COMMIT;
