# VerifyVerificationBySocialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_data** | **object** | A json object constructed from the url query params returned by the social platform. Typically it contains &#x60;code&#x60;, &#x60;state&#x60; and &#x60;redirectUri&#x60; fields. | 
**verification_record_id** | **str** |  | 
**verification_id** | **object** | The verification ID of the SocialVerification record. | [optional] 

## Example

```python
from py_logto.models.verify_verification_by_social_request import VerifyVerificationBySocialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyVerificationBySocialRequest from a JSON string
verify_verification_by_social_request_instance = VerifyVerificationBySocialRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyVerificationBySocialRequest.to_json())

# convert the object into a dict
verify_verification_by_social_request_dict = verify_verification_by_social_request_instance.to_dict()
# create an instance of VerifyVerificationBySocialRequest from a dict
verify_verification_by_social_request_from_dict = VerifyVerificationBySocialRequest.from_dict(verify_verification_by_social_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


