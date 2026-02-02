# EmbeddedWalletSetupStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**EmbeddedWalletSetUpStatus**](EmbeddedWalletSetUpStatus.md) |  | 
**required_algorithms** | [**List[EmbeddedWalletRequiredAlgorithms]**](EmbeddedWalletRequiredAlgorithms.md) | Required algorithms for the wallet | 
**device_setup_status** | [**List[EmbeddedWalletDeviceKeySetupResponse]**](EmbeddedWalletDeviceKeySetupResponse.md) | Setup status for each device | 

## Example

```python
from fireblocks.models.embedded_wallet_setup_status_response import EmbeddedWalletSetupStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletSetupStatusResponse from a JSON string
embedded_wallet_setup_status_response_instance = EmbeddedWalletSetupStatusResponse.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletSetupStatusResponse.to_json())

# convert the object into a dict
embedded_wallet_setup_status_response_dict = embedded_wallet_setup_status_response_instance.to_dict()
# create an instance of EmbeddedWalletSetupStatusResponse from a dict
embedded_wallet_setup_status_response_from_dict = EmbeddedWalletSetupStatusResponse.from_dict(embedded_wallet_setup_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


