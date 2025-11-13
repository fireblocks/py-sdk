# SourceConfig

Source account configuration for policy rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**List[AccountType2]**](AccountType2.md) | Source account types | [optional] 
**sub_type** | [**List[AccountIdentifier]**](AccountIdentifier.md) | Source account subtypes | [optional] 
**ids** | [**List[AccountIdentifier]**](AccountIdentifier.md) | Source account identifiers | [optional] 
**tags** | [**List[PolicyTag]**](PolicyTag.md) | Tags for source matching | [optional] 
**operator** | [**PolicyOperator**](PolicyOperator.md) |  | 
**match_from** | **str** | Whether to match from account (relevant only for ORDER policy type) | [optional] 

## Example

```python
from fireblocks.models.source_config import SourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SourceConfig from a JSON string
source_config_instance = SourceConfig.from_json(json)
# print the JSON string representation of the object
print(SourceConfig.to_json())

# convert the object into a dict
source_config_dict = source_config_instance.to_dict()
# create an instance of SourceConfig from a dict
source_config_from_dict = SourceConfig.from_dict(source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


