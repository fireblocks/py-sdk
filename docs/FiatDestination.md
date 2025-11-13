# FiatDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**MobileMoneyAddress**](MobileMoneyAddress.md) |  | 

## Example

```python
from fireblocks.models.fiat_destination import FiatDestination

# TODO update the JSON string below
json = "{}"
# create an instance of FiatDestination from a JSON string
fiat_destination_instance = FiatDestination.from_json(json)
# print the JSON string representation of the object
print(FiatDestination.to_json())

# convert the object into a dict
fiat_destination_dict = fiat_destination_instance.to_dict()
# create an instance of FiatDestination from a dict
fiat_destination_from_dict = FiatDestination.from_dict(fiat_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


