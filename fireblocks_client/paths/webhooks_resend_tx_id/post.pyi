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
TxIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'txId': typing.Union[TxIdSchema, str, ],
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


request_path_tx_id = api_client.PathParameter(
    name="txId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TxIdSchema,
    required=True,
)
# body param


class SchemaForRequestBodyApplicationJson(
    schemas.AnyTypeSchema,
):


    class MetaOapg:
        
        class properties:
            resendCreated = schemas.BoolSchema
            resendStatusUpdated = schemas.BoolSchema
            __annotations__ = {
                "resendCreated": resendCreated,
                "resendStatusUpdated": resendStatusUpdated,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resendCreated"]) -> MetaOapg.properties.resendCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resendStatusUpdated"]) -> MetaOapg.properties.resendStatusUpdated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resendCreated", "resendStatusUpdated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resendCreated"]) -> typing.Union[MetaOapg.properties.resendCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resendStatusUpdated"]) -> typing.Union[MetaOapg.properties.resendStatusUpdated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resendCreated", "resendStatusUpdated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        resendCreated: typing.Union[MetaOapg.properties.resendCreated, bool, schemas.Unset] = schemas.unset,
        resendStatusUpdated: typing.Union[MetaOapg.properties.resendStatusUpdated, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            resendCreated=resendCreated,
            resendStatusUpdated=resendStatusUpdated,
            _configuration=_configuration,
            **kwargs,
        )
request_body_any_type = api_client.RequestBody(
content={
    'application/json': api_client.MediaType(
        schema=SchemaForRequestBodyApplicationJson),
},
    required=True,
)
XRequestIDSchema = schemas.StrSchema
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
    'application/json',
        )


class BaseApi(api_client.Api):

    def _resend_webhooks_for_transaction_oapg(self, params: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, RequestPathParams] = None, request_options: RequestOptions = None):
        """
        Resend failed webhooks for a transaction by ID
        """
        path_params = {}
        for parameter in (
            request_path_tx_id,
        ):
            path_params[parameter.name] =  params.get(parameter.name,None)

        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)

        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_tx_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
        _headers = HTTPHeaderDict()

        body =  params.get(any_type, schemas.unset)
        if body is schemas.unset:
            raise exceptions.ApiValueError(
            'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_any_type.serialize(params, "application/json")
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


class ResendWebhooksForTransaction(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def resend_webhooks_for_transaction(self ,params: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, RequestPathParams] = None, request_options: RequestOptions = None):
        return self._resend_webhooks_for_transaction_oapg(params, request_options)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        content_type: typing_extensions.Literal["application/json"] = ...,
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
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        content_type: str = ...,
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
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        content_type: str = ...,
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

    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        content_type: str = 'application/json',
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._resend_webhooks_for_transaction_oapg(
        body=body,
        path_params=path_params,
        content_type=content_type,
        accept_content_types=accept_content_types,
        stream=stream,
        timeout=timeout,
        skip_deserialization=skip_deserialization
    )


