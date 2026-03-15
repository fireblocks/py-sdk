# PaymentInstructionsOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**InternalTransferAddress**](InternalTransferAddress.md) |  | 
**reference_id** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.payment_instructions_one_of import PaymentInstructionsOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInstructionsOneOf from a JSON string
payment_instructions_one_of_instance = PaymentInstructionsOneOf.from_json(json)
# print the JSON string representation of the object
print(PaymentInstructionsOneOf.to_json())

# convert the object into a dict
payment_instructions_one_of_dict = payment_instructions_one_of_instance.to_dict()
# create an instance of PaymentInstructionsOneOf from a dict
payment_instructions_one_of_from_dict = PaymentInstructionsOneOf.from_dict(payment_instructions_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


