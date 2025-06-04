# EmbeddedWalletAddressDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | accountName | 
**account_id** | **str** | accountId | 
**asset** | **str** | asset | 
**address** | **str** | address | 
**address_type** | **str** | addressType | 
**address_description** | **str** | addressDescription | 
**tag** | **str** | tag | 
**address_index** | **float** | addressIndex | [optional] 
**change** | **float** | change | [optional] 
**coin_type** | **float** | Unique identifier of an asset (0 for BTC, 60 for ETH, etc.) | [optional] 
**customer_ref_id** | **str** | customerRefId | [optional] 
**address_format** | **str** | addressFormat | [optional] 
**legacy_address** | **str** | legacyAddress | [optional] 
**payment_address** | **str** | paymentAddress | [optional] 
**user_defined** | **bool** | userDefined | [optional] 
**state** | **str** | state | [optional] 

## Example

```python
from fireblocks.models.embedded_wallet_address_details import EmbeddedWalletAddressDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedWalletAddressDetails from a JSON string
embedded_wallet_address_details_instance = EmbeddedWalletAddressDetails.from_json(json)
# print the JSON string representation of the object
print(EmbeddedWalletAddressDetails.to_json())

# convert the object into a dict
embedded_wallet_address_details_dict = embedded_wallet_address_details_instance.to_dict()
# create an instance of EmbeddedWalletAddressDetails from a dict
embedded_wallet_address_details_from_dict = EmbeddedWalletAddressDetails.from_dict(embedded_wallet_address_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


