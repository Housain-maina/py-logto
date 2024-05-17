# ApiConfigsJwtCustomizerTokenTypePathGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** |  | [optional] 
**environment_variables** | **Dict[str, str]** |  | [optional] 
**context_sample** | **object** | arbitrary | [optional] 
**token_sample** | [**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOf1TokenSample.md) |  | [optional] 

## Example

```python
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response import ApiConfigsJwtCustomizerTokenTypePathGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfigsJwtCustomizerTokenTypePathGet200Response from a JSON string
api_configs_jwt_customizer_token_type_path_get200_response_instance = ApiConfigsJwtCustomizerTokenTypePathGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiConfigsJwtCustomizerTokenTypePathGet200Response.to_json())

# convert the object into a dict
api_configs_jwt_customizer_token_type_path_get200_response_dict = api_configs_jwt_customizer_token_type_path_get200_response_instance.to_dict()
# create an instance of ApiConfigsJwtCustomizerTokenTypePathGet200Response from a dict
api_configs_jwt_customizer_token_type_path_get200_response_from_dict = ApiConfigsJwtCustomizerTokenTypePathGet200Response.from_dict(api_configs_jwt_customizer_token_type_path_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


