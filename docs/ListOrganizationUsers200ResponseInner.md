# ListOrganizationUsers200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | 
**primary_email** | **str** |  | 
**primary_phone** | **str** |  | 
**name** | **str** |  | 
**avatar** | **str** |  | 
**custom_data** | **object** | arbitrary | 
**identities** | [**Dict[str, GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue]**](GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue.md) |  | 
**last_sign_in_at** | **float** |  | 
**created_at** | **float** |  | 
**updated_at** | **float** |  | 
**profile** | [**GetJwtCustomizer200ResponseOneOfContextSampleUserProfile**](GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.md) |  | 
**application_id** | **str** |  | 
**is_suspended** | **bool** |  | 
**organization_roles** | [**List[ListApplicationOrganizations200ResponseInnerOrganizationRolesInner]**](ListApplicationOrganizations200ResponseInnerOrganizationRolesInner.md) |  | 

## Example

```python
from py_logto.models.list_organization_users200_response_inner import ListOrganizationUsers200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizationUsers200ResponseInner from a JSON string
list_organization_users200_response_inner_instance = ListOrganizationUsers200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListOrganizationUsers200ResponseInner.to_json())

# convert the object into a dict
list_organization_users200_response_inner_dict = list_organization_users200_response_inner_instance.to_dict()
# create an instance of ListOrganizationUsers200ResponseInner from a dict
list_organization_users200_response_inner_from_dict = ListOrganizationUsers200ResponseInner.from_dict(list_organization_users200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


