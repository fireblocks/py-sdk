# SettlementSourceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**account_id** | **str** |  | 

## Example

```python
from fireblocks.models.settlement_source_account import SettlementSourceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SettlementSourceAccount from a JSON string
settlement_source_account_instance = SettlementSourceAccount.from_json(json)
# print the JSON string representation of the object
print(SettlementSourceAccount.to_json())

# convert the object into a dict
settlement_source_account_dict = settlement_source_account_instance.to_dict()
# create an instance of SettlementSourceAccount from a dict
settlement_source_account_from_dict = SettlementSourceAccount.from_dict(settlement_source_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


