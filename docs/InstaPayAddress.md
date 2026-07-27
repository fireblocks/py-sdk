# InstaPayAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_holder** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**bank_name** | **str** | Name of the recipient&#39;s bank or wallet (e.g. BDO, BPI, GCash, Maya) | 
**account_number** | **str** | Recipient bank account or wallet number | 

## Example

```python
from fireblocks.models.insta_pay_address import InstaPayAddress

# TODO update the JSON string below
json = "{}"
# create an instance of InstaPayAddress from a JSON string
insta_pay_address_instance = InstaPayAddress.from_json(json)
# print the JSON string representation of the object
print(InstaPayAddress.to_json())

# convert the object into a dict
insta_pay_address_dict = insta_pay_address_instance.to_dict()
# create an instance of InstaPayAddress from a dict
insta_pay_address_from_dict = InstaPayAddress.from_dict(insta_pay_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


