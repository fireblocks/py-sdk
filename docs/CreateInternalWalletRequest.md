# CreateInternalWalletRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the wallet&#39;s display name | [optional] 
**customer_ref_id** | **str** | Optional - Sets a customer reference ID | [optional] 

## Example

```python
from fireblocks_client.models.create_internal_wallet_request import CreateInternalWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInternalWalletRequest from a JSON string
create_internal_wallet_request_instance = CreateInternalWalletRequest.from_json(json)
# print the JSON string representation of the object
print CreateInternalWalletRequest.to_json()

# convert the object into a dict
create_internal_wallet_request_dict = create_internal_wallet_request_instance.to_dict()
# create an instance of CreateInternalWalletRequest from a dict
create_internal_wallet_request_form_dict = create_internal_wallet_request.from_dict(create_internal_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


