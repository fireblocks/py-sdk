# DestinationConfig

Destination configuration for policy rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**List[AccountType2]**](AccountType2.md) | Destination account types | [optional] 
**sub_type** | [**List[AccountIdentifier]**](AccountIdentifier.md) |  | [optional] 
**ids** | [**List[AccountIdentifier]**](AccountIdentifier.md) |  | [optional] 
**tags** | [**List[PolicyTag]**](PolicyTag.md) | Tags for destination matching | [optional] 
**operator** | [**PolicyOperator**](PolicyOperator.md) |  | 
**match_from** | **str** | Whether to match from account or source (relevant only for ORDER policy type). If set to ACCOUNT, only matchFrom is allowed and other fields are not required. | [optional] 
**address_type** | **str** | Type of destination addresses allowed | 

## Example

```python
from fireblocks.models.destination_config import DestinationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationConfig from a JSON string
destination_config_instance = DestinationConfig.from_json(json)
# print the JSON string representation of the object
print(DestinationConfig.to_json())

# convert the object into a dict
destination_config_dict = destination_config_instance.to_dict()
# create an instance of DestinationConfig from a dict
destination_config_from_dict = DestinationConfig.from_dict(destination_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


