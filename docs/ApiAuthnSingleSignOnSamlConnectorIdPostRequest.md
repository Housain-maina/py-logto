# ApiAuthnSingleSignOnSamlConnectorIdPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relay_state** | **str** | SAML standard parameter that will be transmitted between the identity provider and the service provider. It will be used as the session ID (jti) of the user&#39;s Logto authentication session. This API will use this session ID to retrieve the SSO connector authentication session from the database. | 
**saml_response** | **str** | The SAML assertion response from the identity provider (IdP). | 

## Example

```python
from py_logto.models.api_authn_single_sign_on_saml_connector_id_post_request import ApiAuthnSingleSignOnSamlConnectorIdPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAuthnSingleSignOnSamlConnectorIdPostRequest from a JSON string
api_authn_single_sign_on_saml_connector_id_post_request_instance = ApiAuthnSingleSignOnSamlConnectorIdPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiAuthnSingleSignOnSamlConnectorIdPostRequest.to_json())

# convert the object into a dict
api_authn_single_sign_on_saml_connector_id_post_request_dict = api_authn_single_sign_on_saml_connector_id_post_request_instance.to_dict()
# create an instance of ApiAuthnSingleSignOnSamlConnectorIdPostRequest from a dict
api_authn_single_sign_on_saml_connector_id_post_request_from_dict = ApiAuthnSingleSignOnSamlConnectorIdPostRequest.from_dict(api_authn_single_sign_on_saml_connector_id_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


