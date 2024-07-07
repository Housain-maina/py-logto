# CreateRoleUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | An array of user IDs to be assigned. | 

## Example

```python
from py_logto.models.create_role_user_request import CreateRoleUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRoleUserRequest from a JSON string
create_role_user_request_instance = CreateRoleUserRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRoleUserRequest.to_json())

# convert the object into a dict
create_role_user_request_dict = create_role_user_request_instance.to_dict()
# create an instance of CreateRoleUserRequest from a dict
create_role_user_request_from_dict = CreateRoleUserRequest.from_dict(create_role_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


