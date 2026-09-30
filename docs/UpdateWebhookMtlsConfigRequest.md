# UpdateWebhookMtlsConfigRequest

At least one property must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A new label for this mTLS configuration, or &#x60;null&#x60; to remove it. Letters, digits and spaces only. | [optional] 
**signed_cert** | **str** | A replacement signed certificate PEM. Every webhook and OAuth credentials set using this configuration switches to it, and the private key it was issued for is re-derived from the certificate. | [optional] 

## Example

```python
from fireblocks.models.update_webhook_mtls_config_request import UpdateWebhookMtlsConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookMtlsConfigRequest from a JSON string
update_webhook_mtls_config_request_instance = UpdateWebhookMtlsConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookMtlsConfigRequest.to_json())

# convert the object into a dict
update_webhook_mtls_config_request_dict = update_webhook_mtls_config_request_instance.to_dict()
# create an instance of UpdateWebhookMtlsConfigRequest from a dict
update_webhook_mtls_config_request_from_dict = UpdateWebhookMtlsConfigRequest.from_dict(update_webhook_mtls_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


