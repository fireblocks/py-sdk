# PaymentInstructionsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.payment_instructions_details import PaymentInstructionsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentInstructionsDetails from a JSON string
payment_instructions_details_instance = PaymentInstructionsDetails.from_json(json)
# print the JSON string representation of the object
print(PaymentInstructionsDetails.to_json())

# convert the object into a dict
payment_instructions_details_dict = payment_instructions_details_instance.to_dict()
# create an instance of PaymentInstructionsDetails from a dict
payment_instructions_details_from_dict = PaymentInstructionsDetails.from_dict(payment_instructions_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


