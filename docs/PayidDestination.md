# PayidDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**PayidAddress**](PayidAddress.md) |  | 

## Example

```python
from fireblocks.models.payid_destination import PayidDestination

# TODO update the JSON string below
json = "{}"
# create an instance of PayidDestination from a JSON string
payid_destination_instance = PayidDestination.from_json(json)
# print the JSON string representation of the object
print(PayidDestination.to_json())

# convert the object into a dict
payid_destination_dict = payid_destination_instance.to_dict()
# create an instance of PayidDestination from a dict
payid_destination_from_dict = PayidDestination.from_dict(payid_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


