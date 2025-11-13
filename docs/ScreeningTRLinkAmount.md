# ScreeningTRLinkAmount

TRLink amount definition with range and currency, compatible with TAP format from Policy Engine V2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**AmountRangeMinMax**](AmountRangeMinMax.md) |  | [optional] 
**currency** | **str** | Currency type | [optional] 

## Example

```python
from fireblocks.models.screening_tr_link_amount import ScreeningTRLinkAmount

# TODO update the JSON string below
json = "{}"
# create an instance of ScreeningTRLinkAmount from a JSON string
screening_tr_link_amount_instance = ScreeningTRLinkAmount.from_json(json)
# print the JSON string representation of the object
print(ScreeningTRLinkAmount.to_json())

# convert the object into a dict
screening_tr_link_amount_dict = screening_tr_link_amount_instance.to_dict()
# create an instance of ScreeningTRLinkAmount from a dict
screening_tr_link_amount_from_dict = ScreeningTRLinkAmount.from_dict(screening_tr_link_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


