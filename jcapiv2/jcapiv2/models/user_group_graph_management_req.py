# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserGroupGraphManagementReq(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'op': 'str',
        'type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'op': 'op',
        'type': 'type',
        'id': 'id'
    }

    def __init__(self, op=None, type=None, id=None):
        """
        UserGroupGraphManagementReq - a model defined in Swagger
        """

        self._op = None
        self._type = None
        self._id = None

        self.op = op
        self.type = type
        self.id = id

    @property
    def op(self):
        """
        Gets the op of this UserGroupGraphManagementReq.
        How to modify the graph connection.

        :return: The op of this UserGroupGraphManagementReq.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """
        Sets the op of this UserGroupGraphManagementReq.
        How to modify the graph connection.

        :param op: The op of this UserGroupGraphManagementReq.
        :type: str
        """
        if op is None:
            raise ValueError("Invalid value for `op`, must not be `None`")
        allowed_values = ["add", "remove", "update"]
        if op not in allowed_values:
            raise ValueError(
                "Invalid value for `op` ({0}), must be one of {1}"
                .format(op, allowed_values)
            )

        self._op = op

    @property
    def type(self):
        """
        Gets the type of this UserGroupGraphManagementReq.
        The graph type

        :return: The type of this UserGroupGraphManagementReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserGroupGraphManagementReq.
        The graph type

        :param type: The type of this UserGroupGraphManagementReq.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["active_directory", "application", "command", "g_suite", "ldap_server", "office_365", "policy", "radius_server", "system", "system_group"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """
        Gets the id of this UserGroupGraphManagementReq.
        The ObjectID of graph object being added or removed as an association.

        :return: The id of this UserGroupGraphManagementReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserGroupGraphManagementReq.
        The ObjectID of graph object being added or removed as an association.

        :param id: The id of this UserGroupGraphManagementReq.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UserGroupGraphManagementReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
