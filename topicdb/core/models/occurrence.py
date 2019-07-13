"""
Occurrence class. Part of the StoryTechnologies project.

June 12, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

from typing import Optional, Union

from slugify import slugify  # type: ignore

from topicdb.core.models.entity import Entity
from topicdb.core.models.language import Language
from topicdb.core.topicdberror import TopicDbError


class Occurrence(Entity):

    def __init__(self,
                 identifier: str = '',
                 instance_of: str = 'occurrence',
                 topic_identifier: str = '',
                 scope: str = '*',  # Universal scope
                 resource_ref: str = '',
                 resource_data: Optional[Union[str, bytes]] = None,
                 language: Language = Language.ENG) -> None:
        super().__init__(identifier, instance_of)

        if topic_identifier == '*':  # Universal scope
            self.__topic_identifier = '*'
        else:
            self.__topic_identifier = slugify(str(topic_identifier))

        self.__scope = scope if scope == '*' else slugify(str(scope))

        self.resource_ref = resource_ref

        if resource_data:
            self.__resource_data = resource_data if isinstance(resource_data, bytes) else bytes(resource_data,
                                                                                                encoding="utf-8")
        else:
            self.__resource_data = None

        self.language = language

    @property
    def scope(self) -> str:
        return self.__scope

    @scope.setter
    def scope(self, value: str) -> None:
        if value == '':
            raise TopicDbError("Empty 'value' parameter")
        self.__scope = value if value == '*' else slugify(str(value))

    @property
    def topic_identifier(self) -> str:
        return self.__topic_identifier

    @topic_identifier.setter
    def topic_identifier(self, value: str) -> None:
        if value == '':
            raise TopicDbError("Empty 'value' parameter")
        elif value == '*':  # Universal scope
            self.__topic_identifier = '*'
        else:
            self.__topic_identifier = slugify(str(value))

    @property
    def resource_data(self) -> Optional[bytes]:
        return self.__resource_data

    @resource_data.setter
    def resource_data(self, value: Union[str, bytes]) -> None:
        self.__resource_data = value if isinstance(value, bytes) else bytes(value, encoding="utf-8")

    def has_data(self) -> bool:
        return self.__resource_data is not None
