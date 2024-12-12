# openapi_client.DefaultApi

All URIs are relative to *http://localhost:9000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_tasks_get**](DefaultApi.md#api_tasks_get) | **GET** /api/tasks/ | Lấy danh sách tất cả các nhiệm vụ
[**api_tasks_id_delete**](DefaultApi.md#api_tasks_id_delete) | **DELETE** /api/tasks/{id}/ | Xóa một nhiệm vụ cụ thể
[**api_tasks_id_get**](DefaultApi.md#api_tasks_id_get) | **GET** /api/tasks/{id}/ | Lấy thông tin một nhiệm vụ cụ thể
[**api_tasks_id_put**](DefaultApi.md#api_tasks_id_put) | **PUT** /api/tasks/{id}/ | Cập nhật thông tin một nhiệm vụ cụ thể
[**api_tasks_post**](DefaultApi.md#api_tasks_post) | **POST** /api/tasks/ | Tạo một nhiệm vụ mới


# **api_tasks_get**
> List[Task] api_tasks_get()

Lấy danh sách tất cả các nhiệm vụ

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:9000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        # Lấy danh sách tất cả các nhiệm vụ
        api_response = api_instance.api_tasks_get()
        print("The response of DefaultApi->api_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_tasks_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Task]**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thành công |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_delete**
> api_tasks_id_delete(id)

Xóa một nhiệm vụ cụ thể

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:9000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | ID của nhiệm vụ

    try:
        # Xóa một nhiệm vụ cụ thể
        api_instance.api_tasks_id_delete(id)
    except Exception as e:
        print("Exception when calling DefaultApi->api_tasks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID của nhiệm vụ | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Nhiệm vụ đã được xóa thành công |  -  |
**404** | Nhiệm vụ không tồn tại |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_get**
> Task api_tasks_id_get(id)

Lấy thông tin một nhiệm vụ cụ thể

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:9000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | ID của nhiệm vụ

    try:
        # Lấy thông tin một nhiệm vụ cụ thể
        api_response = api_instance.api_tasks_id_get(id)
        print("The response of DefaultApi->api_tasks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_tasks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID của nhiệm vụ | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thành công |  -  |
**404** | Nhiệm vụ không tồn tại |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_put**
> Task api_tasks_id_put(id, task)

Cập nhật thông tin một nhiệm vụ cụ thể

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:9000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 56 # int | ID của nhiệm vụ
    task = openapi_client.Task() # Task | 

    try:
        # Cập nhật thông tin một nhiệm vụ cụ thể
        api_response = api_instance.api_tasks_id_put(id, task)
        print("The response of DefaultApi->api_tasks_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_tasks_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID của nhiệm vụ | 
 **task** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Nhiệm vụ đã được cập nhật thành công |  -  |
**400** | Dữ liệu đầu vào không hợp lệ |  -  |
**404** | Nhiệm vụ không tồn tại |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_post**
> Task api_tasks_post(task)

Tạo một nhiệm vụ mới

### Example


```python
import openapi_client
from openapi_client.models.task import Task
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:9000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:9000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    task = openapi_client.Task() # Task | 

    try:
        # Tạo một nhiệm vụ mới
        api_response = api_instance.api_tasks_post(task)
        print("The response of DefaultApi->api_tasks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->api_tasks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | [**Task**](Task.md)|  | 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Nhiệm vụ đã được tạo thành công |  -  |
**400** | Dữ liệu đầu vào không hợp lệ |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

