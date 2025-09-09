# PaymentInstructions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**address** | [**AccountHolderDetails**](AccountHolderDetails.md) |  | 
**reference_id** | **str** |  | 

## Example

```python
from fireblocks.models.payment_instructions import PaymentInstructions

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInstructions from a JSON string
payment_instructions_instance = PaymentInstructions.from_json(json)
# print the JSON string representation of the object
print(PaymentInstructions.to_json())

# convert the object into a dict
payment_instructions_dict = payment_instructions_instance.to_dict()
# create an instance of PaymentInstructions from a dict
payment_instructions_from_dict = PaymentInstructions.from_dict(payment_instructions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


