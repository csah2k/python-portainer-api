# coding: utf-8

"""
    Portainer API

    Portainer API is an HTTP API served by Portainer. It is used by the Portainer UI and everything you can do with the UI can be done using the HTTP API. Examples are available at https://gist.github.com/deviantony/77026d402366b4b43fa5918d41bc42f8 You can find out more about Portainer at [http://portainer.io](http://portainer.io) and get some support on [Slack](http://portainer.io/slack/).  # Authentication  Most of the API endpoints require to be authenticated as well as some level of authorization to be used. Portainer API uses JSON Web Token to manage authentication and thus requires you to provide a token in the **Authorization** header of each request with the **Bearer** authentication mechanism.  Example: ``` Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJhZG1pbiIsInJvbGUiOjEsImV4cCI6MTQ5OTM3NjE1NH0.NJ6vE8FY1WG6jsRQzfMqeatJ4vh2TWAeeYfDhP71YEE ```  # Security  Each API endpoint has an associated access policy, it is documented in the description of each endpoint.  Different access policies are available: * Public access * Authenticated access * Restricted access * Administrator access  ### Public access  No authentication is required to access the endpoints with this access policy.  ### Authenticated access  Authentication is required to access the endpoints with this access policy.  ### Restricted access  Authentication is required to access the endpoints with this access policy. Extra-checks might be added to ensure access to the resource is granted. Returned data might also be filtered.  ### Administrator access  Authentication as well as an administrator role are required to access the endpoints with this access policy.  # Execute Docker requests  Portainer **DO NOT** expose specific endpoints to manage your Docker resources (create a container, remove a volume, etc...).  Instead, it acts as a reverse-proxy to the Docker HTTP API. This means that you can execute Docker requests **via** the Portainer HTTP API.  To do so, you can use the `/endpoints/{id}/docker` Portainer API endpoint (which is not documented below due to Swagger limitations). This endpoint has a restricted access policy so you still need to be authenticated to be able to query this endpoint. Any query on this endpoint will be proxied to the Docker API of the associated endpoint (requests and responses objects are the same as documented in the Docker API).  **NOTE**: You can find more information on how to query the Docker API in the [Docker official documentation](https://docs.docker.com/engine/api/v1.30/) as well as in [this Portainer example](https://gist.github.com/deviantony/77026d402366b4b43fa5918d41bc42f8).   # noqa: E501

    OpenAPI spec version: 1.22.1
    Contact: info@portainer.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PublicSettingsInspectResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'logo_url': 'str',
        'display_external_contributors': 'bool',
        'authentication_method': 'int',
        'allow_bind_mounts_for_regular_users': 'bool',
        'allow_privileged_mode_for_regular_users': 'bool'
    }

    attribute_map = {
        'logo_url': 'LogoURL',
        'display_external_contributors': 'DisplayExternalContributors',
        'authentication_method': 'AuthenticationMethod',
        'allow_bind_mounts_for_regular_users': 'AllowBindMountsForRegularUsers',
        'allow_privileged_mode_for_regular_users': 'AllowPrivilegedModeForRegularUsers'
    }

    def __init__(self, logo_url=None, display_external_contributors=None, authentication_method=None, allow_bind_mounts_for_regular_users=None, allow_privileged_mode_for_regular_users=None):  # noqa: E501
        """PublicSettingsInspectResponse - a model defined in Swagger"""  # noqa: E501

        self._logo_url = None
        self._display_external_contributors = None
        self._authentication_method = None
        self._allow_bind_mounts_for_regular_users = None
        self._allow_privileged_mode_for_regular_users = None
        self.discriminator = None

        if logo_url is not None:
            self.logo_url = logo_url
        if display_external_contributors is not None:
            self.display_external_contributors = display_external_contributors
        if authentication_method is not None:
            self.authentication_method = authentication_method
        if allow_bind_mounts_for_regular_users is not None:
            self.allow_bind_mounts_for_regular_users = allow_bind_mounts_for_regular_users
        if allow_privileged_mode_for_regular_users is not None:
            self.allow_privileged_mode_for_regular_users = allow_privileged_mode_for_regular_users

    @property
    def logo_url(self):
        """Gets the logo_url of this PublicSettingsInspectResponse.  # noqa: E501

        URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string  # noqa: E501

        :return: The logo_url of this PublicSettingsInspectResponse.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this PublicSettingsInspectResponse.

        URL to a logo that will be displayed on the login page as well as on top of the sidebar. Will use default Portainer logo when value is empty string  # noqa: E501

        :param logo_url: The logo_url of this PublicSettingsInspectResponse.  # noqa: E501
        :type: str
        """

        self._logo_url = logo_url

    @property
    def display_external_contributors(self):
        """Gets the display_external_contributors of this PublicSettingsInspectResponse.  # noqa: E501

        Whether to display or not external templates contributions as sub-menus in the UI.  # noqa: E501

        :return: The display_external_contributors of this PublicSettingsInspectResponse.  # noqa: E501
        :rtype: bool
        """
        return self._display_external_contributors

    @display_external_contributors.setter
    def display_external_contributors(self, display_external_contributors):
        """Sets the display_external_contributors of this PublicSettingsInspectResponse.

        Whether to display or not external templates contributions as sub-menus in the UI.  # noqa: E501

        :param display_external_contributors: The display_external_contributors of this PublicSettingsInspectResponse.  # noqa: E501
        :type: bool
        """

        self._display_external_contributors = display_external_contributors

    @property
    def authentication_method(self):
        """Gets the authentication_method of this PublicSettingsInspectResponse.  # noqa: E501

        Active authentication method for the Portainer instance. Valid values are: 1 for managed or 2 for LDAP.  # noqa: E501

        :return: The authentication_method of this PublicSettingsInspectResponse.  # noqa: E501
        :rtype: int
        """
        return self._authentication_method

    @authentication_method.setter
    def authentication_method(self, authentication_method):
        """Sets the authentication_method of this PublicSettingsInspectResponse.

        Active authentication method for the Portainer instance. Valid values are: 1 for managed or 2 for LDAP.  # noqa: E501

        :param authentication_method: The authentication_method of this PublicSettingsInspectResponse.  # noqa: E501
        :type: int
        """

        self._authentication_method = authentication_method

    @property
    def allow_bind_mounts_for_regular_users(self):
        """Gets the allow_bind_mounts_for_regular_users of this PublicSettingsInspectResponse.  # noqa: E501

        Whether non-administrator should be able to use bind mounts when creating containers  # noqa: E501

        :return: The allow_bind_mounts_for_regular_users of this PublicSettingsInspectResponse.  # noqa: E501
        :rtype: bool
        """
        return self._allow_bind_mounts_for_regular_users

    @allow_bind_mounts_for_regular_users.setter
    def allow_bind_mounts_for_regular_users(self, allow_bind_mounts_for_regular_users):
        """Sets the allow_bind_mounts_for_regular_users of this PublicSettingsInspectResponse.

        Whether non-administrator should be able to use bind mounts when creating containers  # noqa: E501

        :param allow_bind_mounts_for_regular_users: The allow_bind_mounts_for_regular_users of this PublicSettingsInspectResponse.  # noqa: E501
        :type: bool
        """

        self._allow_bind_mounts_for_regular_users = allow_bind_mounts_for_regular_users

    @property
    def allow_privileged_mode_for_regular_users(self):
        """Gets the allow_privileged_mode_for_regular_users of this PublicSettingsInspectResponse.  # noqa: E501

        Whether non-administrator should be able to use privileged mode when creating containers  # noqa: E501

        :return: The allow_privileged_mode_for_regular_users of this PublicSettingsInspectResponse.  # noqa: E501
        :rtype: bool
        """
        return self._allow_privileged_mode_for_regular_users

    @allow_privileged_mode_for_regular_users.setter
    def allow_privileged_mode_for_regular_users(self, allow_privileged_mode_for_regular_users):
        """Sets the allow_privileged_mode_for_regular_users of this PublicSettingsInspectResponse.

        Whether non-administrator should be able to use privileged mode when creating containers  # noqa: E501

        :param allow_privileged_mode_for_regular_users: The allow_privileged_mode_for_regular_users of this PublicSettingsInspectResponse.  # noqa: E501
        :type: bool
        """

        self._allow_privileged_mode_for_regular_users = allow_privileged_mode_for_regular_users

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PublicSettingsInspectResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicSettingsInspectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
