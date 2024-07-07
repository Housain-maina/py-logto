# TestJwtCustomizerRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_type** | **str** |  | 
**environment_variables** | **Dict[str, str]** |  | [optional] 
**script** | **str** |  | 
**token** | [**GetJwtCustomizer200ResponseOneOf1TokenSample**](GetJwtCustomizer200ResponseOneOf1TokenSample.md) |  | 

## Example

```python
from py_logto.models.test_jwt_customizer_request_one_of1 import TestJwtCustomizerRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of TestJwtCustomizerRequestOneOf1 from a JSON string
test_jwt_customizer_request_one_of1_instance = TestJwtCustomizerRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(TestJwtCustomizerRequestOneOf1.to_json())

# convert the object into a dict
test_jwt_customizer_request_one_of1_dict = test_jwt_customizer_request_one_of1_instance.to_dict()
# create an instance of TestJwtCustomizerRequestOneOf1 from a dict
test_jwt_customizer_request_one_of1_from_dict = TestJwtCustomizerRequestOneOf1.from_dict(test_jwt_customizer_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


