# ListApplicationOrganizations200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**custom_data** | **object** | arbitrary | 
**is_mfa_required** | **bool** |  | 
**created_at** | **float** |  | 
**organization_roles** | [**List[ListApplicationOrganizations200ResponseInnerOrganizationRolesInner]**](ListApplicationOrganizations200ResponseInnerOrganizationRolesInner.md) |  | 

## Example

```python
from py_logto.models.list_application_organizations200_response_inner import ListApplicationOrganizations200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplicationOrganizations200ResponseInner from a JSON string
list_application_organizations200_response_inner_instance = ListApplicationOrganizations200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListApplicationOrganizations200ResponseInner.to_json())

# convert the object into a dict
list_application_organizations200_response_inner_dict = list_application_organizations200_response_inner_instance.to_dict()
# create an instance of ListApplicationOrganizations200ResponseInner from a dict
list_application_organizations200_response_inner_from_dict = ListApplicationOrganizations200ResponseInner.from_dict(list_application_organizations200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


