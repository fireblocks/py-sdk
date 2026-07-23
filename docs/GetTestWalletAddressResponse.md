# GetTestWalletAddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_wallet_address** | **str** | Ethereum address derived from BLOCKCHAIN_LINK_EXTERNAL_WALLET_PRIVATE_KEY (for UI display). | [optional] 

## Example

```python
from fireblocks.models.get_test_wallet_address_response import GetTestWalletAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTestWalletAddressResponse from a JSON string
get_test_wallet_address_response_instance = GetTestWalletAddressResponse.from_json(json)
# print the JSON string representation of the object
print(GetTestWalletAddressResponse.to_json())

# convert the object into a dict
get_test_wallet_address_response_dict = get_test_wallet_address_response_instance.to_dict()
# create an instance of GetTestWalletAddressResponse from a dict
get_test_wallet_address_response_from_dict = GetTestWalletAddressResponse.from_dict(get_test_wallet_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


