"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import platform


class UserAgentUtil:
    @staticmethod
    def get_user_agent(is_anonymous_platform: bool, custom_user_agent: str) -> str:
        user_agent = "fireblocks/sdk/python/1.0.0"
        if not is_anonymous_platform:
            os_type = platform.system()
            os_version = platform.release()
            os_arch = platform.machine()

            user_agent += f" ({os_type} {os_version}; {os_arch})"

        if custom_user_agent is not None:
            user_agent = custom_user_agent + " " + user_agent

        return user_agent
