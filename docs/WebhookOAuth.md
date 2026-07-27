# WebhookOAuth

OAuth 2.0 client credentials configuration for the webhook. When set, the webhook dispatcher fetches a bearer token from the configured token endpoint before each delivery and attaches it as `Authorization: Bearer {token}`. Send `null` to remove OAuth configuration entirely.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | OAuth client ID used to authenticate with the token endpoint. | 
**client_secret** | **str** | OAuth client secret. Write-only — never returned in responses. | 
**url** | **str** | Token endpoint URL. Must be HTTPS. | 
**mtls_client_signed_cert** | **str** | Signed client certificate PEM used for mTLS when connecting to the token endpoint. Same format as the webhook mTLS certificate. Send &#x60;null&#x60; to remove. | [optional] 

## Example

```python
from fireblocks.models.webhook_o_auth import WebhookOAuth

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOAuth from a JSON string
webhook_o_auth_instance = WebhookOAuth.from_json(json)
# print the JSON string representation of the object
print(WebhookOAuth.to_json())

# convert the object into a dict
webhook_o_auth_dict = webhook_o_auth_instance.to_dict()
# create an instance of WebhookOAuth from a dict
webhook_o_auth_from_dict = WebhookOAuth.from_dict(webhook_o_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


