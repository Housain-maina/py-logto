# ListApplications200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**secret** | **str** |  | 
**description** | **str** |  | 
**type** | **str** |  | 
**oidc_client_metadata** | [**ListApplications200ResponseInnerOidcClientMetadata**](ListApplications200ResponseInnerOidcClientMetadata.md) |  | 
**custom_client_metadata** | [**ListApplications200ResponseInnerCustomClientMetadata**](ListApplications200ResponseInnerCustomClientMetadata.md) |  | 
**protected_app_metadata** | [**ListApplications200ResponseInnerProtectedAppMetadata**](ListApplications200ResponseInnerProtectedAppMetadata.md) |  | 
**is_third_party** | **bool** |  | 
**created_at** | **float** |  | 

## Example

```python
from py_logto.models.list_applications200_response_inner import ListApplications200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplications200ResponseInner from a JSON string
list_applications200_response_inner_instance = ListApplications200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListApplications200ResponseInner.to_json())

# convert the object into a dict
list_applications200_response_inner_dict = list_applications200_response_inner_instance.to_dict()
# create an instance of ListApplications200ResponseInner from a dict
list_applications200_response_inner_from_dict = ListApplications200ResponseInner.from_dict(list_applications200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


