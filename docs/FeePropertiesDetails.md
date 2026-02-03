# FeePropertiesDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_type** | [**FeeTypeEnum**](FeeTypeEnum.md) |  | 
**asset_id** | **str** | The asset identifier for the fee. | 

## Example

```python
from fireblocks.models.fee_properties_details import FeePropertiesDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FeePropertiesDetails from a JSON string
fee_properties_details_instance = FeePropertiesDetails.from_json(json)
# print the JSON string representation of the object
print(FeePropertiesDetails.to_json())

# convert the object into a dict
fee_properties_details_dict = fee_properties_details_instance.to_dict()
# create an instance of FeePropertiesDetails from a dict
fee_properties_details_from_dict = FeePropertiesDetails.from_dict(fee_properties_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


