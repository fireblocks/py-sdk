# PrefundedSettlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**destination_account** | [**AccountReference**](AccountReference.md) |  | 

## Example

```python
from fireblocks.models.prefunded_settlement import PrefundedSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of PrefundedSettlement from a JSON string
prefunded_settlement_instance = PrefundedSettlement.from_json(json)
# print the JSON string representation of the object
print(PrefundedSettlement.to_json())

# convert the object into a dict
prefunded_settlement_dict = prefunded_settlement_instance.to_dict()
# create an instance of PrefundedSettlement from a dict
prefunded_settlement_from_dict = PrefundedSettlement.from_dict(prefunded_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


