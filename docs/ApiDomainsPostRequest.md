# ApiDomainsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain name, e.g. &#x60;example.com&#x60;. | 

## Example

```python
from py_logto.models.api_domains_post_request import ApiDomainsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDomainsPostRequest from a JSON string
api_domains_post_request_instance = ApiDomainsPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiDomainsPostRequest.to_json())

# convert the object into a dict
api_domains_post_request_dict = api_domains_post_request_instance.to_dict()
# create an instance of ApiDomainsPostRequest from a dict
api_domains_post_request_from_dict = ApiDomainsPostRequest.from_dict(api_domains_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


