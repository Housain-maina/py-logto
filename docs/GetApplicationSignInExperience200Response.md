# GetApplicationSignInExperience200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**application_id** | **str** |  | 
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | 
**terms_of_use_url** | **str** |  | 
**privacy_policy_url** | **str** |  | 
**display_name** | **str** |  | 

## Example

```python
from py_logto.models.get_application_sign_in_experience200_response import GetApplicationSignInExperience200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApplicationSignInExperience200Response from a JSON string
get_application_sign_in_experience200_response_instance = GetApplicationSignInExperience200Response.from_json(json)
# print the JSON string representation of the object
print(GetApplicationSignInExperience200Response.to_json())

# convert the object into a dict
get_application_sign_in_experience200_response_dict = get_application_sign_in_experience200_response_instance.to_dict()
# create an instance of GetApplicationSignInExperience200Response from a dict
get_application_sign_in_experience200_response_from_dict = GetApplicationSignInExperience200Response.from_dict(get_application_sign_in_experience200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


