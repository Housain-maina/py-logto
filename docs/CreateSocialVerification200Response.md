# CreateSocialVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_uri** | **str** | The social authorization URI. | 
**verification_id** | **str** | The unique verification ID of the newly created SocialVerification record. The &#x60;verificationId&#x60; is required when verifying the social authorization response. | 

## Example

```python
from py_logto.models.create_social_verification200_response import CreateSocialVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSocialVerification200Response from a JSON string
create_social_verification200_response_instance = CreateSocialVerification200Response.from_json(json)
# print the JSON string representation of the object
print(CreateSocialVerification200Response.to_json())

# convert the object into a dict
create_social_verification200_response_dict = create_social_verification200_response_instance.to_dict()
# create an instance of CreateSocialVerification200Response from a dict
create_social_verification200_response_from_dict = CreateSocialVerification200Response.from_dict(create_social_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


