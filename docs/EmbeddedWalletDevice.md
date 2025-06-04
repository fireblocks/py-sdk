# EmbeddedWalletDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | deviceId | 
**enabled** | **bool** | enabled | 
**physical_device_id** | **str** | physicalDeviceId | 

## Example

```python
from fireblocks.models.embedded_wallet_device import EmbeddedWalletDevice

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletDevice from a JSON string
embedded_wallet_device_instance = EmbeddedWalletDevice.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletDevice.to_json())

# convert the object into a dict
embedded_wallet_device_dict = embedded_wallet_device_instance.to_dict()
# create an instance of EmbeddedWalletDevice from a dict
embedded_wallet_device_from_dict = EmbeddedWalletDevice.from_dict(embedded_wallet_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


