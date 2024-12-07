# CreateTotpSecret200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification_id** | **str** | The unique verification ID for the TOTP record. This ID is required to verify the TOTP code. | 
**secret** | **str** | The newly generated TOTP secret. | 
**secret_qr_code** | **str** | A QR code image data URL for the TOTP secret. The user can scan this QR code with their TOTP authenticator app. | 

## Example

```python
from py_logto.models.create_totp_secret200_response import CreateTotpSecret200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTotpSecret200Response from a JSON string
create_totp_secret200_response_instance = CreateTotpSecret200Response.from_json(json)
# print the JSON string representation of the object
print(CreateTotpSecret200Response.to_json())

# convert the object into a dict
create_totp_secret200_response_dict = create_totp_secret200_response_instance.to_dict()
# create an instance of CreateTotpSecret200Response from a dict
create_totp_secret200_response_from_dict = CreateTotpSecret200Response.from_dict(create_totp_secret200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


