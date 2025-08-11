# fireblocks.WebhooksV2Api

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksV2Api.md#create_webhook) | **POST** /webhooks | Create new webhook
[**delete_webhook**](WebhooksV2Api.md#delete_webhook) | **DELETE** /webhooks/{webhookId} | Delete webhook
[**get_notification**](WebhooksV2Api.md#get_notification) | **GET** /webhooks/{webhookId}/notifications/{notificationId} | Get notification by id
[**get_notification_attempts**](WebhooksV2Api.md#get_notification_attempts) | **GET** /webhooks/{webhookId}/notifications/{notificationId}/attempts | Get notification attempts
[**get_notifications**](WebhooksV2Api.md#get_notifications) | **GET** /webhooks/{webhookId}/notifications | Get all notifications by webhook id
[**get_resend_job_status**](WebhooksV2Api.md#get_resend_job_status) | **GET** /webhooks/{webhookId}/notifications/resend_failed/jobs/{jobId} | Get resend job status
[**get_webhook**](WebhooksV2Api.md#get_webhook) | **GET** /webhooks/{webhookId} | Get webhook by id
[**get_webhooks**](WebhooksV2Api.md#get_webhooks) | **GET** /webhooks | Get all webhooks
[**resend_failed_notifications**](WebhooksV2Api.md#resend_failed_notifications) | **POST** /webhooks/{webhookId}/notifications/resend_failed | Resend failed notifications
[**resend_notification_by_id**](WebhooksV2Api.md#resend_notification_by_id) | **POST** /webhooks/{webhookId}/notifications/{notificationId}/resend | Resend notification by id
[**resend_notifications_by_resource_id**](WebhooksV2Api.md#resend_notifications_by_resource_id) | **POST** /webhooks/{webhookId}/notifications/resend_by_resource | Resend notifications by resource Id
[**update_webhook**](WebhooksV2Api.md#update_webhook) | **PATCH** /webhooks/{webhookId} | Update webhook


# **create_webhook**
> Webhook create_webhook(create_webhook_request, idempotency_key=idempotency_key)

Create new webhook

Creates a new webhook, which will be triggered on the specified events

Endpoint Permission: Owner, Admin, Non-Signing Admin.


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
        api_response = fireblocks.webhooks_v2.create_webhook(create_webhook_request, idempotency_key=idempotency_key).result()
        print("The response of WebhooksV2Api->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->create_webhook: %s\n" % e)
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

Delete a webhook by its id

Endpoint Permission: Owner, Admin, Non-Signing Admin.


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
        api_response = fireblocks.webhooks_v2.delete_webhook(webhook_id).result()
        print("The response of WebhooksV2Api->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->delete_webhook: %s\n" % e)
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

Get notification by id


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
        api_response = fireblocks.webhooks_v2.get_notification(webhook_id, notification_id, include_data=include_data).result()
        print("The response of WebhooksV2Api->get_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->get_notification: %s\n" % e)
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

# **get_notification_attempts**
> NotificationAttemptsPaginatedResponse get_notification_attempts(webhook_id, notification_id, page_cursor=page_cursor, page_size=page_size)

Get notification attempts

Get notification attempts by notification id


### Example


```python
from fireblocks.models.notification_attempts_paginated_response import NotificationAttemptsPaginatedResponse
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
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 10 # float | Maximum number of items in the page (optional) (default to 10)

    try:
        # Get notification attempts
        api_response = fireblocks.webhooks_v2.get_notification_attempts(webhook_id, notification_id, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of WebhooksV2Api->get_notification_attempts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->get_notification_attempts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The ID of the webhook to fetch | 
 **notification_id** | **str**| The ID of the notification to fetch | 
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **float**| Maximum number of items in the page | [optional] [default to 10]

### Return type

[**NotificationAttemptsPaginatedResponse**](NotificationAttemptsPaginatedResponse.md)

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
> NotificationPaginatedResponse get_notifications(webhook_id, order=order, sort_by=sort_by, page_cursor=page_cursor, page_size=page_size)

Get all notifications by webhook id

Get all notifications by webhook id (paginated)


### Example


```python
from fireblocks.models.notification_paginated_response import NotificationPaginatedResponse
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
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)
    sort_by = updatedAt # str | Sort by field (optional) (default to updatedAt)
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 100 # float | Maximum number of items in the page (optional) (default to 100)

    try:
        # Get all notifications by webhook id
        api_response = fireblocks.webhooks_v2.get_notifications(webhook_id, order=order, sort_by=sort_by, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of WebhooksV2Api->get_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->get_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]
 **sort_by** | **str**| Sort by field | [optional] [default to updatedAt]
 **page_cursor** | **str**| Cursor of the required page | [optional] 
 **page_size** | **float**| Maximum number of items in the page | [optional] [default to 100]

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

# **get_resend_job_status**
> ResendFailedNotificationsJobStatusResponse get_resend_job_status(webhook_id, job_id)

Get resend job status

Get the status of a resend job


### Example


```python
from fireblocks.models.resend_failed_notifications_job_status_response import ResendFailedNotificationsJobStatusResponse
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
    webhook_id = 'webhook_id_example' # str | The ID of the webhook
    job_id = 'job_id_example' # str | The ID of the resend job

    try:
        # Get resend job status
        api_response = fireblocks.webhooks_v2.get_resend_job_status(webhook_id, job_id).result()
        print("The response of WebhooksV2Api->get_resend_job_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->get_resend_job_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The ID of the webhook | 
 **job_id** | **str**| The ID of the resend job | 

### Return type

[**ResendFailedNotificationsJobStatusResponse**](ResendFailedNotificationsJobStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Job status |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> Webhook get_webhook(webhook_id)

Get webhook by id

Retrieve a webhook by its id


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
        api_response = fireblocks.webhooks_v2.get_webhook(webhook_id).result()
        print("The response of WebhooksV2Api->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->get_webhook: %s\n" % e)
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

Get all webhooks (paginated)


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
    order = DESC # str | ASC / DESC ordering (default DESC) (optional) (default to DESC)
    page_cursor = 'page_cursor_example' # str | Cursor of the required page (optional)
    page_size = 10 # float | Maximum number of items in the page (optional) (default to 10)

    try:
        # Get all webhooks
        api_response = fireblocks.webhooks_v2.get_webhooks(order=order, page_cursor=page_cursor, page_size=page_size).result()
        print("The response of WebhooksV2Api->get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->get_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| ASC / DESC ordering (default DESC) | [optional] [default to DESC]
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

# **resend_failed_notifications**
> ResendFailedNotificationsResponse resend_failed_notifications(webhook_id, resend_failed_notifications_request, idempotency_key=idempotency_key)

Resend failed notifications

Resend all failed notifications for a webhook in the last 24 hours

Endpoint Permission: Owner, Admin, Non-Signing Admin.


### Example


```python
from fireblocks.models.resend_failed_notifications_request import ResendFailedNotificationsRequest
from fireblocks.models.resend_failed_notifications_response import ResendFailedNotificationsResponse
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
    webhook_id = 'webhook_id_example' # str | The ID of the webhook
    resend_failed_notifications_request = fireblocks.ResendFailedNotificationsRequest() # ResendFailedNotificationsRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Resend failed notifications
        api_response = fireblocks.webhooks_v2.resend_failed_notifications(webhook_id, resend_failed_notifications_request, idempotency_key=idempotency_key).result()
        print("The response of WebhooksV2Api->resend_failed_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->resend_failed_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The ID of the webhook | 
 **resend_failed_notifications_request** | [**ResendFailedNotificationsRequest**](ResendFailedNotificationsRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**ResendFailedNotificationsResponse**](ResendFailedNotificationsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No failed notifications to resend |  * X-Request-ID -  <br>  |
**202** | Resend failed notifications request was accepted and is being processed |  * X-Request-ID -  <br>  * Location -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_notification_by_id**
> resend_notification_by_id(webhook_id, notification_id, idempotency_key=idempotency_key)

Resend notification by id

Resend notification by ID

Endpoint Permission: Owner, Admin, Non-Signing Admin.


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
        fireblocks.webhooks_v2.resend_notification_by_id(webhook_id, notification_id, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling WebhooksV2Api->resend_notification_by_id: %s\n" % e)
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

# **resend_notifications_by_resource_id**
> resend_notifications_by_resource_id(webhook_id, resend_notifications_by_resource_id_request, idempotency_key=idempotency_key)

Resend notifications by resource Id

Resend notifications by resource Id

Endpoint Permission: Owner, Admin, Non-Signing Admin.


### Example


```python
from fireblocks.models.resend_notifications_by_resource_id_request import ResendNotificationsByResourceIdRequest
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
    resend_notifications_by_resource_id_request = fireblocks.ResendNotificationsByResourceIdRequest() # ResendNotificationsByResourceIdRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Resend notifications by resource Id
        fireblocks.webhooks_v2.resend_notifications_by_resource_id(webhook_id, resend_notifications_by_resource_id_request, idempotency_key=idempotency_key).result()
    except Exception as e:
        print("Exception when calling WebhooksV2Api->resend_notifications_by_resource_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| The ID of the webhook | 
 **resend_notifications_by_resource_id_request** | [**ResendNotificationsByResourceIdRequest**](ResendNotificationsByResourceIdRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

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
**202** | Resend notifications by resource request was accepted and is being processed |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> Webhook update_webhook(webhook_id, update_webhook_request)

Update webhook

Update a webhook by its id

Endpoint Permission: Owner, Admin, Non-Signing Admin.


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
        api_response = fireblocks.webhooks_v2.update_webhook(webhook_id, update_webhook_request).result()
        print("The response of WebhooksV2Api->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksV2Api->update_webhook: %s\n" % e)
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

