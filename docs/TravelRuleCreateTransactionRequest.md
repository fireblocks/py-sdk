# TravelRuleCreateTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originator_vas_pdid** | **str** | The Decentralized Identifier (DID) of the exchange (VASP) that is sending the virtual assets. This identifier is unique to the exchange and is generated when the exchange&#39;s account is  created in the Notabene network. | [optional] 
**beneficiary_vas_pdid** | **str** | The Decentralized Identifier (DID) of the exchange (VASP) that is receiving the virtual assets. This identifier is unique to the exchange and is generated when the exchange&#39;s account is  created in the Notabene network. | [optional] 
**originator_vas_pname** | **str** | The name of the VASP acting as the transaction originator. | [optional] 
**beneficiary_vas_pname** | **str** | The name of the VASP acting as the transaction beneficiary. | [optional] 
**beneficiary_vas_pwebsite** | **str** | The website of the VASP acting as the transaction beneficiary. | [optional] 
**transaction_blockchain_info** | [**TravelRuleTransactionBlockchainInfo**](TravelRuleTransactionBlockchainInfo.md) |  | [optional] 
**originator** | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) |  | 
**beneficiary** | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) |  | 
**encrypted** | **str** | Encrypted data related to the transaction. | [optional] 
**protocol** | **str** | The protocol used to perform the travel rule. | [optional] 
**target_protocol** | **str** | The target protocol for GTR (Global Travel Rule) transfers. | [optional] 
**skip_beneficiary_data_validation** | **bool** | Whether to skip validation of beneficiary data. | [optional] 
**travel_rule_behavior** | **bool** | Whether to check if the transaction complies with the travel rule in the beneficiary VASP&#39;s jurisdiction. | [optional] 
**originator_ref** | **str** | A reference ID related to the originator of the transaction. | [optional] 
**beneficiary_ref** | **str** | A reference ID related to the beneficiary of the transaction. | [optional] 
**travel_rule_behavior_ref** | **str** | A reference ID related to the travel rule behavior. | [optional] 
**originator_proof** | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) |  | [optional] 
**beneficiary_proof** | [**TravelRuleOwnershipProof**](TravelRuleOwnershipProof.md) |  | [optional] 
**beneficiary_did** | **str** | The Decentralized Identifier (DID) of the person at the receiving exchange (VASP).  This identifier is generated when the customer is registered in the Notabene network,  or automatically created based on the &#x60;beneficiaryRef&#x60;.  - If neither &#x60;beneficiaryRef&#x60; nor &#x60;beneficiaryDid&#x60; is provided in the &#x60;txCreate&#x60; payload,    a new random DID is generated for every transaction. | [optional] 
**originator_did** | **str** | The Decentralized Identifier (DID) of the person at the exchange (VASP) who is requesting the withdrawal. This identifier is generated when the customer is registered in the Notabene network or automatically created based on the &#x60;originatorRef&#x60;.  - If neither &#x60;originatorRef&#x60; nor &#x60;originatorDid&#x60; is provided in the &#x60;txCreate&#x60; payload,    a new random DID is generated for every transaction. | [optional] 
**is_non_custodial** | **bool** | Indicates if the transaction involves a non-custodial wallet. | [optional] 

## Example

```python
from fireblocks.models.travel_rule_create_transaction_request import TravelRuleCreateTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleCreateTransactionRequest from a JSON string
travel_rule_create_transaction_request_instance = TravelRuleCreateTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(TravelRuleCreateTransactionRequest.to_json())

# convert the object into a dict
travel_rule_create_transaction_request_dict = travel_rule_create_transaction_request_instance.to_dict()
# create an instance of TravelRuleCreateTransactionRequest from a dict
travel_rule_create_transaction_request_from_dict = TravelRuleCreateTransactionRequest.from_dict(travel_rule_create_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


