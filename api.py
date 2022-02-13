from typing import Union

from fastapi import APIRouter, HTTPException

from data import ArticleData
from models import ArticleModel, ArticleUpdateModel

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
    :return: The Animal retriaeved by id if it exists
    """
    return article_data.get_article(id)


@article_router.post('/')
async def create_article(article: ArticleModel) -> ArticleModel:
    """
    Create Article\n
    :param article: The body with Article information to be created\n
    :return: The Article created
    """
    return article_data.insert(article)


@article_router.put('/{id}')
async def update_article(id: int, article_update: ArticleUpdateModel) \
        -> Union[ArticleModel, HTTPException]:
    """
    Update an Article\n
    :param id: The id of the Article to be updated\n
    :param article_update: The body with Article information to be updated\n
    :return: The Article updated if it exists
    """
    return article_data.update(id, article_update)


@article_router.delete('/{id}')
async def remove_article(id: int) -> Union[ArticleModel, HTTPException]:
    """
    Delete an Article\n
    :param id: The id of the Article to be deleted\n
    :return: The Article removed if it exists
    """
    return article_data.delete(id)
