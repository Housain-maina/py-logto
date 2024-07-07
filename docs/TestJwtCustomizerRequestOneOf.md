# TestJwtCustomizerRequestOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **str** |  | 
**environment_variables** | **Dict[str, str]** |  | [optional] 
**script** | **str** |  | 
**token** | [**GetJwtCustomizer200ResponseOneOfTokenSample**](GetJwtCustomizer200ResponseOneOfTokenSample.md) |  | 
**context** | [**GetJwtCustomizer200ResponseOneOfContextSample**](GetJwtCustomizer200ResponseOneOfContextSample.md) |  | 

## Example

```python
from py_logto.models.test_jwt_customizer_request_one_of import TestJwtCustomizerRequestOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of TestJwtCustomizerRequestOneOf from a JSON string
test_jwt_customizer_request_one_of_instance = TestJwtCustomizerRequestOneOf.from_json(json)
# print the JSON string representation of the object
print(TestJwtCustomizerRequestOneOf.to_json())

# convert the object into a dict
test_jwt_customizer_request_one_of_dict = test_jwt_customizer_request_one_of_instance.to_dict()
# create an instance of TestJwtCustomizerRequestOneOf from a dict
test_jwt_customizer_request_one_of_from_dict = TestJwtCustomizerRequestOneOf.from_dict(test_jwt_customizer_request_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


