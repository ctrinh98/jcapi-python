# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from jcapiv2.models.orgcryptosettings_ssh_keys import OrgcryptosettingsSshKeys  # noqa: F401,E501


class OrgCryptoSettings(object):
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
        'ssh_keys': 'OrgcryptosettingsSshKeys'
    }

    attribute_map = {
        'ssh_keys': 'sshKeys'
    }

    def __init__(self, ssh_keys=None):  # noqa: E501
        """OrgCryptoSettings - a model defined in Swagger"""  # noqa: E501

        self._ssh_keys = None
        self.discriminator = None

        if ssh_keys is not None:
            self.ssh_keys = ssh_keys

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this OrgCryptoSettings.  # noqa: E501


        :return: The ssh_keys of this OrgCryptoSettings.  # noqa: E501
        :rtype: OrgcryptosettingsSshKeys
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this OrgCryptoSettings.


        :param ssh_keys: The ssh_keys of this OrgCryptoSettings.  # noqa: E501
        :type: OrgcryptosettingsSshKeys
        """

        self._ssh_keys = ssh_keys

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
        if issubclass(OrgCryptoSettings, dict):
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
        if not isinstance(other, OrgCryptoSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
