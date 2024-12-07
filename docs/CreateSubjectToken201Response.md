# CreateSubjectToken201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_token** | **str** |  | 
**expires_in** | **float** |  | 

## Example

```python
from py_logto.models.create_subject_token201_response import CreateSubjectToken201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubjectToken201Response from a JSON string
create_subject_token201_response_instance = CreateSubjectToken201Response.from_json(json)
# print the JSON string representation of the object
print(CreateSubjectToken201Response.to_json())

# convert the object into a dict
create_subject_token201_response_dict = create_subject_token201_response_instance.to_dict()
# create an instance of CreateSubjectToken201Response from a dict
create_subject_token201_response_from_dict = CreateSubjectToken201Response.from_dict(create_subject_token201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


