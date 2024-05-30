# TravelRuleOwnershipProof


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of ownership proof | [optional] 
**proof** | **str** | Identification number | [optional] 

## Example

```python
from fireblocks_client.models.travel_rule_ownership_proof import TravelRuleOwnershipProof

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleOwnershipProof from a JSON string
travel_rule_ownership_proof_instance = TravelRuleOwnershipProof.from_json(json)
# print the JSON string representation of the object
print(TravelRuleOwnershipProof.to_json())

# convert the object into a dict
travel_rule_ownership_proof_dict = travel_rule_ownership_proof_instance.to_dict()
# create an instance of TravelRuleOwnershipProof from a dict
travel_rule_ownership_proof_from_dict = TravelRuleOwnershipProof.from_dict(travel_rule_ownership_proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


