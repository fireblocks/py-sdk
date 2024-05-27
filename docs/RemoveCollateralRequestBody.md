# RemoveCollateralRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_request** | [**TransactionRequest**](TransactionRequest.md) |  | [optional] 
**is_dst_collateral** | **bool** | optional | [optional] 

## Example

```python
from fireblocks_client.models.remove_collateral_request_body import RemoveCollateralRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveCollateralRequestBody from a JSON string
remove_collateral_request_body_instance = RemoveCollateralRequestBody.from_json(json)
# print the JSON string representation of the object
print RemoveCollateralRequestBody.to_json()

# convert the object into a dict
remove_collateral_request_body_dict = remove_collateral_request_body_instance.to_dict()
# create an instance of RemoveCollateralRequestBody from a dict
remove_collateral_request_body_form_dict = remove_collateral_request_body.from_dict(remove_collateral_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


