# CreatePasswordVerification200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID of the newly created Password verification record. The &#x60;verificationId&#x60; is required when verifying the user&#39;s identity via the &#x60;Identification&#x60; API. | 

## Example

```python
from py_logto.models.create_password_verification200_response import CreatePasswordVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePasswordVerification200Response from a JSON string
create_password_verification200_response_instance = CreatePasswordVerification200Response.from_json(json)
# print the JSON string representation of the object
print(CreatePasswordVerification200Response.to_json())

# convert the object into a dict
create_password_verification200_response_dict = create_password_verification200_response_instance.to_dict()
# create an instance of CreatePasswordVerification200Response from a dict
create_password_verification200_response_from_dict = CreatePasswordVerification200Response.from_dict(create_password_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


