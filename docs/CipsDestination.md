# CipsDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transfer rail type for the destination | 
**address** | [**CipsAddress**](CipsAddress.md) |  | 
**reference_id** | **str** | Optional payment reference | [optional] 

## Example

```python
from fireblocks.models.cips_destination import CipsDestination

# TODO update the JSON string below
json = "{}"
# create an instance of CipsDestination from a JSON string
cips_destination_instance = CipsDestination.from_json(json)
# print the JSON string representation of the object
print(CipsDestination.to_json())

# convert the object into a dict
cips_destination_dict = cips_destination_instance.to_dict()
# create an instance of CipsDestination from a dict
cips_destination_from_dict = CipsDestination.from_dict(cips_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


