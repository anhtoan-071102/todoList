# coding: utf-8

"""
    Task Management API

    API cho việc quản lý các nhiệm vụ trong ngày

    The version of the OpenAPI document: 1.0.0
    Contact: anhtoan07112002@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "openapi-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Task Management API",
    author="Anh Toan",
    author_email="anhtoan07112002@gmail.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Task Management API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    API cho việc quản lý các nhiệm vụ trong ngày
    """,  # noqa: E501
    package_data={"openapi_client": ["py.typed"]},
)
