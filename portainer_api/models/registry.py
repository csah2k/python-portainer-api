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


class Registry(object):
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
        'id': 'int',
        'name': 'str',
        'url': 'str',
        'authentication': 'bool',
        'username': 'str',
        'password': 'str',
        'authorized_users': 'list[int]',
        'authorized_teams': 'list[int]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'url': 'URL',
        'authentication': 'Authentication',
        'username': 'Username',
        'password': 'Password',
        'authorized_users': 'AuthorizedUsers',
        'authorized_teams': 'AuthorizedTeams'
    }

    def __init__(self, id=None, name=None, url=None, authentication=None, username=None, password=None, authorized_users=None, authorized_teams=None):  # noqa: E501
        """Registry - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._url = None
        self._authentication = None
        self._username = None
        self._password = None
        self._authorized_users = None
        self._authorized_teams = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if url is not None:
            self.url = url
        if authentication is not None:
            self.authentication = authentication
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if authorized_users is not None:
            self.authorized_users = authorized_users
        if authorized_teams is not None:
            self.authorized_teams = authorized_teams

    @property
    def id(self):
        """Gets the id of this Registry.  # noqa: E501

        Registry identifier  # noqa: E501

        :return: The id of this Registry.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Registry.

        Registry identifier  # noqa: E501

        :param id: The id of this Registry.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Registry.  # noqa: E501

        Registry name  # noqa: E501

        :return: The name of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Registry.

        Registry name  # noqa: E501

        :param name: The name of this Registry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this Registry.  # noqa: E501

        URL or IP address of the Docker registry  # noqa: E501

        :return: The url of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Registry.

        URL or IP address of the Docker registry  # noqa: E501

        :param url: The url of this Registry.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def authentication(self):
        """Gets the authentication of this Registry.  # noqa: E501

        Is authentication against this registry enabled  # noqa: E501

        :return: The authentication of this Registry.  # noqa: E501
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this Registry.

        Is authentication against this registry enabled  # noqa: E501

        :param authentication: The authentication of this Registry.  # noqa: E501
        :type: bool
        """

        self._authentication = authentication

    @property
    def username(self):
        """Gets the username of this Registry.  # noqa: E501

        Username used to authenticate against this registry  # noqa: E501

        :return: The username of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Registry.

        Username used to authenticate against this registry  # noqa: E501

        :param username: The username of this Registry.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this Registry.  # noqa: E501

        Password used to authenticate against this registry  # noqa: E501

        :return: The password of this Registry.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Registry.

        Password used to authenticate against this registry  # noqa: E501

        :param password: The password of this Registry.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def authorized_users(self):
        """Gets the authorized_users of this Registry.  # noqa: E501

        List of user identifiers authorized to use this registry  # noqa: E501

        :return: The authorized_users of this Registry.  # noqa: E501
        :rtype: list[int]
        """
        return self._authorized_users

    @authorized_users.setter
    def authorized_users(self, authorized_users):
        """Sets the authorized_users of this Registry.

        List of user identifiers authorized to use this registry  # noqa: E501

        :param authorized_users: The authorized_users of this Registry.  # noqa: E501
        :type: list[int]
        """

        self._authorized_users = authorized_users

    @property
    def authorized_teams(self):
        """Gets the authorized_teams of this Registry.  # noqa: E501

        List of team identifiers authorized to use this registry  # noqa: E501

        :return: The authorized_teams of this Registry.  # noqa: E501
        :rtype: list[int]
        """
        return self._authorized_teams

    @authorized_teams.setter
    def authorized_teams(self, authorized_teams):
        """Sets the authorized_teams of this Registry.

        List of team identifiers authorized to use this registry  # noqa: E501

        :param authorized_teams: The authorized_teams of this Registry.  # noqa: E501
        :type: list[int]
        """

        self._authorized_teams = authorized_teams

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
        if issubclass(Registry, dict):
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
        if not isinstance(other, Registry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
