# TestJwtCustomizerRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **object** | The code snippet of the JWT customizer. | [optional] 
**environment_variables** | **object** | The environment variables for the JWT customizer. | [optional] 
**context_sample** | **object** | The sample context for the JWT customizer script testing purpose. | [optional] 
**token_sample** | **object** | The sample token payload for the JWT customizer script testing purpose. | [optional] 

## Example

```python
from py_logto.models.test_jwt_customizer_request_payload import TestJwtCustomizerRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TestJwtCustomizerRequestPayload from a JSON string
test_jwt_customizer_request_payload_instance = TestJwtCustomizerRequestPayload.from_json(json)
# print the JSON string representation of the object
print(TestJwtCustomizerRequestPayload.to_json())

# convert the object into a dict
test_jwt_customizer_request_payload_dict = test_jwt_customizer_request_payload_instance.to_dict()
# create an instance of TestJwtCustomizerRequestPayload from a dict
test_jwt_customizer_request_payload_from_dict = TestJwtCustomizerRequestPayload.from_dict(test_jwt_customizer_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


