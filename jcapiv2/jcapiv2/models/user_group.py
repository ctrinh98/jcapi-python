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


class UserGroup(object):
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
        'id': 'str',
        'type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, id=None, type=None, name=None):
        """
        UserGroup - a model defined in Swagger
        """

        self._id = None
        self._type = None
        self._name = None

        if id is not None:
          self.id = id
        if type is not None:
          self.type = type
        if name is not None:
          self.name = name

    @property
    def id(self):
        """
        Gets the id of this UserGroup.
        ObjectId uniquely identifying a User Group.

        :return: The id of this UserGroup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserGroup.
        ObjectId uniquely identifying a User Group.

        :param id: The id of this UserGroup.
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this UserGroup.
        The type of the group.

        :return: The type of this UserGroup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserGroup.
        The type of the group.

        :param type: The type of this UserGroup.
        :type: str
        """
        allowed_values = ["user_group"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this UserGroup.
        Display name of a User Group.

        :return: The name of this UserGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserGroup.
        Display name of a User Group.

        :param name: The name of this UserGroup.
        :type: str
        """

        self._name = name

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
        if not isinstance(other, UserGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
