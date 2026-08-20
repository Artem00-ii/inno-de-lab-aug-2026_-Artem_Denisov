-- Lesson 5: Data Warehouse for an electric scooter rental service
-- Star Schema

-- Dimension: users
CREATE TABLE dim_user (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    registration_date DATE
);

-- Dimension: scooters
CREATE TABLE dim_scooter (
    scooter_id SERIAL PRIMARY KEY,
    model VARCHAR(100),
    scooter_type VARCHAR(50),
    battery_capacity INT
);

-- Dimension: locations
CREATE TABLE dim_location (
    location_id SERIAL PRIMARY KEY,
    city VARCHAR(100),
    district VARCHAR(100),
    address VARCHAR(200)
);

-- Dimension: dates
CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    full_date DATE NOT NULL,
    day INT,
    month INT,
    year INT,
    day_of_week VARCHAR(20)
);
-- Fact table: scooter rides
-- Grain: one row represents one completed scooter ride

CREATE TABLE fact_rides (
    ride_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    scooter_id INT NOT NULL,
    start_location_id INT NOT NULL,
    end_location_id INT NOT NULL,
    date_id INT NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    duration_minutes INT NOT NULL,
    distance_km NUMERIC(10,2) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    battery_start INT,
    battery_end INT,

    CONSTRAINT fk_ride_user
        FOREIGN KEY (user_id)
        REFERENCES dim_user(user_id),

    CONSTRAINT fk_ride_scooter
        FOREIGN KEY (scooter_id)
        REFERENCES dim_scooter(scooter_id),

    CONSTRAINT fk_start_location
        FOREIGN KEY (start_location_id)
        REFERENCES dim_location(location_id),

    CONSTRAINT fk_end_location
        FOREIGN KEY (end_location_id)
        REFERENCES dim_location(location_id),

    CONSTRAINT fk_ride_date
        FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);
-- Load sample users
INSERT INTO dim_user (first_name, last_name, age, registration_date)
VALUES
('Artem', 'Ivanov', 22, '2026-01-10'),
('Anna', 'Petrova', 28, '2026-02-15'),
('Dmitry', 'Sokolov', 31, '2026-03-05'),
('Maria', 'Smirnova', 25, '2026-03-20');

-- Load sample scooters
INSERT INTO dim_scooter (model, scooter_type, battery_capacity)
VALUES
('Xiaomi Pro 2', 'City', 12800),
('Ninebot Max G30', 'City', 15300),
('Kugoo M4', 'Comfort', 13000),
('Ninebot F40', 'City', 10200);

-- Load sample locations
INSERT INTO dim_location (city, district, address)
VALUES
('Minsk', 'Central District', 'Independence Avenue 10'),
('Minsk', 'Leninsky District', 'Pervomayskaya Street 20'),
('Minsk', 'Sovetsky District', 'Bogdanovicha Street 15'),
('Minsk', 'Frunzensky District', 'Pobediteley Avenue 30');

-- Load sample dates
INSERT INTO dim_date (full_date, day, month, year, day_of_week)
VALUES
('2026-08-01', 1, 8, 2026, 'Saturday'),
('2026-08-02', 2, 8, 2026, 'Sunday'),
('2026-08-03', 3, 8, 2026, 'Monday'),
('2026-08-04', 4, 8, 2026, 'Tuesday'),
('2026-08-05', 5, 8, 2026, 'Wednesday');
-- Load sample scooter rides
-- Grain: one row = one completed ride

INSERT INTO fact_rides
(user_id, scooter_id, start_location_id, end_location_id, date_id,
 start_time, end_time, duration_minutes, distance_km, price,
 battery_start, battery_end)
VALUES
(1, 1, 1, 2, 1,
 '2026-08-01 09:10:00', '2026-08-01 09:35:00',
 25, 5.20, 7.50, 95, 82),

(2, 2, 2, 3, 1,
 '2026-08-01 12:20:00', '2026-08-01 13:05:00',
 45, 9.80, 13.50, 88, 65),

(3, 3, 3, 1, 2,
 '2026-08-02 10:15:00', '2026-08-02 10:50:00',
 35, 7.10, 10.00, 92, 76),

(4, 4, 1, 4, 2,
 '2026-08-02 18:30:00', '2026-08-02 19:10:00',
 40, 8.60, 12.00, 80, 62),

(1, 2, 4, 2, 3,
 '2026-08-03 08:45:00', '2026-08-03 09:20:00',
 35, 6.70, 9.50, 75, 60),

(2, 1, 2, 1, 3,
 '2026-08-03 17:10:00', '2026-08-03 17:55:00',
 45, 10.20, 14.00, 90, 68),

(3, 4, 3, 4, 4,
 '2026-08-04 14:00:00', '2026-08-04 14:30:00',
 30, 5.90, 8.50, 85, 72),

(4, 3, 4, 1, 5,
 '2026-08-05 20:15:00', '2026-08-05 21:05:00',
 50, 11.30, 16.00, 78, 55);
-- Analytical query 1:
-- Business question: How many rides were completed on each day?

SELECT
    d.full_date,
    COUNT(f.ride_id) AS total_rides
FROM fact_rides f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.full_date
ORDER BY d.full_date;
-- Analytical query 2:
-- Business question: How much revenue was generated each day?

SELECT
    d.full_date,
    SUM(f.price) AS total_revenue
FROM fact_rides f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.full_date
ORDER BY d.full_date;
-- Analytical query 3:
-- Business question: Which scooter models are used most often?

SELECT
    s.model,
    COUNT(f.ride_id) AS total_rides,
    ROUND(AVG(f.duration_minutes), 2) AS avg_duration_minutes
FROM fact_rides f
JOIN dim_scooter s
    ON f.scooter_id = s.scooter_id
GROUP BY s.model
ORDER BY total_rides DESC;