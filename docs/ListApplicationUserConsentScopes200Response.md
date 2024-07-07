# ListApplicationUserConsentScopes200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_scopes** | [**List[ListApplicationUserConsentScopes200ResponseOrganizationScopesInner]**](ListApplicationUserConsentScopes200ResponseOrganizationScopesInner.md) | A list of organization scope details assigned to the application. | 
**resource_scopes** | [**List[ListApplicationUserConsentScopes200ResponseResourceScopesInner]**](ListApplicationUserConsentScopes200ResponseResourceScopesInner.md) | A list of resource scope details grouped by resource id assigned to the application. | 
**organization_resource_scopes** | [**List[ListApplicationUserConsentScopes200ResponseResourceScopesInner]**](ListApplicationUserConsentScopes200ResponseResourceScopesInner.md) | A list of organization resource scope details grouped by resource id assigned to the application. | 
**user_scopes** | **List[str]** | A list of user scope enum value assigned to the application. | 

## Example

```python
from py_logto.models.list_application_user_consent_scopes200_response import ListApplicationUserConsentScopes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplicationUserConsentScopes200Response from a JSON string
list_application_user_consent_scopes200_response_instance = ListApplicationUserConsentScopes200Response.from_json(json)
# print the JSON string representation of the object
print(ListApplicationUserConsentScopes200Response.to_json())

# convert the object into a dict
list_application_user_consent_scopes200_response_dict = list_application_user_consent_scopes200_response_instance.to_dict()
# create an instance of ListApplicationUserConsentScopes200Response from a dict
list_application_user_consent_scopes200_response_from_dict = ListApplicationUserConsentScopes200Response.from_dict(list_application_user_consent_scopes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


