# VerifySocialVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID of the SocialVerification record. This ID is required when identifying the user in the current interaction. | 

## Example

```python
from py_logto.models.verify_social_verification200_response import VerifySocialVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifySocialVerification200Response from a JSON string
verify_social_verification200_response_instance = VerifySocialVerification200Response.from_json(json)
# print the JSON string representation of the object
print(VerifySocialVerification200Response.to_json())

# convert the object into a dict
verify_social_verification200_response_dict = verify_social_verification200_response_instance.to_dict()
# create an instance of VerifySocialVerification200Response from a dict
verify_social_verification200_response_from_dict = VerifySocialVerification200Response.from_dict(verify_social_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


