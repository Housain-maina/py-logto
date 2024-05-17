# ApiOrganizationScopesIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The updated name of the organization scope. It must be unique within the organization template. | [optional] 
**description** | **str** | The updated description of the organization scope. | [optional] 

## Example

```python
from py_logto.models.api_organization_scopes_id_patch_request import ApiOrganizationScopesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiOrganizationScopesIdPatchRequest from a JSON string
api_organization_scopes_id_patch_request_instance = ApiOrganizationScopesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ApiOrganizationScopesIdPatchRequest.to_json())

# convert the object into a dict
api_organization_scopes_id_patch_request_dict = api_organization_scopes_id_patch_request_instance.to_dict()
# create an instance of ApiOrganizationScopesIdPatchRequest from a dict
api_organization_scopes_id_patch_request_from_dict = ApiOrganizationScopesIdPatchRequest.from_dict(api_organization_scopes_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


