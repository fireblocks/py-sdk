# fireblocks_client.AssetsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_assets_bulk**](AssetsApi.md#create_assets_bulk) | **POST** /vault/assets/bulk | Bulk creation of wallets


# **create_assets_bulk**
> JobCreated create_assets_bulk(create_assets_bulk_request, idempotency_key=idempotency_key)

Bulk creation of wallets

Create multiple wallets for a given vault account by running an async job. </br> **Note**: - These endpoints are currently in beta and might be subject to changes. - We limit accounts to 10k per operation and 200k per customer during beta testing. - Currently, we are only supporting EVM wallets. 

### Example


```python
import fireblocks_client
from fireblocks_client.models.create_assets_bulk_request import CreateAssetsBulkRequest
from fireblocks_client.models.job_created import JobCreated
from fireblocks_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.fireblocks.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = fireblocks_client.Configuration(
    host = "https://api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with fireblocks_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fireblocks_client.AssetsApi(api_client)
    create_assets_bulk_request = fireblocks_client.CreateAssetsBulkRequest() # CreateAssetsBulkRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Bulk creation of wallets
        api_response = api_instance.create_assets_bulk(create_assets_bulk_request, idempotency_key=idempotency_key)
        print("The response of AssetsApi->create_assets_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->create_assets_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_assets_bulk_request** | [**CreateAssetsBulkRequest**](CreateAssetsBulkRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**JobCreated**](JobCreated.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JobCreated object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

