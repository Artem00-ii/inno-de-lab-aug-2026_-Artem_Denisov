CREATE OR REPLACE FUNCTION CalculateAnnualBonus(
    employee_id INT,
    Salary NUMERIC
)
RETURNS NUMERIC
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN Salary * 0.10;
END;
$$;
SELECT
    employeeid,
    firstname,
    lastname,
    salary,
    CalculateAnnualBonus(employeeid, salary) AS annual_bonus
FROM public.employees;
CREATE OR REPLACE VIEW IT_Department_View AS
SELECT
    employeeid,
    firstname,
    lastname,
    salary
FROM public.employees
WHERE department = 'IT';
SELECT *
FROM public.IT_Department_View;