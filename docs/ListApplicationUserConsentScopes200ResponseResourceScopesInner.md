# ListApplicationUserConsentScopes200ResponseResourceScopesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**ListApplicationUserConsentScopes200ResponseResourceScopesInnerResource**](ListApplicationUserConsentScopes200ResponseResourceScopesInnerResource.md) |  | 
**scopes** | [**List[ListApplicationUserConsentScopes200ResponseResourceScopesInnerScopesInner]**](ListApplicationUserConsentScopes200ResponseResourceScopesInnerScopesInner.md) |  | 

## Example

```python
from py_logto.models.list_application_user_consent_scopes200_response_resource_scopes_inner import ListApplicationUserConsentScopes200ResponseResourceScopesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplicationUserConsentScopes200ResponseResourceScopesInner from a JSON string
list_application_user_consent_scopes200_response_resource_scopes_inner_instance = ListApplicationUserConsentScopes200ResponseResourceScopesInner.from_json(json)
# print the JSON string representation of the object
print(ListApplicationUserConsentScopes200ResponseResourceScopesInner.to_json())

# convert the object into a dict
list_application_user_consent_scopes200_response_resource_scopes_inner_dict = list_application_user_consent_scopes200_response_resource_scopes_inner_instance.to_dict()
# create an instance of ListApplicationUserConsentScopes200ResponseResourceScopesInner from a dict
list_application_user_consent_scopes200_response_resource_scopes_inner_from_dict = ListApplicationUserConsentScopes200ResponseResourceScopesInner.from_dict(list_application_user_consent_scopes200_response_resource_scopes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


