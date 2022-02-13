from fastapi import APIRouter

from data import ArticleData
from models import ArticleModel

article_data = ArticleData()
article_router = APIRouter()


@article_router.get('/')
async def get_all_articles():
    """
    Get all Articles\n
    :return: A list of Articles
    """
    return article_data.get_all_articles()


@article_router.get('/{id}')
async def get_article(id: int) -> ArticleModel:
    """
    Get Article by id\n
    :param id: The id of the Article to be retrieved
    :return: The Animal retrieved by id if it exists
    """
    return article_data.get_article(id)
