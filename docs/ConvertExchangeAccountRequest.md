# ConvertExchangeAccountRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_asset** | **str** | Name of the source asset (must be in a currency that is supported for conversions in the selected exchange type that corresponds to your exchange ID) | 
**dest_asset** | **str** | Name of the destination asset (must be in a currency that is supported for conversions in the selected exchange type that corresponds to your exchange ID) | 
**amount** | **float** | The amount to transfer (in the currency of the source asset) | 

## Example

```python
from fireblocks_client.models.convert_exchange_account_request import ConvertExchangeAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertExchangeAccountRequest from a JSON string
convert_exchange_account_request_instance = ConvertExchangeAccountRequest.from_json(json)
# print the JSON string representation of the object
print ConvertExchangeAccountRequest.to_json()

# convert the object into a dict
convert_exchange_account_request_dict = convert_exchange_account_request_instance.to_dict()
# create an instance of ConvertExchangeAccountRequest from a dict
convert_exchange_account_request_form_dict = convert_exchange_account_request.from_dict(convert_exchange_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


