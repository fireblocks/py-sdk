# AddAssetToContractRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The contract&#39;s address (or xpub) of the wallet | 
**tag** | **str** | The destination tag, for XRP wallets | [optional] 

## Example

```python
from fireblocks_client.models.add_asset_to_contract_request import AddAssetToContractRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddAssetToContractRequest from a JSON string
add_asset_to_contract_request_instance = AddAssetToContractRequest.from_json(json)
# print the JSON string representation of the object
print AddAssetToContractRequest.to_json()

# convert the object into a dict
add_asset_to_contract_request_dict = add_asset_to_contract_request_instance.to_dict()
# create an instance of AddAssetToContractRequest from a dict
add_asset_to_contract_request_form_dict = add_asset_to_contract_request.from_dict(add_asset_to_contract_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


