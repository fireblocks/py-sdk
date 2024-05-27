# RelatedTransactionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tx_id** | **str** | The transaction ID | 
**completed** | **bool** | Is the transaction completed or not | 

## Example

```python
from fireblocks_client.models.related_transaction_dto import RelatedTransactionDto

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedTransactionDto from a JSON string
related_transaction_dto_instance = RelatedTransactionDto.from_json(json)
# print the JSON string representation of the object
print RelatedTransactionDto.to_json()

# convert the object into a dict
related_transaction_dto_dict = related_transaction_dto_instance.to_dict()
# create an instance of RelatedTransactionDto from a dict
related_transaction_dto_form_dict = related_transaction_dto.from_dict(related_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


