"""
Fireblocks API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.6.2
Contact: support@fireblocks.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


def validate_not_empty_string(function_name: str, param_name: str, param_value: str):
    if not param_value:
        raise ValueError(
            f"The required parameter '{param_name}' was empty when calling '{function_name}'"
        )
