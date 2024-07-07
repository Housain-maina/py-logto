# ListApplicationUserConsentOrganizations200ResponseOrganizationsInner


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

## Example

```python
from py_logto.models.list_application_user_consent_organizations200_response_organizations_inner import ListApplicationUserConsentOrganizations200ResponseOrganizationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplicationUserConsentOrganizations200ResponseOrganizationsInner from a JSON string
list_application_user_consent_organizations200_response_organizations_inner_instance = ListApplicationUserConsentOrganizations200ResponseOrganizationsInner.from_json(json)
# print the JSON string representation of the object
print(ListApplicationUserConsentOrganizations200ResponseOrganizationsInner.to_json())

# convert the object into a dict
list_application_user_consent_organizations200_response_organizations_inner_dict = list_application_user_consent_organizations200_response_organizations_inner_instance.to_dict()
# create an instance of ListApplicationUserConsentOrganizations200ResponseOrganizationsInner from a dict
list_application_user_consent_organizations200_response_organizations_inner_from_dict = ListApplicationUserConsentOrganizations200ResponseOrganizationsInner.from_dict(list_application_user_consent_organizations200_response_organizations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


