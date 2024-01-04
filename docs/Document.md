# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Web of Science Unique Identifier | 
**title** | **str** | Document title | [optional] 
**types** | **List[str]** | Normalized Document Types | [optional] 
**source_types** | **List[str]** | Source Document Types | [optional] 
**source** | [**DocumentSource**](DocumentSource.md) |  | [optional] 
**names** | [**DocumentNames**](DocumentNames.md) |  | [optional] 
**links** | [**DocumentLinks**](DocumentLinks.md) |  | [optional] 
**citations** | [**List[DocumentCitationsInner]**](DocumentCitationsInner.md) | Times Cited | [optional] 
**identifiers** | [**DocumentIdentifiers**](DocumentIdentifiers.md) |  | [optional] 
**keywords** | [**DocumentKeywords**](DocumentKeywords.md) |  | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print Document.to_json()

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_form_dict = document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


