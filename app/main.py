from fastapi import FastAPI, APIRouter

from typing import Optional


app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Tasting Fast-API !!!"}


@api_router.get("/recipe/{recipe_id}", status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    """

    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]


# https://fastapi.tiangolo.com/tutorial/query-params/
@api_router.get("/search/", status_code=200)
def search_recipes(
    keyword: Optional[str] = None, max_results: Optional[int] = 10
) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        # RECIPES está sendo limitado por max_results
        return {"results": RECIPES[:max_results]}

        # Estudar mais sobre expressões lambda em python
    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")