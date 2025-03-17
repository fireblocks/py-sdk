# TravelRuleVASP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**did** | **str** | The Decentralized Identifier (DID) of the VASP. | 
**name** | **str** | The name of the VASP. | 
**verification_status** | **str** | The current verification status of the VASP. | 
**address_line1** | **str** | The first line of the VASP&#39;s address. | 
**address_line2** | **str** | The second line of the VASP&#39;s address (if applicable). | [optional] 
**city** | **str** | The city where the VASP is located. | 
**country** | **str** | The country where the VASP is registered (ISO-3166 Alpha-2 code). | 
**email_domains** | **str** | Comma-separated list of email domains associated with the VASP. | 
**website** | **str** | The official website of the VASP. | 
**logo** | **str** | URL to the logo of the VASP. | [optional] 
**legal_structure** | **str** | The legal structure of the VASP (e.g., Corporation, LLC). | 
**legal_name** | **str** | The legal name of the VASP. | 
**year_founded** | **str** | The year the VASP was founded. | 
**incorporation_country** | **str** | The country where the VASP is incorporated (ISO-3166 Alpha-2 code). | 
**is_regulated** | **str** | Indicates whether the VASP is regulated. | 
**other_names** | **str** | Other names the VASP is known by. | [optional] 
**identification_type** | **str** | The type of identification used by the VASP. | [optional] 
**identification_country** | **str** | The country of identification for the VASP (ISO-3166 Alpha-2 code). | [optional] 
**business_number** | **str** | The business registration number of the VASP. | [optional] 
**regulatory_authorities** | **str** | The regulatory authorities overseeing the VASP. | [optional] 
**jurisdictions** | **str** | The jurisdictions where the VASP operates. | 
**street** | **str** | The street name where the VASP is located. | [optional] 
**number** | **str** | The building number of the VASP&#39;s address. | [optional] 
**unit** | **str** | The unit or suite number of the VASP&#39;s address. | [optional] 
**post_code** | **str** | The postal code of the VASP&#39;s location. | [optional] 
**state** | **str** | The state or region where the VASP is located. | [optional] 
**certificates** | **str** | Certificates or licenses held by the VASP. | [optional] 
**description** | **str** | A brief description of the VASP. | [optional] 
**travel_rule_openvasp** | **str** | Travel rule compliance status for OpenVASP. | [optional] 
**travel_rule_sygna** | **str** | Travel rule compliance status for Sygna. | [optional] 
**travel_rule_trisa** | **str** | Travel rule compliance status for TRISA. | [optional] 
**travel_rule_trlight** | **str** | Travel rule compliance status for TRLight. | 
**travel_rule_email** | **str** | Travel rule compliance status for EMAIL. | [optional] 
**travel_rule_trp** | **str** | Travel rule compliance status for TRP. | [optional] 
**travel_rule_shyft** | **str** | Travel rule compliance status for Shyft. | [optional] 
**travel_rule_ustravelrulewg** | **str** | Travel rule compliance status for US Travel Rule WG. | [optional] 
**created_at** | **str** | Timestamp when the VASP record was created. | 
**created_by** | **str** | User or system that created the VASP record. | [optional] 
**updated_at** | **str** | Timestamp of the last update to the VASP record. | [optional] 
**updated_by** | **str** | User or system that last updated the VASP record. | [optional] 
**last_sent_date** | **str** | The last date a transaction was sent by the VASP. | [optional] 
**last_received_date** | **str** | The last date a transaction was received by the VASP. | [optional] 
**documents** | **str** | Documents associated with the VASP. | [optional] 
**has_admin** | **bool** | Indicates if the VASP has an admin. | 
**is_notifiable** | **bool** | Indicates if the VASP is notifiable for compliance reasons. | 
**issuers** | [**TravelRuleIssuers**](TravelRuleIssuers.md) |  | 

## Example

```python
from fireblocks.models.travel_rule_vasp import TravelRuleVASP

# TODO update the JSON string below
json = "{}"
# create an instance of TravelRuleVASP from a JSON string
travel_rule_vasp_instance = TravelRuleVASP.from_json(json)
# print the JSON string representation of the object
print(TravelRuleVASP.to_json())

# convert the object into a dict
travel_rule_vasp_dict = travel_rule_vasp_instance.to_dict()
# create an instance of TravelRuleVASP from a dict
travel_rule_vasp_from_dict = TravelRuleVASP.from_dict(travel_rule_vasp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


