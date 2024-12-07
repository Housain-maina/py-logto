# VerifySocialVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_data** | **object** | Arbitrary data returned by the social provider to complete the verification process. | 
**verification_id** | **str** | The ID of the Social verification record. | [optional] 

## Example

```python
from py_logto.models.verify_social_verification_request import VerifySocialVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifySocialVerificationRequest from a JSON string
verify_social_verification_request_instance = VerifySocialVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(VerifySocialVerificationRequest.to_json())

# convert the object into a dict
verify_social_verification_request_dict = verify_social_verification_request_instance.to_dict()
# create an instance of VerifySocialVerificationRequest from a dict
verify_social_verification_request_from_dict = VerifySocialVerificationRequest.from_dict(verify_social_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


