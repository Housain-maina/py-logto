# GetJwtCustomizer200ResponseOneOf1TokenSample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jti** | **str** |  | [optional] 
**aud** | [**GetJwtCustomizer200ResponseOneOfTokenSampleAud**](GetJwtCustomizer200ResponseOneOfTokenSampleAud.md) |  | [optional] 
**scope** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 

## Example

```python
from py_logto.models.get_jwt_customizer200_response_one_of1_token_sample import GetJwtCustomizer200ResponseOneOf1TokenSample

# TODO update the JSON string below
json = "{}"
# create an instance of GetJwtCustomizer200ResponseOneOf1TokenSample from a JSON string
get_jwt_customizer200_response_one_of1_token_sample_instance = GetJwtCustomizer200ResponseOneOf1TokenSample.from_json(json)
# print the JSON string representation of the object
print(GetJwtCustomizer200ResponseOneOf1TokenSample.to_json())

# convert the object into a dict
get_jwt_customizer200_response_one_of1_token_sample_dict = get_jwt_customizer200_response_one_of1_token_sample_instance.to_dict()
# create an instance of GetJwtCustomizer200ResponseOneOf1TokenSample from a dict
get_jwt_customizer200_response_one_of1_token_sample_from_dict = GetJwtCustomizer200ResponseOneOf1TokenSample.from_dict(get_jwt_customizer200_response_one_of1_token_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


