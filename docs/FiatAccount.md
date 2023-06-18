# FiatAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**FiatAccountType**](FiatAccountType.md) |  | [optional] 
**name** | **str** | Display name of the fiat account | [optional] 
**address** | **str** |  | [optional] 
**assets** | [**List[FiatAsset]**](FiatAsset.md) |  | [optional] 

## Example

```python
from fireblocks_client.models.fiat_account import FiatAccount

# TODO update the JSON string below
json = "{}"
# create an instance of FiatAccount from a JSON string
fiat_account_instance = FiatAccount.from_json(json)
# print the JSON string representation of the object
print FiatAccount.to_json()

# convert the object into a dict
fiat_account_dict = fiat_account_instance.to_dict()
# create an instance of FiatAccount from a dict
fiat_account_form_dict = fiat_account.from_dict(fiat_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


