# TravelRuleOwnershipProof


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of ownership proof | 
**id** | **str** | Identification number | 
**name** | **str** | Name of owner | 
**country** | **str** | Country of issuance | 
**issue_date** | **str** | Date of issuance | 
**issuer** | **str** | Name of issuing entity | 

## Example

```python
from fireblocks_client.models.travel_rule_ownership_proof import TravelRuleOwnershipProof

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleOwnershipProof from a JSON string
travel_rule_ownership_proof_instance = TravelRuleOwnershipProof.from_json(json)
# print the JSON string representation of the object
print TravelRuleOwnershipProof.to_json()

# convert the object into a dict
travel_rule_ownership_proof_dict = travel_rule_ownership_proof_instance.to_dict()
# create an instance of TravelRuleOwnershipProof from a dict
travel_rule_ownership_proof_form_dict = travel_rule_ownership_proof.from_dict(travel_rule_ownership_proof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


