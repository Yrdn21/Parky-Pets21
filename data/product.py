import csv
from models.product import ProductBase

database = "products.csv"

column_fields = ["id", "name", "price", "category", "expiration_date"]

def write_register_csv(register:ProductBase):
    with open(database, "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile,column_fields,)
        writer.writerow(register.model_dump())
        csvfile.close()

def create_product_csv(new_product:ProductBase):
    write_register_csv(new_product)
    return True


def read_all_products_csv():
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile,column_fields)
        return [ProductBase(**row) for row in reader]
