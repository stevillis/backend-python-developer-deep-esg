from typing import List, Optional

from pydantic import BaseModel


class LaunchModel(BaseModel):
    id: Optional[int]
    provider: str


class EventModel(BaseModel):
    id: Optional[int]
    provider: str


class ArticleModel(BaseModel):
    id: Optional[int]
    featured: bool
    title: str
    url: str
    image_url: str
    news_site: str
    summary: str
    published_at: str
    launches: List[LaunchModel]
    events: List[EventModel]


class ArticleUpdateModel(BaseModel):
    featured: bool
    title: str
    url: str
    image_url: str
    news_site: str
    summary: str
    published_at: str
    launches: List[LaunchModel]
    events: List[EventModel]
