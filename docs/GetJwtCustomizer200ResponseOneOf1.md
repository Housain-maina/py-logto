# GetJwtCustomizer200ResponseOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | 
**environment_variables** | **Dict[str, str]** |  | [optional] 
**context_sample** | **object** | arbitrary | [optional] 
**token_sample** | [**GetJwtCustomizer200ResponseOneOf1TokenSample**](GetJwtCustomizer200ResponseOneOf1TokenSample.md) |  | [optional] 

## Example

```python
from py_logto.models.get_jwt_customizer200_response_one_of1 import GetJwtCustomizer200ResponseOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of GetJwtCustomizer200ResponseOneOf1 from a JSON string
get_jwt_customizer200_response_one_of1_instance = GetJwtCustomizer200ResponseOneOf1.from_json(json)
# print the JSON string representation of the object
print(GetJwtCustomizer200ResponseOneOf1.to_json())

# convert the object into a dict
get_jwt_customizer200_response_one_of1_dict = get_jwt_customizer200_response_one_of1_instance.to_dict()
# create an instance of GetJwtCustomizer200ResponseOneOf1 from a dict
get_jwt_customizer200_response_one_of1_from_dict = GetJwtCustomizer200ResponseOneOf1.from_dict(get_jwt_customizer200_response_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


