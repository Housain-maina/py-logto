# ApiConfigsJwtCustomizerTokenTypePathPutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **object** | The script of the JWT customizer. | [optional] 
**environment_variables** | **object** | The environment variables for the JWT customizer. | [optional] 
**context_sample** | **object** | The sample context for the JWT customizer script testing purpose. | [optional] 
**token_sample** | **object** | The sample raw token payload for the JWT customizer script testing purpose. | [optional] 

## Example

```python
from py_logto.models.api_configs_jwt_customizer_token_type_path_put_request import ApiConfigsJwtCustomizerTokenTypePathPutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfigsJwtCustomizerTokenTypePathPutRequest from a JSON string
api_configs_jwt_customizer_token_type_path_put_request_instance = ApiConfigsJwtCustomizerTokenTypePathPutRequest.from_json(json)
# print the JSON string representation of the object
print(ApiConfigsJwtCustomizerTokenTypePathPutRequest.to_json())

# convert the object into a dict
api_configs_jwt_customizer_token_type_path_put_request_dict = api_configs_jwt_customizer_token_type_path_put_request_instance.to_dict()
# create an instance of ApiConfigsJwtCustomizerTokenTypePathPutRequest from a dict
api_configs_jwt_customizer_token_type_path_put_request_from_dict = ApiConfigsJwtCustomizerTokenTypePathPutRequest.from_dict(api_configs_jwt_customizer_token_type_path_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


