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

from portainer_api.models.pair import Pair  # noqa: F401,E501
from portainer_api.models.template_env import TemplateEnv  # noqa: F401,E501
from portainer_api.models.template_repository import TemplateRepository  # noqa: F401,E501
from portainer_api.models.template_volume import TemplateVolume  # noqa: F401,E501


class TemplateCreateRequest(object):
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
        'type': 'int',
        'title': 'str',
        'description': 'str',
        'administrator_only': 'bool',
        'image': 'str',
        'repository': 'TemplateRepository',
        'name': 'str',
        'logo': 'str',
        'env': 'list[TemplateEnv]',
        'note': 'str',
        'platform': 'str',
        'categories': 'list[str]',
        'registry': 'str',
        'command': 'str',
        'network': 'str',
        'volumes': 'list[TemplateVolume]',
        'ports': 'list[str]',
        'labels': 'list[Pair]',
        'privileged': 'bool',
        'interactive': 'bool',
        'restart_policy': 'str',
        'hostname': 'str'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'description': 'description',
        'administrator_only': 'administrator_only',
        'image': 'image',
        'repository': 'repository',
        'name': 'name',
        'logo': 'logo',
        'env': 'env',
        'note': 'note',
        'platform': 'platform',
        'categories': 'categories',
        'registry': 'registry',
        'command': 'command',
        'network': 'network',
        'volumes': 'volumes',
        'ports': 'ports',
        'labels': 'labels',
        'privileged': 'privileged',
        'interactive': 'interactive',
        'restart_policy': 'restart_policy',
        'hostname': 'hostname'
    }

    def __init__(self, type=None, title=None, description=None, administrator_only=None, image=None, repository=None, name=None, logo=None, env=None, note=None, platform=None, categories=None, registry=None, command=None, network=None, volumes=None, ports=None, labels=None, privileged=None, interactive=None, restart_policy=None, hostname=None):  # noqa: E501
        """TemplateCreateRequest - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._title = None
        self._description = None
        self._administrator_only = None
        self._image = None
        self._repository = None
        self._name = None
        self._logo = None
        self._env = None
        self._note = None
        self._platform = None
        self._categories = None
        self._registry = None
        self._command = None
        self._network = None
        self._volumes = None
        self._ports = None
        self._labels = None
        self._privileged = None
        self._interactive = None
        self._restart_policy = None
        self._hostname = None
        self.discriminator = None

        self.type = type
        self.title = title
        self.description = description
        if administrator_only is not None:
            self.administrator_only = administrator_only
        if image is not None:
            self.image = image
        if repository is not None:
            self.repository = repository
        if name is not None:
            self.name = name
        if logo is not None:
            self.logo = logo
        if env is not None:
            self.env = env
        if note is not None:
            self.note = note
        if platform is not None:
            self.platform = platform
        if categories is not None:
            self.categories = categories
        if registry is not None:
            self.registry = registry
        if command is not None:
            self.command = command
        if network is not None:
            self.network = network
        if volumes is not None:
            self.volumes = volumes
        if ports is not None:
            self.ports = ports
        if labels is not None:
            self.labels = labels
        if privileged is not None:
            self.privileged = privileged
        if interactive is not None:
            self.interactive = interactive
        if restart_policy is not None:
            self.restart_policy = restart_policy
        if hostname is not None:
            self.hostname = hostname

    @property
    def type(self):
        """Gets the type of this TemplateCreateRequest.  # noqa: E501

        Template type. Valid values are: 1 (container), 2 (Swarm stack) or 3 (Compose stack)  # noqa: E501

        :return: The type of this TemplateCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateCreateRequest.

        Template type. Valid values are: 1 (container), 2 (Swarm stack) or 3 (Compose stack)  # noqa: E501

        :param type: The type of this TemplateCreateRequest.  # noqa: E501
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def title(self):
        """Gets the title of this TemplateCreateRequest.  # noqa: E501

        Title of the template  # noqa: E501

        :return: The title of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TemplateCreateRequest.

        Title of the template  # noqa: E501

        :param title: The title of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this TemplateCreateRequest.  # noqa: E501

        Description of the template  # noqa: E501

        :return: The description of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateCreateRequest.

        Description of the template  # noqa: E501

        :param description: The description of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def administrator_only(self):
        """Gets the administrator_only of this TemplateCreateRequest.  # noqa: E501

        Whether the template should be available to administrators only  # noqa: E501

        :return: The administrator_only of this TemplateCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._administrator_only

    @administrator_only.setter
    def administrator_only(self, administrator_only):
        """Sets the administrator_only of this TemplateCreateRequest.

        Whether the template should be available to administrators only  # noqa: E501

        :param administrator_only: The administrator_only of this TemplateCreateRequest.  # noqa: E501
        :type: bool
        """

        self._administrator_only = administrator_only

    @property
    def image(self):
        """Gets the image of this TemplateCreateRequest.  # noqa: E501

        Image associated to a container template. Mandatory for a container template  # noqa: E501

        :return: The image of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this TemplateCreateRequest.

        Image associated to a container template. Mandatory for a container template  # noqa: E501

        :param image: The image of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def repository(self):
        """Gets the repository of this TemplateCreateRequest.  # noqa: E501


        :return: The repository of this TemplateCreateRequest.  # noqa: E501
        :rtype: TemplateRepository
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this TemplateCreateRequest.


        :param repository: The repository of this TemplateCreateRequest.  # noqa: E501
        :type: TemplateRepository
        """

        self._repository = repository

    @property
    def name(self):
        """Gets the name of this TemplateCreateRequest.  # noqa: E501

        Default name for the stack/container to be used on deployment  # noqa: E501

        :return: The name of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateCreateRequest.

        Default name for the stack/container to be used on deployment  # noqa: E501

        :param name: The name of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def logo(self):
        """Gets the logo of this TemplateCreateRequest.  # noqa: E501

        URL of the template's logo  # noqa: E501

        :return: The logo of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this TemplateCreateRequest.

        URL of the template's logo  # noqa: E501

        :param logo: The logo of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def env(self):
        """Gets the env of this TemplateCreateRequest.  # noqa: E501

        A list of environment variables used during the template deployment  # noqa: E501

        :return: The env of this TemplateCreateRequest.  # noqa: E501
        :rtype: list[TemplateEnv]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this TemplateCreateRequest.

        A list of environment variables used during the template deployment  # noqa: E501

        :param env: The env of this TemplateCreateRequest.  # noqa: E501
        :type: list[TemplateEnv]
        """

        self._env = env

    @property
    def note(self):
        """Gets the note of this TemplateCreateRequest.  # noqa: E501

        A note that will be displayed in the UI. Supports HTML content  # noqa: E501

        :return: The note of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this TemplateCreateRequest.

        A note that will be displayed in the UI. Supports HTML content  # noqa: E501

        :param note: The note of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def platform(self):
        """Gets the platform of this TemplateCreateRequest.  # noqa: E501

        Platform associated to the template. Valid values are: 'linux', 'windows' or leave empty for multi-platform  # noqa: E501

        :return: The platform of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this TemplateCreateRequest.

        Platform associated to the template. Valid values are: 'linux', 'windows' or leave empty for multi-platform  # noqa: E501

        :param platform: The platform of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def categories(self):
        """Gets the categories of this TemplateCreateRequest.  # noqa: E501

        A list of categories associated to the template  # noqa: E501

        :return: The categories of this TemplateCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this TemplateCreateRequest.

        A list of categories associated to the template  # noqa: E501

        :param categories: The categories of this TemplateCreateRequest.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def registry(self):
        """Gets the registry of this TemplateCreateRequest.  # noqa: E501

        The URL of a registry associated to the image for a container template  # noqa: E501

        :return: The registry of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """Sets the registry of this TemplateCreateRequest.

        The URL of a registry associated to the image for a container template  # noqa: E501

        :param registry: The registry of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._registry = registry

    @property
    def command(self):
        """Gets the command of this TemplateCreateRequest.  # noqa: E501

        The command that will be executed in a container template  # noqa: E501

        :return: The command of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this TemplateCreateRequest.

        The command that will be executed in a container template  # noqa: E501

        :param command: The command of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._command = command

    @property
    def network(self):
        """Gets the network of this TemplateCreateRequest.  # noqa: E501

        Name of a network that will be used on container deployment if it exists inside the environment  # noqa: E501

        :return: The network of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this TemplateCreateRequest.

        Name of a network that will be used on container deployment if it exists inside the environment  # noqa: E501

        :param network: The network of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._network = network

    @property
    def volumes(self):
        """Gets the volumes of this TemplateCreateRequest.  # noqa: E501

        A list of volumes used during the container template deployment  # noqa: E501

        :return: The volumes of this TemplateCreateRequest.  # noqa: E501
        :rtype: list[TemplateVolume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this TemplateCreateRequest.

        A list of volumes used during the container template deployment  # noqa: E501

        :param volumes: The volumes of this TemplateCreateRequest.  # noqa: E501
        :type: list[TemplateVolume]
        """

        self._volumes = volumes

    @property
    def ports(self):
        """Gets the ports of this TemplateCreateRequest.  # noqa: E501

        A list of ports exposed by the container  # noqa: E501

        :return: The ports of this TemplateCreateRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this TemplateCreateRequest.

        A list of ports exposed by the container  # noqa: E501

        :param ports: The ports of this TemplateCreateRequest.  # noqa: E501
        :type: list[str]
        """

        self._ports = ports

    @property
    def labels(self):
        """Gets the labels of this TemplateCreateRequest.  # noqa: E501

        Container labels  # noqa: E501

        :return: The labels of this TemplateCreateRequest.  # noqa: E501
        :rtype: list[Pair]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this TemplateCreateRequest.

        Container labels  # noqa: E501

        :param labels: The labels of this TemplateCreateRequest.  # noqa: E501
        :type: list[Pair]
        """

        self._labels = labels

    @property
    def privileged(self):
        """Gets the privileged of this TemplateCreateRequest.  # noqa: E501

        Whether the container should be started in privileged mode  # noqa: E501

        :return: The privileged of this TemplateCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """Sets the privileged of this TemplateCreateRequest.

        Whether the container should be started in privileged mode  # noqa: E501

        :param privileged: The privileged of this TemplateCreateRequest.  # noqa: E501
        :type: bool
        """

        self._privileged = privileged

    @property
    def interactive(self):
        """Gets the interactive of this TemplateCreateRequest.  # noqa: E501

        Whether the container should be started in interactive mode (-i -t equivalent on the CLI)  # noqa: E501

        :return: The interactive of this TemplateCreateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._interactive

    @interactive.setter
    def interactive(self, interactive):
        """Sets the interactive of this TemplateCreateRequest.

        Whether the container should be started in interactive mode (-i -t equivalent on the CLI)  # noqa: E501

        :param interactive: The interactive of this TemplateCreateRequest.  # noqa: E501
        :type: bool
        """

        self._interactive = interactive

    @property
    def restart_policy(self):
        """Gets the restart_policy of this TemplateCreateRequest.  # noqa: E501

        Container restart policy  # noqa: E501

        :return: The restart_policy of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._restart_policy

    @restart_policy.setter
    def restart_policy(self, restart_policy):
        """Sets the restart_policy of this TemplateCreateRequest.

        Container restart policy  # noqa: E501

        :param restart_policy: The restart_policy of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._restart_policy = restart_policy

    @property
    def hostname(self):
        """Gets the hostname of this TemplateCreateRequest.  # noqa: E501

        Container hostname  # noqa: E501

        :return: The hostname of this TemplateCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this TemplateCreateRequest.

        Container hostname  # noqa: E501

        :param hostname: The hostname of this TemplateCreateRequest.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

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
        if issubclass(TemplateCreateRequest, dict):
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
        if not isinstance(other, TemplateCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
