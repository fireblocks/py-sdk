# fireblocks.PaymentsPayoutApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payout**](PaymentsPayoutApi.md#create_payout) | **POST** /payments/payout | Create a payout instruction set
[**execute_payout_action**](PaymentsPayoutApi.md#execute_payout_action) | **POST** /payments/payout/{payoutId}/actions/execute | Execute a payout instruction set
[**get_payout**](PaymentsPayoutApi.md#get_payout) | **GET** /payments/payout/{payoutId} | Get the status of a payout instruction set


# **create_payout**
> PayoutResponse create_payout(idempotency_key=idempotency_key, create_payout_request=create_payout_request)

Create a payout instruction set

**Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoints include APIs available only for customers with Payments Engine enabled on their accounts. </br> </br>These endpoints are currently in beta and might be subject to changes.</br> </br>If you want to learn more about Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or email CSM@fireblocks.com. </br> </br> <b u>Create a payout instruction set.</b> </u></br> A payout instruction set is a set of instructions for distributing payments from a single payment account to a list of payee accounts. </br> The instruction set defines: </br> <ul> <li>the payment account and its account type (vault, exchange, or fiat). </li> <li>the account type (vault account, exchange account, whitelisted address, network connection, fiat account, or merchant account), the amount, and the asset of payment for each payee account.</li> </ul> 

### Example


```python
from fireblocks.models.create_payout_request import CreatePayoutRequest
from fireblocks.models.payout_response import PayoutResponse
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
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)
    create_payout_request = {"paymentAccount":{"id":"EX_SUB1","type":"EXCHANGE_ACCOUNT"},"instructionSet":[{"payeeAccount":{"id":"bef85a1c-b605-4b2e-bdb5-2d400f4d0bf3","type":"EXTERNAL_WALLET"},"amount":{"amount":"43","assetId":"USDC"}},{"payeeAccount":{"id":"3adc1f92-e791-44a8-9aee-7f31c2108b78","type":"NETWORK_CONNECTION"},"amount":{"amount":"4423","assetId":"USDC"}}]} # CreatePayoutRequest |  (optional)

    try:
        # Create a payout instruction set
        api_response = fireblocks.payments_payout.create_payout(idempotency_key=idempotency_key, create_payout_request=create_payout_request).result()
        print("The response of PaymentsPayoutApi->create_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsPayoutApi->create_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 
 **create_payout_request** | [**CreatePayoutRequest**](CreatePayoutRequest.md)|  | [optional] 

### Return type

[**PayoutResponse**](PayoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The payout instruction set creation succeeded and returns the generated instruction set with a unique payout IDThe payout ID will be used for executing the payout and checking the payout status. |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_payout_action**
> DispatchPayoutResponse execute_payout_action(payout_id, idempotency_key=idempotency_key)

Execute a payout instruction set

**Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoints include APIs available only for customers with Payments Engine enabled on their accounts. </br> </br>These endpoints are currently in beta and might be subject to changes.</br> </br>If you want to learn more about Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or email CSM@fireblocks.com. </br> </br><b u>Execute a payout instruction set.</b> </u> </br> </br>The instruction set will be verified and executed.</br> <b><u>Source locking</br></b> </u> If you are executing a payout instruction set from a payment account with an already active payout the active payout will complete before the new payout instruction set can be executed. </br> You cannot execute the same payout instruction set more than once. 

### Example


```python
from fireblocks.models.dispatch_payout_response import DispatchPayoutResponse
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
    payout_id = '1fe3b61f-7e1f-4a19-aff0-4f0a524d44d7' # str | the payout id received from the creation of the payout instruction set
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Execute a payout instruction set
        api_response = fireblocks.payments_payout.execute_payout_action(payout_id, idempotency_key=idempotency_key).result()
        print("The response of PaymentsPayoutApi->execute_payout_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsPayoutApi->execute_payout_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| the payout id received from the creation of the payout instruction set | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**DispatchPayoutResponse**](DispatchPayoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Executed the payout instruction set |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout**
> PayoutResponse get_payout(payout_id)

Get the status of a payout instruction set

**Note:** The reference content in this section documents the Payments Engine endpoint. The Payments Engine endpoints include APIs available only for customers with Payments Engine enabled on their accounts. </br> </br>These endpoints are currently in beta and might be subject to changes.</br> </br>If you want to learn more about Fireblocks Payments Engine, please contact your Fireblocks Customer Success Manager or email CSM@fireblocks.com. </br> 

### Example


```python
from fireblocks.models.payout_response import PayoutResponse
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
    payout_id = '1fe3b61f-7e1f-4a19-aff0-4f0a524d44d7' # str | the payout id received from the creation of the payout instruction set

    try:
        # Get the status of a payout instruction set
        api_response = fireblocks.payments_payout.get_payout(payout_id).result()
        print("The response of PaymentsPayoutApi->get_payout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsPayoutApi->get_payout: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| the payout id received from the creation of the payout instruction set | 

### Return type

[**PayoutResponse**](PayoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the current status of the payout instruction set, including the status of each payout instruction and the transactions created in the process. |  -  |
**401** | Unauthorized. Missing / invalid JWT token in Authorization header. |  -  |
**404** | No payout with the given payout ID exists. |  -  |
**5XX** | Internal error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

