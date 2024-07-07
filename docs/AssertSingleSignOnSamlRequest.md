# AssertSingleSignOnSamlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relay_state** | **str** | SAML standard parameter that will be transmitted between the identity provider and the service provider. It will be used as the session ID (jti) of the user&#39;s Logto authentication session. This API will use this session ID to retrieve the SSO connector authentication session from the database. | 
**saml_response** | **str** | The SAML assertion response from the identity provider (IdP). | 

## Example

```python
from py_logto.models.assert_single_sign_on_saml_request import AssertSingleSignOnSamlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssertSingleSignOnSamlRequest from a JSON string
assert_single_sign_on_saml_request_instance = AssertSingleSignOnSamlRequest.from_json(json)
# print the JSON string representation of the object
print(AssertSingleSignOnSamlRequest.to_json())

# convert the object into a dict
assert_single_sign_on_saml_request_dict = assert_single_sign_on_saml_request_instance.to_dict()
# create an instance of AssertSingleSignOnSamlRequest from a dict
assert_single_sign_on_saml_request_from_dict = AssertSingleSignOnSamlRequest.from_dict(assert_single_sign_on_saml_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


