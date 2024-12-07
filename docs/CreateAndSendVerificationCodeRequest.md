# CreateAndSendVerificationCodeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | [**CreateAndSendVerificationCodeRequestIdentifier**](CreateAndSendVerificationCodeRequestIdentifier.md) |  | 
**interaction_event** | **str** | The interaction event for which the verification code will be used. Supported values are &#x60;SignIn&#x60;, &#x60;Register&#x60;, and &#x60;ForgotPassword&#x60;. This determines the template for the verification code. | 

## Example

```python
from py_logto.models.create_and_send_verification_code_request import CreateAndSendVerificationCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAndSendVerificationCodeRequest from a JSON string
create_and_send_verification_code_request_instance = CreateAndSendVerificationCodeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAndSendVerificationCodeRequest.to_json())

# convert the object into a dict
create_and_send_verification_code_request_dict = create_and_send_verification_code_request_instance.to_dict()
# create an instance of CreateAndSendVerificationCodeRequest from a dict
create_and_send_verification_code_request_from_dict = CreateAndSendVerificationCodeRequest.from_dict(create_and_send_verification_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


