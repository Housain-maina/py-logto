# GetOrganizationInvitation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**inviter_id** | **str** |  | 
**invitee** | **str** |  | 
**accepted_user_id** | **str** |  | 
**organization_id** | **str** |  | 
**status** | **str** |  | 
**created_at** | **float** |  | 
**updated_at** | **float** |  | 
**expires_at** | **float** |  | 
**organization_roles** | [**List[ListApplicationOrganizations200ResponseInnerOrganizationRolesInner]**](ListApplicationOrganizations200ResponseInnerOrganizationRolesInner.md) |  | 

## Example

```python
from py_logto.models.get_organization_invitation200_response import GetOrganizationInvitation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationInvitation200Response from a JSON string
get_organization_invitation200_response_instance = GetOrganizationInvitation200Response.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationInvitation200Response.to_json())

# convert the object into a dict
get_organization_invitation200_response_dict = get_organization_invitation200_response_instance.to_dict()
# create an instance of GetOrganizationInvitation200Response from a dict
get_organization_invitation200_response_from_dict = GetOrganizationInvitation200Response.from_dict(get_organization_invitation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


