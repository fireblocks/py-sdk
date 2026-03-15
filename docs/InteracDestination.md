# InteracDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**InteracAddress**](InteracAddress.md) |  | 

## Example

```python
from fireblocks.models.interac_destination import InteracDestination

# TODO update the JSON string below
json = "{}"
# create an instance of InteracDestination from a JSON string
interac_destination_instance = InteracDestination.from_json(json)
# print the JSON string representation of the object
print(InteracDestination.to_json())

# convert the object into a dict
interac_destination_dict = interac_destination_instance.to_dict()
# create an instance of InteracDestination from a dict
interac_destination_from_dict = InteracDestination.from_dict(interac_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


