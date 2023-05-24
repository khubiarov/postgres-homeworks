CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE employees
(
	employee_id  int PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date,
	notes text
);

CREATE TABLE orders
(
	order_id int NOT NULL,
	customer_id varchar(5) REFERENCES customers(customer_id) ,
	employee_id int REFERENCES employees(employee_id) ,
	order_date date NOT NULL,
	ship_city varchar(40)
);
