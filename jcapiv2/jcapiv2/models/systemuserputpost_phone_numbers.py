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


class SystemuserputpostPhoneNumbers(object):
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
        'type': 'str',
        'number': 'str'
    }

    attribute_map = {
        'type': 'type',
        'number': 'number'
    }

    def __init__(self, type=None, number=None):
        """
        SystemuserputpostPhoneNumbers - a model defined in Swagger
        """

        self._type = None
        self._number = None

        if type is not None:
          self.type = type
        if number is not None:
          self.number = number

    @property
    def type(self):
        """
        Gets the type of this SystemuserputpostPhoneNumbers.

        :return: The type of this SystemuserputpostPhoneNumbers.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SystemuserputpostPhoneNumbers.

        :param type: The type of this SystemuserputpostPhoneNumbers.
        :type: str
        """

        self._type = type

    @property
    def number(self):
        """
        Gets the number of this SystemuserputpostPhoneNumbers.

        :return: The number of this SystemuserputpostPhoneNumbers.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this SystemuserputpostPhoneNumbers.

        :param number: The number of this SystemuserputpostPhoneNumbers.
        :type: str
        """

        self._number = number

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
        if not isinstance(other, SystemuserputpostPhoneNumbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
