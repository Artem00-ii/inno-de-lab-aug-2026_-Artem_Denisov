CREATE USER hr_user WITH PASSWORD 'HrUser123!';

GRANT USAGE ON SCHEMA public TO hr_user;

GRANT SELECT, INSERT, UPDATE
ON TABLE public.employees
TO hr_user;

GRANT USAGE, SELECT
ON SEQUENCE public.employees_employeeid_seq
TO hr_user;