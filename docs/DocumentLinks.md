# DocumentLinks

Web of Science URLs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record** | **str** |  | [optional] 
**citing_articles** | **str** |  | [optional] 
**references** | **str** |  | [optional] 
**related** | **str** |  | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.document_links import DocumentLinks

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentLinks from a JSON string
document_links_instance = DocumentLinks.from_json(json)
# print the JSON string representation of the object
print DocumentLinks.to_json()

# convert the object into a dict
document_links_dict = document_links_instance.to_dict()
# create an instance of DocumentLinks from a dict
document_links_form_dict = document_links.from_dict(document_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


