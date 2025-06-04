# EmbeddedWalletDeviceKeySetupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**EmbeddedWalletSetUpStatus**](EmbeddedWalletSetUpStatus.md) |  | 
**device_id** | **str** | deviceId | 
**enabled** | **bool** | enabled | 
**setup_status** | [**List[EmbeddedWalletDeviceKeySetupResponseSetupStatusInner]**](EmbeddedWalletDeviceKeySetupResponseSetupStatusInner.md) | setupStatus | 

## Example

```python
from fireblocks.models.embedded_wallet_device_key_setup_response import EmbeddedWalletDeviceKeySetupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletDeviceKeySetupResponse from a JSON string
embedded_wallet_device_key_setup_response_instance = EmbeddedWalletDeviceKeySetupResponse.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletDeviceKeySetupResponse.to_json())

# convert the object into a dict
embedded_wallet_device_key_setup_response_dict = embedded_wallet_device_key_setup_response_instance.to_dict()
# create an instance of EmbeddedWalletDeviceKeySetupResponse from a dict
embedded_wallet_device_key_setup_response_from_dict = EmbeddedWalletDeviceKeySetupResponse.from_dict(embedded_wallet_device_key_setup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


