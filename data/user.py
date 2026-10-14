import csv
from models.user import UserBase


database = "users.csv"

column_fields = ["id", "first_name", "last_name", "id_type", "id_number", "phone_number", "email"]

def write_into_csv(register: UserBase):

    with open(database, "a", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            column_fields,
        )
        writer.writerow(register.model_dump())
    csvfile.close()

def create_user_register(new_user: UserBase):
    write_into_csv(new_user)
    return True






