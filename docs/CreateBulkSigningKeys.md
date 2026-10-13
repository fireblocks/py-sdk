# CreateBulkSigningKeys


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_key_id** | **str** | The id of the validation key that signed every certificate in this request, as returned when the validation key was registered. Not the signingDeviceKeyId of any signing key. | 
**keys** | [**List[BulkSigningKey]**](BulkSigningKey.md) | The signing keys to register. | 

## Example

```python
from fireblocks.models.create_bulk_signing_keys import CreateBulkSigningKeys

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkSigningKeys from a JSON string
create_bulk_signing_keys_instance = CreateBulkSigningKeys.from_json(json)
# print the JSON string representation of the object
print(CreateBulkSigningKeys.to_json())

# convert the object into a dict
create_bulk_signing_keys_dict = create_bulk_signing_keys_instance.to_dict()
# create an instance of CreateBulkSigningKeys from a dict
create_bulk_signing_keys_from_dict = CreateBulkSigningKeys.from_dict(create_bulk_signing_keys_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


