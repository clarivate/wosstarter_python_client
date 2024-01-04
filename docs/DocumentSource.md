# DocumentSource

Web of Science document source metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_title** | **str** | Source title | [optional] 
**publish_year** | **int** | Published Year | [optional] 
**publish_month** | **str** | Published Month | [optional] 
**volume** | **str** | Volume | [optional] 
**issue** | **str** | Issue | [optional] 
**supplement** | **str** | Journal supplement | [optional] 
**special_issue** | **str** | Journal special issue | [optional] 
**article_number** | **str** | Source Article Number | [optional] 
**pages** | [**DocumentSourcePages**](DocumentSourcePages.md) |  | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.document_source import DocumentSource

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSource from a JSON string
document_source_instance = DocumentSource.from_json(json)
# print the JSON string representation of the object
print DocumentSource.to_json()

# convert the object into a dict
document_source_dict = document_source_instance.to_dict()
# create an instance of DocumentSource from a dict
document_source_form_dict = document_source.from_dict(document_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


