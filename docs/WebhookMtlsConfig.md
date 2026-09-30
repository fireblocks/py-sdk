# WebhookMtlsConfig

A signed client certificate stored for the workspace, and the id a webhook or OAuth credentials set references to use it. Several of them may share one configuration, so replacing the certificate here switches all of them at once.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the mTLS configuration, to be set as &#x60;webhookMtlsId&#x60; on a webhook or on OAuth credentials. | 
**name** | **str** | The label given to this mTLS configuration. | [optional] 
**signed_cert** | **str** | The signed client certificate PEM. | 
**expires_at** | **int** | When the certificate itself expires, in milliseconds since the epoch. | 
**created_at** | **int** | When the certificate was uploaded, in milliseconds since the epoch. | 
**updated_at** | **int** | When this configuration was last changed, in milliseconds since the epoch. Differs from createdAt once the certificate has been replaced or the configuration renamed. | 

## Example

```python
from fireblocks.models.webhook_mtls_config import WebhookMtlsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMtlsConfig from a JSON string
webhook_mtls_config_instance = WebhookMtlsConfig.from_json(json)
# print the JSON string representation of the object
print(WebhookMtlsConfig.to_json())

# convert the object into a dict
webhook_mtls_config_dict = webhook_mtls_config_instance.to_dict()
# create an instance of WebhookMtlsConfig from a dict
webhook_mtls_config_from_dict = WebhookMtlsConfig.from_dict(webhook_mtls_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


