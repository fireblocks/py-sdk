# SmartTransferFundTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | Asset name | 
**amount** | **str** | Amount | 
**network_connection_id** | **str** | Id of the network connection used. | 
**src_id** | **str** | Id of the vault that is used as the source of the asset. | 
**src_type** | **str** | Source of the asset. | 
**fee** | **str** | Transaction fee | [optional] 
**fee_level** | **str** | Transaction fee level. | [optional] 
**note** | **str** | Transaction note | [optional] 

## Example

```python
from fireblocks.models.smart_transfer_fund_term import SmartTransferFundTerm

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferFundTerm from a JSON string
smart_transfer_fund_term_instance = SmartTransferFundTerm.from_json(json)
# print the JSON string representation of the object
print(SmartTransferFundTerm.to_json())

# convert the object into a dict
smart_transfer_fund_term_dict = smart_transfer_fund_term_instance.to_dict()
# create an instance of SmartTransferFundTerm from a dict
smart_transfer_fund_term_from_dict = SmartTransferFundTerm.from_dict(smart_transfer_fund_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


