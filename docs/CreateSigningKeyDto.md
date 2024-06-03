# CreateSigningKeyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_device_key_id** | **str** | The ID, name or label of the key specified on the customer&#39;s signing device. | 
**signed_cert_pem** | **str** | The signed certificate that includes the public key PEM of the signing key, signed by a validation key. | 
**agent_user_id** | **str** | Id of user to which this key belongs | 

## Example

```python
from fireblocks.models.create_signing_key_dto import CreateSigningKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSigningKeyDto from a JSON string
create_signing_key_dto_instance = CreateSigningKeyDto.from_json(json)
# print the JSON string representation of the object
print(CreateSigningKeyDto.to_json())

# convert the object into a dict
create_signing_key_dto_dict = create_signing_key_dto_instance.to_dict()
# create an instance of CreateSigningKeyDto from a dict
create_signing_key_dto_from_dict = CreateSigningKeyDto.from_dict(create_signing_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


