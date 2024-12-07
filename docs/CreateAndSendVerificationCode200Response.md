# CreateAndSendVerificationCode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique ID of the verification record. Required to verify the code. | 

## Example

```python
from py_logto.models.create_and_send_verification_code200_response import CreateAndSendVerificationCode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAndSendVerificationCode200Response from a JSON string
create_and_send_verification_code200_response_instance = CreateAndSendVerificationCode200Response.from_json(json)
# print the JSON string representation of the object
print(CreateAndSendVerificationCode200Response.to_json())

# convert the object into a dict
create_and_send_verification_code200_response_dict = create_and_send_verification_code200_response_instance.to_dict()
# create an instance of CreateAndSendVerificationCode200Response from a dict
create_and_send_verification_code200_response_from_dict = CreateAndSendVerificationCode200Response.from_dict(create_and_send_verification_code200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


