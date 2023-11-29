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

from fireblocks_client.model.error import Error

# Path params
ConnectionIdSchema = schemas.StrSchema


class AssetTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CRYPTO(cls):
        return cls("CRYPTO")
    
    @schemas.classproperty
    def SIGNET(cls):
        return cls("SIGNET")
    
    @schemas.classproperty
    def SEN(cls):
        return cls("SEN")
    
    @schemas.classproperty
    def SIGNET_TEST(cls):
        return cls("SIGNET_TEST")
    
    @schemas.classproperty
    def SEN_TEST(cls):
        return cls("SEN_TEST")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'connectionId': typing.Union[ConnectionIdSchema, str, ],
        'assetType': typing.Union[AssetTypeSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_connection_id = api_client.PathParameter(
    name="connectionId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ConnectionIdSchema,
    required=True,
)
request_path_asset_type = api_client.PathParameter(
    name="assetType",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AssetTypeSchema,
    required=True,
)
XRequestIDSchema = schemas.StrSchema


class SchemaFor200ResponseBody(
    schemas.AnyTypeSchema,
):


    class MetaOapg:
        
        class properties:
            isThirdPartyRouting = schemas.BoolSchema
            description = schemas.StrSchema
            __annotations__ = {
                "isThirdPartyRouting": isThirdPartyRouting,
                "description": description,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isThirdPartyRouting"]) -> MetaOapg.properties.isThirdPartyRouting: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["isThirdPartyRouting", "description", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isThirdPartyRouting"]) -> typing.Union[MetaOapg.properties.isThirdPartyRouting, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["isThirdPartyRouting", "description", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        isThirdPartyRouting: typing.Union[MetaOapg.properties.isThirdPartyRouting, bool, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBody':
        return super().__new__(
            cls,
            *_args,
            isThirdPartyRouting=isThirdPartyRouting,
            description=description,
            _configuration=_configuration,
            **kwargs,
        )
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
        SchemaFor200ResponseBody,
    ]
    headers: ResponseHeadersFor200


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        '*/*': api_client.MediaType(
            schema=SchemaFor200ResponseBody),
    },
    headers=[
        x_request_id_parameter,
    ]
)
XRequestIDSchema = schemas.StrSchema
SchemaFor0ResponseBodyApplicationJson = Error
ResponseHeadersFor0 = typing_extensions.TypedDict(
    'ResponseHeadersFor0',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor0ResponseBodyApplicationJson,
    ]
    headers: ResponseHeadersFor0


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
    headers=[
        x_request_id_parameter,
    ]
)
_all_accept_content_types = (
    '*/*',
    'application/json',
)


class BaseApi(api_client.Api):

    def _check_third_party_routing_for_network_connection_oapg(self, params: typing.Union[RequestPathParams] = None, request_options: RequestOptions = None):
        """
        Retrieve third-party network routing validation by asset type.
        """
        path_params = {}
        for parameter in (
            request_path_connection_id,
            request_path_asset_type,
        ):
            path_params[parameter.name] = params.get(parameter.name)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_connection_id,
            request_path_asset_type,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()

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
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class CheckThirdPartyRoutingForNetworkConnection(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def check_third_party_routing_for_network_connection(self , params: typing.Union[RequestPathParams] = None, request_options: RequestOptions = None):
        return self._check_third_party_routing_for_network_connection_oapg(params, request_options)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(self , params: typing.Union[RequestPathParams] = None, request_options: RequestOptions = None):
        return self._check_third_party_routing_for_network_connection_oapg(params, request_options)


