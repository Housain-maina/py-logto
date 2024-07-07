# ListOrganizations200ResponseInner


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
**users_count** | **float** |  | [optional] 
**featured_users** | [**List[ListRoles200ResponseInnerFeaturedUsersInner]**](ListRoles200ResponseInnerFeaturedUsersInner.md) |  | [optional] 

## Example

```python
from py_logto.models.list_organizations200_response_inner import ListOrganizations200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizations200ResponseInner from a JSON string
list_organizations200_response_inner_instance = ListOrganizations200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListOrganizations200ResponseInner.to_json())

# convert the object into a dict
list_organizations200_response_inner_dict = list_organizations200_response_inner_instance.to_dict()
# create an instance of ListOrganizations200ResponseInner from a dict
list_organizations200_response_inner_from_dict = ListOrganizations200ResponseInner.from_dict(list_organizations200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


