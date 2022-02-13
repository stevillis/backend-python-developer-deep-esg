from fastapi import FastAPI

from api import article_router

app = FastAPI()


@app.get('/', tags=['challenge'])
async def home():
    """
    Show the challenge description
    :return: The challenge name
    """
    return "Back-end Challenge 2021 🏅 - Space Flight News"


app.include_router(article_router, prefix='/articles', tags=['articles'])
