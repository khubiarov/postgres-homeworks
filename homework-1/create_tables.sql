create table customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)

);


create table orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(100)UNIQUE REFERENCES orders(customer_id),
	employee_id varchar(100),
	order_date varchar(100),
	ship_city varchar(100)
);

create table employees
(
    first_name varchar(100),
	last_name varchar(100),
	title varchar(100),
	birth_date varchar(100),
	notes text
);

