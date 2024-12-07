# VerifyTotpVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID of the TOTP verification record. For newly created TOTP secret verification record, this ID is required to bind the TOTP secret to the user account through &#x60;Profile&#x60; API. | 

## Example

```python
from py_logto.models.verify_totp_verification200_response import VerifyTotpVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyTotpVerification200Response from a JSON string
verify_totp_verification200_response_instance = VerifyTotpVerification200Response.from_json(json)
# print the JSON string representation of the object
print(VerifyTotpVerification200Response.to_json())

# convert the object into a dict
verify_totp_verification200_response_dict = verify_totp_verification200_response_instance.to_dict()
# create an instance of VerifyTotpVerification200Response from a dict
verify_totp_verification200_response_from_dict = VerifyTotpVerification200Response.from_dict(verify_totp_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


