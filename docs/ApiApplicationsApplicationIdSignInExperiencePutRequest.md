# ApiApplicationsApplicationIdSignInExperiencePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branding** | [**ApiInteractionConsentGet200ResponseApplicationBranding**](ApiInteractionConsentGet200ResponseApplicationBranding.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**terms_of_use_url** | [**ApiApplicationsApplicationIdSignInExperiencePutRequestTermsOfUseUrl**](ApiApplicationsApplicationIdSignInExperiencePutRequestTermsOfUseUrl.md) |  | 
**privacy_policy_url** | [**ApiApplicationsApplicationIdSignInExperiencePutRequestTermsOfUseUrl**](ApiApplicationsApplicationIdSignInExperiencePutRequestTermsOfUseUrl.md) |  | 

## Example

```python
from py_logto.models.api_applications_application_id_sign_in_experience_put_request import ApiApplicationsApplicationIdSignInExperiencePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApplicationsApplicationIdSignInExperiencePutRequest from a JSON string
api_applications_application_id_sign_in_experience_put_request_instance = ApiApplicationsApplicationIdSignInExperiencePutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiApplicationsApplicationIdSignInExperiencePutRequest.to_json())

# convert the object into a dict
api_applications_application_id_sign_in_experience_put_request_dict = api_applications_application_id_sign_in_experience_put_request_instance.to_dict()
# create an instance of ApiApplicationsApplicationIdSignInExperiencePutRequest from a dict
api_applications_application_id_sign_in_experience_put_request_from_dict = ApiApplicationsApplicationIdSignInExperiencePutRequest.from_dict(api_applications_application_id_sign_in_experience_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


