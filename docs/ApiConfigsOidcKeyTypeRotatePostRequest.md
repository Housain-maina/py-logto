# ApiConfigsOidcKeyTypeRotatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_key_algorithm** | **str** | The signing key algorithm the new generated private key is using.  Only applicable when &#x60;keyType&#x60; is &#x60;private-keys&#x60;. | [optional] 

## Example

```python
from py_logto.models.api_configs_oidc_key_type_rotate_post_request import ApiConfigsOidcKeyTypeRotatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfigsOidcKeyTypeRotatePostRequest from a JSON string
api_configs_oidc_key_type_rotate_post_request_instance = ApiConfigsOidcKeyTypeRotatePostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiConfigsOidcKeyTypeRotatePostRequest.to_json())

# convert the object into a dict
api_configs_oidc_key_type_rotate_post_request_dict = api_configs_oidc_key_type_rotate_post_request_instance.to_dict()
# create an instance of ApiConfigsOidcKeyTypeRotatePostRequest from a dict
api_configs_oidc_key_type_rotate_post_request_from_dict = ApiConfigsOidcKeyTypeRotatePostRequest.from_dict(api_configs_oidc_key_type_rotate_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


