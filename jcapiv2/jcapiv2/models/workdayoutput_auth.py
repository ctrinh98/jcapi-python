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


class WorkdayoutputAuth(object):
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
        'basic': 'AuthInfo',
        'oauth': 'AuthInfo'
    }

    attribute_map = {
        'basic': 'basic',
        'oauth': 'oauth'
    }

    def __init__(self, basic=None, oauth=None):
        """
        WorkdayoutputAuth - a model defined in Swagger
        """

        self._basic = None
        self._oauth = None

        if basic is not None:
          self.basic = basic
        if oauth is not None:
          self.oauth = oauth

    @property
    def basic(self):
        """
        Gets the basic of this WorkdayoutputAuth.

        :return: The basic of this WorkdayoutputAuth.
        :rtype: AuthInfo
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        """
        Sets the basic of this WorkdayoutputAuth.

        :param basic: The basic of this WorkdayoutputAuth.
        :type: AuthInfo
        """

        self._basic = basic

    @property
    def oauth(self):
        """
        Gets the oauth of this WorkdayoutputAuth.

        :return: The oauth of this WorkdayoutputAuth.
        :rtype: AuthInfo
        """
        return self._oauth

    @oauth.setter
    def oauth(self, oauth):
        """
        Sets the oauth of this WorkdayoutputAuth.

        :param oauth: The oauth of this WorkdayoutputAuth.
        :type: AuthInfo
        """

        self._oauth = oauth

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
        if not isinstance(other, WorkdayoutputAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
