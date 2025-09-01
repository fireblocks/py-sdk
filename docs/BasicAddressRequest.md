# BasicAddressRequest

Basic external wallet request with address information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The wallet&#39;s address (or xpub) of the external wallet | 
**tag** | **str** | For XRP wallets, the destination tag; for EOS/XLM, the memo; for the fiat providers (BLINC by BCB Group), the Bank Transfer Description | [optional] 

## Example

```python
from fireblocks.models.basic_address_request import BasicAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BasicAddressRequest from a JSON string
basic_address_request_instance = BasicAddressRequest.from_json(json)
# print the JSON string representation of the object
print(BasicAddressRequest.to_json())

# convert the object into a dict
basic_address_request_dict = basic_address_request_instance.to_dict()
# create an instance of BasicAddressRequest from a dict
basic_address_request_from_dict = BasicAddressRequest.from_dict(basic_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


