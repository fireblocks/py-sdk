# TravelRuleValidateFullTransactionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_asset** | **str** | The asset involved in the transaction | 
**transaction_amount** | **str** | The amount of the transaction | 
**originator_did** | **str** | The DID of the transaction originator | 
**beneficiary_did** | **str** | The DID of the transaction beneficiary | 
**originator_vas_pdid** | **str** | The VASP ID of the transaction originator | 
**beneficiary_vas_pdid** | **str** | The VASP ID of the transaction beneficiary | 
**beneficiary_vas_pname** | **str** | The name of the VASP acting as the beneficiary | 
**transaction_blockchain_info** | [**TravelRuleValidateFullTransactionRequestTransactionBlockchainInfo**](TravelRuleValidateFullTransactionRequestTransactionBlockchainInfo.md) |  | 
**originator** | [**TravelRuleValidateFullTransactionRequestOriginator**](TravelRuleValidateFullTransactionRequestOriginator.md) |  | 
**beneficiary** | [**TravelRuleValidateFullTransactionRequestBeneficiary**](TravelRuleValidateFullTransactionRequestBeneficiary.md) |  | 
**encrypted** | **str** | Encrypted data related to the transaction | 
**protocol** | **str** | The protocol used to perform the travel rule | 
**notification_email** | **str** | The email address where a notification should be sent upon completion of the travel rule | 
**skip_beneficiary_data_validation** | **bool** | Whether to skip validation of beneficiary data | 
**travel_rule_behavior** | **bool** | Whether to check if the transaction is a TRAVEL_RULE in the beneficiary VASP&#39;s jurisdiction | 
**originator_proof** | [**TravelRuleValidateFullTransactionRequestOriginatorProof**](TravelRuleValidateFullTransactionRequestOriginatorProof.md) |  | 
**beneficiary_proof** | [**TravelRuleValidateFullTransactionRequestBeneficiaryProof**](TravelRuleValidateFullTransactionRequestBeneficiaryProof.md) |  | 
**pii** | [**TravelRuleValidateFullTransactionRequestPii**](TravelRuleValidateFullTransactionRequestPii.md) |  | 

## Example

```python
from fireblocks_client.models.travel_rule_validate_full_transaction_request import TravelRuleValidateFullTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateFullTransactionRequest from a JSON string
travel_rule_validate_full_transaction_request_instance = TravelRuleValidateFullTransactionRequest.from_json(json)
# print the JSON string representation of the object
print TravelRuleValidateFullTransactionRequest.to_json()

# convert the object into a dict
travel_rule_validate_full_transaction_request_dict = travel_rule_validate_full_transaction_request_instance.to_dict()
# create an instance of TravelRuleValidateFullTransactionRequest from a dict
travel_rule_validate_full_transaction_request_form_dict = travel_rule_validate_full_transaction_request.from_dict(travel_rule_validate_full_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


