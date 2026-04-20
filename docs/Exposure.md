# Exposure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_address** | **str** | On-chain address of the exposure asset. | [optional] 
**symbol** | **str** | Ticker for the exposure asset. | [optional] 
**amount** | **str** | Human-readable decimal string (raw on-chain value scaled by 10^decimals). | [optional] 

## Example

```python
from fireblocks.models.exposure import Exposure

# TODO update the JSON string below
json = "{}"
# create an instance of Exposure from a JSON string
exposure_instance = Exposure.from_json(json)
# print the JSON string representation of the object
print(Exposure.to_json())

# convert the object into a dict
exposure_dict = exposure_instance.to_dict()
# create an instance of Exposure from a dict
exposure_from_dict = Exposure.from_dict(exposure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


