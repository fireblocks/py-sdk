# coding: utf-8
from dataclasses import dataclass
import typing_extensions
from fireblocks_client.model.request_options import RequestOptions
import urllib3
from urllib3._collections import HTTPHeaderDict

from fireblocks_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fireblocks_client import schemas  # noqa: F401

from fireblocks_client.model.get_connections_response import GetConnectionsResponse

# Query params


class OrderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ASC(cls):
        return cls("ASC")
    
    @schemas.classproperty
    def DESC(cls):
        return cls("DESC")


class FilterSchema(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            id = schemas.StrSchema
            userId = schemas.StrSchema
            vaultAccountId = schemas.NumberSchema
            connectionMethod = schemas.StrSchema
            feeLevel = schemas.StrSchema
            appUrl = schemas.StrSchema
            appName = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "userId": userId,
                "vaultAccountId": vaultAccountId,
                "connectionMethod": connectionMethod,
                "feeLevel": feeLevel,
                "appUrl": appUrl,
                "appName": appName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vaultAccountId"]) -> MetaOapg.properties.vaultAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionMethod"]) -> MetaOapg.properties.connectionMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeLevel"]) -> MetaOapg.properties.feeLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appUrl"]) -> MetaOapg.properties.appUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["appName"]) -> MetaOapg.properties.appName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "userId", "vaultAccountId", "connectionMethod", "feeLevel", "appUrl", "appName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vaultAccountId"]) -> typing.Union[MetaOapg.properties.vaultAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionMethod"]) -> typing.Union[MetaOapg.properties.connectionMethod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeLevel"]) -> typing.Union[MetaOapg.properties.feeLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appUrl"]) -> typing.Union[MetaOapg.properties.appUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["appName"]) -> typing.Union[MetaOapg.properties.appName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "userId", "vaultAccountId", "connectionMethod", "feeLevel", "appUrl", "appName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        vaultAccountId: typing.Union[MetaOapg.properties.vaultAccountId, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        connectionMethod: typing.Union[MetaOapg.properties.connectionMethod, str, schemas.Unset] = schemas.unset,
        feeLevel: typing.Union[MetaOapg.properties.feeLevel, str, schemas.Unset] = schemas.unset,
        appUrl: typing.Union[MetaOapg.properties.appUrl, str, schemas.Unset] = schemas.unset,
        appName: typing.Union[MetaOapg.properties.appName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FilterSchema':
        return super().__new__(
            cls,
            *_args,
            id=id,
            userId=userId,
            vaultAccountId=vaultAccountId,
            connectionMethod=connectionMethod,
            feeLevel=feeLevel,
            appUrl=appUrl,
            appName=appName,
            _configuration=_configuration,
            **kwargs,
        )


class SortSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ID(cls):
        return cls("id")
    
    @schemas.classproperty
    def USER_ID(cls):
        return cls("userId")
    
    @schemas.classproperty
    def VAULT_ACCOUNT_ID(cls):
        return cls("vaultAccountId")
    
    @schemas.classproperty
    def CREATED_AT(cls):
        return cls("createdAt")
    
    @schemas.classproperty
    def FEE_LEVEL(cls):
        return cls("feeLevel")
    
    @schemas.classproperty
    def APP_URL(cls):
        return cls("appUrl")
    
    @schemas.classproperty
    def APP_NAME(cls):
        return cls("appName")


class PageSizeSchema(
    schemas.NumberSchema
):
    pass
NextSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'order': typing.Union[OrderSchema, str, ],
        'filter': typing.Union[FilterSchema, dict, frozendict.frozendict, ],
        'sort': typing.Union[SortSchema, str, ],
        'pageSize': typing.Union[PageSizeSchema, decimal.Decimal, int, float, ],
        'next': typing.Union[NextSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_order = api_client.QueryParameter(
    name="order",
    style=api_client.ParameterStyle.FORM,
    schema=OrderSchema,
    explode=True,
)
request_query_filter = api_client.QueryParameter(
    name="filter",
    style=api_client.ParameterStyle.FORM,
    schema=FilterSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="pageSize",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_next = api_client.QueryParameter(
    name="next",
    style=api_client.ParameterStyle.FORM,
    schema=NextSchema,
    explode=True,
)
XRequestIDSchema = schemas.StrSchema
SchemaFor200ResponseBodyApplicationJson = GetConnectionsResponse
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: ResponseHeadersFor200


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
    headers=[
        x_request_id_parameter,
    ]
)
XRequestIDSchema = schemas.StrSchema
ResponseHeadersFor400 = typing_extensions.TypedDict(
    'ResponseHeadersFor400',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    headers: ResponseHeadersFor400
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    headers=[
        x_request_id_parameter,
    ]
)
XRequestIDSchema = schemas.StrSchema
ResponseHeadersFor500 = typing_extensions.TypedDict(
    'ResponseHeadersFor500',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    headers: ResponseHeadersFor500
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    headers=[
        x_request_id_parameter,
    ]
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_oapg(self, params: typing.Union[ RequestQueryParams,] = None, request_options: RequestOptions = None):
        """
        List all open Web3 connections.
        """
        query_params = {}
        if params and params.get("order"):
            query_params["order"] = params.get("order")
        if params and params.get("filter"):
            query_params["filter"] = params.get("filter")
        if params and params.get("sort"):
            query_params["sort"] = params.get("sort")
        if params and params.get("page_size"):
            query_params["page_size"] = params.get("page_size")
        if params and params.get("next"):
            query_params["next"] = params.get("next")
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_order,
            request_query_filter,
            request_query_sort,
            request_query_page_size,
            request_query_next,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
        _headers = HTTPHeaderDict()
        _fields = None
        _body = None

        if request_options and request_options.get("idempotency_key"):
            idempotency_key = request_options.get("idempotency_key")
            if idempotency_key:
                _headers.add("Idempotency-Key", idempotency_key)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            timeout=10000,
        )

        response_for_status = _status_code_to_response.get(str(response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(response, self.api_client.configuration)
        else:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response.body


class Get(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def get(self , params: typing.Union[ RequestQueryParams,] = None, request_options: RequestOptions = None):
        return self._get_oapg(params, request_options)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(self , params: typing.Union[ RequestQueryParams,] = None, request_options: RequestOptions = None):
        return self._get_oapg(params, request_options)


