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

from fireblocks_client.model.travel_rule_validate_transaction_response import TravelRuleValidateTransactionResponse
from fireblocks_client.model.travel_rule_validate_transaction_request import TravelRuleValidateTransactionRequest

# body param
SchemaForRequestBodyApplicationJson = TravelRuleValidateTransactionRequest


request_body_travel_rule_validate_transaction_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = TravelRuleValidateTransactionResponse


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


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _validate_travel_rule_transaction_oapg(self, params: typing.Union[SchemaForRequestBodyApplicationJson,] = None, request_options: RequestOptions = None):
        """
        Validate Travel Rule Transaction
        """
        used_path = path.value
        _headers = HTTPHeaderDict()
        _fields = None
        _body = None
        serialized_data = request_body_travel_rule_validate_transaction_request.serialize(params, "application/json")
        _headers.add('Content-Type', "application/json")
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']

        elif 'body' in serialized_data:
                _body = serialized_data['body']

        if request_options and request_options.get("idempotency_key"):
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

        return api_response.body


class ValidateTravelRuleTransaction(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def validate_travel_rule_transaction(self , params: typing.Union[SchemaForRequestBodyApplicationJson,] = None, request_options: RequestOptions = None):
        return self._validate_travel_rule_transaction_oapg(params, request_options)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def post(self , params: typing.Union[SchemaForRequestBodyApplicationJson,] = None, request_options: RequestOptions = None):
        return self._validate_travel_rule_transaction_oapg(params, request_options)


