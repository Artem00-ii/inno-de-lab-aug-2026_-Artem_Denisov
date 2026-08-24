-- Task 3: Create HR user
CREATE USER hr_user WITH PASSWORD 'HrUser123!';

-- Allow access to public schema
GRANT USAGE ON SCHEMA public TO hr_user;

-- Initial permission: SELECT only
GRANT SELECT
ON TABLE public.employees
TO hr_user;

-- Additional permissions: INSERT and UPDATE
GRANT INSERT, UPDATE
ON TABLE public.employees
TO hr_user;

-- Allow use of employee ID sequence
GRANT USAGE, SELECT
ON SEQUENCE public.employees_employeeid_seq
TO hr_user;