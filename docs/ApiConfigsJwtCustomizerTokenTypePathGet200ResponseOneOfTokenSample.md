# ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfTokenSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jti** | **str** |  | [optional] 
**aud** | [**ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfTokenSampleAud**](ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfTokenSampleAud.md) |  | [optional] 
**scope** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**expires_with_session** | **bool** |  | [optional] 
**grant_id** | **str** |  | [optional] 
**gty** | **str** |  | [optional] 
**session_uid** | **str** |  | [optional] 
**sid** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_token_sample import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfTokenSample

# TODO update the JSON string below
json = "{}"
# create an instance of ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfTokenSample from a JSON string
api_configs_jwt_customizer_token_type_path_get200_response_one_of_token_sample_instance = ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfTokenSample.from_json(json)
# print the JSON string representation of the object
print(ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfTokenSample.to_json())

# convert the object into a dict
api_configs_jwt_customizer_token_type_path_get200_response_one_of_token_sample_dict = api_configs_jwt_customizer_token_type_path_get200_response_one_of_token_sample_instance.to_dict()
# create an instance of ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfTokenSample from a dict
api_configs_jwt_customizer_token_type_path_get200_response_one_of_token_sample_from_dict = ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfTokenSample.from_dict(api_configs_jwt_customizer_token_type_path_get200_response_one_of_token_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


