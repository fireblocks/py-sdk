# IbanDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**IbanAddress**](IbanAddress.md) |  | 

## Example

```python
from fireblocks.models.iban_destination import IbanDestination

# TODO update the JSON string below
json = "{}"
# create an instance of IbanDestination from a JSON string
iban_destination_instance = IbanDestination.from_json(json)
# print the JSON string representation of the object
print(IbanDestination.to_json())

# convert the object into a dict
iban_destination_dict = iban_destination_instance.to_dict()
# create an instance of IbanDestination from a dict
iban_destination_from_dict = IbanDestination.from_dict(iban_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


