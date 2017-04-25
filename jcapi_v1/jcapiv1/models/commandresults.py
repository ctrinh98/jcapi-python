# coding: utf-8

"""
    JumpCloud Directory API

    JumpCloud RESTful APIs for the headless operation of core functions

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Commandresults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, command=None, system=None, organization=None, user=None, files=None, request_time=None, response_time=None, response_id=None, response_data_output=None):
        """
        Commandresults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'command': 'str',
            'system': 'str',
            'organization': 'str',
            'user': 'str',
            'files': 'list[str]',
            'request_time': 'date',
            'response_time': 'date',
            'response_id': 'str',
            'response_data_output': 'int'
        }

        self.attribute_map = {
            'command': 'command',
            'system': 'system',
            'organization': 'organization',
            'user': 'user',
            'files': 'files',
            'request_time': 'requestTime',
            'response_time': 'responseTime',
            'response_id': 'response.id',
            'response_data_output': 'response.data.output'
        }

        self._command = command
        self._system = system
        self._organization = organization
        self._user = user
        self._files = files
        self._request_time = request_time
        self._response_time = response_time
        self._response_id = response_id
        self._response_data_output = response_data_output

    @property
    def command(self):
        """
        Gets the command of this Commandresults.
        The command that was executed on the system.

        :return: The command of this Commandresults.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this Commandresults.
        The command that was executed on the system.

        :param command: The command of this Commandresults.
        :type: str
        """

        self._command = command

    @property
    def system(self):
        """
        Gets the system of this Commandresults.
        The ID of the system on which the command was executed.

        :return: The system of this Commandresults.
        :rtype: str
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this Commandresults.
        The ID of the system on which the command was executed.

        :param system: The system of this Commandresults.
        :type: str
        """

        self._system = system

    @property
    def organization(self):
        """
        Gets the organization of this Commandresults.
        The ID of the organization.

        :return: The organization of this Commandresults.
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this Commandresults.
        The ID of the organization.

        :param organization: The organization of this Commandresults.
        :type: str
        """

        self._organization = organization

    @property
    def user(self):
        """
        Gets the user of this Commandresults.
        The user which ran the command.

        :return: The user of this Commandresults.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Commandresults.
        The user which ran the command.

        :param user: The user of this Commandresults.
        :type: str
        """

        self._user = user

    @property
    def files(self):
        """
        Gets the files of this Commandresults.
        An array of file IDs that were included with the command.

        :return: The files of this Commandresults.
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this Commandresults.
        An array of file IDs that were included with the command.

        :param files: The files of this Commandresults.
        :type: list[str]
        """

        self._files = files

    @property
    def request_time(self):
        """
        Gets the request_time of this Commandresults.
        The time that the command was sent.

        :return: The request_time of this Commandresults.
        :rtype: date
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """
        Sets the request_time of this Commandresults.
        The time that the command was sent.

        :param request_time: The request_time of this Commandresults.
        :type: date
        """

        self._request_time = request_time

    @property
    def response_time(self):
        """
        Gets the response_time of this Commandresults.
        The time that the command was completed.

        :return: The response_time of this Commandresults.
        :rtype: date
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """
        Sets the response_time of this Commandresults.
        The time that the command was completed.

        :param response_time: The response_time of this Commandresults.
        :type: date
        """

        self._response_time = response_time

    @property
    def response_id(self):
        """
        Gets the response_id of this Commandresults.
        The ID of the parent command.

        :return: The response_id of this Commandresults.
        :rtype: str
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id):
        """
        Sets the response_id of this Commandresults.
        The ID of the parent command.

        :param response_id: The response_id of this Commandresults.
        :type: str
        """

        self._response_id = response_id

    @property
    def response_data_output(self):
        """
        Gets the response_data_output of this Commandresults.
        the stdout from the command that ran.

        :return: The response_data_output of this Commandresults.
        :rtype: int
        """
        return self._response_data_output

    @response_data_output.setter
    def response_data_output(self, response_data_output):
        """
        Sets the response_data_output of this Commandresults.
        the stdout from the command that ran.

        :param response_data_output: The response_data_output of this Commandresults.
        :type: int
        """

        self._response_data_output = response_data_output

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
        if not isinstance(other, Commandresults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
