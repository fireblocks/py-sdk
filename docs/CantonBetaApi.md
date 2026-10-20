# fireblocks.CantonBetaApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_canton_call**](CantonBetaApi.md#create_canton_call) | **POST** /operations/canton/calls | Make a Canton call
[**respond_to_canton_offer**](CantonBetaApi.md#respond_to_canton_offer) | **POST** /operations/canton/offers/{offerId}/responses | Answer an offer


# **create_canton_call**
> CallAccepted create_canton_call(canton_call, idempotency_key=idempotency_key)

Make a Canton call

Submits a Canton call from a vault account's Canton wallet. `type` selects the call and the shape of `payload`.

### Example


```python
from fireblocks.models.call_accepted import CallAccepted
from fireblocks.models.canton_call import CantonCall
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
    canton_call = fireblocks.CantonCall() # CantonCall | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Make a Canton call
        api_response = fireblocks.canton_beta.create_canton_call(canton_call, idempotency_key=idempotency_key).result()
        print("The response of CantonBetaApi->create_canton_call:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CantonBetaApi->create_canton_call: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **canton_call** | [**CantonCall**](CantonCall.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**CallAccepted**](CallAccepted.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The outgoing transaction that carries the call. |  * X-Request-ID -  <br>  |
**400** | Unknown or missing type, a missing required payload field, or an invalid party id, blockchainId, or expiry |  * X-Request-ID -  <br>  |
**404** | No Canton wallet for this vault account and blockchainId, or an unknown end investor for this tenant |  * X-Request-ID -  <br>  |
**409** | The target is not in a state this call can act on, or more than one candidate contract matched the wallet |  * X-Request-ID -  <br>  |
**501** | This call type is not yet available: DTCC_END_INVESTOR_INVITE_CANCEL, DTCC_ALLOW_LIST_ADD, DTCC_ALLOW_LIST_REMOVE |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respond_to_canton_offer**
> OfferResponseAccepted respond_to_canton_offer(offer_id, offer_response, idempotency_key=idempotency_key)

Answer an offer

Responds to an incoming Canton offer. Set `responseType` to one of the values in the offer transaction's `cantonDetails.offerResponse.availableResponses`.

### Example


```python
from fireblocks.models.offer_response import OfferResponse
from fireblocks.models.offer_response_accepted import OfferResponseAccepted
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
    offer_id = '5a1d8b0f-2c31-4c7e-9d0a-118e7b6c4a21' # str | The Fireblocks transaction id of the incoming offer being answered.
    offer_response = fireblocks.OfferResponse() # OfferResponse | 
    idempotency_key = 'idempotency_key_example' # str | A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. (optional)

    try:
        # Answer an offer
        api_response = fireblocks.canton_beta.respond_to_canton_offer(offer_id, offer_response, idempotency_key=idempotency_key).result()
        print("The response of CantonBetaApi->respond_to_canton_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CantonBetaApi->respond_to_canton_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| The Fireblocks transaction id of the incoming offer being answered. | 
 **offer_response** | [**OfferResponse**](OfferResponse.md)|  | 
 **idempotency_key** | **str**| A unique identifier for the request. If the request is sent multiple times with the same idempotency key, the server will return the same response as the first request. The idempotency key is valid for 24 hours. | [optional] 

### Return type

[**OfferResponseAccepted**](OfferResponseAccepted.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The outgoing transaction that carries the response. Its on-chain outcome arrives by webhook as a status update on this transaction. |  * X-Request-ID -  <br>  |
**400** | Unknown or missing responseType, or a missing required payload field, or the response is not available to this workspace&#39;s side of the offer (a sender sending accept/reject, a receiver sending withdraw) |  * X-Request-ID -  <br>  |
**404** | Unknown offer id for this tenant |  * X-Request-ID -  <br>  |
**409** | The offer cannot take this response now. An accept or reject: the offer is already answered, expired, or a response is in flight. ALLOCATION_WITHDRAW — which is sent AFTER the accept, on the same offer: the allocation is not ALLOCATED, because the accept has not settled yet, or it was already withdrawn or settled by the venue. The message names the state. |  * X-Request-ID -  <br>  |
**501** | This responseType is not yet available |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

