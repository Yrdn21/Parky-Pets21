from enum import Enum


class ProductCategory(str,Enum):
    VACCINE = "Vacuna"
    DEWORMER = "Desparacitante"
    TOY = "Juguete"
    MEDICINE = "Medicina"
    CREAM = "Crema"
    FOOD = "Comida"

