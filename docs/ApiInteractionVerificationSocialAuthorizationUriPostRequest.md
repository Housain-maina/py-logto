# ApiInteractionVerificationSocialAuthorizationUriPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | 
**state** | **str** |  | 
**redirect_uri** | **object** | Validator function | 

## Example

```python
from py_logto.models.api_interaction_verification_social_authorization_uri_post_request import ApiInteractionVerificationSocialAuthorizationUriPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionVerificationSocialAuthorizationUriPostRequest from a JSON string
api_interaction_verification_social_authorization_uri_post_request_instance = ApiInteractionVerificationSocialAuthorizationUriPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionVerificationSocialAuthorizationUriPostRequest.to_json())

# convert the object into a dict
api_interaction_verification_social_authorization_uri_post_request_dict = api_interaction_verification_social_authorization_uri_post_request_instance.to_dict()
# create an instance of ApiInteractionVerificationSocialAuthorizationUriPostRequest from a dict
api_interaction_verification_social_authorization_uri_post_request_from_dict = ApiInteractionVerificationSocialAuthorizationUriPostRequest.from_dict(api_interaction_verification_social_authorization_uri_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


