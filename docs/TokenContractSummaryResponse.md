# TokenContractSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_asset_id** | **str** | The base asset ID | 
**contract_address** | **str** | The contract address | 
**total_addresses** | **float** | Total number of addresses with balances | 
**total_supply** | **str** | The total supply of the token | 

## Example

```python
from fireblocks.models.token_contract_summary_response import TokenContractSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenContractSummaryResponse from a JSON string
token_contract_summary_response_instance = TokenContractSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(TokenContractSummaryResponse.to_json())

# convert the object into a dict
token_contract_summary_response_dict = token_contract_summary_response_instance.to_dict()
# create an instance of TokenContractSummaryResponse from a dict
token_contract_summary_response_from_dict = TokenContractSummaryResponse.from_dict(token_contract_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


