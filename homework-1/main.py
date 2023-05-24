# os.path.join('north_data', 'customers_data.csv'
"""Скрипт для заполнения данными таблиц в БД Postgres."""
#импортируем
import psycopg2, os, csv


class BaseClass:
    def __init__(self):
        '''инициализиуоем пути и пароль'''
        self.paswd = input('Введите пароль')
        self.csv_file = ""

    def get_csv(self):
        '''универсальный ридер из csv возвращает список'''
        with open(self.csv_file, encoding='utf-8') as file:

            data = []
            file_reader = csv.DictReader(file, delimiter=",")
            for row in file_reader:

                data.append(row)
        return data

    def customers(self):
        '''Метод для customers'''
        self.csv_file = os.path.join('north_data', 'customers_data.csv')
        data = self.get_csv()

        with psycopg2.connect(database='north', user='postgres', password=self.paswd) as conn:
            with conn.cursor() as cur:
                count = 0
                for row in data:
                    if count == 0:# это что  бы название стобцов не лезло в бд
                        count = 1
                        continue
                    cur.execute(f'INSERT INTO customers(customer_id, company_name, contact_name) VALUES (%s, %s, %s)',
                    (row["customer_id"], row["company_name"], row["contact_name"]))



    def employees(self):
        '''МЕтод для  employees'''
        self.csv_file = os.path.join('north_data', 'employees_data.csv')
        data = self.get_csv()
        count = 0
        with psycopg2.connect(database='north', user='postgres', password=self.paswd) as conn:
            with conn.cursor() as cur:
                for row in data:

                    if count == 0:
                        count = 1
                        continue

                    cur.execute(
                    f'INSERT INTO employees(first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s)',
                    (row["first_name"], row["last_name"], row["title"], row["birth_date"], row["notes"]))

            #conn.commit()
    def orders(self):
        '''Метод для orders'''
        self.csv_file = os.path.join('north_data', 'orders_data.csv')
        data = self.get_csv()
        count = 0
        with psycopg2.connect(database='north', user='postgres', password=self.paswd) as conn:
            with conn.cursor() as cur:
                for row in data:

                    if count == 0:
                        count = 1
                        continue

                    cur.execute(
                        f'INSERT INTO orders(order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)',
                    (row["order_id"], row["customer_id"], row["employee_id"], row["order_date"], row["ship_city"]))
            #conn.commit()
# я хотел что бы синтаксис был типа copy1 = BaseClass(файл,ф-строка), что бы можно было подключать любые csv

copy1 = BaseClass()
copy1.customers()
copy1.employees()
copy1.orders()

