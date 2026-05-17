# fireblocks.GenieBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_genie_session**](GenieBetaApi.md#create_genie_session) | **POST** /genie/sessions | Create a Genie session
[**send_genie_message**](GenieBetaApi.md#send_genie_message) | **POST** /genie/sessions/{sessionId}/messages | Send a message to a Genie session


# **create_genie_session**
> GenieCreateSessionResponse create_genie_session(idempotency_key=idempotency_key)

Create a Genie session

Starts a new conversation with Genie, the Fireblocks AI assistant. Returns a `sessionId` — pass it when sending messages, and reuse it across calls to keep one continuous conversation.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.genie_create_session_response import GenieCreateSessionResponse
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
        # Create a Genie session
        api_response = fireblocks.genie_beta.create_genie_session(idempotency_key=idempotency_key).result()
        print("The response of GenieBetaApi->create_genie_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenieBetaApi->create_genie_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**GenieCreateSessionResponse**](GenieCreateSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session created |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_genie_message**
> GenieChatMessage send_genie_message(session_id, genie_send_message_request, idempotency_key=idempotency_key)

Send a message to a Genie session

Sends a question to Genie and returns a single answer. Reuse the `sessionId` from the original session on follow-up messages to continue the conversation with prior context.

**Note:** This endpoint is currently in beta and might be subject to changes.


### Example


```python
from fireblocks.models.genie_chat_message import GenieChatMessage
from fireblocks.models.genie_send_message_request import GenieSendMessageRequest
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
    session_id = '7c1b2e1c-1c2a-4f3a-9c2d-2e0a8a1f8e1a' # str | The Genie session ID returned from `POST /genie/sessions`.
    genie_send_message_request = fireblocks.GenieSendMessageRequest() # GenieSendMessageRequest | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Send a message to a Genie session
        api_response = fireblocks.genie_beta.send_genie_message(session_id, genie_send_message_request, idempotency_key=idempotency_key).result()
        print("The response of GenieBetaApi->send_genie_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenieBetaApi->send_genie_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| The Genie session ID returned from &#x60;POST /genie/sessions&#x60;. | 
 **genie_send_message_request** | [**GenieSendMessageRequest**](GenieSendMessageRequest.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**GenieChatMessage**](GenieChatMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Genie response |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

