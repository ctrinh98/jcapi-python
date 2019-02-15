# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V1 API. This set of endpoints allows JumpCloud customers to manage commands, systems, & system users.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from jcapiv1.models.mfa import Mfa  # noqa: F401,E501
from jcapiv1.models.sshkeypost import Sshkeypost  # noqa: F401,E501
from jcapiv1.models.systemuserput_addresses import SystemuserputAddresses  # noqa: F401,E501
from jcapiv1.models.systemuserput_phone_numbers import SystemuserputPhoneNumbers  # noqa: F401,E501


class Systemuserput(object):
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
        'email': 'str',
        'username': 'str',
        'allow_public_key': 'bool',
        'public_key': 'str',
        'ssh_keys': 'list[Sshkeypost]',
        'sudo': 'bool',
        'enable_managed_uid': 'bool',
        'unix_uid': 'int',
        'unix_guid': 'int',
        'tags': 'list[str]',
        'account_locked': 'bool',
        'externally_managed': 'bool',
        'external_dn': 'str',
        'external_source_type': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'ldap_binding_user': 'bool',
        'enable_user_portal_multifactor': 'bool',
        'attributes': 'list[object]',
        'samba_service_user': 'bool',
        'addresses': 'list[SystemuserputAddresses]',
        'job_title': 'str',
        'department': 'str',
        'phone_numbers': 'list[SystemuserputPhoneNumbers]',
        'relationships': 'list[object]',
        'password': 'str',
        'password_never_expires': 'bool',
        'middlename': 'str',
        'displayname': 'str',
        'description': 'str',
        'location': 'str',
        'cost_center': 'str',
        'employee_type': 'str',
        'company': 'str',
        'employee_identifier': 'str',
        'mfa': 'Mfa'
    }

    attribute_map = {
        'email': 'email',
        'username': 'username',
        'allow_public_key': 'allow_public_key',
        'public_key': 'public_key',
        'ssh_keys': 'ssh_keys',
        'sudo': 'sudo',
        'enable_managed_uid': 'enable_managed_uid',
        'unix_uid': 'unix_uid',
        'unix_guid': 'unix_guid',
        'tags': 'tags',
        'account_locked': 'account_locked',
        'externally_managed': 'externally_managed',
        'external_dn': 'external_dn',
        'external_source_type': 'external_source_type',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'ldap_binding_user': 'ldap_binding_user',
        'enable_user_portal_multifactor': 'enable_user_portal_multifactor',
        'attributes': 'attributes',
        'samba_service_user': 'samba_service_user',
        'addresses': 'addresses',
        'job_title': 'jobTitle',
        'department': 'department',
        'phone_numbers': 'phoneNumbers',
        'relationships': 'relationships',
        'password': 'password',
        'password_never_expires': 'password_never_expires',
        'middlename': 'middlename',
        'displayname': 'displayname',
        'description': 'description',
        'location': 'location',
        'cost_center': 'costCenter',
        'employee_type': 'employeeType',
        'company': 'company',
        'employee_identifier': 'employeeIdentifier',
        'mfa': 'mfa'
    }

    def __init__(self, email=None, username=None, allow_public_key=None, public_key=None, ssh_keys=None, sudo=None, enable_managed_uid=None, unix_uid=None, unix_guid=None, tags=None, account_locked=None, externally_managed=None, external_dn=None, external_source_type=None, firstname=None, lastname=None, ldap_binding_user=None, enable_user_portal_multifactor=None, attributes=None, samba_service_user=None, addresses=None, job_title=None, department=None, phone_numbers=None, relationships=None, password=None, password_never_expires=None, middlename=None, displayname=None, description=None, location=None, cost_center=None, employee_type=None, company=None, employee_identifier=None, mfa=None):  # noqa: E501
        """Systemuserput - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._username = None
        self._allow_public_key = None
        self._public_key = None
        self._ssh_keys = None
        self._sudo = None
        self._enable_managed_uid = None
        self._unix_uid = None
        self._unix_guid = None
        self._tags = None
        self._account_locked = None
        self._externally_managed = None
        self._external_dn = None
        self._external_source_type = None
        self._firstname = None
        self._lastname = None
        self._ldap_binding_user = None
        self._enable_user_portal_multifactor = None
        self._attributes = None
        self._samba_service_user = None
        self._addresses = None
        self._job_title = None
        self._department = None
        self._phone_numbers = None
        self._relationships = None
        self._password = None
        self._password_never_expires = None
        self._middlename = None
        self._displayname = None
        self._description = None
        self._location = None
        self._cost_center = None
        self._employee_type = None
        self._company = None
        self._employee_identifier = None
        self._mfa = None
        self.discriminator = None

        self.email = email
        self.username = username
        if allow_public_key is not None:
            self.allow_public_key = allow_public_key
        if public_key is not None:
            self.public_key = public_key
        if ssh_keys is not None:
            self.ssh_keys = ssh_keys
        if sudo is not None:
            self.sudo = sudo
        if enable_managed_uid is not None:
            self.enable_managed_uid = enable_managed_uid
        if unix_uid is not None:
            self.unix_uid = unix_uid
        if unix_guid is not None:
            self.unix_guid = unix_guid
        if tags is not None:
            self.tags = tags
        if account_locked is not None:
            self.account_locked = account_locked
        if externally_managed is not None:
            self.externally_managed = externally_managed
        if external_dn is not None:
            self.external_dn = external_dn
        if external_source_type is not None:
            self.external_source_type = external_source_type
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if ldap_binding_user is not None:
            self.ldap_binding_user = ldap_binding_user
        if enable_user_portal_multifactor is not None:
            self.enable_user_portal_multifactor = enable_user_portal_multifactor
        if attributes is not None:
            self.attributes = attributes
        if samba_service_user is not None:
            self.samba_service_user = samba_service_user
        if addresses is not None:
            self.addresses = addresses
        if job_title is not None:
            self.job_title = job_title
        if department is not None:
            self.department = department
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if relationships is not None:
            self.relationships = relationships
        if password is not None:
            self.password = password
        if password_never_expires is not None:
            self.password_never_expires = password_never_expires
        if middlename is not None:
            self.middlename = middlename
        if displayname is not None:
            self.displayname = displayname
        if description is not None:
            self.description = description
        if location is not None:
            self.location = location
        if cost_center is not None:
            self.cost_center = cost_center
        if employee_type is not None:
            self.employee_type = employee_type
        if company is not None:
            self.company = company
        if employee_identifier is not None:
            self.employee_identifier = employee_identifier
        if mfa is not None:
            self.mfa = mfa

    @property
    def email(self):
        """Gets the email of this Systemuserput.  # noqa: E501


        :return: The email of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Systemuserput.


        :param email: The email of this Systemuserput.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) > 1024:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `1024`")  # noqa: E501

        self._email = email

    @property
    def username(self):
        """Gets the username of this Systemuserput.  # noqa: E501


        :return: The username of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Systemuserput.


        :param username: The username of this Systemuserput.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if username is not None and len(username) > 1024:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `1024`")  # noqa: E501

        self._username = username

    @property
    def allow_public_key(self):
        """Gets the allow_public_key of this Systemuserput.  # noqa: E501


        :return: The allow_public_key of this Systemuserput.  # noqa: E501
        :rtype: bool
        """
        return self._allow_public_key

    @allow_public_key.setter
    def allow_public_key(self, allow_public_key):
        """Sets the allow_public_key of this Systemuserput.


        :param allow_public_key: The allow_public_key of this Systemuserput.  # noqa: E501
        :type: bool
        """

        self._allow_public_key = allow_public_key

    @property
    def public_key(self):
        """Gets the public_key of this Systemuserput.  # noqa: E501


        :return: The public_key of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this Systemuserput.


        :param public_key: The public_key of this Systemuserput.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def ssh_keys(self):
        """Gets the ssh_keys of this Systemuserput.  # noqa: E501


        :return: The ssh_keys of this Systemuserput.  # noqa: E501
        :rtype: list[Sshkeypost]
        """
        return self._ssh_keys

    @ssh_keys.setter
    def ssh_keys(self, ssh_keys):
        """Sets the ssh_keys of this Systemuserput.


        :param ssh_keys: The ssh_keys of this Systemuserput.  # noqa: E501
        :type: list[Sshkeypost]
        """

        self._ssh_keys = ssh_keys

    @property
    def sudo(self):
        """Gets the sudo of this Systemuserput.  # noqa: E501


        :return: The sudo of this Systemuserput.  # noqa: E501
        :rtype: bool
        """
        return self._sudo

    @sudo.setter
    def sudo(self, sudo):
        """Sets the sudo of this Systemuserput.


        :param sudo: The sudo of this Systemuserput.  # noqa: E501
        :type: bool
        """

        self._sudo = sudo

    @property
    def enable_managed_uid(self):
        """Gets the enable_managed_uid of this Systemuserput.  # noqa: E501


        :return: The enable_managed_uid of this Systemuserput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_managed_uid

    @enable_managed_uid.setter
    def enable_managed_uid(self, enable_managed_uid):
        """Sets the enable_managed_uid of this Systemuserput.


        :param enable_managed_uid: The enable_managed_uid of this Systemuserput.  # noqa: E501
        :type: bool
        """

        self._enable_managed_uid = enable_managed_uid

    @property
    def unix_uid(self):
        """Gets the unix_uid of this Systemuserput.  # noqa: E501


        :return: The unix_uid of this Systemuserput.  # noqa: E501
        :rtype: int
        """
        return self._unix_uid

    @unix_uid.setter
    def unix_uid(self, unix_uid):
        """Sets the unix_uid of this Systemuserput.


        :param unix_uid: The unix_uid of this Systemuserput.  # noqa: E501
        :type: int
        """
        if unix_uid is not None and unix_uid < 1:  # noqa: E501
            raise ValueError("Invalid value for `unix_uid`, must be a value greater than or equal to `1`")  # noqa: E501

        self._unix_uid = unix_uid

    @property
    def unix_guid(self):
        """Gets the unix_guid of this Systemuserput.  # noqa: E501


        :return: The unix_guid of this Systemuserput.  # noqa: E501
        :rtype: int
        """
        return self._unix_guid

    @unix_guid.setter
    def unix_guid(self, unix_guid):
        """Sets the unix_guid of this Systemuserput.


        :param unix_guid: The unix_guid of this Systemuserput.  # noqa: E501
        :type: int
        """
        if unix_guid is not None and unix_guid < 1:  # noqa: E501
            raise ValueError("Invalid value for `unix_guid`, must be a value greater than or equal to `1`")  # noqa: E501

        self._unix_guid = unix_guid

    @property
    def tags(self):
        """Gets the tags of this Systemuserput.  # noqa: E501


        :return: The tags of this Systemuserput.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Systemuserput.


        :param tags: The tags of this Systemuserput.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def account_locked(self):
        """Gets the account_locked of this Systemuserput.  # noqa: E501


        :return: The account_locked of this Systemuserput.  # noqa: E501
        :rtype: bool
        """
        return self._account_locked

    @account_locked.setter
    def account_locked(self, account_locked):
        """Sets the account_locked of this Systemuserput.


        :param account_locked: The account_locked of this Systemuserput.  # noqa: E501
        :type: bool
        """

        self._account_locked = account_locked

    @property
    def externally_managed(self):
        """Gets the externally_managed of this Systemuserput.  # noqa: E501


        :return: The externally_managed of this Systemuserput.  # noqa: E501
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """Sets the externally_managed of this Systemuserput.


        :param externally_managed: The externally_managed of this Systemuserput.  # noqa: E501
        :type: bool
        """

        self._externally_managed = externally_managed

    @property
    def external_dn(self):
        """Gets the external_dn of this Systemuserput.  # noqa: E501


        :return: The external_dn of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._external_dn

    @external_dn.setter
    def external_dn(self, external_dn):
        """Sets the external_dn of this Systemuserput.


        :param external_dn: The external_dn of this Systemuserput.  # noqa: E501
        :type: str
        """

        self._external_dn = external_dn

    @property
    def external_source_type(self):
        """Gets the external_source_type of this Systemuserput.  # noqa: E501


        :return: The external_source_type of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._external_source_type

    @external_source_type.setter
    def external_source_type(self, external_source_type):
        """Sets the external_source_type of this Systemuserput.


        :param external_source_type: The external_source_type of this Systemuserput.  # noqa: E501
        :type: str
        """

        self._external_source_type = external_source_type

    @property
    def firstname(self):
        """Gets the firstname of this Systemuserput.  # noqa: E501


        :return: The firstname of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this Systemuserput.


        :param firstname: The firstname of this Systemuserput.  # noqa: E501
        :type: str
        """
        if firstname is not None and len(firstname) > 1024:
            raise ValueError("Invalid value for `firstname`, length must be less than or equal to `1024`")  # noqa: E501

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this Systemuserput.  # noqa: E501


        :return: The lastname of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this Systemuserput.


        :param lastname: The lastname of this Systemuserput.  # noqa: E501
        :type: str
        """
        if lastname is not None and len(lastname) > 1024:
            raise ValueError("Invalid value for `lastname`, length must be less than or equal to `1024`")  # noqa: E501

        self._lastname = lastname

    @property
    def ldap_binding_user(self):
        """Gets the ldap_binding_user of this Systemuserput.  # noqa: E501


        :return: The ldap_binding_user of this Systemuserput.  # noqa: E501
        :rtype: bool
        """
        return self._ldap_binding_user

    @ldap_binding_user.setter
    def ldap_binding_user(self, ldap_binding_user):
        """Sets the ldap_binding_user of this Systemuserput.


        :param ldap_binding_user: The ldap_binding_user of this Systemuserput.  # noqa: E501
        :type: bool
        """

        self._ldap_binding_user = ldap_binding_user

    @property
    def enable_user_portal_multifactor(self):
        """Gets the enable_user_portal_multifactor of this Systemuserput.  # noqa: E501


        :return: The enable_user_portal_multifactor of this Systemuserput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_user_portal_multifactor

    @enable_user_portal_multifactor.setter
    def enable_user_portal_multifactor(self, enable_user_portal_multifactor):
        """Sets the enable_user_portal_multifactor of this Systemuserput.


        :param enable_user_portal_multifactor: The enable_user_portal_multifactor of this Systemuserput.  # noqa: E501
        :type: bool
        """

        self._enable_user_portal_multifactor = enable_user_portal_multifactor

    @property
    def attributes(self):
        """Gets the attributes of this Systemuserput.  # noqa: E501


        :return: The attributes of this Systemuserput.  # noqa: E501
        :rtype: list[object]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Systemuserput.


        :param attributes: The attributes of this Systemuserput.  # noqa: E501
        :type: list[object]
        """

        self._attributes = attributes

    @property
    def samba_service_user(self):
        """Gets the samba_service_user of this Systemuserput.  # noqa: E501


        :return: The samba_service_user of this Systemuserput.  # noqa: E501
        :rtype: bool
        """
        return self._samba_service_user

    @samba_service_user.setter
    def samba_service_user(self, samba_service_user):
        """Sets the samba_service_user of this Systemuserput.


        :param samba_service_user: The samba_service_user of this Systemuserput.  # noqa: E501
        :type: bool
        """

        self._samba_service_user = samba_service_user

    @property
    def addresses(self):
        """Gets the addresses of this Systemuserput.  # noqa: E501

        type, poBox, extendedAddress, streetAddress, locality, region, postalCode, country  # noqa: E501

        :return: The addresses of this Systemuserput.  # noqa: E501
        :rtype: list[SystemuserputAddresses]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Systemuserput.

        type, poBox, extendedAddress, streetAddress, locality, region, postalCode, country  # noqa: E501

        :param addresses: The addresses of this Systemuserput.  # noqa: E501
        :type: list[SystemuserputAddresses]
        """

        self._addresses = addresses

    @property
    def job_title(self):
        """Gets the job_title of this Systemuserput.  # noqa: E501


        :return: The job_title of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this Systemuserput.


        :param job_title: The job_title of this Systemuserput.  # noqa: E501
        :type: str
        """
        if job_title is not None and len(job_title) > 1024:
            raise ValueError("Invalid value for `job_title`, length must be less than or equal to `1024`")  # noqa: E501

        self._job_title = job_title

    @property
    def department(self):
        """Gets the department of this Systemuserput.  # noqa: E501


        :return: The department of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this Systemuserput.


        :param department: The department of this Systemuserput.  # noqa: E501
        :type: str
        """
        if department is not None and len(department) > 1024:
            raise ValueError("Invalid value for `department`, length must be less than or equal to `1024`")  # noqa: E501

        self._department = department

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this Systemuserput.  # noqa: E501


        :return: The phone_numbers of this Systemuserput.  # noqa: E501
        :rtype: list[SystemuserputPhoneNumbers]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this Systemuserput.


        :param phone_numbers: The phone_numbers of this Systemuserput.  # noqa: E501
        :type: list[SystemuserputPhoneNumbers]
        """

        self._phone_numbers = phone_numbers

    @property
    def relationships(self):
        """Gets the relationships of this Systemuserput.  # noqa: E501


        :return: The relationships of this Systemuserput.  # noqa: E501
        :rtype: list[object]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this Systemuserput.


        :param relationships: The relationships of this Systemuserput.  # noqa: E501
        :type: list[object]
        """

        self._relationships = relationships

    @property
    def password(self):
        """Gets the password of this Systemuserput.  # noqa: E501


        :return: The password of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Systemuserput.


        :param password: The password of this Systemuserput.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def password_never_expires(self):
        """Gets the password_never_expires of this Systemuserput.  # noqa: E501


        :return: The password_never_expires of this Systemuserput.  # noqa: E501
        :rtype: bool
        """
        return self._password_never_expires

    @password_never_expires.setter
    def password_never_expires(self, password_never_expires):
        """Sets the password_never_expires of this Systemuserput.


        :param password_never_expires: The password_never_expires of this Systemuserput.  # noqa: E501
        :type: bool
        """

        self._password_never_expires = password_never_expires

    @property
    def middlename(self):
        """Gets the middlename of this Systemuserput.  # noqa: E501


        :return: The middlename of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._middlename

    @middlename.setter
    def middlename(self, middlename):
        """Sets the middlename of this Systemuserput.


        :param middlename: The middlename of this Systemuserput.  # noqa: E501
        :type: str
        """
        if middlename is not None and len(middlename) > 1024:
            raise ValueError("Invalid value for `middlename`, length must be less than or equal to `1024`")  # noqa: E501

        self._middlename = middlename

    @property
    def displayname(self):
        """Gets the displayname of this Systemuserput.  # noqa: E501


        :return: The displayname of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._displayname

    @displayname.setter
    def displayname(self, displayname):
        """Sets the displayname of this Systemuserput.


        :param displayname: The displayname of this Systemuserput.  # noqa: E501
        :type: str
        """
        if displayname is not None and len(displayname) > 1024:
            raise ValueError("Invalid value for `displayname`, length must be less than or equal to `1024`")  # noqa: E501

        self._displayname = displayname

    @property
    def description(self):
        """Gets the description of this Systemuserput.  # noqa: E501


        :return: The description of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Systemuserput.


        :param description: The description of this Systemuserput.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501

        self._description = description

    @property
    def location(self):
        """Gets the location of this Systemuserput.  # noqa: E501


        :return: The location of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Systemuserput.


        :param location: The location of this Systemuserput.  # noqa: E501
        :type: str
        """
        if location is not None and len(location) > 1024:
            raise ValueError("Invalid value for `location`, length must be less than or equal to `1024`")  # noqa: E501

        self._location = location

    @property
    def cost_center(self):
        """Gets the cost_center of this Systemuserput.  # noqa: E501


        :return: The cost_center of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._cost_center

    @cost_center.setter
    def cost_center(self, cost_center):
        """Sets the cost_center of this Systemuserput.


        :param cost_center: The cost_center of this Systemuserput.  # noqa: E501
        :type: str
        """
        if cost_center is not None and len(cost_center) > 1024:
            raise ValueError("Invalid value for `cost_center`, length must be less than or equal to `1024`")  # noqa: E501

        self._cost_center = cost_center

    @property
    def employee_type(self):
        """Gets the employee_type of this Systemuserput.  # noqa: E501


        :return: The employee_type of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._employee_type

    @employee_type.setter
    def employee_type(self, employee_type):
        """Sets the employee_type of this Systemuserput.


        :param employee_type: The employee_type of this Systemuserput.  # noqa: E501
        :type: str
        """
        if employee_type is not None and len(employee_type) > 1024:
            raise ValueError("Invalid value for `employee_type`, length must be less than or equal to `1024`")  # noqa: E501

        self._employee_type = employee_type

    @property
    def company(self):
        """Gets the company of this Systemuserput.  # noqa: E501


        :return: The company of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Systemuserput.


        :param company: The company of this Systemuserput.  # noqa: E501
        :type: str
        """
        if company is not None and len(company) > 1024:
            raise ValueError("Invalid value for `company`, length must be less than or equal to `1024`")  # noqa: E501

        self._company = company

    @property
    def employee_identifier(self):
        """Gets the employee_identifier of this Systemuserput.  # noqa: E501

        Must be unique per user.   # noqa: E501

        :return: The employee_identifier of this Systemuserput.  # noqa: E501
        :rtype: str
        """
        return self._employee_identifier

    @employee_identifier.setter
    def employee_identifier(self, employee_identifier):
        """Sets the employee_identifier of this Systemuserput.

        Must be unique per user.   # noqa: E501

        :param employee_identifier: The employee_identifier of this Systemuserput.  # noqa: E501
        :type: str
        """
        if employee_identifier is not None and len(employee_identifier) > 256:
            raise ValueError("Invalid value for `employee_identifier`, length must be less than or equal to `256`")  # noqa: E501

        self._employee_identifier = employee_identifier

    @property
    def mfa(self):
        """Gets the mfa of this Systemuserput.  # noqa: E501


        :return: The mfa of this Systemuserput.  # noqa: E501
        :rtype: Mfa
        """
        return self._mfa

    @mfa.setter
    def mfa(self, mfa):
        """Sets the mfa of this Systemuserput.


        :param mfa: The mfa of this Systemuserput.  # noqa: E501
        :type: Mfa
        """

        self._mfa = mfa

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Systemuserput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
