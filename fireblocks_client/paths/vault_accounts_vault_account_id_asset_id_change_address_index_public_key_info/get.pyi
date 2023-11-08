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

from fireblocks_client.model.public_key_information import PublicKeyInformation
from fireblocks_client.model.error import Error


# Query params
CompressedSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'compressed': typing.Union[CompressedSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_compressed = api_client.QueryParameter(
    name="compressed",
    style=api_client.ParameterStyle.FORM,
    schema=CompressedSchema,
    explode=True,
)
# Path params
VaultAccountIdSchema = schemas.StrSchema
AssetIdSchema = schemas.StrSchema
ChangeSchema = schemas.NumberSchema
AddressIndexSchema = schemas.NumberSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'vaultAccountId': typing.Union[VaultAccountIdSchema, str, ],
        'assetId': typing.Union[AssetIdSchema, str, ],
        'change': typing.Union[ChangeSchema, decimal.Decimal, int, float, ],
        'addressIndex': typing.Union[AddressIndexSchema, decimal.Decimal, int, float, ],
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


request_path_vault_account_id = api_client.PathParameter(
    name="vaultAccountId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VaultAccountIdSchema,
    required=True,
)
request_path_asset_id = api_client.PathParameter(
    name="assetId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AssetIdSchema,
    required=True,
)
request_path_change = api_client.PathParameter(
    name="change",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ChangeSchema,
    required=True,
)
request_path_address_index = api_client.PathParameter(
    name="addressIndex",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AddressIndexSchema,
    required=True,
)
XRequestIDSchema = schemas.StrSchema
SchemaFor200ResponseBody = PublicKeyInformation
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

    def _get_public_key_info_for_address_oapg(self, params: typing.Union[RequestQueryParams,RequestPathParams] = None, request_options: RequestOptions = None):
        """
        Get the public key for a vault account
        """
        query_params = {}
        query_params["compressed"] = params.get("compressed")
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        path_params = {}
        for parameter in (
            request_path_vault_account_id,
            request_path_asset_id,
            request_path_change,
            request_path_address_index,
        ):
            path_params[parameter.name] =  params.get(parameter.name,None)

        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)

        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_vault_account_id,
            request_path_asset_id,
            request_path_change,
            request_path_address_index,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
                request_query_compressed,
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


class GetPublicKeyInfoForAddress(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def get_public_key_info_for_address(self ,params: typing.Union[RequestQueryParams,RequestPathParams] = None, request_options: RequestOptions = None):
        return self._get_public_key_info_for_address_oapg(params, request_options)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_public_key_info_for_address_oapg(
        query_params=query_params,
        path_params=path_params,
        accept_content_types=accept_content_types,
        stream=stream,
        timeout=timeout,
        skip_deserialization=skip_deserialization
    )


