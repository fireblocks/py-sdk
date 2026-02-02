# TRLinkThresholds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Threshold amount | [optional] 
**currency** | **str** | Currency code | [optional] 

## Example

```python
from fireblocks.models.tr_link_thresholds import TRLinkThresholds

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkThresholds from a JSON string
tr_link_thresholds_instance = TRLinkThresholds.from_json(json)
# print the JSON string representation of the object
print(TRLinkThresholds.to_json())

# convert the object into a dict
tr_link_thresholds_dict = tr_link_thresholds_instance.to_dict()
# create an instance of TRLinkThresholds from a dict
tr_link_thresholds_from_dict = TRLinkThresholds.from_dict(tr_link_thresholds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


