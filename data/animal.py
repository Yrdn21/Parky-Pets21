import csv
from models.animal import AnimalBase
from enums import *

data_base = "animal.csv"

column_fields = [
    "id",
    "name",
    "species",
    "breed",
    "birth_day",
    "gender",
    "status"
]

def write_animal_into_csv(register: AnimalBase):
    with open(
        data_base, mode="a", newline=""
    ) as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=column_fields,
        )
        writer.writerow(register.model_dump())


def create_animal(animal: AnimalBase):
    write_animal_into_csv(animal)
    return True

def read_all_animals():
    with open(data_base) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=column_fields)
        return [AnimalBase(**row) for row in reader]

def read_one_animal_by_id(animal_id: str):
    with open(data_base) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=column_fields)
        for row in reader:
            if row["id"] == animal_id:
                return AnimalBase(**row)
        return None















