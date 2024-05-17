# ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInnerResource**](ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInnerResource.md) |  | 
**scopes** | [**List[ApiInteractionConsentGet200ResponseMissingResourceScopesInnerScopesInner]**](ApiInteractionConsentGet200ResponseMissingResourceScopesInnerScopesInner.md) |  | 

## Example

```python
from py_logto.models.api_applications_application_id_user_consent_scopes_get200_response_resource_scopes_inner import ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInner from a JSON string
api_applications_application_id_user_consent_scopes_get200_response_resource_scopes_inner_instance = ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInner.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInner.to_json())

# convert the object into a dict
api_applications_application_id_user_consent_scopes_get200_response_resource_scopes_inner_dict = api_applications_application_id_user_consent_scopes_get200_response_resource_scopes_inner_instance.to_dict()
# create an instance of ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInner from a dict
api_applications_application_id_user_consent_scopes_get200_response_resource_scopes_inner_from_dict = ApiApplicationsApplicationIdUserConsentScopesGet200ResponseResourceScopesInner.from_dict(api_applications_application_id_user_consent_scopes_get200_response_resource_scopes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


