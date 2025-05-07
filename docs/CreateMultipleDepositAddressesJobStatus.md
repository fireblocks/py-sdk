# CreateMultipleDepositAddressesJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**addresses** | [**List[NewAddress]**](NewAddress.md) |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from fireblocks.models.create_multiple_deposit_addresses_job_status import CreateMultipleDepositAddressesJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultipleDepositAddressesJobStatus from a JSON string
create_multiple_deposit_addresses_job_status_instance = CreateMultipleDepositAddressesJobStatus.from_json(json)
# print the JSON string representation of the object
print(CreateMultipleDepositAddressesJobStatus.to_json())

# convert the object into a dict
create_multiple_deposit_addresses_job_status_dict = create_multiple_deposit_addresses_job_status_instance.to_dict()
# create an instance of CreateMultipleDepositAddressesJobStatus from a dict
create_multiple_deposit_addresses_job_status_from_dict = CreateMultipleDepositAddressesJobStatus.from_dict(create_multiple_deposit_addresses_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


