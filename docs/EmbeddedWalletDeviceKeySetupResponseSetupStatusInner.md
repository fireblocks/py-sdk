# EmbeddedWalletDeviceKeySetupResponseSetupStatusInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm_name** | [**EmbeddedWalletAlgoritm**](EmbeddedWalletAlgoritm.md) |  | 
**confirmed** | **bool** | confirmed | 
**backed_up** | **bool** | backedUp | 

## Example

```python
from fireblocks.models.embedded_wallet_device_key_setup_response_setup_status_inner import EmbeddedWalletDeviceKeySetupResponseSetupStatusInner

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletDeviceKeySetupResponseSetupStatusInner from a JSON string
embedded_wallet_device_key_setup_response_setup_status_inner_instance = EmbeddedWalletDeviceKeySetupResponseSetupStatusInner.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletDeviceKeySetupResponseSetupStatusInner.to_json())

# convert the object into a dict
embedded_wallet_device_key_setup_response_setup_status_inner_dict = embedded_wallet_device_key_setup_response_setup_status_inner_instance.to_dict()
# create an instance of EmbeddedWalletDeviceKeySetupResponseSetupStatusInner from a dict
embedded_wallet_device_key_setup_response_setup_status_inner_from_dict = EmbeddedWalletDeviceKeySetupResponseSetupStatusInner.from_dict(embedded_wallet_device_key_setup_response_setup_status_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


