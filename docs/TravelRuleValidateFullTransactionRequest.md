# TravelRuleValidateFullTransactionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**originator_vas_pdid** | **str** | The Decentralized Identifier (DID) of the exchange (VASP) that is sending the virtual assets. This identifier is unique to the exchange and is generated when the exchange&#39;s account is  created in the Notabene network. | [optional] 
**beneficiary_vas_pdid** | **str** | The Decentralized Identifier (DID) of the exchange (VASP) that is receiving the virtual assets. This identifier is unique to the exchange and is generated when the exchange&#39;s account is  created in the Notabene network. | [optional] 
**transaction_asset** | **str** | Transaction asset symbol (e.g., BTC, ETH, USDC).  By using the &#x60;notation&#x60; query string, users can select the type of asset notation: - &#x60;fireblocks&#x60;: Converts asset symbols to Fireblocks notation. - &#x60;notabene&#x60;: Retains the original Notabene asset symbol format. | [optional] 
**transaction_amount** | **str** | Transaction amount in the transaction asset. For example, if the asset is BTC, the amount  is the value in BTC units.  By using the &#x60;notation&#x60; query string, users can select the type of amount notation: - &#x60;fireblocks&#x60;: Converts the amount to Fireblocks notation (e.g., adjusted for decimals). - &#x60;notabene&#x60;: Retains the original Notabene amount format. | [optional] 
**originator_vas_pname** | **str** | The name of the VASP acting as the transaction originator. | [optional] 
**beneficiary_vas_pname** | **str** | The name of the VASP acting as the transaction beneficiary. | [optional] 
**transaction_blockchain_info** | [**TravelRuleTransactionBlockchainInfo**](TravelRuleTransactionBlockchainInfo.md) |  | [optional] 
**originator** | [**TravelRuleValidatePiiIVMS**](TravelRuleValidatePiiIVMS.md) |  | 
**beneficiary** | [**TravelRuleValidatePiiIVMS**](TravelRuleValidatePiiIVMS.md) |  | 
**encrypted** | **str** | Encrypted data related to the transaction. | [optional] 
**protocol** | **str** | The protocol used to perform the travel rule. | [optional] 
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
**notification_email** | **str** | The email address where a notification should be sent upon completion of the travel rule | [optional] 
**pii** | [**TravelRulePiiIVMS**](TravelRulePiiIVMS.md) |  | [optional] 
**pii_url** | **str** | The URL of the personal identifiable information related to the transaction | [optional] 

## Example

```python
from fireblocks.models.travel_rule_validate_full_transaction_request import TravelRuleValidateFullTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateFullTransactionRequest from a JSON string
travel_rule_validate_full_transaction_request_instance = TravelRuleValidateFullTransactionRequest.from_json(json)
# print the JSON string representation of the object
print(TravelRuleValidateFullTransactionRequest.to_json())

# convert the object into a dict
travel_rule_validate_full_transaction_request_dict = travel_rule_validate_full_transaction_request_instance.to_dict()
# create an instance of TravelRuleValidateFullTransactionRequest from a dict
travel_rule_validate_full_transaction_request_from_dict = TravelRuleValidateFullTransactionRequest.from_dict(travel_rule_validate_full_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


