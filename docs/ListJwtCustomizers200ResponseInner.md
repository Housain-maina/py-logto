# ListJwtCustomizers200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value** | [**GetJwtCustomizer200ResponseOneOf1**](GetJwtCustomizer200ResponseOneOf1.md) |  | 

## Example

```python
from py_logto.models.list_jwt_customizers200_response_inner import ListJwtCustomizers200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListJwtCustomizers200ResponseInner from a JSON string
list_jwt_customizers200_response_inner_instance = ListJwtCustomizers200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListJwtCustomizers200ResponseInner.to_json())

# convert the object into a dict
list_jwt_customizers200_response_inner_dict = list_jwt_customizers200_response_inner_instance.to_dict()
# create an instance of ListJwtCustomizers200ResponseInner from a dict
list_jwt_customizers200_response_inner_from_dict = ListJwtCustomizers200ResponseInner.from_dict(list_jwt_customizers200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


