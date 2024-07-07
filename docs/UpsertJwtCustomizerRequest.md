# UpsertJwtCustomizerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **object** | The script of the JWT customizer. | [optional] 
**environment_variables** | **object** | The environment variables for the JWT customizer. | [optional] 
**context_sample** | **object** | The sample context for the JWT customizer script testing purpose. | [optional] 
**token_sample** | **object** | The sample raw token payload for the JWT customizer script testing purpose. | [optional] 

## Example

```python
from py_logto.models.upsert_jwt_customizer_request import UpsertJwtCustomizerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertJwtCustomizerRequest from a JSON string
upsert_jwt_customizer_request_instance = UpsertJwtCustomizerRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertJwtCustomizerRequest.to_json())

# convert the object into a dict
upsert_jwt_customizer_request_dict = upsert_jwt_customizer_request_instance.to_dict()
# create an instance of UpsertJwtCustomizerRequest from a dict
upsert_jwt_customizer_request_from_dict = UpsertJwtCustomizerRequest.from_dict(upsert_jwt_customizer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


