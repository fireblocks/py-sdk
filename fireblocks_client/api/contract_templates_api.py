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

from pydantic import Field, StrictBool, StrictStr, field_validator
from typing import Optional, Union
from typing_extensions import Annotated
from fireblocks_client.models.abi_function import AbiFunction
from fireblocks_client.models.contract_deploy_request import ContractDeployRequest
from fireblocks_client.models.contract_deploy_response import ContractDeployResponse
from fireblocks_client.models.contract_template_dto import ContractTemplateDto
from fireblocks_client.models.contract_upload_request import ContractUploadRequest
from fireblocks_client.models.templates_paginated_response import TemplatesPaginatedResponse

from fireblocks_client.api_client import ApiClient, RequestSerialized
from fireblocks_client.api_response import ApiResponse
from fireblocks_client.rest import RESTResponseType


class ContractTemplatesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def delete_contract_template_by_id(
        self,
        contract_template_id: Annotated[StrictStr, Field(description="The Contract Template identifier")],
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
    ) -> Future[ApiResponse[None]]:
        """Delete a contract template by id

        Delete a contract by id. allowed only for private contract templates. Notice: it is irreversible!

        :param contract_template_id: The Contract Template identifier (required)
        :type contract_template_id: str
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

        _param = self._delete_contract_template_by_id_serialize(
            contract_template_id=contract_template_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '404': "HttpContractDoesNotExistError",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _delete_contract_template_by_id_serialize(
        self,
        contract_template_id,
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
        if contract_template_id is not None:
            _path_params['contractTemplateId'] = contract_template_id
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
            method='DELETE',
            resource_path='/tokenization/templates/{contractTemplateId}',
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
    def deploy_contract(
        self,
        contract_template_id: Annotated[StrictStr, Field(description="The Contract Template identifier")],
        contract_deploy_request: ContractDeployRequest,
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
    ) -> Future[ApiResponse[ContractDeployResponse]]:
        """Deploy contract

        Deploy a new contract by contract template id. If you wish to deploy a token (ERC20, ERC721 etc), and create asset please use POST /tokenization

        :param contract_template_id: The Contract Template identifier (required)
        :type contract_template_id: str
        :param contract_deploy_request: (required)
        :type contract_deploy_request: ContractDeployRequest
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

        _param = self._deploy_contract_serialize(
            contract_template_id=contract_template_id,
            contract_deploy_request=contract_deploy_request,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '202': "ContractDeployResponse",
            '404': "HttpContractDoesNotExistError",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _deploy_contract_serialize(
        self,
        contract_template_id,
        contract_deploy_request,
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
        if contract_template_id is not None:
            _path_params['contractTemplateId'] = contract_template_id
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if contract_deploy_request is not None:
            _body_params = contract_deploy_request


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
            resource_path='/tokenization/templates/{contractTemplateId}/deploy',
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
    def get_constructor_by_contract_template_id(
        self,
        contract_template_id: Annotated[StrictStr, Field(description="The Contract Template identifier")],
        with_docs: Annotated[Optional[StrictBool], Field(description="true if you want to get the abi with its docs")] = None,
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
    ) -> Future[ApiResponse[AbiFunction]]:
        """Return contract template's constructor

        Return contract template's constructor ABI

        :param contract_template_id: The Contract Template identifier (required)
        :type contract_template_id: str
        :param with_docs: true if you want to get the abi with its docs
        :type with_docs: bool
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

        _param = self._get_constructor_by_contract_template_id_serialize(
            contract_template_id=contract_template_id,
            with_docs=with_docs,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AbiFunction",
            '404': "HttpContractDoesNotExistError",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _get_constructor_by_contract_template_id_serialize(
        self,
        contract_template_id,
        with_docs,
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
        if contract_template_id is not None:
            _path_params['contractTemplateId'] = contract_template_id
        # process the query parameters
        if with_docs is not None:
            
            _query_params.append(('withDocs', with_docs))
            
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
            resource_path='/tokenization/templates/{contractTemplateId}/constructor',
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
    def get_contract_template_by_id(
        self,
        contract_template_id: Annotated[StrictStr, Field(description="The Contract Template identifier")],
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
    ) -> Future[ApiResponse[ContractTemplateDto]]:
        """Return contract template by id

        Return detailed information about the contract template

        :param contract_template_id: The Contract Template identifier (required)
        :type contract_template_id: str
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

        _param = self._get_contract_template_by_id_serialize(
            contract_template_id=contract_template_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ContractTemplateDto",
            '404': "HttpContractDoesNotExistError",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _get_contract_template_by_id_serialize(
        self,
        contract_template_id,
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
        if contract_template_id is not None:
            _path_params['contractTemplateId'] = contract_template_id
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
            resource_path='/tokenization/templates/{contractTemplateId}',
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
    def get_contract_templates(
        self,
        limit: Annotated[Optional[Union[Annotated[float, Field(le=100, strict=True, ge=1)], Annotated[int, Field(le=100, strict=True, ge=1)]]], Field(description="Items per page (max 100)")] = None,
        offset: Annotated[Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]], Field(description="Paging offset")] = None,
        page_cursor: Annotated[Optional[StrictStr], Field(description="Page cursor to get the next page")] = None,
        page_size: Annotated[Optional[Union[Annotated[float, Field(le=100, strict=True, ge=1)], Annotated[int, Field(le=100, strict=True, ge=1)]]], Field(description="Number of items per page, requesting more then max will return max items")] = None,
        type: Annotated[Optional[StrictStr], Field(description="The type of the contract templates you wish to retrieve. Can accept one type, more or none")] = None,
        initialization_phase: Optional[StrictStr] = None,
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
    ) -> Future[ApiResponse[TemplatesPaginatedResponse]]:
        """List all contract templates

        Return minimal representation of all the contract templates available for the workspace

        :param limit: Items per page (max 100)
        :type limit: float
        :param offset: Paging offset
        :type offset: float
        :param page_cursor: Page cursor to get the next page
        :type page_cursor: str
        :param page_size: Number of items per page, requesting more then max will return max items
        :type page_size: float
        :param type: The type of the contract templates you wish to retrieve. Can accept one type, more or none
        :type type: str
        :param initialization_phase:
        :type initialization_phase: str
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

        _param = self._get_contract_templates_serialize(
            limit=limit,
            offset=offset,
            page_cursor=page_cursor,
            page_size=page_size,
            type=type,
            initialization_phase=initialization_phase,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "TemplatesPaginatedResponse",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _get_contract_templates_serialize(
        self,
        limit,
        offset,
        page_cursor,
        page_size,
        type,
        initialization_phase,
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
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if page_cursor is not None:
            
            _query_params.append(('pageCursor', page_cursor))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if type is not None:
            
            _query_params.append(('type', type))
            
        if initialization_phase is not None:
            
            _query_params.append(('initializationPhase', initialization_phase))
            
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
            resource_path='/tokenization/templates',
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
    def get_function_abi_by_contract_template_id(
        self,
        contract_template_id: Annotated[StrictStr, Field(description="The Contract Template identifier")],
        function_signature: StrictStr,
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
    ) -> Future[ApiResponse[AbiFunction]]:
        """Return contract template's function

        Return contract template`s function ABI by signature

        :param contract_template_id: The Contract Template identifier (required)
        :type contract_template_id: str
        :param function_signature: (required)
        :type function_signature: str
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

        _param = self._get_function_abi_by_contract_template_id_serialize(
            contract_template_id=contract_template_id,
            function_signature=function_signature,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "AbiFunction",
            '404': "HttpContractDoesNotExistError",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _get_function_abi_by_contract_template_id_serialize(
        self,
        contract_template_id,
        function_signature,
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
        if contract_template_id is not None:
            _path_params['contractTemplateId'] = contract_template_id
        # process the query parameters
        if function_signature is not None:
            
            _query_params.append(('functionSignature', function_signature))
            
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
            resource_path='/tokenization/templates/{contractTemplateId}/function',
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
    def upload_contract_template(
        self,
        contract_upload_request: ContractUploadRequest,
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
    ) -> Future[ApiResponse[ContractTemplateDto]]:
        """Upload contract template

        Upload a new contract template. This contract template will be available for the workspace

        :param contract_upload_request: (required)
        :type contract_upload_request: ContractUploadRequest
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

        _param = self._upload_contract_template_serialize(
            contract_upload_request=contract_upload_request,
            idempotency_key=idempotency_key,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "ContractTemplateDto",
            'default': "ErrorSchema",
        }

        return self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout,
            _response_types_map=_response_types_map,
        )

    def _upload_contract_template_serialize(
        self,
        contract_upload_request,
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
        # process the query parameters
        # process the header parameters
        if idempotency_key is not None:
            _header_params['Idempotency-Key'] = idempotency_key
        # process the form parameters
        # process the body parameter
        if contract_upload_request is not None:
            _body_params = contract_upload_request


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
            resource_path='/tokenization/templates',
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


