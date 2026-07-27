# WebhookOAuthResponse

OAuth 2.0 client credentials configuration for the webhook. Present only when OAuth is configured. The `clientSecret` is write-only and is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | OAuth client ID used to authenticate with the token endpoint. | 
**url** | **str** | Token endpoint URL. | 
**mtls_client_signed_cert** | **str** | Signed client certificate PEM used for mTLS when connecting to the token endpoint. | [optional] 

## Example

```python
from fireblocks.models.webhook_o_auth_response import WebhookOAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOAuthResponse from a JSON string
webhook_o_auth_response_instance = WebhookOAuthResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookOAuthResponse.to_json())

# convert the object into a dict
webhook_o_auth_response_dict = webhook_o_auth_response_instance.to_dict()
# create an instance of WebhookOAuthResponse from a dict
webhook_o_auth_response_from_dict = WebhookOAuthResponse.from_dict(webhook_o_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


