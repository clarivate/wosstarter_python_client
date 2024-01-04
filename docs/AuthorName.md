# AuthorName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Web of Science display name | [optional] 
**wos_standard** | **str** | Web of Science standard name | [optional] 
**researcher_id** | **str** | Web of Science ResearcherID | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.author_name import AuthorName

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorName from a JSON string
author_name_instance = AuthorName.from_json(json)
# print the JSON string representation of the object
print AuthorName.to_json()

# convert the object into a dict
author_name_dict = author_name_instance.to_dict()
# create an instance of AuthorName from a dict
author_name_form_dict = author_name.from_dict(author_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


