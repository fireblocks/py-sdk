# SEPADestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**SEPAAddress**](SEPAAddress.md) |  | 

## Example

```python
from fireblocks.models.sepa_destination import SEPADestination

# TODO update the JSON string below
json = "{}"
# create an instance of SEPADestination from a JSON string
sepa_destination_instance = SEPADestination.from_json(json)
# print the JSON string representation of the object
print(SEPADestination.to_json())

# convert the object into a dict
sepa_destination_dict = sepa_destination_instance.to_dict()
# create an instance of SEPADestination from a dict
sepa_destination_from_dict = SEPADestination.from_dict(sepa_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


