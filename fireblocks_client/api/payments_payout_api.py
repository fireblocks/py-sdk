# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from concurrent.futures import Future
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from fireblocks_client.models.create_payout_request import CreatePayoutRequest
from fireblocks_client.models.dispatch_payout_response import DispatchPayoutResponse
from fireblocks_client.models.payout_response import PayoutResponse

from fireblocks_client.api_client import ApiClient, RequestSerialized
from fireblocks_client.api_response import ApiResponse
from fireblocks_client.rest import RESTResponseType


class PaymentsPayoutApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def create_payout(
        self,
        idempotency_key: Annotated[Optional[StrictStr], Field(description="A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours.")] = None,
        create_payout_request: Optional[CreatePayoutRequest] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Future[ApiResponse[PayoutResponse]]:
        """Create a payout instruction set

        **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoints include APIs available only for customers with Payments Engine enabled on their accounts. </br> </br>These endpoints are currently in beta and might be subject to changes.</br> </br>If you want to learn more about Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or email CSM@fireblocks.com. </br> </br> <b u>Create a payout instruction set.</b> </u></br> A payout instruction set is a set of instructions for distributing payments from a single payment account to a list of payee accounts. </br> The instruction set defines: </br> <ul> <li>the payment account and its account type (vault, exchange, or fiat). </li> <li>the account type (vault account, exchange account, whitelisted address, network connection, fiat account, or merchant account), the amount, and the asset of payment for each payee account.</li> </ul> 

        :param idempotency_key: A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours.
        :type idempotency_key: str
        :param create_payout_request:
        :type create_payout_request: CreatePayoutRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._create_payout_serialize(
            idempotency_key=idempotency_key,
            create_payout_request=create_payout_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PayoutResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '5XX': "ErrorResponse",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _create_payout_serialize(
        self,
        idempotency_key,
        create_payout_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if create_payout_request is not None:
            _body_params = create_payout_request


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/payments/payout',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def execute_payout_action(
        self,
        payout_id: Annotated[StrictStr, Field(description="the payout id received from the creation of the payout instruction set")],
        idempotency_key: Annotated[Optional[StrictStr], Field(description="A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Future[ApiResponse[DispatchPayoutResponse]]:
        """Execute a payout instruction set

        **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoints include APIs available only for customers with Payments Engine enabled on their accounts. </br> </br>These endpoints are currently in beta and might be subject to changes.</br> </br>If you want to learn more about Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or email CSM@fireblocks.com. </br> </br><b u>Execute a payout instruction set.</b> </u> </br> </br>The instruction set will be verified and executed.</br> <b><u>Source locking</br></b> </u> If you are executing a payout instruction set from a payment account with an already active payout the active payout will complete before the new payout instruction set can be executed. </br> You cannot execute the same payout instruction set more than once. 

        :param payout_id: the payout id received from the creation of the payout instruction set (required)
        :type payout_id: str
        :param idempotency_key: A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours.
        :type idempotency_key: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._execute_payout_action_serialize(
            payout_id=payout_id,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "DispatchPayoutResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '5XX': "ErrorResponse",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _execute_payout_action_serialize(
        self,
        payout_id,
        idempotency_key,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if payout_id is not None:
            _path_params['payoutId'] = payout_id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/payments/payout/{payoutId}/actions/execute',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_payout(
        self,
        payout_id: Annotated[StrictStr, Field(description="the payout id received from the creation of the payout instruction set")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Future[ApiResponse[PayoutResponse]]:
        """Get the status of a payout instruction set

        **Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoints include APIs available only for customers with Payments Engine enabled on their accounts. </br> </br>These endpoints are currently in beta and might be subject to changes.</br> </br>If you want to learn more about Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or email CSM@fireblocks.com. </br> 

        :param payout_id: the payout id received from the creation of the payout instruction set (required)
        :type payout_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_payout_serialize(
            payout_id=payout_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PayoutResponse",
            '401': "ErrorResponse",
            '404': "ErrorResponse",
            '5XX': "ErrorResponse",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _get_payout_serialize(
        self,
        payout_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if payout_id is not None:
            _path_params['payoutId'] = payout_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/payments/payout/{payoutId}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


