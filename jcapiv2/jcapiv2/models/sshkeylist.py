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


class Sshkeylist(object):
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
        'create_date': 'str',
        'id': 'str',
        'public_key': 'str',
        'name': 'str'
    }

    attribute_map = {
        'create_date': 'create_date',
        'id': '_id',
        'public_key': 'public_key',
        'name': 'name'
    }

    def __init__(self, create_date=None, id=None, public_key=None, name=None):
        """
        Sshkeylist - a model defined in Swagger
        """

        self._create_date = None
        self._id = None
        self._public_key = None
        self._name = None

        if create_date is not None:
          self.create_date = create_date
        if id is not None:
          self.id = id
        if public_key is not None:
          self.public_key = public_key
        if name is not None:
          self.name = name

    @property
    def create_date(self):
        """
        Gets the create_date of this Sshkeylist.
        The date the SSH key was created.

        :return: The create_date of this Sshkeylist.
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this Sshkeylist.
        The date the SSH key was created.

        :param create_date: The create_date of this Sshkeylist.
        :type: str
        """

        self._create_date = create_date

    @property
    def id(self):
        """
        Gets the id of this Sshkeylist.
        The ID of the SSH key.

        :return: The id of this Sshkeylist.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Sshkeylist.
        The ID of the SSH key.

        :param id: The id of this Sshkeylist.
        :type: str
        """

        self._id = id

    @property
    def public_key(self):
        """
        Gets the public_key of this Sshkeylist.
        The Public SSH key.

        :return: The public_key of this Sshkeylist.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """
        Sets the public_key of this Sshkeylist.
        The Public SSH key.

        :param public_key: The public_key of this Sshkeylist.
        :type: str
        """

        self._public_key = public_key

    @property
    def name(self):
        """
        Gets the name of this Sshkeylist.
        The name of the SSH key.

        :return: The name of this Sshkeylist.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Sshkeylist.
        The name of the SSH key.

        :param name: The name of this Sshkeylist.
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
        if not isinstance(other, Sshkeylist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other