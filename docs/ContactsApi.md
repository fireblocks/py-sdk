# fireblocks.ContactsApi

All URIs are relative to *https://api.fireblocks.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contacts**](ContactsApi.md#get_contacts) | **GET** /contacts | List contacts


# **get_contacts**
> ContactsPagedResponse get_contacts(page_cursor=page_cursor, page_size=page_size, include_total=include_total, name=name, types=types, container_id=container_id, archived=archived, access_control=access_control, include_tag_ids=include_tag_ids, exclude_tag_ids=exclude_tag_ids, sort_by=sort_by, order=order)

List contacts

Returns a paginated list of the workspace's address book contacts.

Live contacts are returned by default; pass `archived=true` to return only the archived
ones. Results are sorted by `name` ascending unless `sortBy`/`order` say otherwise.
Because the sort column is the page cursor's leading key, a `pageCursor` must be replayed
with the same sort it was minted under, or the request is rejected.

Endpoint Permissions: any workspace role may read the address book. Writes are role-gated.


### Example


```python
from fireblocks.models.contacts_paged_response import ContactsPagedResponse
from fireblocks.client import Fireblocks
from fireblocks.client_configuration import ClientConfiguration
from fireblocks.exceptions import ApiException
from fireblocks.base_path import BasePath
from pprint import pprint

# load the secret key content from a file
with open('your_secret_key_file_path', 'r') as file:
    secret_key_value = file.read()

# build the configuration
configuration = ClientConfiguration(
        api_key="your_api_key",
        secret_key=secret_key_value,
        base_path=BasePath.Sandbox, # or set it directly to a string "https://sandbox-api.fireblocks.io/v1"
)


# Enter a context with an instance of the API client
with Fireblocks(configuration) as fireblocks:
    page_cursor = 'bmFtZS1BU0M=~QWNtZSBDb3Jw:NA==' # str | Cursor indicating the page position. Omit to fetch the first page. (optional)
    page_size = 100 # int | Number of results per page (optional) (default to 100)
    include_total = False # bool | Return the total count of matching contacts alongside the page. Counting is opt-in because it costs an extra pass over the filtered set; `total` is omitted from the response unless this is `true`. (optional) (default to False)
    name = 'acme' # str | Filter by a case-insensitive substring of the contact name (optional)
    types = ['[\"COUNTERPARTY\"]'] # List[str] | Filter by one or more contact types (optional)
    container_id = '11111111-1111-1111-1111-111111111111' # str | Filter by the container holding the contact (optional)
    archived = False # bool | Return only archived contacts instead of live ones (optional) (default to False)
    access_control = 'WHITELIST' # str | Filter by the access control applied to the contact (optional)
    include_tag_ids = ['[\"df4c0987-30da-4976-8dcf-bc2dd41ae331\"]'] # List[str] | List of tag IDs to include. Contacts with any of these tags will be included (optional)
    exclude_tag_ids = ['[\"df4c0987-30da-4976-8dcf-bc2dd41ae331\"]'] # List[str] | List of tag IDs to exclude. Contacts with any of these tags will be filtered out (optional)
    sort_by = name # str | The field to sort by (optional) (default to name)
    order = ASC # str | The sort direction (optional) (default to ASC)

    try:
        # List contacts
        api_response = fireblocks.contacts.get_contacts(page_cursor=page_cursor, page_size=page_size, include_total=include_total, name=name, types=types, container_id=container_id, archived=archived, access_control=access_control, include_tag_ids=include_tag_ids, exclude_tag_ids=exclude_tag_ids, sort_by=sort_by, order=order).result()
        print("The response of ContactsApi->get_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactsApi->get_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_cursor** | **str**| Cursor indicating the page position. Omit to fetch the first page. | [optional] 
 **page_size** | **int**| Number of results per page | [optional] [default to 100]
 **include_total** | **bool**| Return the total count of matching contacts alongside the page. Counting is opt-in because it costs an extra pass over the filtered set; &#x60;total&#x60; is omitted from the response unless this is &#x60;true&#x60;. | [optional] [default to False]
 **name** | **str**| Filter by a case-insensitive substring of the contact name | [optional] 
 **types** | [**List[str]**](str.md)| Filter by one or more contact types | [optional] 
 **container_id** | **str**| Filter by the container holding the contact | [optional] 
 **archived** | **bool**| Return only archived contacts instead of live ones | [optional] [default to False]
 **access_control** | **str**| Filter by the access control applied to the contact | [optional] 
 **include_tag_ids** | [**List[str]**](str.md)| List of tag IDs to include. Contacts with any of these tags will be included | [optional] 
 **exclude_tag_ids** | [**List[str]**](str.md)| List of tag IDs to exclude. Contacts with any of these tags will be filtered out | [optional] 
 **sort_by** | **str**| The field to sort by | [optional] [default to name]
 **order** | **str**| The sort direction | [optional] [default to ASC]

### Return type

[**ContactsPagedResponse**](ContactsPagedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A paginated list of contacts |  * X-Request-ID -  <br>  |
**0** | Error Response |  * X-Request-ID -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

