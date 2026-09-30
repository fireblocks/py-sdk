# DeleteWebhookMtlsConfigResponse

The deleted mTLS configuration, plus the ids of any webhooks and OAuth credentials the delete detached from it. They are only detached by `forceDelete=true`; without it a delete is refused with `409` while anything still references the configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the mTLS configuration, to be set as &#x60;webhookMtlsId&#x60; on a webhook or on OAuth credentials. | 
**name** | **str** | The label given to this mTLS configuration. | [optional] 
**signed_cert** | **str** | The signed client certificate PEM. | 
**expires_at** | **int** | When the certificate itself expires, in milliseconds since the epoch. | 
**created_at** | **int** | When the certificate was uploaded, in milliseconds since the epoch. | 
**updated_at** | **int** | When this configuration was last changed, in milliseconds since the epoch. Differs from createdAt once the certificate has been replaced or the configuration renamed. | 
**detached_webhook_ids** | **List[str]** | Webhooks whose &#x60;webhookMtlsId&#x60; was cleared. The webhooks themselves are not deleted and keep delivering, just without a client certificate. Empty unless &#x60;forceDelete&#x3D;true&#x60; detached something. | 
**detached_webhook_oauth_ids** | **List[str]** | OAuth credentials whose &#x60;webhookMtlsId&#x60; was cleared. Their token requests continue without a client certificate. Empty unless &#x60;forceDelete&#x3D;true&#x60; detached something. | 

## Example

```python
from fireblocks.models.delete_webhook_mtls_config_response import DeleteWebhookMtlsConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteWebhookMtlsConfigResponse from a JSON string
delete_webhook_mtls_config_response_instance = DeleteWebhookMtlsConfigResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteWebhookMtlsConfigResponse.to_json())

# convert the object into a dict
delete_webhook_mtls_config_response_dict = delete_webhook_mtls_config_response_instance.to_dict()
# create an instance of DeleteWebhookMtlsConfigResponse from a dict
delete_webhook_mtls_config_response_from_dict = DeleteWebhookMtlsConfigResponse.from_dict(delete_webhook_mtls_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


