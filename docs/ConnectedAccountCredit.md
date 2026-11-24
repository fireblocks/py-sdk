# ConnectedAccountCredit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The credit amount, as a decimal number string. | 
**denominated_asset_id** | **str** | The asset ID the credit amount is denominated in. Omitted when the denomination asset ID is unavailable; the amount is still returned, but its denomination is unknown. Do not assume it matches the asset used for totalBalance. | [optional] 

## Example

```python
from fireblocks.models.connected_account_credit import ConnectedAccountCredit

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountCredit from a JSON string
connected_account_credit_instance = ConnectedAccountCredit.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountCredit.to_json())

# convert the object into a dict
connected_account_credit_dict = connected_account_credit_instance.to_dict()
# create an instance of ConnectedAccountCredit from a dict
connected_account_credit_from_dict = ConnectedAccountCredit.from_dict(connected_account_credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


