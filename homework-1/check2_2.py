import psycopg2, os, csv

with open(os.path.join('north_data', 'customers_data.csv'), encoding='utf-8') as file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(file, delimiter=",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла

    with psycopg2.connect(database='north', user='postgres', password=input('Введите пароль')) as conn:
        with conn.cursor() as cur:
            for row in file_reader:
                if count == 0:
                    count += 1
                    continue
                # Вывод строк
                #row['company_name'] = row['company_name'].replace("'", "''")

                #cur.execute
                cur.execute(
                    f'INSERT INTO customers(customer_id, company_name, contact_name) VALUES (%s, %s, %s)',
                    (row["customer_id"], row["company_name"], row["contact_name"]))
                #conn.commit()

