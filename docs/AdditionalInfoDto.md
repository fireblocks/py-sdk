# AdditionalInfoDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_annual_reward** | **float** | The estimated annual reward rate for the blockchain, represented as a decimal percentage value. | 
**lockup_period** | **float** | The duration of the lockup period for certain actions on the blockchain, measured in milliseconds. | 
**activation_period** | **float** | The duration of the activation period for certain actions on the blockchain, measured in milliseconds. | 

## Example

```python
from fireblocks_client.models.additional_info_dto import AdditionalInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalInfoDto from a JSON string
additional_info_dto_instance = AdditionalInfoDto.from_json(json)
# print the JSON string representation of the object
print(AdditionalInfoDto.to_json())

# convert the object into a dict
additional_info_dto_dict = additional_info_dto_instance.to_dict()
# create an instance of AdditionalInfoDto from a dict
additional_info_dto_from_dict = AdditionalInfoDto.from_dict(additional_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


