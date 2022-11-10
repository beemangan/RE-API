# coding: utf-8

"""
    Public Robot Events API

    An API to access data on Robot Events officially. ## Request Metadata Pagination is performed the same way throughout each pageable endpoint using the query parameters `page` and `per_page`. Please not that dates should be formatted according to RFC3339.   # noqa: E501

    The version of the OpenAPI document: 1.0.21
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class Ranking(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int32Schema
        
            @staticmethod
            def event() -> typing.Type['IdInfo']:
                return IdInfo
        
            @staticmethod
            def division() -> typing.Type['IdInfo']:
                return IdInfo
            rank = schemas.Int32Schema
        
            @staticmethod
            def team() -> typing.Type['IdInfo']:
                return IdInfo
            wins = schemas.Int32Schema
            losses = schemas.Int32Schema
            ties = schemas.Int32Schema
            wp = schemas.Int32Schema
            ap = schemas.Int32Schema
            sp = schemas.Int32Schema
            high_score = schemas.Int32Schema
            average_points = schemas.NumberSchema
            total_points = schemas.Int32Schema
            __annotations__ = {
                "id": id,
                "event": event,
                "division": division,
                "rank": rank,
                "team": team,
                "wins": wins,
                "losses": losses,
                "ties": ties,
                "wp": wp,
                "ap": ap,
                "sp": sp,
                "high_score": high_score,
                "average_points": average_points,
                "total_points": total_points,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event"]) -> 'IdInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["division"]) -> 'IdInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rank"]) -> MetaOapg.properties.rank: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team"]) -> 'IdInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wins"]) -> MetaOapg.properties.wins: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["losses"]) -> MetaOapg.properties.losses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ties"]) -> MetaOapg.properties.ties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wp"]) -> MetaOapg.properties.wp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ap"]) -> MetaOapg.properties.ap: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sp"]) -> MetaOapg.properties.sp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["high_score"]) -> MetaOapg.properties.high_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["average_points"]) -> MetaOapg.properties.average_points: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_points"]) -> MetaOapg.properties.total_points: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "event", "division", "rank", "team", "wins", "losses", "ties", "wp", "ap", "sp", "high_score", "average_points", "total_points", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event"]) -> typing.Union['IdInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["division"]) -> typing.Union['IdInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rank"]) -> typing.Union[MetaOapg.properties.rank, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> typing.Union['IdInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wins"]) -> typing.Union[MetaOapg.properties.wins, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["losses"]) -> typing.Union[MetaOapg.properties.losses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ties"]) -> typing.Union[MetaOapg.properties.ties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wp"]) -> typing.Union[MetaOapg.properties.wp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ap"]) -> typing.Union[MetaOapg.properties.ap, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sp"]) -> typing.Union[MetaOapg.properties.sp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["high_score"]) -> typing.Union[MetaOapg.properties.high_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["average_points"]) -> typing.Union[MetaOapg.properties.average_points, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_points"]) -> typing.Union[MetaOapg.properties.total_points, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "event", "division", "rank", "team", "wins", "losses", "ties", "wp", "ap", "sp", "high_score", "average_points", "total_points", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        event: typing.Union['IdInfo', schemas.Unset] = schemas.unset,
        division: typing.Union['IdInfo', schemas.Unset] = schemas.unset,
        rank: typing.Union[MetaOapg.properties.rank, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        team: typing.Union['IdInfo', schemas.Unset] = schemas.unset,
        wins: typing.Union[MetaOapg.properties.wins, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        losses: typing.Union[MetaOapg.properties.losses, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ties: typing.Union[MetaOapg.properties.ties, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wp: typing.Union[MetaOapg.properties.wp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ap: typing.Union[MetaOapg.properties.ap, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sp: typing.Union[MetaOapg.properties.sp, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        high_score: typing.Union[MetaOapg.properties.high_score, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        average_points: typing.Union[MetaOapg.properties.average_points, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        total_points: typing.Union[MetaOapg.properties.total_points, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Ranking':
        return super().__new__(
            cls,
            *args,
            id=id,
            event=event,
            division=division,
            rank=rank,
            team=team,
            wins=wins,
            losses=losses,
            ties=ties,
            wp=wp,
            ap=ap,
            sp=sp,
            high_score=high_score,
            average_points=average_points,
            total_points=total_points,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.id_info import IdInfo
