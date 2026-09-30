# CantonCallDetails

A call made through the Canton calls endpoint. Written once and never changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The shape of this block. Stamped at creation and never changed, so a reader always knows which version it is holding. | [optional] 
**domain** | [**CantonDomainEnum**](CantonDomainEnum.md) |  | [optional] 
**type** | **str** | The call type, matching the &#x60;type&#x60; sent when the call was created. | [optional] 
**vendor** | [**CantonVendorEnum**](CantonVendorEnum.md) |  | [optional] 
**original_transaction_id** | **str** | The transaction this call acts on. On a withdraw it is the allocation that was withdrawn, so the withdraw transaction read on its own still says what it withdrew. | [optional] 

## Example

```python
from fireblocks.models.canton_call_details import CantonCallDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CantonCallDetails from a JSON string
canton_call_details_instance = CantonCallDetails.from_json(json)
# print the JSON string representation of the object
print(CantonCallDetails.to_json())

# convert the object into a dict
canton_call_details_dict = canton_call_details_instance.to_dict()
# create an instance of CantonCallDetails from a dict
canton_call_details_from_dict = CantonCallDetails.from_dict(canton_call_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


