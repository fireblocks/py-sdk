# USWireAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**bank_name** | **str** | Name of the bank. | [optional] 
**bank_account_number** | **str** | The bank account number for the wire transfer. | 
**routing_number** | **str** | Routing number identifying the bank account. | 
**bank_address** | **str** | Address of the bank. | [optional] 

## Example

```python
from fireblocks.models.us_wire_address import USWireAddress

# TODO update the JSON string below
json = "{}"
# create an instance of USWireAddress from a JSON string
us_wire_address_instance = USWireAddress.from_json(json)
# print the JSON string representation of the object
print(USWireAddress.to_json())

# convert the object into a dict
us_wire_address_dict = us_wire_address_instance.to_dict()
# create an instance of USWireAddress from a dict
us_wire_address_from_dict = USWireAddress.from_dict(us_wire_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


