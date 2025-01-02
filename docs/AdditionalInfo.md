# AdditionalInfo

Additional information related to the blockchain. This may include extra details about the blockchain network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_annual_reward** | **float** | The estimated annual reward rate for the blockchain, represented as a decimal percentage value. | 
**lockup_period** | **float** | The duration of the lockup period for certain actions on the blockchain, measured in milliseconds. | 
**activation_period** | **float** | The duration of the activation period for certain actions on the blockchain, measured in milliseconds. | 

## Example

```python
from fireblocks.models.additional_info import AdditionalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalInfo from a JSON string
additional_info_instance = AdditionalInfo.from_json(json)
# print the JSON string representation of the object
print(AdditionalInfo.to_json())

# convert the object into a dict
additional_info_dict = additional_info_instance.to_dict()
# create an instance of AdditionalInfo from a dict
additional_info_from_dict = AdditionalInfo.from_dict(additional_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


