# WebhookMtls

mTLS configuration for the webhook. On responses, present only when a signed client certificate is set. On requests, provide a signed client certificate to enable mTLS, or null to remove it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_signed_cert** | **str** | Signed client certificate PEM used for mTLS when delivering notifications. | 

## Example

```python
from fireblocks.models.webhook_mtls import WebhookMtls

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMtls from a JSON string
webhook_mtls_instance = WebhookMtls.from_json(json)
# print the JSON string representation of the object
print(WebhookMtls.to_json())

# convert the object into a dict
webhook_mtls_dict = webhook_mtls_instance.to_dict()
# create an instance of WebhookMtls from a dict
webhook_mtls_from_dict = WebhookMtls.from_dict(webhook_mtls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


