# InstaPayDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The transfer rail type for the destination | 
**address** | [**InstaPayAddress**](InstaPayAddress.md) |  | 

## Example

```python
from fireblocks.models.insta_pay_destination import InstaPayDestination

# TODO update the JSON string below
json = "{}"
# create an instance of InstaPayDestination from a JSON string
insta_pay_destination_instance = InstaPayDestination.from_json(json)
# print the JSON string representation of the object
print(InstaPayDestination.to_json())

# convert the object into a dict
insta_pay_destination_dict = insta_pay_destination_instance.to_dict()
# create an instance of InstaPayDestination from a dict
insta_pay_destination_from_dict = InstaPayDestination.from_dict(insta_pay_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


