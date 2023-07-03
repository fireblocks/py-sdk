# TravelRuleValidateTransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** | \&quot;isValid\&quot; will tell you if you have collected all the information needed for the travel rule data transfer. Once this field &#x3D; \&quot;true\&quot;, you can move on to the next step which is to transfer the front-end information to your back-end and perform Travel Rule Transaction create | 
**type** | **str** | \&quot;type\&quot; will tell you if the virtual asset value converted to FIAT value of the withdrawal request is above (&#x3D;TRAVELRULE) or below (&#x3D;BELOW_THRESHOLD) the threshold in your jurisdiction. If it is to an unhosted wallet which does not require travel rule information to  be sent and only collected, it will say NON_CUSTODIAL. | 
**beneficiary_address_type** | **str** | \&quot;beneficiaryAddressType\&quot; will tell you if your blockchain analytics provider or internal address book has been able to identify the wallet address. | 
**address_source** | **str** | \&quot;addressSource\&quot; will tell you if the address was found in your internal address book or identified by the blockchain analytics provider. | 
**beneficiary_vas_pdid** | **str** | The VASP DID of the beneficiary VASP | 
**beneficiary_vas_pname** | **str** | \&quot;beneficiaryVASPname\&quot; will tell you the name of the VASP that has been identified as the owner of the wallet address. This name is used in a subsequent call to get its DID. | 
**warnings** | **List[str]** | \&quot;errors/warnings\&quot; will tell you what information about the beneficiary you need to collect from the sender. | 

## Example

```python
from fireblocks_client.models.travel_rule_validate_transaction_response import TravelRuleValidateTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleValidateTransactionResponse from a JSON string
travel_rule_validate_transaction_response_instance = TravelRuleValidateTransactionResponse.from_json(json)
# print the JSON string representation of the object
print TravelRuleValidateTransactionResponse.to_json()

# convert the object into a dict
travel_rule_validate_transaction_response_dict = travel_rule_validate_transaction_response_instance.to_dict()
# create an instance of TravelRuleValidateTransactionResponse from a dict
travel_rule_validate_transaction_response_form_dict = travel_rule_validate_transaction_response.from_dict(travel_rule_validate_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


