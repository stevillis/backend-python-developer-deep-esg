from fastapi import APIRouter

from data import ArticleData

article_data = ArticleData()
article_router = APIRouter()


@article_router.get('/')
async def get_all_articles():
    """
    Get all Articles\n
    :return: A list of Articles
    """
    return article_data.get_all_articles()
