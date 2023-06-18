# AddCollateralRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_request** | [**TransactionRequest**](TransactionRequest.md) |  | [optional] 
**is_src_collateral** | **bool** | optional | [optional] 

## Example

```python
from fireblocks_client.models.add_collateral_request_body import AddCollateralRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddCollateralRequestBody from a JSON string
add_collateral_request_body_instance = AddCollateralRequestBody.from_json(json)
# print the JSON string representation of the object
print AddCollateralRequestBody.to_json()

# convert the object into a dict
add_collateral_request_body_dict = add_collateral_request_body_instance.to_dict()
# create an instance of AddCollateralRequestBody from a dict
add_collateral_request_body_form_dict = add_collateral_request_body.from_dict(add_collateral_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


