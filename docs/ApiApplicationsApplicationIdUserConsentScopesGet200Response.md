# ApiApplicationsApplicationIdUserConsentScopesGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_scopes** | [**List[ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner]**](ApiApplicationsApplicationIdUserConsentScopesGet200ResponseOrganizationScopesInner.md) | A list of organization scope details assigned to the application. | 
**resource_scopes** | [**List[ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInner]**](ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInner.md) | A list of resource scope details grouped by resource id assigned to the application. | 
**user_scopes** | **List[str]** | A list of user scope enum value assigned to the application. | 

## Example

```python
from py_logto.models.api_applications_application_id_user_consent_scopes_get200_response import ApiApplicationsApplicationIdUserConsentScopesGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsApplicationIdUserConsentScopesGet200Response from a JSON string
api_applications_application_id_user_consent_scopes_get200_response_instance = ApiApplicationsApplicationIdUserConsentScopesGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsApplicationIdUserConsentScopesGet200Response.to_json())

# convert the object into a dict
api_applications_application_id_user_consent_scopes_get200_response_dict = api_applications_application_id_user_consent_scopes_get200_response_instance.to_dict()
# create an instance of ApiApplicationsApplicationIdUserConsentScopesGet200Response from a dict
api_applications_application_id_user_consent_scopes_get200_response_from_dict = ApiApplicationsApplicationIdUserConsentScopesGet200Response.from_dict(api_applications_application_id_user_consent_scopes_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


