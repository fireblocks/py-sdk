# ChainInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_descriptor** | **str** | The protocol identifier (e.g. \&quot;ETH\&quot;/\&quot;SOL\&quot;). | 
**current_epoch** | **float** | The current epoch number of the blockchain network. | 
**epoch_elapsed** | **float** | The percentage of time that has elapsed within the current epoch, represented as a decimal value between 0 and 1. | 
**epoch_duration** | **float** | The total duration in milliseconds of a single epoch. | 
**additional_info** | [**AdditionalInfo**](AdditionalInfo.md) |  | 

## Example

```python
from fireblocks.models.chain_info_response import ChainInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChainInfoResponse from a JSON string
chain_info_response_instance = ChainInfoResponse.from_json(json)
# print the JSON string representation of the object
print(ChainInfoResponse.to_json())

# convert the object into a dict
chain_info_response_dict = chain_info_response_instance.to_dict()
# create an instance of ChainInfoResponse from a dict
chain_info_response_from_dict = ChainInfoResponse.from_dict(chain_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


