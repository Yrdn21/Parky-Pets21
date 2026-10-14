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


def read_all_users_csv():
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile,column_fields)
        return [UserBase(**row) for row in reader]


def read_one_user_csv(user_id: int):
    with open(database) as csvfile:
        reader = csv.DictReader(csvfile,column_fields)

        for row in reader:
            if int(row["id"]) == user_id:
                return UserBase(**row)
        return None


def update_user_csv():
    #readoneuser
    #TODO implements the update user function
    pass

