# TRLinkAmount

TRLink amount definition with range and currency, compatible with TAP format from Policy Engine V2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**AmountRangeMinMax**](AmountRangeMinMax.md) |  | [optional] 
**currency** | **str** | Currency type | [optional] 

## Example

```python
from fireblocks.models.tr_link_amount import TRLinkAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkAmount from a JSON string
tr_link_amount_instance = TRLinkAmount.from_json(json)
# print the JSON string representation of the object
print(TRLinkAmount.to_json())

# convert the object into a dict
tr_link_amount_dict = tr_link_amount_instance.to_dict()
# create an instance of TRLinkAmount from a dict
tr_link_amount_from_dict = TRLinkAmount.from_dict(tr_link_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


