# ApiRolesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the role. It should be unique within the tenant. | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_roles_id_patch_request import ApiRolesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRolesIdPatchRequest from a JSON string
api_roles_id_patch_request_instance = ApiRolesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiRolesIdPatchRequest.to_json())

# convert the object into a dict
api_roles_id_patch_request_dict = api_roles_id_patch_request_instance.to_dict()
# create an instance of ApiRolesIdPatchRequest from a dict
api_roles_id_patch_request_from_dict = ApiRolesIdPatchRequest.from_dict(api_roles_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


