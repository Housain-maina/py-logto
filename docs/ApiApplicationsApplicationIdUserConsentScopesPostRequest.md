# ApiApplicationsApplicationIdUserConsentScopesPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_scopes** | **List[str]** | A list of organization scope id to assign to the application. Throws error if any given organization scope is not found. | [optional] 
**resource_scopes** | **List[str]** | A list of resource scope id to assign to the application. Throws error if any given resource scope is not found. | [optional] 
**user_scopes** | **List[str]** | A list of user scope enum value to assign to the application. | [optional] 

## Example

```python
from py_logto.models.api_applications_application_id_user_consent_scopes_post_request import ApiApplicationsApplicationIdUserConsentScopesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsApplicationIdUserConsentScopesPostRequest from a JSON string
api_applications_application_id_user_consent_scopes_post_request_instance = ApiApplicationsApplicationIdUserConsentScopesPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsApplicationIdUserConsentScopesPostRequest.to_json())

# convert the object into a dict
api_applications_application_id_user_consent_scopes_post_request_dict = api_applications_application_id_user_consent_scopes_post_request_instance.to_dict()
# create an instance of ApiApplicationsApplicationIdUserConsentScopesPostRequest from a dict
api_applications_application_id_user_consent_scopes_post_request_from_dict = ApiApplicationsApplicationIdUserConsentScopesPostRequest.from_dict(api_applications_application_id_user_consent_scopes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


