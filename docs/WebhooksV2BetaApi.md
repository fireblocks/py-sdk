# fireblocks.WebhooksV2BetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksV2BetaApi.md#create_webhook) | **POST** /webhooks | Create new webhook
[**delete_webhook**](WebhooksV2BetaApi.md#delete_webhook) | **DELETE** /webhooks/{webhookId} | Delete webhook
[**get_notification**](WebhooksV2BetaApi.md#get_notification) | **GET** /webhooks/{webhookId}/notifications/{notificationId} | Get notification by id
[**get_notifications**](WebhooksV2BetaApi.md#get_notifications) | **GET** /webhooks/{webhookId}/notifications | Get all notifications by webhook id
[**get_webhook**](WebhooksV2BetaApi.md#get_webhook) | **GET** /webhooks/{webhookId} | Get webhook by id
[**get_webhooks**](WebhooksV2BetaApi.md#get_webhooks) | **GET** /webhooks | Get all webhooks
[**resend_notification_by_id**](WebhooksV2BetaApi.md#resend_notification_by_id) | **POST** /webhooks/{webhookId}/notifications/{notificationId}/resend | Resend notification by id
[**update_webhook**](WebhooksV2BetaApi.md#update_webhook) | **PATCH** /webhooks/{webhookId} | Update webhook


# **create_webhook**
> Webhook create_webhook(create_webhook_request, idempotency_key=idempotency_key)

Create new webhook

Creates a new webhook, which will be triggered on the specified events **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks.models.create_webhook_request import CreateWebhookRequest
from fireblocks.models.webhook import Webhook
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
    create_webhook_request = fireblocks.CreateWebhookRequest() # CreateWebhookRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Create new webhook
        api_response = fireblocks.webhooks_v2_beta.create_webhook(create_webhook_request, idempotency_key=idempotency_key).result()
        print("The response of WebhooksV2BetaApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2BetaApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created new webhook successfully |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> Webhook delete_webhook(webhook_id)

Delete webhook

Delete a webhook by its id **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks.models.webhook import Webhook
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
    webhook_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the webhook

    try:
        # Delete webhook
        api_response = fireblocks.webhooks_v2_beta.delete_webhook(webhook_id).result()
        print("The response of WebhooksV2BetaApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2BetaApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The unique identifier of the webhook | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted webhook object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification**
> NotificationWithData get_notification(webhook_id, notification_id, include_data=include_data)

Get notification by id

Get notification by id **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks.models.notification_with_data import NotificationWithData
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
    webhook_id = 'webhook_id_example' # str | The ID of the webhook to fetch
    notification_id = 'notification_id_example' # str | The ID of the notification to fetch
    include_data = True # bool | Include the data of the notification (optional)

    try:
        # Get notification by id
        api_response = fireblocks.webhooks_v2_beta.get_notification(webhook_id, notification_id, include_data=include_data).result()
        print("The response of WebhooksV2BetaApi->get_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2BetaApi->get_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The ID of the webhook to fetch | 
 **notification_id** | **str**| The ID of the notification to fetch | 
 **include_data** | **bool**| Include the data of the notification | [optional] 

### Return type

[**NotificationWithData**](NotificationWithData.md)

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

# **get_notifications**
> NotificationPaginatedResponse get_notifications(webhook_id, order=order, page_cursor=page_cursor, page_size=page_size, created_start_date=created_start_date, created_end_date=created_end_date, statuses=statuses, event_types=event_types, resource_id=resource_id)

Get all notifications by webhook id

Get all notifications by webhook id (paginated) **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks.models.notification_paginated_response import NotificationPaginatedResponse
from fireblocks.models.notification_status import NotificationStatus
from fireblocks.models.webhook_event import WebhookEvent
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
    webhook_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | 
    order = 'DESC' # str | ASC / DESC ordering (default DESC) (optional) (default to 'DESC')
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 100 # float | Maximum number of items in the page (optional) (default to 100)
    created_start_date = '2024-09-24T09:14:38.356Z' # str | sort by start date (optional)
    created_end_date = '2024-09-24T09:14:38.356Z' # str | sort by end date (optional)
    statuses = [fireblocks.NotificationStatus()] # List[NotificationStatus] | Filter by Notification statues (optional)
    event_types = [fireblocks.WebhookEvent()] # List[WebhookEvent] | Filter by Notification eventTypes (optional)
    resource_id = 'resource_id_example' # str | Filter by resourceId (optional)

    try:
        # Get all notifications by webhook id
        api_response = fireblocks.webhooks_v2_beta.get_notifications(webhook_id, order=order, page_cursor=page_cursor, page_size=page_size, created_start_date=created_start_date, created_end_date=created_end_date, statuses=statuses, event_types=event_types, resource_id=resource_id).result()
        print("The response of WebhooksV2BetaApi->get_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2BetaApi->get_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to &#39;DESC&#39;]
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **float**| Maximum number of items in the page | [optional] [default to 100]
 **created_start_date** | **str**| sort by start date | [optional] 
 **created_end_date** | **str**| sort by end date | [optional] 
 **statuses** | [**List[NotificationStatus]**](NotificationStatus.md)| Filter by Notification statues | [optional] 
 **event_types** | [**List[WebhookEvent]**](WebhookEvent.md)| Filter by Notification eventTypes | [optional] 
 **resource_id** | **str**| Filter by resourceId | [optional] 

### Return type

[**NotificationPaginatedResponse**](NotificationPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated response containing NotificationExternalDTO objects |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> Webhook get_webhook(webhook_id)

Get webhook by id

Retrieve a webhook by its id **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks.models.webhook import Webhook
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
    webhook_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the webhook

    try:
        # Get webhook by id
        api_response = fireblocks.webhooks_v2_beta.get_webhook(webhook_id).result()
        print("The response of WebhooksV2BetaApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2BetaApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The unique identifier of the webhook | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A webhook object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> WebhookPaginatedResponse get_webhooks(order=order, page_cursor=page_cursor, page_size=page_size)

Get all webhooks

Get all webhooks (paginated) **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks.models.webhook_paginated_response import WebhookPaginatedResponse
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
    order = 'DESC' # str | ASC / DESC ordering (default DESC) (optional) (default to 'DESC')
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 10 # float | Maximum number of items in the page (optional) (default to 10)

    try:
        # Get all webhooks
        api_response = fireblocks.webhooks_v2_beta.get_webhooks(order=order, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of WebhooksV2BetaApi->get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2BetaApi->get_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to &#39;DESC&#39;]
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **float**| Maximum number of items in the page | [optional] [default to 10]

### Return type

[**WebhookPaginatedResponse**](WebhookPaginatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated response containing WebhookDto objects |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_notification_by_id**
> resend_notification_by_id(webhook_id, notification_id, idempotency_key=idempotency_key)

Resend notification by id

Resend notification by ID **Note:** These endpoints are currently in beta and might be subject to changes. 

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
    webhook_id = 'webhook_id_example' # str | The ID of the webhook
    notification_id = 'notification_id_example' # str | The ID of the notification
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Resend notification by id
        fireblocks.webhooks_v2_beta.resend_notification_by_id(webhook_id, notification_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling WebhooksV2BetaApi->resend_notification_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The ID of the webhook | 
 **notification_id** | **str**| The ID of the notification | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

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
**202** | Resend notification request was accepted and is being processed |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> Webhook update_webhook(webhook_id, update_webhook_request)

Update webhook

Update a webhook by its id **Note:** These endpoints are currently in beta and might be subject to changes. 

### Example


```python
from fireblocks.models.update_webhook_request import UpdateWebhookRequest
from fireblocks.models.webhook import Webhook
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
    webhook_id = '44fcead0-7053-4831-a53a-df7fb90d440f' # str | The unique identifier of the webhook
    update_webhook_request = fireblocks.UpdateWebhookRequest() # UpdateWebhookRequest | 

    try:
        # Update webhook
        api_response = fireblocks.webhooks_v2_beta.update_webhook(webhook_id, update_webhook_request).result()
        print("The response of WebhooksV2BetaApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2BetaApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The unique identifier of the webhook | 
 **update_webhook_request** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated webhook object |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

