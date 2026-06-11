# WebhookMtlsCsrResponse

mTLS Certificate Signing Request response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** | The Fireblocks PEM-encoded Certificate Signing Request (CSR). | 

## Example

```python
from fireblocks.models.webhook_mtls_csr_response import WebhookMtlsCsrResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMtlsCsrResponse from a JSON string
webhook_mtls_csr_response_instance = WebhookMtlsCsrResponse.from_json(json)
# print the JSON string representation of the object
print(WebhookMtlsCsrResponse.to_json())

# convert the object into a dict
webhook_mtls_csr_response_dict = webhook_mtls_csr_response_instance.to_dict()
# create an instance of WebhookMtlsCsrResponse from a dict
webhook_mtls_csr_response_from_dict = WebhookMtlsCsrResponse.from_dict(webhook_mtls_csr_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


