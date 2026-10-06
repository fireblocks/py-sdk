# fireblocks.TempoBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tempo_transfer**](TempoBetaApi.md#create_tempo_transfer) | **POST** /operations/tempo/transfer | Create a Tempo transfer transaction


# **create_tempo_transfer**
> CreateTempoTransferResponse create_tempo_transfer(create_tempo_transfer_request, idempotency_key=idempotency_key)

Create a Tempo transfer transaction

Creates a new Tempo transfer transaction.

### Example


```python
from fireblocks.models.create_tempo_transfer_request import CreateTempoTransferRequest
from fireblocks.models.create_tempo_transfer_response import CreateTempoTransferResponse
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
    create_tempo_transfer_request = fireblocks.CreateTempoTransferRequest() # CreateTempoTransferRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create a Tempo transfer transaction
        api_response = fireblocks.tempo_beta.create_tempo_transfer(create_tempo_transfer_request, idempotency_key=idempotency_key).result()
        print("The response of TempoBetaApi->create_tempo_transfer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TempoBetaApi->create_tempo_transfer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tempo_transfer_request** | [**CreateTempoTransferRequest**](CreateTempoTransferRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CreateTempoTransferResponse**](CreateTempoTransferResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction created. |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

