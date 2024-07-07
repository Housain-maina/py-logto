# GetJwtCustomizer200ResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | 
**environment_variables** | **Dict[str, str]** |  | [optional] 
**context_sample** | [**GetJwtCustomizer200ResponseOneOfContextSample**](GetJwtCustomizer200ResponseOneOfContextSample.md) |  | [optional] 
**token_sample** | [**GetJwtCustomizer200ResponseOneOfTokenSample**](GetJwtCustomizer200ResponseOneOfTokenSample.md) |  | [optional] 

## Example

```python
from py_logto.models.get_jwt_customizer200_response_one_of import GetJwtCustomizer200ResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetJwtCustomizer200ResponseOneOf from a JSON string
get_jwt_customizer200_response_one_of_instance = GetJwtCustomizer200ResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(GetJwtCustomizer200ResponseOneOf.to_json())

# convert the object into a dict
get_jwt_customizer200_response_one_of_dict = get_jwt_customizer200_response_one_of_instance.to_dict()
# create an instance of GetJwtCustomizer200ResponseOneOf from a dict
get_jwt_customizer200_response_one_of_from_dict = GetJwtCustomizer200ResponseOneOf.from_dict(get_jwt_customizer200_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


