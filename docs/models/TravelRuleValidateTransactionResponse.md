# fireblocks_client.model.travel_rule_validate_transaction_response.TravelRuleValidateTransactionResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**beneficiaryVASPname** | str,  | str,  | \&quot;beneficiaryVASPname\&quot; will tell you the name of the VASP that has been identified as the owner of the wallet address. This name is used in a subsequent call to get its DID. | 
**addressSource** | str,  | str,  | \&quot;addressSource\&quot; will tell you if the address was found in your internal address book or identified by the blockchain analytics provider. | 
**beneficiaryAddressType** | str,  | str,  | \&quot;beneficiaryAddressType\&quot; will tell you if your blockchain analytics provider or internal address book has been able to identify the wallet address. | 
**isValid** | bool,  | BoolClass,  | \&quot;isValid\&quot; will tell you if you have collected all the information needed for the travel rule data transfer. Once this field &#x3D; \&quot;true\&quot;, you can move on to the next step which is to transfer the front-end information to your back-end and perform Travel Rule Transaction create | 
**[warnings](#warnings)** | list, tuple,  | tuple,  | \&quot;errors/warnings\&quot; will tell you what information about the beneficiary you need to collect from the sender. | 
**type** | str,  | str,  | \&quot;type\&quot; will tell you if the virtual asset value converted to FIAT value of the withdrawal request is above (&#x3D;TRAVELRULE) or below (&#x3D;BELOW_THRESHOLD) the threshold in your jurisdiction. If it is to an unhosted wallet which does not require travel rule information to be sent and only collected, it will say NON_CUSTODIAL. | 
**beneficiaryVASPdid** | str,  | str,  | The VASP DID of the beneficiary VASP | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# warnings

\"errors/warnings\" will tell you what information about the beneficiary you need to collect from the sender.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | \&quot;errors/warnings\&quot; will tell you what information about the beneficiary you need to collect from the sender. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

