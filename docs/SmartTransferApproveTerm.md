# SmartTransferApproveTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | **str** | Asset name | 
**amount** | **str** | Amount | 
**src_id** | **str** | Id of the vault that is used as the source of the asset. | 
**fee** | **str** | Transaction fee | [optional] 
**fee_level** | **str** | Transaction fee level. | [optional] 
**note** | **str** | Transaction note | [optional] 

## Example

```python
from fireblocks.models.smart_transfer_approve_term import SmartTransferApproveTerm

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferApproveTerm from a JSON string
smart_transfer_approve_term_instance = SmartTransferApproveTerm.from_json(json)
# print the JSON string representation of the object
print(SmartTransferApproveTerm.to_json())

# convert the object into a dict
smart_transfer_approve_term_dict = smart_transfer_approve_term_instance.to_dict()
# create an instance of SmartTransferApproveTerm from a dict
smart_transfer_approve_term_from_dict = SmartTransferApproveTerm.from_dict(smart_transfer_approve_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


