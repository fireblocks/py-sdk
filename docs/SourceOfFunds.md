# SourceOfFunds

Information about the source and purpose of the funds being transacted. Used by providers that require additional context for compliance and reporting. Provide this field when the provider manifest indicates it is required. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_for_payment** | [**ReasonForPaymentEnum**](ReasonForPaymentEnum.md) |  | [optional] 

## Example

```python
from fireblocks.models.source_of_funds import SourceOfFunds

# TODO update the JSON string below
json = "{}"
# create an instance of SourceOfFunds from a JSON string
source_of_funds_instance = SourceOfFunds.from_json(json)
# print the JSON string representation of the object
print(SourceOfFunds.to_json())

# convert the object into a dict
source_of_funds_dict = source_of_funds_instance.to_dict()
# create an instance of SourceOfFunds from a dict
source_of_funds_from_dict = SourceOfFunds.from_dict(source_of_funds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


