# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID của nhiệm vụ | [optional] 
**tittle** | **str** | Tiêu đề của nhiệm vụ | 
**description** | **str** | Mô tả chi tiết của nhiệm vụ | 
**status** | **str** | Trạng thái của nhiệm vụ (PENDING, IN_PROGRESS, COMPLETED, OVERDUE) | 
**start_time** | **datetime** | Thời gian bắt đầu nhiệm vụ | 
**end_time** | **datetime** | Thời gian kết thúc nhiệm vụ | 

## Example

```python
from openapi_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


