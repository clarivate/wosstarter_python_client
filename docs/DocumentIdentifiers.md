# DocumentIdentifiers

Document and Source Identifiers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doi** | **str** |  | [optional] 
**issn** | **str** |  | [optional] 
**eissn** | **str** |  | [optional] 
**isbn** | **str** |  | [optional] 
**eisbn** | **str** |  | [optional] 
**pmid** | **str** |  | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.document_identifiers import DocumentIdentifiers

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentIdentifiers from a JSON string
document_identifiers_instance = DocumentIdentifiers.from_json(json)
# print the JSON string representation of the object
print DocumentIdentifiers.to_json()

# convert the object into a dict
document_identifiers_dict = document_identifiers_instance.to_dict()
# create an instance of DocumentIdentifiers from a dict
document_identifiers_form_dict = document_identifiers.from_dict(document_identifiers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


