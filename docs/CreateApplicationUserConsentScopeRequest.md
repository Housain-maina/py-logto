# CreateApplicationUserConsentScopeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_scopes** | **List[str]** | A list of organization scope id to assign to the application. Throws error if any given organization scope is not found. | [optional] 
**resource_scopes** | **List[str]** | A list of resource scope id to assign to the application. Throws error if any given resource scope is not found. | [optional] 
**organization_resource_scopes** | **List[str]** | A list of organization resource scope id to assign to the application. Throws error if any given resource scope is not found. | [optional] 
**user_scopes** | **List[str]** | A list of user scope enum value to assign to the application. | [optional] 

## Example

```python
from py_logto.models.create_application_user_consent_scope_request import CreateApplicationUserConsentScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationUserConsentScopeRequest from a JSON string
create_application_user_consent_scope_request_instance = CreateApplicationUserConsentScopeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateApplicationUserConsentScopeRequest.to_json())

# convert the object into a dict
create_application_user_consent_scope_request_dict = create_application_user_consent_scope_request_instance.to_dict()
# create an instance of CreateApplicationUserConsentScopeRequest from a dict
create_application_user_consent_scope_request_from_dict = CreateApplicationUserConsentScopeRequest.from_dict(create_application_user_consent_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


