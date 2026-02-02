# TRLinkFiatValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Fiat amount | 
**currency** | **str** | Fiat currency code | 

## Example

```python
from fireblocks.models.tr_link_fiat_value import TRLinkFiatValue

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkFiatValue from a JSON string
tr_link_fiat_value_instance = TRLinkFiatValue.from_json(json)
# print the JSON string representation of the object
print(TRLinkFiatValue.to_json())

# convert the object into a dict
tr_link_fiat_value_dict = tr_link_fiat_value_instance.to_dict()
# create an instance of TRLinkFiatValue from a dict
tr_link_fiat_value_from_dict = TRLinkFiatValue.from_dict(tr_link_fiat_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


