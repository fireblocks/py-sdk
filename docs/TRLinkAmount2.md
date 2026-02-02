# TRLinkAmount2

Amount specification with range and currency type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**TRLinkAmountRange**](TRLinkAmountRange.md) |  | 
**currency** | [**TRLinkCurrency**](TRLinkCurrency.md) |  | 

## Example

```python
from fireblocks.models.tr_link_amount2 import TRLinkAmount2

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkAmount2 from a JSON string
tr_link_amount2_instance = TRLinkAmount2.from_json(json)
# print the JSON string representation of the object
print(TRLinkAmount2.to_json())

# convert the object into a dict
tr_link_amount2_dict = tr_link_amount2_instance.to_dict()
# create an instance of TRLinkAmount2 from a dict
tr_link_amount2_from_dict = TRLinkAmount2.from_dict(tr_link_amount2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


