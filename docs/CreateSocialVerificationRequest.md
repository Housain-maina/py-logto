# CreateSocialVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state parameter to pass to the social connector. | 
**redirect_uri** | **str** | The URI to redirect the user after the social authorization is completed. | 

## Example

```python
from py_logto.models.create_social_verification_request import CreateSocialVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSocialVerificationRequest from a JSON string
create_social_verification_request_instance = CreateSocialVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSocialVerificationRequest.to_json())

# convert the object into a dict
create_social_verification_request_dict = create_social_verification_request_instance.to_dict()
# create an instance of CreateSocialVerificationRequest from a dict
create_social_verification_request_from_dict = CreateSocialVerificationRequest.from_dict(create_social_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


