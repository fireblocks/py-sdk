# Opportunity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique opportunity identifier. | [optional] 
**provider_id** | **str** | Lending protocol (&#x60;MORPHO&#x60; or &#x60;AAVE&#x60;). | [optional] 
**type** | **str** | Opportunity kind — vault or market. | [optional] 
**chain_id** | **str** | Chain identifier as a string (e.g. \&quot;1\&quot; for Ethereum mainnet). | [optional] 
**address** | **str** | Primary contract address for the vault or market. | [optional] 
**name** | **str** | Display name of the opportunity. | [optional] 
**symbol** | **str** | Symbol or share token ticker for the position asset. | [optional] 
**principal_asset** | [**EarnAsset**](EarnAsset.md) | Underlying token the user deposits (principal). | [optional] 
**position_asset** | [**EarnAsset**](EarnAsset.md) | Token representing the user’s position in the protocol (e.g. vault share). | [optional] 
**total_assets** | **str** | Human-readable total value locked / assets in the opportunity. | [optional] 
**liquidity** | **str** | Human-readable available liquidity. | [optional] 
**apy** | [**Apy**](Apy.md) | APY breakdown; values are percentages (e.g. 4.25 means 4.25%). | [optional] 
**performance_fee** | **str** | Performance fee as a human-readable decimal string. | [optional] 
**management_fee** | **str** | Management fee as a human-readable decimal string. | [optional] 
**exposure** | [**List[Exposure]**](Exposure.md) | Optional per-asset exposure breakdown. | [optional] 

## Example

```python
from fireblocks.models.opportunity import Opportunity

# TODO update the JSON string below
json = "{}"
# create an instance of Opportunity from a JSON string
opportunity_instance = Opportunity.from_json(json)
# print the JSON string representation of the object
print(Opportunity.to_json())

# convert the object into a dict
opportunity_dict = opportunity_instance.to_dict()
# create an instance of Opportunity from a dict
opportunity_from_dict = Opportunity.from_dict(opportunity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


