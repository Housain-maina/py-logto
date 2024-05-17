# ApiInteractionConsentGet200ResponseApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**privacy_policy_url** | **str** |  | [optional] 
**terms_of_use_url** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_consent_get200_response_application import ApiInteractionConsentGet200ResponseApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionConsentGet200ResponseApplication from a JSON string
api_interaction_consent_get200_response_application_instance = ApiInteractionConsentGet200ResponseApplication.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionConsentGet200ResponseApplication.to_json())

# convert the object into a dict
api_interaction_consent_get200_response_application_dict = api_interaction_consent_get200_response_application_instance.to_dict()
# create an instance of ApiInteractionConsentGet200ResponseApplication from a dict
api_interaction_consent_get200_response_application_from_dict = ApiInteractionConsentGet200ResponseApplication.from_dict(api_interaction_consent_get200_response_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


