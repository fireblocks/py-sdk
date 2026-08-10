# TravelRuleIssuer

An attestation of a single VASP attribute by an issuing party.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_did** | **str** | The Decentralized Identifier (DID) of the party that issued the attestation. | 
**issued_date** | **str** | Timestamp when the attestation was issued. Present on every attestation observed to date, but not guaranteed, so treat it as optional. | [optional] 
**issuer_name** | **str** | The human-readable name of the issuing party. Returned only for issuers that publish a name, such as GLEIF; absent for others, including in the same response. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_issuer import TravelRuleIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleIssuer from a JSON string
travel_rule_issuer_instance = TravelRuleIssuer.from_json(json)
# print the JSON string representation of the object
print(TravelRuleIssuer.to_json())

# convert the object into a dict
travel_rule_issuer_dict = travel_rule_issuer_instance.to_dict()
# create an instance of TravelRuleIssuer from a dict
travel_rule_issuer_from_dict = TravelRuleIssuer.from_dict(travel_rule_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


