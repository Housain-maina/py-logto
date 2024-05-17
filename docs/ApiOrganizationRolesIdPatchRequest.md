# ApiOrganizationRolesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The updated name of the organization role. It must be unique within the organization template. | [optional] 
**description** | **str** | The updated description of the organization role. | [optional] 

## Example

```python
from py_logto.models.api_organization_roles_id_patch_request import ApiOrganizationRolesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationRolesIdPatchRequest from a JSON string
api_organization_roles_id_patch_request_instance = ApiOrganizationRolesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationRolesIdPatchRequest.to_json())

# convert the object into a dict
api_organization_roles_id_patch_request_dict = api_organization_roles_id_patch_request_instance.to_dict()
# create an instance of ApiOrganizationRolesIdPatchRequest from a dict
api_organization_roles_id_patch_request_from_dict = ApiOrganizationRolesIdPatchRequest.from_dict(api_organization_roles_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


