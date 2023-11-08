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

from fireblocks_client.model.xb_settlement_flow_execution_request_body import XBSettlementFlowExecutionRequestBody
from fireblocks_client.model.error_response import ErrorResponse
from fireblocks_client.model.xb_settlement_flow_execution_model import XBSettlementFlowExecutionModel

from . import path

# Path params
FlowIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'flowId': typing.Union[FlowIdSchema, str, ],
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


request_path_flow_id = api_client.PathParameter(
    name="flowId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FlowIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = XBSettlementFlowExecutionRequestBody
request_body_xb_settlement_flow_execution_request_body = api_client.RequestBody(
content={
    'application/json': api_client.MediaType(
        schema=SchemaForRequestBodyApplicationJson),
},
)
SchemaFor200ResponseBodyApplicationJson = XBSettlementFlowExecutionModel


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
                    SchemaFor200ResponseBodyApplicationJson,
                ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
    'application/json': api_client.MediaType(
    schema=SchemaFor200ResponseBodyApplicationJson),
    },
    )
SchemaFor400ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
                    SchemaFor400ResponseBodyApplicationJson,
                ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
    'application/json': api_client.MediaType(
    schema=SchemaFor400ResponseBodyApplicationJson),
    },
    )
SchemaFor404ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
                    SchemaFor404ResponseBodyApplicationJson,
                ]
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    content={
    'application/json': api_client.MediaType(
    schema=SchemaFor404ResponseBodyApplicationJson),
    },
    )
SchemaFor401ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
                    SchemaFor401ResponseBodyApplicationJson,
                ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
    'application/json': api_client.MediaType(
    schema=SchemaFor401ResponseBodyApplicationJson),
    },
    )
SchemaFor5XXResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor5XX(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
                    SchemaFor5XXResponseBodyApplicationJson,
                ]
    headers: schemas.Unset = schemas.unset


_response_for_5XX = api_client.OpenApiResponse(
    response_cls=ApiResponseFor5XX,
    content={
    'application/json': api_client.MediaType(
    schema=SchemaFor5XXResponseBodyApplicationJson),
    },
    )
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
    '401': _response_for_401,
    '5XX': _response_for_5XX,
}
_all_accept_content_types = (
    'application/json',
        )


class BaseApi(api_client.Api):

    def _execute_xb_settlement_flow_action_oapg(self, params: typing.Union[SchemaForRequestBodyApplicationJson,RequestPathParams] = None, request_options: RequestOptions = None):
        """
        Execute cross-border settlement flow
        """
        path_params = {}
        for parameter in (
            request_path_flow_id,
        ):
            path_params[parameter.name] =  params.get(parameter.name,None)

        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)

        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_flow_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
        _headers = HTTPHeaderDict()

        _fields = None
        _body = None
        serialized_data = request_body_xb_settlement_flow_execution_request_body.serialize(params, "application/json")
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
            method='post'.upper(),
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


class ExecuteXbSettlementFlowAction(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def execute_xb_settlement_flow_action(self ,params: typing.Union[SchemaForRequestBodyApplicationJson,RequestPathParams] = None, request_options: RequestOptions = None):
        return self._execute_xb_settlement_flow_action_oapg(params, request_options)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def post(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, schemas.Unset] = schemas.unset,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._execute_xb_settlement_flow_action_oapg(
        body=body,
        path_params=path_params,
        content_type=content_type,
        accept_content_types=accept_content_types,
        stream=stream,
        timeout=timeout,
        skip_deserialization=skip_deserialization
    )


