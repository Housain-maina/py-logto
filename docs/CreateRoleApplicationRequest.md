# CreateRoleApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **List[str]** | An array of application IDs to be assigned. | 

## Example

```python
from py_logto.models.create_role_application_request import CreateRoleApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleApplicationRequest from a JSON string
create_role_application_request_instance = CreateRoleApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRoleApplicationRequest.to_json())

# convert the object into a dict
create_role_application_request_dict = create_role_application_request_instance.to_dict()
# create an instance of CreateRoleApplicationRequest from a dict
create_role_application_request_from_dict = CreateRoleApplicationRequest.from_dict(create_role_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


