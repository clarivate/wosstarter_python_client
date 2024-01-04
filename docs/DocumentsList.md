# DocumentsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) |  | [optional] 
**hits** | [**List[Document]**](Document.md) |  | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.documents_list import DocumentsList

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsList from a JSON string
documents_list_instance = DocumentsList.from_json(json)
# print the JSON string representation of the object
print DocumentsList.to_json()

# convert the object into a dict
documents_list_dict = documents_list_instance.to_dict()
# create an instance of DocumentsList from a dict
documents_list_form_dict = documents_list.from_dict(documents_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


