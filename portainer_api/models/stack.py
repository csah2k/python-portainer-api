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

from portainer_api.models.stack_env import StackEnv  # noqa: F401,E501


class Stack(object):
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
        'id': 'str',
        'name': 'str',
        'type': 'int',
        'endpoint_id': 'int',
        'entry_point': 'str',
        'swarm_id': 'str',
        'project_path': 'str',
        'env': 'list[StackEnv]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'type': 'Type',
        'endpoint_id': 'EndpointID',
        'entry_point': 'EntryPoint',
        'swarm_id': 'SwarmID',
        'project_path': 'ProjectPath',
        'env': 'Env'
    }

    def __init__(self, id=None, name=None, type=None, endpoint_id=None, entry_point=None, swarm_id=None, project_path=None, env=None):  # noqa: E501
        """Stack - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._type = None
        self._endpoint_id = None
        self._entry_point = None
        self._swarm_id = None
        self._project_path = None
        self._env = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if entry_point is not None:
            self.entry_point = entry_point
        if swarm_id is not None:
            self.swarm_id = swarm_id
        if project_path is not None:
            self.project_path = project_path
        if env is not None:
            self.env = env

    @property
    def id(self):
        """Gets the id of this Stack.  # noqa: E501

        Stack identifier  # noqa: E501

        :return: The id of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Stack.

        Stack identifier  # noqa: E501

        :param id: The id of this Stack.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Stack.  # noqa: E501

        Stack name  # noqa: E501

        :return: The name of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Stack.

        Stack name  # noqa: E501

        :param name: The name of this Stack.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Stack.  # noqa: E501

        Stack type. 1 for a Swarm stack, 2 for a Compose stack  # noqa: E501

        :return: The type of this Stack.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Stack.

        Stack type. 1 for a Swarm stack, 2 for a Compose stack  # noqa: E501

        :param type: The type of this Stack.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def endpoint_id(self):
        """Gets the endpoint_id of this Stack.  # noqa: E501

        Endpoint identifier. Reference the endpoint that will be used for deployment   # noqa: E501

        :return: The endpoint_id of this Stack.  # noqa: E501
        :rtype: int
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """Sets the endpoint_id of this Stack.

        Endpoint identifier. Reference the endpoint that will be used for deployment   # noqa: E501

        :param endpoint_id: The endpoint_id of this Stack.  # noqa: E501
        :type: int
        """

        self._endpoint_id = endpoint_id

    @property
    def entry_point(self):
        """Gets the entry_point of this Stack.  # noqa: E501

        Path to the Stack file  # noqa: E501

        :return: The entry_point of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._entry_point

    @entry_point.setter
    def entry_point(self, entry_point):
        """Sets the entry_point of this Stack.

        Path to the Stack file  # noqa: E501

        :param entry_point: The entry_point of this Stack.  # noqa: E501
        :type: str
        """

        self._entry_point = entry_point

    @property
    def swarm_id(self):
        """Gets the swarm_id of this Stack.  # noqa: E501

        Cluster identifier of the Swarm cluster where the stack is deployed  # noqa: E501

        :return: The swarm_id of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._swarm_id

    @swarm_id.setter
    def swarm_id(self, swarm_id):
        """Sets the swarm_id of this Stack.

        Cluster identifier of the Swarm cluster where the stack is deployed  # noqa: E501

        :param swarm_id: The swarm_id of this Stack.  # noqa: E501
        :type: str
        """

        self._swarm_id = swarm_id

    @property
    def project_path(self):
        """Gets the project_path of this Stack.  # noqa: E501

        Path on disk to the repository hosting the Stack file  # noqa: E501

        :return: The project_path of this Stack.  # noqa: E501
        :rtype: str
        """
        return self._project_path

    @project_path.setter
    def project_path(self, project_path):
        """Sets the project_path of this Stack.

        Path on disk to the repository hosting the Stack file  # noqa: E501

        :param project_path: The project_path of this Stack.  # noqa: E501
        :type: str
        """

        self._project_path = project_path

    @property
    def env(self):
        """Gets the env of this Stack.  # noqa: E501

        A list of environment variables used during stack deployment  # noqa: E501

        :return: The env of this Stack.  # noqa: E501
        :rtype: list[StackEnv]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this Stack.

        A list of environment variables used during stack deployment  # noqa: E501

        :param env: The env of this Stack.  # noqa: E501
        :type: list[StackEnv]
        """

        self._env = env

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
        if issubclass(Stack, dict):
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
        if not isinstance(other, Stack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
