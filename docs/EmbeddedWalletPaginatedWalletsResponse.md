# EmbeddedWalletPaginatedWalletsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EmbeddedWallet]**](EmbeddedWallet.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks.models.embedded_wallet_paginated_wallets_response import EmbeddedWalletPaginatedWalletsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletPaginatedWalletsResponse from a JSON string
embedded_wallet_paginated_wallets_response_instance = EmbeddedWalletPaginatedWalletsResponse.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletPaginatedWalletsResponse.to_json())

# convert the object into a dict
embedded_wallet_paginated_wallets_response_dict = embedded_wallet_paginated_wallets_response_instance.to_dict()
# create an instance of EmbeddedWalletPaginatedWalletsResponse from a dict
embedded_wallet_paginated_wallets_response_from_dict = EmbeddedWalletPaginatedWalletsResponse.from_dict(embedded_wallet_paginated_wallets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


