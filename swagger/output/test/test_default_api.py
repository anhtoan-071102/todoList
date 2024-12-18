# coding: utf-8

"""
    Task Management API

    API cho việc quản lý các nhiệm vụ trong ngày

    The version of the OpenAPI document: 1.0.0
    Contact: anhtoan07112002@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.default_api import DefaultApi


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DefaultApi()

    def tearDown(self) -> None:
        pass

    def test_api_tasks_get(self) -> None:
        """Test case for api_tasks_get

        Lấy danh sách tất cả các nhiệm vụ
        """
        pass

    def test_api_tasks_id_delete(self) -> None:
        """Test case for api_tasks_id_delete

        Xóa một nhiệm vụ cụ thể
        """
        pass

    def test_api_tasks_id_get(self) -> None:
        """Test case for api_tasks_id_get

        Lấy thông tin một nhiệm vụ cụ thể
        """
        pass

    def test_api_tasks_id_put(self) -> None:
        """Test case for api_tasks_id_put

        Cập nhật thông tin một nhiệm vụ cụ thể
        """
        pass

    def test_api_tasks_post(self) -> None:
        """Test case for api_tasks_post

        Tạo một nhiệm vụ mới
        """
        pass


if __name__ == '__main__':
    unittest.main()
