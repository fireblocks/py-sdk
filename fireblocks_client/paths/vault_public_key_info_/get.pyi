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
DerivationPathSchema = schemas.StrSchema
AlgorithmSchema = schemas.StrSchema
CompressedSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'derivationPath': typing.Union[DerivationPathSchema, str, ],
        'algorithm': typing.Union[AlgorithmSchema, str, ],
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


request_query_derivation_path = api_client.QueryParameter(
    name="derivationPath",
    style=api_client.ParameterStyle.FORM,
    schema=DerivationPathSchema,
    required=True,
    explode=True,
)
request_query_algorithm = api_client.QueryParameter(
    name="algorithm",
    style=api_client.ParameterStyle.FORM,
    schema=AlgorithmSchema,
    required=True,
    explode=True,
)
request_query_compressed = api_client.QueryParameter(
    name="compressed",
    style=api_client.ParameterStyle.FORM,
    schema=CompressedSchema,
    explode=True,
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

    def _get_public_key_info_oapg(self, params: typing.Union[RequestQueryParams,] = None, request_options: RequestOptions = None):
        """
        Get the public key information
        """
        query_params = {}
        query_params["derivation_path"] = params.get("derivation_path")
        query_params["algorithm"] = params.get("algorithm")
        query_params["compressed"] = params.get("compressed")
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)

        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
                request_query_derivation_path,
                request_query_algorithm,
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


class GetPublicKeyInfo(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def get_public_key_info(self ,params: typing.Union[RequestQueryParams,] = None, request_options: RequestOptions = None):
        return self._get_public_key_info_oapg(params, request_options)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
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
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_public_key_info_oapg(
        query_params=query_params,
        accept_content_types=accept_content_types,
        stream=stream,
        timeout=timeout,
        skip_deserialization=skip_deserialization
    )


