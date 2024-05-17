# ApiRolesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the role. It should be unique within the tenant. | 
**description** | **str** |  | 
**type** | **str** | The type of the role. It cannot be changed after creation. | [optional] 
**scope_ids** | **List[str]** | The initial API resource scopes assigned to the role. | [optional] 

## Example

```python
from py_logto.models.api_roles_post_request import ApiRolesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRolesPostRequest from a JSON string
api_roles_post_request_instance = ApiRolesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiRolesPostRequest.to_json())

# convert the object into a dict
api_roles_post_request_dict = api_roles_post_request_instance.to_dict()
# create an instance of ApiRolesPostRequest from a dict
api_roles_post_request_from_dict = ApiRolesPostRequest.from_dict(api_roles_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


