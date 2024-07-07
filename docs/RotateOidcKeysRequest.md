# RotateOidcKeysRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_key_algorithm** | **str** | The signing key algorithm the new generated private key is using.  Only applicable when &#x60;keyType&#x60; is &#x60;private-keys&#x60;. | [optional] 

## Example

```python
from py_logto.models.rotate_oidc_keys_request import RotateOidcKeysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RotateOidcKeysRequest from a JSON string
rotate_oidc_keys_request_instance = RotateOidcKeysRequest.from_json(json)
# print the JSON string representation of the object
print(RotateOidcKeysRequest.to_json())

# convert the object into a dict
rotate_oidc_keys_request_dict = rotate_oidc_keys_request_instance.to_dict()
# create an instance of RotateOidcKeysRequest from a dict
rotate_oidc_keys_request_from_dict = RotateOidcKeysRequest.from_dict(rotate_oidc_keys_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


