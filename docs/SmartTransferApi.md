# fireblocks.SmartTransferApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_dv_p_ticket_term**](SmartTransferApi.md#approve_dv_p_ticket_term) | **PUT** /smart_transfers/{ticketId}/terms/{termId}/dvp/approve | Define funding source and give approve to contract to transfer asset
[**cancel_ticket**](SmartTransferApi.md#cancel_ticket) | **PUT** /smart-transfers/{ticketId}/cancel | Cancel Ticket
[**create_ticket**](SmartTransferApi.md#create_ticket) | **POST** /smart-transfers | Create Ticket
[**create_ticket_term**](SmartTransferApi.md#create_ticket_term) | **POST** /smart-transfers/{ticketId}/terms | Create leg (term)
[**find_ticket_by_id**](SmartTransferApi.md#find_ticket_by_id) | **GET** /smart-transfers/{ticketId} | Search Tickets by ID
[**find_ticket_term_by_id**](SmartTransferApi.md#find_ticket_term_by_id) | **GET** /smart-transfers/{ticketId}/terms/{termId} | Search ticket by leg (term) ID
[**fulfill_ticket**](SmartTransferApi.md#fulfill_ticket) | **PUT** /smart-transfers/{ticketId}/fulfill | Fund ticket manually
[**fund_dvp_ticket**](SmartTransferApi.md#fund_dvp_ticket) | **PUT** /smart_transfers/{ticketId}/dvp/fund | Fund dvp ticket
[**fund_ticket_term**](SmartTransferApi.md#fund_ticket_term) | **PUT** /smart-transfers/{ticketId}/terms/{termId}/fund | Define funding source
[**get_smart_transfer_statistic**](SmartTransferApi.md#get_smart_transfer_statistic) | **GET** /smart_transfers/statistic | Get smart transfers statistic
[**get_smart_transfer_user_groups**](SmartTransferApi.md#get_smart_transfer_user_groups) | **GET** /smart-transfers/settings/user-groups | Get user group
[**manually_fund_ticket_term**](SmartTransferApi.md#manually_fund_ticket_term) | **PUT** /smart-transfers/{ticketId}/terms/{termId}/manually-fund | Manually add term transaction
[**remove_ticket_term**](SmartTransferApi.md#remove_ticket_term) | **DELETE** /smart-transfers/{ticketId}/terms/{termId} | Delete ticket leg (term)
[**search_tickets**](SmartTransferApi.md#search_tickets) | **GET** /smart-transfers | Find Ticket
[**set_external_ref_id**](SmartTransferApi.md#set_external_ref_id) | **PUT** /smart-transfers/{ticketId}/external-id | Add external ref. ID
[**set_ticket_expiration**](SmartTransferApi.md#set_ticket_expiration) | **PUT** /smart-transfers/{ticketId}/expires-in | Set expiration
[**set_user_groups**](SmartTransferApi.md#set_user_groups) | **POST** /smart-transfers/settings/user-groups | Set user group
[**submit_ticket**](SmartTransferApi.md#submit_ticket) | **PUT** /smart-transfers/{ticketId}/submit | Submit ticket
[**update_ticket_term**](SmartTransferApi.md#update_ticket_term) | **PUT** /smart-transfers/{ticketId}/terms/{termId} | Update ticket leg (term)


# **approve_dv_p_ticket_term**
> SmartTransferTicketTermResponse approve_dv_p_ticket_term(ticket_id, term_id, smart_transfer_approve_term, idempotency_key=idempotency_key)

Define funding source and give approve to contract to transfer asset

Set funding source for ticket term and creating approving transaction for contract to transfer asset

### Example


```python
from fireblocks.models.smart_transfer_approve_term import SmartTransferApproveTerm
from fireblocks.models.smart_transfer_ticket_term_response import SmartTransferTicketTermResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    term_id = 'term_id_example' # str | 
    smart_transfer_approve_term = fireblocks.SmartTransferApproveTerm() # SmartTransferApproveTerm | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Define funding source and give approve to contract to transfer asset
        api_response = fireblocks.smart_transfer.approve_dv_p_ticket_term(ticket_id, term_id, smart_transfer_approve_term, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->approve_dv_p_ticket_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->approve_dv_p_ticket_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **term_id** | **str**|  | 
 **smart_transfer_approve_term** | [**SmartTransferApproveTerm**](SmartTransferApproveTerm.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketTermResponse**](SmartTransferTicketTermResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creating approval transaction started |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_ticket**
> SmartTransferTicketResponse cancel_ticket(ticket_id, idempotency_key=idempotency_key)

Cancel Ticket

Cancel Smart Transfer ticket

### Example


```python
from fireblocks.models.smart_transfer_ticket_response import SmartTransferTicketResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Cancel Ticket
        api_response = fireblocks.smart_transfer.cancel_ticket(ticket_id, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->cancel_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->cancel_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketResponse**](SmartTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Smart Transfer ticket successfully canceled |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ticket**
> SmartTransferTicketResponse create_ticket(smart_transfer_create_ticket, idempotency_key=idempotency_key)

Create Ticket

Creates new Smart Transfer ticket

### Example


```python
from fireblocks.models.smart_transfer_create_ticket import SmartTransferCreateTicket
from fireblocks.models.smart_transfer_ticket_response import SmartTransferTicketResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    smart_transfer_create_ticket = fireblocks.SmartTransferCreateTicket() # SmartTransferCreateTicket | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create Ticket
        api_response = fireblocks.smart_transfer.create_ticket(smart_transfer_create_ticket, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->create_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->create_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_transfer_create_ticket** | [**SmartTransferCreateTicket**](SmartTransferCreateTicket.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketResponse**](SmartTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Smart Transfer ticket was created successfully |  -  |
**403** | Unauthorized |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ticket_term**
> SmartTransferTicketTermResponse create_ticket_term(ticket_id, smart_transfer_create_ticket_term, idempotency_key=idempotency_key)

Create leg (term)

Creates new smart transfer ticket term (when the ticket status is DRAFT)

### Example


```python
from fireblocks.models.smart_transfer_create_ticket_term import SmartTransferCreateTicketTerm
from fireblocks.models.smart_transfer_ticket_term_response import SmartTransferTicketTermResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    smart_transfer_create_ticket_term = fireblocks.SmartTransferCreateTicketTerm() # SmartTransferCreateTicketTerm | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create leg (term)
        api_response = fireblocks.smart_transfer.create_ticket_term(ticket_id, smart_transfer_create_ticket_term, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->create_ticket_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->create_ticket_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **smart_transfer_create_ticket_term** | [**SmartTransferCreateTicketTerm**](SmartTransferCreateTicketTerm.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketTermResponse**](SmartTransferTicketTermResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Smart Transfer ticket term was created successfully |  -  |
**403** | Unauthorized |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ticket_by_id**
> SmartTransferTicketResponse find_ticket_by_id(ticket_id)

Search Tickets by ID

Find Smart Transfer ticket by id

### Example


```python
from fireblocks.models.smart_transfer_ticket_response import SmartTransferTicketResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 

    try:
        # Search Tickets by ID
        api_response = fireblocks.smart_transfer.find_ticket_by_id(ticket_id).result()
        print("The response of SmartTransferApi->find_ticket_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->find_ticket_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 

### Return type

[**SmartTransferTicketResponse**](SmartTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Smart Transfer ticket returned successfully |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ticket_term_by_id**
> SmartTransferTicketTermResponse find_ticket_term_by_id(ticket_id, term_id)

Search ticket by leg (term) ID

Find Smart Transfer ticket term by id

### Example


```python
from fireblocks.models.smart_transfer_ticket_term_response import SmartTransferTicketTermResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    term_id = 'term_id_example' # str | 

    try:
        # Search ticket by leg (term) ID
        api_response = fireblocks.smart_transfer.find_ticket_term_by_id(ticket_id, term_id).result()
        print("The response of SmartTransferApi->find_ticket_term_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->find_ticket_term_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **term_id** | **str**|  | 

### Return type

[**SmartTransferTicketTermResponse**](SmartTransferTicketTermResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Smart Transfer ticket term returned successfully |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fulfill_ticket**
> SmartTransferTicketResponse fulfill_ticket(ticket_id, idempotency_key=idempotency_key)

Fund ticket manually

Manually fulfill ticket, in case when all terms (legs) are funded manually

### Example


```python
from fireblocks.models.smart_transfer_ticket_response import SmartTransferTicketResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Fund ticket manually
        api_response = fireblocks.smart_transfer.fulfill_ticket(ticket_id, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->fulfill_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->fulfill_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketResponse**](SmartTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fulfilled on Smart Transfer ticket |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fund_dvp_ticket**
> SmartTransferTicketResponse fund_dvp_ticket(ticket_id, smart_transfer_fund_dvp_ticket, idempotency_key=idempotency_key)

Fund dvp ticket

Create or fulfill dvp ticket order

### Example


```python
from fireblocks.models.smart_transfer_fund_dvp_ticket import SmartTransferFundDvpTicket
from fireblocks.models.smart_transfer_ticket_response import SmartTransferTicketResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    smart_transfer_fund_dvp_ticket = fireblocks.SmartTransferFundDvpTicket() # SmartTransferFundDvpTicket | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Fund dvp ticket
        api_response = fireblocks.smart_transfer.fund_dvp_ticket(ticket_id, smart_transfer_fund_dvp_ticket, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->fund_dvp_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->fund_dvp_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **smart_transfer_fund_dvp_ticket** | [**SmartTransferFundDvpTicket**](SmartTransferFundDvpTicket.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketResponse**](SmartTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully started creating or fulfilling order on dvp Smart Transfer ticket |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fund_ticket_term**
> SmartTransferTicketTermResponse fund_ticket_term(ticket_id, term_id, smart_transfer_fund_term, idempotency_key=idempotency_key)

Define funding source

Set funding source for ticket term (in case of ASYNC tickets, this will execute transfer immediately)

### Example


```python
from fireblocks.models.smart_transfer_fund_term import SmartTransferFundTerm
from fireblocks.models.smart_transfer_ticket_term_response import SmartTransferTicketTermResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    term_id = 'term_id_example' # str | 
    smart_transfer_fund_term = fireblocks.SmartTransferFundTerm() # SmartTransferFundTerm | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Define funding source
        api_response = fireblocks.smart_transfer.fund_ticket_term(ticket_id, term_id, smart_transfer_fund_term, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->fund_ticket_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->fund_ticket_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **term_id** | **str**|  | 
 **smart_transfer_fund_term** | [**SmartTransferFundTerm**](SmartTransferFundTerm.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketTermResponse**](SmartTransferTicketTermResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Funding source for ticket term successfully done |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smart_transfer_statistic**
> SmartTransferStatistic get_smart_transfer_statistic()

Get smart transfers statistic

Get smart transfer statistic

### Example


```python
from fireblocks.models.smart_transfer_statistic import SmartTransferStatistic
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:

    try:
        # Get smart transfers statistic
        api_response = fireblocks.smart_transfer.get_smart_transfer_statistic().result()
        print("The response of SmartTransferApi->get_smart_transfer_statistic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->get_smart_transfer_statistic: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SmartTransferStatistic**](SmartTransferStatistic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Smart Transfer ticket statistic returned successfully |  -  |
**403** | Unauthorized |  -  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smart_transfer_user_groups**
> SmartTransferUserGroupsResponse get_smart_transfer_user_groups()

Get user group

Get Smart Transfer user groups

### Example


```python
from fireblocks.models.smart_transfer_user_groups_response import SmartTransferUserGroupsResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:

    try:
        # Get user group
        api_response = fireblocks.smart_transfer.get_smart_transfer_user_groups().result()
        print("The response of SmartTransferApi->get_smart_transfer_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->get_smart_transfer_user_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SmartTransferUserGroupsResponse**](SmartTransferUserGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group settings were returned successfully |  -  |
**403** | Unauthorized |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **manually_fund_ticket_term**
> SmartTransferTicketTermResponse manually_fund_ticket_term(ticket_id, term_id, smart_transfer_manually_fund_term, idempotency_key=idempotency_key)

Manually add term transaction

Manually set ticket term transaction

### Example


```python
from fireblocks.models.smart_transfer_manually_fund_term import SmartTransferManuallyFundTerm
from fireblocks.models.smart_transfer_ticket_term_response import SmartTransferTicketTermResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    term_id = 'term_id_example' # str | 
    smart_transfer_manually_fund_term = fireblocks.SmartTransferManuallyFundTerm() # SmartTransferManuallyFundTerm | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Manually add term transaction
        api_response = fireblocks.smart_transfer.manually_fund_ticket_term(ticket_id, term_id, smart_transfer_manually_fund_term, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->manually_fund_ticket_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->manually_fund_ticket_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **term_id** | **str**|  | 
 **smart_transfer_manually_fund_term** | [**SmartTransferManuallyFundTerm**](SmartTransferManuallyFundTerm.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketTermResponse**](SmartTransferTicketTermResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully manually set ticket term transaction |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_ticket_term**
> remove_ticket_term(ticket_id, term_id)

Delete ticket leg (term)

Delete ticket term when ticket is in DRAFT status

### Example


```python
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    term_id = 'term_id_example' # str | 

    try:
        # Delete ticket leg (term)
        fireblocks.smart_transfer.remove_ticket_term(ticket_id, term_id).result()
    except Exception as e:
        print("Exception when calling SmartTransferApi->remove_ticket_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **term_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Smart Transfer ticket term successfully removed |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tickets**
> SmartTransferTicketFilteredResponse search_tickets(q=q, statuses=statuses, network_id=network_id, created_by_me=created_by_me, expires_after=expires_after, expires_before=expires_before, type=type, external_ref_id=external_ref_id, after=after, limit=limit)

Find Ticket

Finds Smart Transfer tickets that match the submitted criteria

### Example


```python
from fireblocks.models.smart_transfer_ticket_filtered_response import SmartTransferTicketFilteredResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    q = 'q_example' # str | Search string - counterparty name or asset or ticketId. Optional (optional)
    statuses = [] # List[str] | Ticket statuses for Smart Transfer tickets. Optional (optional) (default to [])
    network_id = 'network_id_example' # str | NetworkId that is used in the ticket . Optional (optional)
    created_by_me = True # bool | Filter created tickets by created by self or by others. Optional (optional)
    expires_after = '2013-10-20T19:20:30+01:00' # datetime | Lower bound of search range. Optional (optional)
    expires_before = '2013-10-20T19:20:30+01:00' # datetime | Upper bound of search range. Optional (optional)
    type = 'type_example' # str | Type of transfer. ASYNC executes transfers as they are funded, DVP executes all terms (legs) as one dvp transfer (optional)
    external_ref_id = 'external_ref_id_example' # str | External ref. ID that workspace can use to identify ticket outside of Fireblocks system. (optional)
    after = 'after_example' # str | ID of the record after which to fetch $limit records (optional)
    limit = 3.4 # float | Number of records to fetch. By default, it is 100 (optional)

    try:
        # Find Ticket
        api_response = fireblocks.smart_transfer.search_tickets(q=q, statuses=statuses, network_id=network_id, created_by_me=created_by_me, expires_after=expires_after, expires_before=expires_before, type=type, external_ref_id=external_ref_id, after=after, limit=limit).result()
        print("The response of SmartTransferApi->search_tickets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->search_tickets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search string - counterparty name or asset or ticketId. Optional | [optional] 
 **statuses** | [**List[str]**](str.md)| Ticket statuses for Smart Transfer tickets. Optional | [optional] [default to []]
 **network_id** | **str**| NetworkId that is used in the ticket . Optional | [optional] 
 **created_by_me** | **bool**| Filter created tickets by created by self or by others. Optional | [optional] 
 **expires_after** | **datetime**| Lower bound of search range. Optional | [optional] 
 **expires_before** | **datetime**| Upper bound of search range. Optional | [optional] 
 **type** | **str**| Type of transfer. ASYNC executes transfers as they are funded, DVP executes all terms (legs) as one dvp transfer | [optional] 
 **external_ref_id** | **str**| External ref. ID that workspace can use to identify ticket outside of Fireblocks system. | [optional] 
 **after** | **str**| ID of the record after which to fetch $limit records | [optional] 
 **limit** | **float**| Number of records to fetch. By default, it is 100 | [optional] 

### Return type

[**SmartTransferTicketFilteredResponse**](SmartTransferTicketFilteredResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Smart Transfer tickets were returned successfully |  -  |
**403** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_external_ref_id**
> SmartTransferTicketResponse set_external_ref_id(ticket_id, smart_transfer_set_ticket_external_id, idempotency_key=idempotency_key)

Add external ref. ID

Set external id Smart Transfer ticket

### Example


```python
from fireblocks.models.smart_transfer_set_ticket_external_id import SmartTransferSetTicketExternalId
from fireblocks.models.smart_transfer_ticket_response import SmartTransferTicketResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    smart_transfer_set_ticket_external_id = fireblocks.SmartTransferSetTicketExternalId() # SmartTransferSetTicketExternalId | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Add external ref. ID
        api_response = fireblocks.smart_transfer.set_external_ref_id(ticket_id, smart_transfer_set_ticket_external_id, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->set_external_ref_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->set_external_ref_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **smart_transfer_set_ticket_external_id** | [**SmartTransferSetTicketExternalId**](SmartTransferSetTicketExternalId.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketResponse**](SmartTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully set external id on Smart Transfer ticket |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ticket_expiration**
> SmartTransferTicketResponse set_ticket_expiration(ticket_id, smart_transfer_set_ticket_expiration, idempotency_key=idempotency_key)

Set expiration

Set expiration date on Smart Transfer ticket

### Example


```python
from fireblocks.models.smart_transfer_set_ticket_expiration import SmartTransferSetTicketExpiration
from fireblocks.models.smart_transfer_ticket_response import SmartTransferTicketResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    smart_transfer_set_ticket_expiration = fireblocks.SmartTransferSetTicketExpiration() # SmartTransferSetTicketExpiration | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set expiration
        api_response = fireblocks.smart_transfer.set_ticket_expiration(ticket_id, smart_transfer_set_ticket_expiration, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->set_ticket_expiration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->set_ticket_expiration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **smart_transfer_set_ticket_expiration** | [**SmartTransferSetTicketExpiration**](SmartTransferSetTicketExpiration.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketResponse**](SmartTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully set expiration date on Smart Transfer ticket |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_groups**
> SmartTransferUserGroupsResponse set_user_groups(smart_transfer_set_user_groups, idempotency_key=idempotency_key)

Set user group

Set Smart Transfer user group

### Example


```python
from fireblocks.models.smart_transfer_set_user_groups import SmartTransferSetUserGroups
from fireblocks.models.smart_transfer_user_groups_response import SmartTransferUserGroupsResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    smart_transfer_set_user_groups = fireblocks.SmartTransferSetUserGroups() # SmartTransferSetUserGroups | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Set user group
        api_response = fireblocks.smart_transfer.set_user_groups(smart_transfer_set_user_groups, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->set_user_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->set_user_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smart_transfer_set_user_groups** | [**SmartTransferSetUserGroups**](SmartTransferSetUserGroups.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferUserGroupsResponse**](SmartTransferUserGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User group settings were set successfully |  -  |
**403** | Unauthorized |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_ticket**
> SmartTransferTicketResponse submit_ticket(ticket_id, smart_transfer_submit_ticket, idempotency_key=idempotency_key)

Submit ticket

Submit Smart Transfer ticket - change status into ready for approval if auto approval is not turned on, or OPEN if auto approval is on

### Example


```python
from fireblocks.models.smart_transfer_submit_ticket import SmartTransferSubmitTicket
from fireblocks.models.smart_transfer_ticket_response import SmartTransferTicketResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    smart_transfer_submit_ticket = fireblocks.SmartTransferSubmitTicket() # SmartTransferSubmitTicket | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Submit ticket
        api_response = fireblocks.smart_transfer.submit_ticket(ticket_id, smart_transfer_submit_ticket, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->submit_ticket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->submit_ticket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **smart_transfer_submit_ticket** | [**SmartTransferSubmitTicket**](SmartTransferSubmitTicket.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketResponse**](SmartTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully submitted Smart Transfer ticket |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |
**422** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ticket_term**
> SmartTransferTicketTermResponse update_ticket_term(ticket_id, term_id, smart_transfer_update_ticket_term, idempotency_key=idempotency_key)

Update ticket leg (term)

Update ticket term (when ticket status is DRAFT)

### Example


```python
from fireblocks.models.smart_transfer_ticket_term_response import SmartTransferTicketTermResponse
from fireblocks.models.smart_transfer_update_ticket_term import SmartTransferUpdateTicketTerm
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    ticket_id = 'ticket_id_example' # str | 
    term_id = 'term_id_example' # str | 
    smart_transfer_update_ticket_term = fireblocks.SmartTransferUpdateTicketTerm() # SmartTransferUpdateTicketTerm | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Update ticket leg (term)
        api_response = fireblocks.smart_transfer.update_ticket_term(ticket_id, term_id, smart_transfer_update_ticket_term, idempotency_key=idempotency_key).result()
        print("The response of SmartTransferApi->update_ticket_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartTransferApi->update_ticket_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_id** | **str**|  | 
 **term_id** | **str**|  | 
 **smart_transfer_update_ticket_term** | [**SmartTransferUpdateTicketTerm**](SmartTransferUpdateTicketTerm.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**SmartTransferTicketTermResponse**](SmartTransferTicketTermResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Smart Transfer ticket term updated successfully |  -  |
**403** | Unauthorized |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

