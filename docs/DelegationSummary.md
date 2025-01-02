# DelegationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**List[AmountAndChainDescriptor]**](AmountAndChainDescriptor.md) | An array of objects containing chain descriptors and associated amounts, representing active positions. | 
**inactive** | [**List[AmountAndChainDescriptor]**](AmountAndChainDescriptor.md) | An array of objects containing chain descriptors and associated amounts, representing inactive positions. | 
**rewards_amount** | [**List[AmountAndChainDescriptor]**](AmountAndChainDescriptor.md) | An array of objects containing chain descriptors and associated amounts, representing rewards positions. | 
**total_staked** | [**List[AmountAndChainDescriptor]**](AmountAndChainDescriptor.md) | An array of objects with chain descriptors and total staked amounts, representing the combined staked totals of active and inactive positions. | 

## Example

```python
from fireblocks.models.delegation_summary import DelegationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DelegationSummary from a JSON string
delegation_summary_instance = DelegationSummary.from_json(json)
# print the JSON string representation of the object
print(DelegationSummary.to_json())

# convert the object into a dict
delegation_summary_dict = delegation_summary_instance.to_dict()
# create an instance of DelegationSummary from a dict
delegation_summary_from_dict = DelegationSummary.from_dict(delegation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


