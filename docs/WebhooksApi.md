# fireblocks.WebhooksApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resend_transaction_webhooks**](WebhooksApi.md#resend_transaction_webhooks) | **POST** /webhooks/resend/{txId} | Resend failed webhooks for a transaction by ID
[**resend_webhooks**](WebhooksApi.md#resend_webhooks) | **POST** /webhooks/resend | Resend failed webhooks


# **resend_transaction_webhooks**
> ResendWebhooksByTransactionIdResponse resend_transaction_webhooks(tx_id, resend_transaction_webhooks_request, idempotency_key=idempotency_key)

Resend failed webhooks for a transaction by ID

Resends failed webhook notifications for a transaction by ID.

### Example


```python
from fireblocks.models.resend_transaction_webhooks_request import ResendTransactionWebhooksRequest
from fireblocks.models.resend_webhooks_by_transaction_id_response import ResendWebhooksByTransactionIdResponse
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
    tx_id = 'tx_id_example' # str | The ID of the transaction for webhooks
    resend_transaction_webhooks_request = fireblocks.ResendTransactionWebhooksRequest() # ResendTransactionWebhooksRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Resend failed webhooks for a transaction by ID
        api_response = fireblocks.webhooks.resend_transaction_webhooks(tx_id, resend_transaction_webhooks_request, idempotency_key=idempotency_key).result()
        print("The response of WebhooksApi->resend_transaction_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->resend_transaction_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| The ID of the transaction for webhooks | 
 **resend_transaction_webhooks_request** | [**ResendTransactionWebhooksRequest**](ResendTransactionWebhooksRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ResendWebhooksByTransactionIdResponse**](ResendWebhooksByTransactionIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_webhooks**
> ResendWebhooksResponse resend_webhooks(idempotency_key=idempotency_key)

Resend failed webhooks

Resends all failed webhook notifications.

### Example


```python
from fireblocks.models.resend_webhooks_response import ResendWebhooksResponse
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

    try:
        # Resend failed webhooks
        api_response = fireblocks.webhooks.resend_webhooks(idempotency_key=idempotency_key).result()
        print("The response of WebhooksApi->resend_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->resend_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ResendWebhooksResponse**](ResendWebhooksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

