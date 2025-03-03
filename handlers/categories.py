from fastapi import FastAPI, APIRouter, status

from pydantic import BaseModel
from fixtures import categories as fixture_categories
from schema.category import Category

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/all", response_model=list[Category])
async def get_taks():
    return fixture_categories


@router.post("/", response_model=Category)
async def create_task(category: Category):
    fixture_categories.append(category)
    return category


@router.patch("/{category_id}", response_model=Category)
async def path_task(id: int, name: str):
    for category in fixture_categories:
        if category["id"] == id:
            category["name"] = name
            return category


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(id: int):
    for index, category in enumerate(fixture_categories):
        if category["id"] == id:
            del fixture_categories[index]
            return {"message": "category deleted"}
        return {"message": "category not found"}
