-- SQL Schema for Retail Chain Management Database

-- Creating 'customers' table
CREATE TABLE customers (
    cust_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255),
    country CHAR(2)
);

-- Sample data for 'customers'
INSERT INTO customers (cust_id, name, country) VALUES
('a', 'Arfa', 'pk'),
('b', 'Brendon', 'us'),
('c', 'Chiyo', 'ja');

-- Creating 'employees' table
CREATE TABLE employees (
    empl_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    salary INT,
    office_id VARCHAR(50),
    FOREIGN KEY (office_id) REFERENCES offices(office_id)
);

-- Sample data for 'employees'
INSERT INTO employees (empl_id, first_name, last_name, salary, office_id) VALUES
(1, 'Ambrosio', 'Rojas', 25784, 'c'),
(2, 'Val', 'Snyder', 37506, 'e'),
(3, 'Virginia', 'Levitt', 54523, 'b');

-- Creating 'offices' table
CREATE TABLE offices (
    office_id VARCHAR(50) PRIMARY KEY,
    city VARCHAR(255),
    state_province VARCHAR(255),
    country CHAR(2)
);

-- Sample data for 'offices'
INSERT INTO offices (office_id, city, state_province, country) VALUES
('a', 'Istanbul', 'Istanbul', 'tr'),
('b', 'Chicago', 'Illinois', 'us'),
('c', 'Rosario', 'Santa Fe', 'ar');

-- Creating 'orders' table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    cust_id VARCHAR(50),
    empl_id INT,
    total DECIMAL(10, 2),
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id),
    FOREIGN KEY (empl_id) REFERENCES employees(empl_id)
);

-- Sample data for 'orders'
INSERT INTO orders (order_id, cust_id, empl_id, total) VALUES
(1, 'c', 1, 24.78),
(2, 'a', 4, 28.54),
(3, 'b', 3, 48.69);

-- Creating 'salary_grades' table
CREATE TABLE salary_grades (
    grade TINYINT PRIMARY KEY,
    min_salary INT,
    max_salary INT
);

-- Sample data for 'salary_grades'
INSERT INTO salary_grades (grade, min_salary, max_salary) VALUES
(1, 10000, 19999),
(2, 20000, 29999),
(3, 30000, 39999);
