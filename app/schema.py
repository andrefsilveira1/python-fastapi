from pydantic import BaseModel

from typing import Sequence


class Recipe(BaseModel):
    id: int
    label: str
    source: str


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]


class RecipeCreate(BaseModel):
    label: str
    source: str
    submitter_id: int