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
from typing import List, Optional
from typing_extensions import Annotated
from fireblocks.models.contract_abi_response_dto import ContractAbiResponseDto
from fireblocks.models.contract_data_decode_request import ContractDataDecodeRequest
from fireblocks.models.contract_data_decoded_response import ContractDataDecodedResponse
from fireblocks.models.parameter_with_value import ParameterWithValue
from fireblocks.models.read_call_function_dto import ReadCallFunctionDto
from fireblocks.models.transaction_receipt_response import TransactionReceiptResponse
from fireblocks.models.write_call_function_dto import WriteCallFunctionDto
from fireblocks.models.write_call_function_response_dto import WriteCallFunctionResponseDto

from fireblocks.api_client import ApiClient, RequestSerialized
from fireblocks.api_response import ApiResponse
from fireblocks.rest import RESTResponseType
from fireblocks.validation_utils import validate_not_empty_string


class ContractInteractionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def decode_contract_data(
        self,
        contract_address: Annotated[StrictStr, Field(description="The contract's onchain address")],
        base_asset_id: Annotated[StrictStr, Field(description="The blockchain native asset identifier")],
        contract_data_decode_request: ContractDataDecodeRequest,
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
    ) -> Future[ApiResponse[ContractDataDecodedResponse]]:
        """Decode a function call data, error, or event log

        Decode a function call data, error, or event log from a deployed contract by blockchain native asset id and contract address.

        :param contract_address: The contract's onchain address (required)
        :type contract_address: str
        :param base_asset_id: The blockchain native asset identifier (required)
        :type base_asset_id: str
        :param contract_data_decode_request: (required)
        :type contract_data_decode_request: ContractDataDecodeRequest
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

        validate_not_empty_string(function_name="decode_contract_data", param_name="contract_address", param_value=contract_address)
        validate_not_empty_string(function_name="decode_contract_data", param_name="base_asset_id", param_value=base_asset_id)

        _param = self._decode_contract_data_serialize(
            contract_address=contract_address,
            base_asset_id=base_asset_id,
            contract_data_decode_request=contract_data_decode_request,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContractDataDecodedResponse",
            '400': "ContractDataDecodeError",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _decode_contract_data_serialize(
        self,
        contract_address,
        base_asset_id,
        contract_data_decode_request,
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
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if contract_address is not None:
            _path_params['contractAddress'] = contract_address
        if base_asset_id is not None:
            _path_params['baseAssetId'] = base_asset_id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if contract_data_decode_request is not None:
            _body_params = contract_data_decode_request


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
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
            resource_path='/contract_interactions/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/decode',
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
    def get_deployed_contract_abi(
        self,
        contract_address: Annotated[StrictStr, Field(description="The contract's onchain address")],
        base_asset_id: StrictStr,
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
    ) -> Future[ApiResponse[ContractAbiResponseDto]]:
        """Return deployed contract's ABI

        Return deployed contract's ABI by blockchain native asset id and contract address

        :param contract_address: The contract's onchain address (required)
        :type contract_address: str
        :param base_asset_id: (required)
        :type base_asset_id: str
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

        validate_not_empty_string(function_name="get_deployed_contract_abi", param_name="contract_address", param_value=contract_address)
        validate_not_empty_string(function_name="get_deployed_contract_abi", param_name="base_asset_id", param_value=base_asset_id)

        _param = self._get_deployed_contract_abi_serialize(
            contract_address=contract_address,
            base_asset_id=base_asset_id,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContractAbiResponseDto",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _get_deployed_contract_abi_serialize(
        self,
        contract_address,
        base_asset_id,
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
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if contract_address is not None:
            _path_params['contractAddress'] = contract_address
        if base_asset_id is not None:
            _path_params['baseAssetId'] = base_asset_id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
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
            resource_path='/contract_interactions/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/functions',
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
    def get_transaction_receipt(
        self,
        base_asset_id: Annotated[StrictStr, Field(description="The blockchain base assetId")],
        tx_hash: Annotated[StrictStr, Field(description="The transaction hash")],
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
    ) -> Future[ApiResponse[TransactionReceiptResponse]]:
        """Get transaction receipt

        Retrieve the transaction receipt by blockchain native asset ID and transaction hash

        :param base_asset_id: The blockchain base assetId (required)
        :type base_asset_id: str
        :param tx_hash: The transaction hash (required)
        :type tx_hash: str
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

        validate_not_empty_string(function_name="get_transaction_receipt", param_name="base_asset_id", param_value=base_asset_id)
        validate_not_empty_string(function_name="get_transaction_receipt", param_name="tx_hash", param_value=tx_hash)

        _param = self._get_transaction_receipt_serialize(
            base_asset_id=base_asset_id,
            tx_hash=tx_hash,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TransactionReceiptResponse",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _get_transaction_receipt_serialize(
        self,
        base_asset_id,
        tx_hash,
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
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if base_asset_id is not None:
            _path_params['baseAssetId'] = base_asset_id
        if tx_hash is not None:
            _path_params['txHash'] = tx_hash
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
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
            resource_path='/contract_interactions/base_asset_id/{baseAssetId}/tx_hash/{txHash}/receipt',
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
    def read_call_function(
        self,
        contract_address: Annotated[StrictStr, Field(description="The contract's onchain address")],
        base_asset_id: StrictStr,
        read_call_function_dto: ReadCallFunctionDto,
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
    ) -> Future[ApiResponse[List[ParameterWithValue]]]:
        """Call a read function on a deployed contract

        Call a read function on a deployed contract by blockchain native asset id and contract address

        :param contract_address: The contract's onchain address (required)
        :type contract_address: str
        :param base_asset_id: (required)
        :type base_asset_id: str
        :param read_call_function_dto: (required)
        :type read_call_function_dto: ReadCallFunctionDto
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

        validate_not_empty_string(function_name="read_call_function", param_name="contract_address", param_value=contract_address)
        validate_not_empty_string(function_name="read_call_function", param_name="base_asset_id", param_value=base_asset_id)

        _param = self._read_call_function_serialize(
            contract_address=contract_address,
            base_asset_id=base_asset_id,
            read_call_function_dto=read_call_function_dto,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[ParameterWithValue]",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _read_call_function_serialize(
        self,
        contract_address,
        base_asset_id,
        read_call_function_dto,
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
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if contract_address is not None:
            _path_params['contractAddress'] = contract_address
        if base_asset_id is not None:
            _path_params['baseAssetId'] = base_asset_id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if read_call_function_dto is not None:
            _body_params = read_call_function_dto


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
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
            resource_path='/contract_interactions/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/functions/read',
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
    def write_call_function(
        self,
        contract_address: Annotated[StrictStr, Field(description="The contract's onchain address")],
        base_asset_id: StrictStr,
        write_call_function_dto: WriteCallFunctionDto,
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
    ) -> Future[ApiResponse[WriteCallFunctionResponseDto]]:
        """Call a write function on a deployed contract

        Call a write function on a deployed contract by blockchain native asset id and contract address. This creates an onchain transaction, thus it is an async operation. It returns a transaction id that can be polled for status check

        :param contract_address: The contract's onchain address (required)
        :type contract_address: str
        :param base_asset_id: (required)
        :type base_asset_id: str
        :param write_call_function_dto: (required)
        :type write_call_function_dto: WriteCallFunctionDto
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

        validate_not_empty_string(function_name="write_call_function", param_name="contract_address", param_value=contract_address)
        validate_not_empty_string(function_name="write_call_function", param_name="base_asset_id", param_value=base_asset_id)

        _param = self._write_call_function_serialize(
            contract_address=contract_address,
            base_asset_id=base_asset_id,
            write_call_function_dto=write_call_function_dto,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': "WriteCallFunctionResponseDto",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _write_call_function_serialize(
        self,
        contract_address,
        base_asset_id,
        write_call_function_dto,
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
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if contract_address is not None:
            _path_params['contractAddress'] = contract_address
        if base_asset_id is not None:
            _path_params['baseAssetId'] = base_asset_id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if write_call_function_dto is not None:
            _body_params = write_call_function_dto


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
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
            resource_path='/contract_interactions/base_asset_id/{baseAssetId}/contract_address/{contractAddress}/functions/write',
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


