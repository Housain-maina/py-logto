# IdentifyUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The ID of the verification record used to identify the user. &lt;br/&gt;- &#x60;SignIn&#x60; and &#x60;ForgotPassword&#x60; interactions: Required to verify the user&#39;s identity. &lt;br/&gt;- &#x60;Register&#x60; interaction: Optional. If provided, it updates the profile data with the verification record before account creation. If omitted, the account is created using existing profile data in the current interaction. | [optional] 
**link_social_identity** | **bool** | Applies to the SignIn interaction only, and is used when a SocialVerification type verificationId is provided. &lt;br/&gt;- If &#x60;true&#x60;, the user is identified using the verified email or phone number from the social identity provider, and the social identity is linked to the user&#39;s account. &lt;br/&gt;- If &#x60;false&#x60; or not provided, the API identifies the user solely through the social identity. &lt;br/&gt; This parameters is used for linking a non-existing social identity to a related user account that can be identified through the verified email or phone number. | [optional] 

## Example

```python
from py_logto.models.identify_user_request import IdentifyUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifyUserRequest from a JSON string
identify_user_request_instance = IdentifyUserRequest.from_json(json)
# print the JSON string representation of the object
print(IdentifyUserRequest.to_json())

# convert the object into a dict
identify_user_request_dict = identify_user_request_instance.to_dict()
# create an instance of IdentifyUserRequest from a dict
identify_user_request_from_dict = IdentifyUserRequest.from_dict(identify_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


