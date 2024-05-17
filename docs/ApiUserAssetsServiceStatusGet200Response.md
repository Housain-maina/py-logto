# ApiUserAssetsServiceStatusGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ApiUserAssetsServiceStatusGet200ResponseStatus**](ApiUserAssetsServiceStatusGet200ResponseStatus.md) |  | 
**allow_upload_mime_types** | **List[str]** |  | [optional] 
**max_upload_file_size** | **float** |  | [optional] 

## Example

```python
from py_logto.models.api_user_assets_service_status_get200_response import ApiUserAssetsServiceStatusGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUserAssetsServiceStatusGet200Response from a JSON string
api_user_assets_service_status_get200_response_instance = ApiUserAssetsServiceStatusGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiUserAssetsServiceStatusGet200Response.to_json())

# convert the object into a dict
api_user_assets_service_status_get200_response_dict = api_user_assets_service_status_get200_response_instance.to_dict()
# create an instance of ApiUserAssetsServiceStatusGet200Response from a dict
api_user_assets_service_status_get200_response_from_dict = ApiUserAssetsServiceStatusGet200Response.from_dict(api_user_assets_service_status_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


