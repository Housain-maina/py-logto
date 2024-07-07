# ApiInteractionConsentGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**ApiInteractionConsentGet200ResponseApplication**](ApiInteractionConsentGet200ResponseApplication.md) |  | 
**user** | [**ApiInteractionConsentGet200ResponseUser**](ApiInteractionConsentGet200ResponseUser.md) |  | 
**organizations** | [**List[ApiInteractionConsentGet200ResponseOrganizationsInner]**](ApiInteractionConsentGet200ResponseOrganizationsInner.md) |  | [optional] 
**missing_oidc_scope** | **List[str]** |  | [optional] 
**missing_resource_scopes** | [**List[ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInner]**](ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInner.md) |  | [optional] 
**redirect_uri** | **str** |  | 

## Example

```python
from py_logto.models.api_interaction_consent_get200_response import ApiInteractionConsentGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionConsentGet200Response from a JSON string
api_interaction_consent_get200_response_instance = ApiInteractionConsentGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionConsentGet200Response.to_json())

# convert the object into a dict
api_interaction_consent_get200_response_dict = api_interaction_consent_get200_response_instance.to_dict()
# create an instance of ApiInteractionConsentGet200Response from a dict
api_interaction_consent_get200_response_from_dict = ApiInteractionConsentGet200Response.from_dict(api_interaction_consent_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


