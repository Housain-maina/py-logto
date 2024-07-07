# ApiInteractionConsentGet200ResponseOrganizationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**missing_resource_scopes** | [**List[ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInner]**](ApiInteractionConsentGet200ResponseOrganizationsInnerMissingResourceScopesInner.md) |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_consent_get200_response_organizations_inner import ApiInteractionConsentGet200ResponseOrganizationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionConsentGet200ResponseOrganizationsInner from a JSON string
api_interaction_consent_get200_response_organizations_inner_instance = ApiInteractionConsentGet200ResponseOrganizationsInner.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionConsentGet200ResponseOrganizationsInner.to_json())

# convert the object into a dict
api_interaction_consent_get200_response_organizations_inner_dict = api_interaction_consent_get200_response_organizations_inner_instance.to_dict()
# create an instance of ApiInteractionConsentGet200ResponseOrganizationsInner from a dict
api_interaction_consent_get200_response_organizations_inner_from_dict = ApiInteractionConsentGet200ResponseOrganizationsInner.from_dict(api_interaction_consent_get200_response_organizations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


