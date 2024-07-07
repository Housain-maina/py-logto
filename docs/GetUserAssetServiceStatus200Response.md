# GetUserAssetServiceStatus200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GetUserAssetServiceStatus200ResponseStatus**](GetUserAssetServiceStatus200ResponseStatus.md) |  | 
**allow_upload_mime_types** | **List[str]** |  | [optional] 
**max_upload_file_size** | **float** |  | [optional] 

## Example

```python
from py_logto.models.get_user_asset_service_status200_response import GetUserAssetServiceStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserAssetServiceStatus200Response from a JSON string
get_user_asset_service_status200_response_instance = GetUserAssetServiceStatus200Response.from_json(json)
# print the JSON string representation of the object
print(GetUserAssetServiceStatus200Response.to_json())

# convert the object into a dict
get_user_asset_service_status200_response_dict = get_user_asset_service_status200_response_instance.to_dict()
# create an instance of GetUserAssetServiceStatus200Response from a dict
get_user_asset_service_status200_response_from_dict = GetUserAssetServiceStatus200Response.from_dict(get_user_asset_service_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


