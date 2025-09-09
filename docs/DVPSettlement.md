# DVPSettlement

Source/Destination accounts for the quote (must have for defi quotes)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**source_account** | [**SettlementSourceAccount**](SettlementSourceAccount.md) |  | 
**destination_account** | [**AccountReference**](AccountReference.md) |  | 

## Example

```python
from fireblocks.models.dvp_settlement import DVPSettlement

# TODO update the JSON string below
json = "{}"
# create an instance of DVPSettlement from a JSON string
dvp_settlement_instance = DVPSettlement.from_json(json)
# print the JSON string representation of the object
print(DVPSettlement.to_json())

# convert the object into a dict
dvp_settlement_dict = dvp_settlement_instance.to_dict()
# create an instance of DVPSettlement from a dict
dvp_settlement_from_dict = DVPSettlement.from_dict(dvp_settlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


