# OtherName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Web of Science display name | [optional] 

## Example

```python
from clarivate.wos_starter.client.models.other_name import OtherName

# TODO update the JSON string below
json = "{}"
# create an instance of OtherName from a JSON string
other_name_instance = OtherName.from_json(json)
# print the JSON string representation of the object
print OtherName.to_json()

# convert the object into a dict
other_name_dict = other_name_instance.to_dict()
# create an instance of OtherName from a dict
other_name_form_dict = other_name.from_dict(other_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


