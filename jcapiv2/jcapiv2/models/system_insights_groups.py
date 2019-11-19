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


class SystemInsightsGroups(object):
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
        'collection_time': 'str',
        'comment': 'str',
        'gid': 'str',
        'gid_signed': 'str',
        'group_sid': 'str',
        'groupname': 'str',
        'system_id': 'str'
    }

    attribute_map = {
        'collection_time': 'collection_time',
        'comment': 'comment',
        'gid': 'gid',
        'gid_signed': 'gid_signed',
        'group_sid': 'group_sid',
        'groupname': 'groupname',
        'system_id': 'system_id'
    }

    def __init__(self, collection_time=None, comment=None, gid=None, gid_signed=None, group_sid=None, groupname=None, system_id=None):  # noqa: E501
        """SystemInsightsGroups - a model defined in Swagger"""  # noqa: E501

        self._collection_time = None
        self._comment = None
        self._gid = None
        self._gid_signed = None
        self._group_sid = None
        self._groupname = None
        self._system_id = None
        self.discriminator = None

        if collection_time is not None:
            self.collection_time = collection_time
        if comment is not None:
            self.comment = comment
        if gid is not None:
            self.gid = gid
        if gid_signed is not None:
            self.gid_signed = gid_signed
        if group_sid is not None:
            self.group_sid = group_sid
        if groupname is not None:
            self.groupname = groupname
        if system_id is not None:
            self.system_id = system_id

    @property
    def collection_time(self):
        """Gets the collection_time of this SystemInsightsGroups.  # noqa: E501


        :return: The collection_time of this SystemInsightsGroups.  # noqa: E501
        :rtype: str
        """
        return self._collection_time

    @collection_time.setter
    def collection_time(self, collection_time):
        """Sets the collection_time of this SystemInsightsGroups.


        :param collection_time: The collection_time of this SystemInsightsGroups.  # noqa: E501
        :type: str
        """

        self._collection_time = collection_time

    @property
    def comment(self):
        """Gets the comment of this SystemInsightsGroups.  # noqa: E501


        :return: The comment of this SystemInsightsGroups.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SystemInsightsGroups.


        :param comment: The comment of this SystemInsightsGroups.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def gid(self):
        """Gets the gid of this SystemInsightsGroups.  # noqa: E501


        :return: The gid of this SystemInsightsGroups.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this SystemInsightsGroups.


        :param gid: The gid of this SystemInsightsGroups.  # noqa: E501
        :type: str
        """

        self._gid = gid

    @property
    def gid_signed(self):
        """Gets the gid_signed of this SystemInsightsGroups.  # noqa: E501


        :return: The gid_signed of this SystemInsightsGroups.  # noqa: E501
        :rtype: str
        """
        return self._gid_signed

    @gid_signed.setter
    def gid_signed(self, gid_signed):
        """Sets the gid_signed of this SystemInsightsGroups.


        :param gid_signed: The gid_signed of this SystemInsightsGroups.  # noqa: E501
        :type: str
        """

        self._gid_signed = gid_signed

    @property
    def group_sid(self):
        """Gets the group_sid of this SystemInsightsGroups.  # noqa: E501


        :return: The group_sid of this SystemInsightsGroups.  # noqa: E501
        :rtype: str
        """
        return self._group_sid

    @group_sid.setter
    def group_sid(self, group_sid):
        """Sets the group_sid of this SystemInsightsGroups.


        :param group_sid: The group_sid of this SystemInsightsGroups.  # noqa: E501
        :type: str
        """

        self._group_sid = group_sid

    @property
    def groupname(self):
        """Gets the groupname of this SystemInsightsGroups.  # noqa: E501


        :return: The groupname of this SystemInsightsGroups.  # noqa: E501
        :rtype: str
        """
        return self._groupname

    @groupname.setter
    def groupname(self, groupname):
        """Sets the groupname of this SystemInsightsGroups.


        :param groupname: The groupname of this SystemInsightsGroups.  # noqa: E501
        :type: str
        """

        self._groupname = groupname

    @property
    def system_id(self):
        """Gets the system_id of this SystemInsightsGroups.  # noqa: E501


        :return: The system_id of this SystemInsightsGroups.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SystemInsightsGroups.


        :param system_id: The system_id of this SystemInsightsGroups.  # noqa: E501
        :type: str
        """

        self._system_id = system_id

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
        if issubclass(SystemInsightsGroups, dict):
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
        if not isinstance(other, SystemInsightsGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other