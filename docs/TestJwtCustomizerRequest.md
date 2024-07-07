# TestJwtCustomizerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **object** | The token type to test the JWT customizer for. | [optional] 
**payload** | [**TestJwtCustomizerRequestPayload**](TestJwtCustomizerRequestPayload.md) |  | [optional] 
**environment_variables** | **Dict[str, str]** |  | [optional] 
**script** | **str** |  | 
**token** | [**GetJwtCustomizer200ResponseOneOf1TokenSample**](GetJwtCustomizer200ResponseOneOf1TokenSample.md) |  | 
**context** | [**GetJwtCustomizer200ResponseOneOfContextSample**](GetJwtCustomizer200ResponseOneOfContextSample.md) |  | 

## Example

```python
from py_logto.models.test_jwt_customizer_request import TestJwtCustomizerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestJwtCustomizerRequest from a JSON string
test_jwt_customizer_request_instance = TestJwtCustomizerRequest.from_json(json)
# print the JSON string representation of the object
print(TestJwtCustomizerRequest.to_json())

# convert the object into a dict
test_jwt_customizer_request_dict = test_jwt_customizer_request_instance.to_dict()
# create an instance of TestJwtCustomizerRequest from a dict
test_jwt_customizer_request_from_dict = TestJwtCustomizerRequest.from_dict(test_jwt_customizer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


