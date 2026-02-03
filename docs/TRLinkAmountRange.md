# TRLinkAmountRange

Minimum and maximum amount range specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **str** | Minimum amount (inclusive) | [optional] 
**max** | **str** | Maximum amount (inclusive) | [optional] 

## Example

```python
from fireblocks.models.tr_link_amount_range import TRLinkAmountRange

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkAmountRange from a JSON string
tr_link_amount_range_instance = TRLinkAmountRange.from_json(json)
# print the JSON string representation of the object
print(TRLinkAmountRange.to_json())

# convert the object into a dict
tr_link_amount_range_dict = tr_link_amount_range_instance.to_dict()
# create an instance of TRLinkAmountRange from a dict
tr_link_amount_range_from_dict = TRLinkAmountRange.from_dict(tr_link_amount_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


