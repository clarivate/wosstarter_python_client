# DocumentSourcePages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **str** | Page range | [optional] 
**begin** | **str** | Page begin | [optional] 
**end** | **str** | Page end | [optional] 
**count** | **int** | Number of pages | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.document_source_pages import DocumentSourcePages

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSourcePages from a JSON string
document_source_pages_instance = DocumentSourcePages.from_json(json)
# print the JSON string representation of the object
print DocumentSourcePages.to_json()

# convert the object into a dict
document_source_pages_dict = document_source_pages_instance.to_dict()
# create an instance of DocumentSourcePages from a dict
document_source_pages_form_dict = document_source_pages.from_dict(document_source_pages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


