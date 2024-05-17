# ApiRolesIdScopesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_ids** | **List[str]** | An array of API resource scope IDs to be linked. | 

## Example

```python
from py_logto.models.api_roles_id_scopes_post_request import ApiRolesIdScopesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRolesIdScopesPostRequest from a JSON string
api_roles_id_scopes_post_request_instance = ApiRolesIdScopesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiRolesIdScopesPostRequest.to_json())

# convert the object into a dict
api_roles_id_scopes_post_request_dict = api_roles_id_scopes_post_request_instance.to_dict()
# create an instance of ApiRolesIdScopesPostRequest from a dict
api_roles_id_scopes_post_request_from_dict = ApiRolesIdScopesPostRequest.from_dict(api_roles_id_scopes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


