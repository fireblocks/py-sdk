# fireblocks_client.WebhooksApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resend_webhooks**](WebhooksApi.md#resend_webhooks) | **POST** /webhooks/resend | Resend failed webhooks
[**resend_webhooks_for_transaction**](WebhooksApi.md#resend_webhooks_for_transaction) | **POST** /webhooks/resend/{txId} | Resend failed webhooks for a transaction by ID


# **resend_webhooks**
> ResendWebhooksResponse resend_webhooks()

Resend failed webhooks

Resends all failed webhook notifications.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.WebhooksApi(api_client)

    try:
        # Resend failed webhooks
        api_response = api_instance.resend_webhooks()
        print("The response of WebhooksApi->resend_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->resend_webhooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResendWebhooksResponse**](ResendWebhooksResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_webhooks_for_transaction**
> resend_webhooks_for_transaction(tx_id, resend_webhooks_for_transaction_request)

Resend failed webhooks for a transaction by ID

Resends failed webhook notifications for a transaction by ID.

### Example

```python
from __future__ import print_function
import time
import os
import fireblocks_client
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
    api_instance = fireblocks_client.WebhooksApi(api_client)
    tx_id = 'tx_id_example' # str | The ID of the transaction for webhooks
    resend_webhooks_for_transaction_request = fireblocks_client.ResendWebhooksForTransactionRequest() # ResendWebhooksForTransactionRequest | 

    try:
        # Resend failed webhooks for a transaction by ID
        api_instance.resend_webhooks_for_transaction(tx_id, resend_webhooks_for_transaction_request)
    except Exception as e:
        print("Exception when calling WebhooksApi->resend_webhooks_for_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tx_id** | **str**| The ID of the transaction for webhooks | 
 **resend_webhooks_for_transaction_request** | [**ResendWebhooksForTransactionRequest**](ResendWebhooksForTransactionRequest.md)|  | 

### Return type

void (empty response body)

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

