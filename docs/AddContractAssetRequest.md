# AddContractAssetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The contract&#39;s address (or xpub) of the wallet | 
**tag** | **str** | The destination tag, for XRP wallets | [optional] 

## Example

```python
from fireblocks_client.models.add_contract_asset_request import AddContractAssetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddContractAssetRequest from a JSON string
add_contract_asset_request_instance = AddContractAssetRequest.from_json(json)
# print the JSON string representation of the object
print AddContractAssetRequest.to_json()

# convert the object into a dict
add_contract_asset_request_dict = add_contract_asset_request_instance.to_dict()
# create an instance of AddContractAssetRequest from a dict
add_contract_asset_request_form_dict = add_contract_asset_request.from_dict(add_contract_asset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


