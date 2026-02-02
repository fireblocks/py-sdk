# EuropeanSEPADestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**EuropeanSEPAAddress**](EuropeanSEPAAddress.md) |  | 

## Example

```python
from fireblocks.models.european_sepa_destination import EuropeanSEPADestination

# TODO update the JSON string below
json = "{}"
# create an instance of EuropeanSEPADestination from a JSON string
european_sepa_destination_instance = EuropeanSEPADestination.from_json(json)
# print the JSON string representation of the object
print(EuropeanSEPADestination.to_json())

# convert the object into a dict
european_sepa_destination_dict = european_sepa_destination_instance.to_dict()
# create an instance of EuropeanSEPADestination from a dict
european_sepa_destination_from_dict = EuropeanSEPADestination.from_dict(european_sepa_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


