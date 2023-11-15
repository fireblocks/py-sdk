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

from fireblocks_client.model.respond_to_connection_request import RespondToConnectionRequest

from . import path

# Path params
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
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


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = RespondToConnectionRequest


request_body_respond_to_connection_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
XRequestIDSchema = schemas.StrSchema
x_request_id_parameter = api_client.HeaderParameter(
    name="X-Request-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XRequestIDSchema,
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
    headers: ResponseHeadersFor200
    body: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    headers=[
        x_request_id_parameter,
    ]
)
XRequestIDSchema = schemas.StrSchema
x_request_id_parameter = api_client.HeaderParameter(
    name="X-Request-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XRequestIDSchema,
)
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
x_request_id_parameter = api_client.HeaderParameter(
    name="X-Request-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XRequestIDSchema,
)
ResponseHeadersFor404 = typing_extensions.TypedDict(
    'ResponseHeadersFor404',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    headers: ResponseHeadersFor404
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    headers=[
        x_request_id_parameter,
    ]
)
XRequestIDSchema = schemas.StrSchema
x_request_id_parameter = api_client.HeaderParameter(
    name="X-Request-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XRequestIDSchema,
)
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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
    '500': _response_for_500,
}


class BaseApi(api_client.Api):

    def _submit_oapg(self, params: typing.Union[SchemaForRequestBodyApplicationJson,RequestPathParams] = None, request_options: RequestOptions = None):
        """
        Respond to a pending Web3 connection request.
        """
        path_params = {}
        for parameter in (
            request_path_id,
        ):
            path_params[parameter.name] = params.get(parameter.name)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        _headers = HTTPHeaderDict()

        body = params.get(respond_to_connection_request, schemas.unset)
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_respond_to_connection_request.serialize(params, "application/json")
        _headers.add('Content-Type', "application/json")
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        idempotency_key = request_options.get("idempotency_key")
        if idempotency_key:
            _headers.add("Idempotency-Key", idempotency_key)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='put'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
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

        return api_response


class Submit(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def submit(self ,params: typing.Union[SchemaForRequestBodyApplicationJson,RequestPathParams] = None, request_options: RequestOptions = None):
        return self._submit_oapg(params, request_options)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def put(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = 'application/json',
        path_params: RequestPathParams = frozendict.frozendict(),
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._submit_oapg(
            body=body,
            path_params=path_params,
            content_type=content_type,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


