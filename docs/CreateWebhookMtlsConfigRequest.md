# CreateWebhookMtlsConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A label for this mTLS configuration, to tell several certificates apart. Letters, digits and spaces only. | [optional] 
**signed_cert** | **str** | Signed client certificate PEM, issued for the CSR from &#x60;GET /v1/webhooks_settings/mtls_csr&#x60;. The private key it belongs to is derived from the certificate itself. | 

## Example

```python
from fireblocks.models.create_webhook_mtls_config_request import CreateWebhookMtlsConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookMtlsConfigRequest from a JSON string
create_webhook_mtls_config_request_instance = CreateWebhookMtlsConfigRequest.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookMtlsConfigRequest.to_json())

# convert the object into a dict
create_webhook_mtls_config_request_dict = create_webhook_mtls_config_request_instance.to_dict()
# create an instance of CreateWebhookMtlsConfigRequest from a dict
create_webhook_mtls_config_request_from_dict = CreateWebhookMtlsConfigRequest.from_dict(create_webhook_mtls_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


