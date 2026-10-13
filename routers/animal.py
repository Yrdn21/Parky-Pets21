from fastapi import APIRouter, status, HTTPException

from models.animal import AnimalBase, AnimalStatusUpdate
from data import animal

animals_list:list[AnimalBase] = []

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_animal(new_animal:AnimalBase):
    status = animal.create_animal(new_animal)
    ##animals_list.append(new_animal)
    if status:
        return new_animal
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Animal not found")

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[AnimalBase])
def show_all_animals():
    '''
    if not animals_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animals found")
    else:
        return animals_list
        '''
    animals = animal.read_all_animals()
    return animals


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=AnimalBase)
def show_one_animal(id: str):
    if not animals_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animal found")
    else:
        for animal in animals_list:
            if animal.id == id:
                return animal
        return None

@router.patch("/{id}", status_code=status.HTTP_200_OK, response_model=AnimalBase)
def update_animal_status(id: str, new_status: AnimalStatusUpdate):
    if not animals_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No animal found")
    else:
        for animal in animals_list:
            if animal.id == id:
                animal.status = new_status.alive
                return animal
        return None









