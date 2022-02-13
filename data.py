from typing import List, Union

from fastapi import HTTPException

from models import ArticleModel, ArticleUpdateModel, EventModel, LaunchModel


class ArticleData:
    articles: List[ArticleModel] = [
        ArticleModel(
            id=1,
            featured=False,
            title="First Lauch to moon",
            url="http://localhost:8000/article/1",
            image_url="",
            news_site="",
            summary="",
            published_at="2020-01-14",
            launches=[
                LaunchModel(
                    id=1,
                    provider=""
                )
            ],
            events=[
                EventModel(
                    id=1,
                    provider=""
                )
            ]
        ),
        ArticleModel(
            id=2,
            featured=False,
            title="First Lauch mars",
            url="http://localhost:8000/article/2",
            image_url="http://localhost:8000/mars.png",
            news_site="",
            summary="",
            published_at="2021-08-28",
            launches=[
                LaunchModel(
                    id=2,
                    provider="SpaceX Falcon 9"
                )
            ],
            events=[
                EventModel(
                    id=2,
                    provider="SpaceX Mars Mission"
                )
            ]
        )
    ]
    current_id = 2

    def __get_article_by_id(self, article_id: int) \
            -> Union[ArticleModel, HTTPException]:
        for article in self.articles:
            if article.id == article_id:
                return article
        raise HTTPException(
            status_code=404,
            detail=f'Article with id {article_id} does not exist'
        )

    def get_all_articles(self) -> List[ArticleModel]:
        return self.articles

    def get_article(self, article_id: int) -> ArticleModel:
        return self.__get_article_by_id(article_id)

    def insert(self, article: ArticleModel) -> ArticleModel:
        self.current_id += 1
        article.id = self.current_id
        self.articles.append(article)
        return article

    def update(self, article_id: int, article_update: ArticleUpdateModel) \
            -> ArticleModel:
        article = self.__get_article_by_id(article_id)
        if article_update.featured is not None:
            article.featured = article_update.featured
        if article_update.title is not None:
            article.title = article_update.title
        if article_update.url is not None:
            article.url = article_update.url
        if article_update.image_url is not None:
            article.image_url = article_update.image_url
        if article_update.news_site is not None:
            article.news_site = article_update.news_site
        if article_update.summary is not None:
            article.summary = article_update.summary
        if article_update.published_at is not None:
            article.published_at = article_update.published_at
        if article_update.launches is not None:
            article.launches = article_update.launches
        if article_update.events is not None:
            article.events = article_update.events
        return article

    def delete(self, article_id: int) -> ArticleModel:
        article = self.__get_article_by_id(article_id)
        self.articles.remove(article)
        return article
