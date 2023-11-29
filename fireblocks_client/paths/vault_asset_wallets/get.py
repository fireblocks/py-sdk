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

from fireblocks_client.model.paginated_asset_wallet_response import PaginatedAssetWalletResponse

from . import path

# Query params
TotalAmountLargerThanSchema = schemas.NumberSchema
AssetIdSchema = schemas.StrSchema
BeforeSchema = schemas.StrSchema
AfterSchema = schemas.StrSchema


class LimitSchema(
    schemas.NumberSchema
):


    class MetaOapg:
        inclusive_maximum = 1000
        inclusive_minimum = 1
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'totalAmountLargerThan': typing.Union[TotalAmountLargerThanSchema, decimal.Decimal, int, float, ],
        'assetId': typing.Union[AssetIdSchema, str, ],
        'before': typing.Union[BeforeSchema, str, ],
        'after': typing.Union[AfterSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, float, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_total_amount_larger_than = api_client.QueryParameter(
    name="totalAmountLargerThan",
    style=api_client.ParameterStyle.FORM,
    schema=TotalAmountLargerThanSchema,
    explode=True,
)
request_query_asset_id = api_client.QueryParameter(
    name="assetId",
    style=api_client.ParameterStyle.FORM,
    schema=AssetIdSchema,
    explode=True,
)
request_query_before = api_client.QueryParameter(
    name="before",
    style=api_client.ParameterStyle.FORM,
    schema=BeforeSchema,
    explode=True,
)
request_query_after = api_client.QueryParameter(
    name="after",
    style=api_client.ParameterStyle.FORM,
    schema=AfterSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
XRequestIDSchema = schemas.StrSchema
x_request_id_parameter = api_client.HeaderParameter(
    name="X-Request-ID",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XRequestIDSchema,
)
SchemaFor200ResponseBody = PaginatedAssetWalletResponse
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
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    '*/*',
)


class BaseApi(api_client.Api):

    def _get_asset_wallets_oapg(self, params: typing.Union[RequestQueryParams,] = None, request_options: RequestOptions = None):
        """
        List asset wallets (Paginated)
        """
        query_params = {}
        query_params["total_amount_larger_than"] = params.get("total_amount_larger_than")
        query_params["asset_id"] = params.get("asset_id")
        query_params["before"] = params.get("before")
        query_params["after"] = params.get("after")
        query_params["limit"] = params.get("limit")
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_total_amount_larger_than,
            request_query_asset_id,
            request_query_before,
            request_query_after,
            request_query_limit,
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
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class GetAssetWallets(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def get_asset_wallets(self , params: typing.Union[RequestQueryParams,] = None, request_options: RequestOptions = None):
        return self._get_asset_wallets_oapg(params, request_options)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    def get(self , params: typing.Union[RequestQueryParams,] = None, request_options: RequestOptions = None):
        return self._get_asset_wallets_oapg(params, request_options)


