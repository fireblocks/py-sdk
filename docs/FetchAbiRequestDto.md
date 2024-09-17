# FetchAbiRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset_id** | **str** | The blockchain base assetId | 
**contract_address** | **str** | The contract&#39;s onchain address | 

## Example

```python
from fireblocks.models.fetch_abi_request_dto import FetchAbiRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of FetchAbiRequestDto from a JSON string
fetch_abi_request_dto_instance = FetchAbiRequestDto.from_json(json)
# print the JSON string representation of the object
print(FetchAbiRequestDto.to_json())

# convert the object into a dict
fetch_abi_request_dto_dict = fetch_abi_request_dto_instance.to_dict()
# create an instance of FetchAbiRequestDto from a dict
fetch_abi_request_dto_from_dict = FetchAbiRequestDto.from_dict(fetch_abi_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


