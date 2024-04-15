# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Zone(object):
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
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'url': 'str',
        'kind': 'str',
        'rrsets': 'list[RRSet]',
        'serial': 'int',
        'notified_serial': 'int',
        'edited_serial': 'int',
        'masters': 'list[str]',
        'dnssec': 'bool',
        'nsec3param': 'str',
        'nsec3narrow': 'bool',
        'presigned': 'bool',
        'soa_edit': 'str',
        'soa_edit_api': 'str',
        'api_rectify': 'bool',
        'zone': 'str',
        'catalog': 'str',
        'account': 'str',
        'nameservers': 'list[str]',
        'master_tsig_key_ids': 'list[str]',
        'slave_tsig_key_ids': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'url': 'url',
        'kind': 'kind',
        'rrsets': 'rrsets',
        'serial': 'serial',
        'notified_serial': 'notified_serial',
        'edited_serial': 'edited_serial',
        'masters': 'masters',
        'dnssec': 'dnssec',
        'nsec3param': 'nsec3param',
        'nsec3narrow': 'nsec3narrow',
        'presigned': 'presigned',
        'soa_edit': 'soa_edit',
        'soa_edit_api': 'soa_edit_api',
        'api_rectify': 'api_rectify',
        'zone': 'zone',
        'catalog': 'catalog',
        'account': 'account',
        'nameservers': 'nameservers',
        'master_tsig_key_ids': 'master_tsig_key_ids',
        'slave_tsig_key_ids': 'slave_tsig_key_ids'
    }

    def __init__(self, id=None, name=None, type=None, url=None, kind=None, rrsets=None, serial=None, notified_serial=None, edited_serial=None, masters=None, dnssec=None, nsec3param=None, nsec3narrow=None, presigned=None, soa_edit=None, soa_edit_api=None, api_rectify=None, zone=None, catalog=None, account=None, nameservers=None, master_tsig_key_ids=None, slave_tsig_key_ids=None):  # noqa: E501
        """Zone - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._type = None
        self._url = None
        self._kind = None
        self._rrsets = None
        self._serial = None
        self._notified_serial = None
        self._edited_serial = None
        self._masters = None
        self._dnssec = None
        self._nsec3param = None
        self._nsec3narrow = None
        self._presigned = None
        self._soa_edit = None
        self._soa_edit_api = None
        self._api_rectify = None
        self._zone = None
        self._catalog = None
        self._account = None
        self._nameservers = None
        self._master_tsig_key_ids = None
        self._slave_tsig_key_ids = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if kind is not None:
            self.kind = kind
        if rrsets is not None:
            self.rrsets = rrsets
        if serial is not None:
            self.serial = serial
        if notified_serial is not None:
            self.notified_serial = notified_serial
        if edited_serial is not None:
            self.edited_serial = edited_serial
        if masters is not None:
            self.masters = masters
        if dnssec is not None:
            self.dnssec = dnssec
        if nsec3param is not None:
            self.nsec3param = nsec3param
        if nsec3narrow is not None:
            self.nsec3narrow = nsec3narrow
        if presigned is not None:
            self.presigned = presigned
        if soa_edit is not None:
            self.soa_edit = soa_edit
        if soa_edit_api is not None:
            self.soa_edit_api = soa_edit_api
        if api_rectify is not None:
            self.api_rectify = api_rectify
        if zone is not None:
            self.zone = zone
        if catalog is not None:
            self.catalog = catalog
        if account is not None:
            self.account = account
        if nameservers is not None:
            self.nameservers = nameservers
        if master_tsig_key_ids is not None:
            self.master_tsig_key_ids = master_tsig_key_ids
        if slave_tsig_key_ids is not None:
            self.slave_tsig_key_ids = slave_tsig_key_ids

    @property
    def id(self):
        """Gets the id of this Zone.  # noqa: E501

        Opaque zone id (string), assigned by the server, should not be interpreted by the application. Guaranteed to be safe for embedding in URLs.  # noqa: E501

        :return: The id of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Zone.

        Opaque zone id (string), assigned by the server, should not be interpreted by the application. Guaranteed to be safe for embedding in URLs.  # noqa: E501

        :param id: The id of this Zone.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Zone.  # noqa: E501

        Name of the zone (e.g. “example.com.”) MUST have a trailing dot  # noqa: E501

        :return: The name of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Zone.

        Name of the zone (e.g. “example.com.”) MUST have a trailing dot  # noqa: E501

        :param name: The name of this Zone.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Zone.  # noqa: E501

        Set to “Zone”  # noqa: E501

        :return: The type of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Zone.

        Set to “Zone”  # noqa: E501

        :param type: The type of this Zone.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this Zone.  # noqa: E501

        API endpoint for this zone  # noqa: E501

        :return: The url of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Zone.

        API endpoint for this zone  # noqa: E501

        :param url: The url of this Zone.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def kind(self):
        """Gets the kind of this Zone.  # noqa: E501

        Zone kind, one of “Native”, “Master”, “Slave”, “Producer”, “Consumer”  # noqa: E501

        :return: The kind of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this Zone.

        Zone kind, one of “Native”, “Master”, “Slave”, “Producer”, “Consumer”  # noqa: E501

        :param kind: The kind of this Zone.  # noqa: E501
        :type: str
        """
        allowed_values = ["Native", "Master", "Slave", "Producer", "Consumer"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def rrsets(self):
        """Gets the rrsets of this Zone.  # noqa: E501

        RRSets in this zone (for zones/{zone_id} endpoint only; omitted during GET on the .../zones list endpoint)  # noqa: E501

        :return: The rrsets of this Zone.  # noqa: E501
        :rtype: list[RRSet]
        """
        return self._rrsets

    @rrsets.setter
    def rrsets(self, rrsets):
        """Sets the rrsets of this Zone.

        RRSets in this zone (for zones/{zone_id} endpoint only; omitted during GET on the .../zones list endpoint)  # noqa: E501

        :param rrsets: The rrsets of this Zone.  # noqa: E501
        :type: list[RRSet]
        """

        self._rrsets = rrsets

    @property
    def serial(self):
        """Gets the serial of this Zone.  # noqa: E501

        The SOA serial number  # noqa: E501

        :return: The serial of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this Zone.

        The SOA serial number  # noqa: E501

        :param serial: The serial of this Zone.  # noqa: E501
        :type: int
        """

        self._serial = serial

    @property
    def notified_serial(self):
        """Gets the notified_serial of this Zone.  # noqa: E501

        The SOA serial notifications have been sent out for  # noqa: E501

        :return: The notified_serial of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._notified_serial

    @notified_serial.setter
    def notified_serial(self, notified_serial):
        """Sets the notified_serial of this Zone.

        The SOA serial notifications have been sent out for  # noqa: E501

        :param notified_serial: The notified_serial of this Zone.  # noqa: E501
        :type: int
        """

        self._notified_serial = notified_serial

    @property
    def edited_serial(self):
        """Gets the edited_serial of this Zone.  # noqa: E501

        The SOA serial as seen in query responses. Calculated using the SOA-EDIT metadata, default-soa-edit and default-soa-edit-signed settings  # noqa: E501

        :return: The edited_serial of this Zone.  # noqa: E501
        :rtype: int
        """
        return self._edited_serial

    @edited_serial.setter
    def edited_serial(self, edited_serial):
        """Sets the edited_serial of this Zone.

        The SOA serial as seen in query responses. Calculated using the SOA-EDIT metadata, default-soa-edit and default-soa-edit-signed settings  # noqa: E501

        :param edited_serial: The edited_serial of this Zone.  # noqa: E501
        :type: int
        """

        self._edited_serial = edited_serial

    @property
    def masters(self):
        """Gets the masters of this Zone.  # noqa: E501

         List of IP addresses configured as a master for this zone (“Slave” type zones only)  # noqa: E501

        :return: The masters of this Zone.  # noqa: E501
        :rtype: list[str]
        """
        return self._masters

    @masters.setter
    def masters(self, masters):
        """Sets the masters of this Zone.

         List of IP addresses configured as a master for this zone (“Slave” type zones only)  # noqa: E501

        :param masters: The masters of this Zone.  # noqa: E501
        :type: list[str]
        """

        self._masters = masters

    @property
    def dnssec(self):
        """Gets the dnssec of this Zone.  # noqa: E501

        Whether or not this zone is DNSSEC signed (inferred from presigned being true XOR presence of at least one cryptokey with active being true)  # noqa: E501

        :return: The dnssec of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._dnssec

    @dnssec.setter
    def dnssec(self, dnssec):
        """Sets the dnssec of this Zone.

        Whether or not this zone is DNSSEC signed (inferred from presigned being true XOR presence of at least one cryptokey with active being true)  # noqa: E501

        :param dnssec: The dnssec of this Zone.  # noqa: E501
        :type: bool
        """

        self._dnssec = dnssec

    @property
    def nsec3param(self):
        """Gets the nsec3param of this Zone.  # noqa: E501

        The NSEC3PARAM record  # noqa: E501

        :return: The nsec3param of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._nsec3param

    @nsec3param.setter
    def nsec3param(self, nsec3param):
        """Sets the nsec3param of this Zone.

        The NSEC3PARAM record  # noqa: E501

        :param nsec3param: The nsec3param of this Zone.  # noqa: E501
        :type: str
        """

        self._nsec3param = nsec3param

    @property
    def nsec3narrow(self):
        """Gets the nsec3narrow of this Zone.  # noqa: E501

        Whether or not the zone uses NSEC3 narrow  # noqa: E501

        :return: The nsec3narrow of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._nsec3narrow

    @nsec3narrow.setter
    def nsec3narrow(self, nsec3narrow):
        """Sets the nsec3narrow of this Zone.

        Whether or not the zone uses NSEC3 narrow  # noqa: E501

        :param nsec3narrow: The nsec3narrow of this Zone.  # noqa: E501
        :type: bool
        """

        self._nsec3narrow = nsec3narrow

    @property
    def presigned(self):
        """Gets the presigned of this Zone.  # noqa: E501

        Whether or not the zone is pre-signed  # noqa: E501

        :return: The presigned of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._presigned

    @presigned.setter
    def presigned(self, presigned):
        """Sets the presigned of this Zone.

        Whether or not the zone is pre-signed  # noqa: E501

        :param presigned: The presigned of this Zone.  # noqa: E501
        :type: bool
        """

        self._presigned = presigned

    @property
    def soa_edit(self):
        """Gets the soa_edit of this Zone.  # noqa: E501

        The SOA-EDIT metadata item  # noqa: E501

        :return: The soa_edit of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._soa_edit

    @soa_edit.setter
    def soa_edit(self, soa_edit):
        """Sets the soa_edit of this Zone.

        The SOA-EDIT metadata item  # noqa: E501

        :param soa_edit: The soa_edit of this Zone.  # noqa: E501
        :type: str
        """

        self._soa_edit = soa_edit

    @property
    def soa_edit_api(self):
        """Gets the soa_edit_api of this Zone.  # noqa: E501

        The SOA-EDIT-API metadata item  # noqa: E501

        :return: The soa_edit_api of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._soa_edit_api

    @soa_edit_api.setter
    def soa_edit_api(self, soa_edit_api):
        """Sets the soa_edit_api of this Zone.

        The SOA-EDIT-API metadata item  # noqa: E501

        :param soa_edit_api: The soa_edit_api of this Zone.  # noqa: E501
        :type: str
        """

        self._soa_edit_api = soa_edit_api

    @property
    def api_rectify(self):
        """Gets the api_rectify of this Zone.  # noqa: E501

        Whether or not the zone will be rectified on data changes via the API  # noqa: E501

        :return: The api_rectify of this Zone.  # noqa: E501
        :rtype: bool
        """
        return self._api_rectify

    @api_rectify.setter
    def api_rectify(self, api_rectify):
        """Sets the api_rectify of this Zone.

        Whether or not the zone will be rectified on data changes via the API  # noqa: E501

        :param api_rectify: The api_rectify of this Zone.  # noqa: E501
        :type: bool
        """

        self._api_rectify = api_rectify

    @property
    def zone(self):
        """Gets the zone of this Zone.  # noqa: E501

        MAY contain a BIND-style zone file when creating a zone  # noqa: E501

        :return: The zone of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this Zone.

        MAY contain a BIND-style zone file when creating a zone  # noqa: E501

        :param zone: The zone of this Zone.  # noqa: E501
        :type: str
        """

        self._zone = zone

    @property
    def catalog(self):
        """Gets the catalog of this Zone.  # noqa: E501

        The catalog this zone is a member of  # noqa: E501

        :return: The catalog of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this Zone.

        The catalog this zone is a member of  # noqa: E501

        :param catalog: The catalog of this Zone.  # noqa: E501
        :type: str
        """

        self._catalog = catalog

    @property
    def account(self):
        """Gets the account of this Zone.  # noqa: E501

        MAY be set. Its value is defined by local policy  # noqa: E501

        :return: The account of this Zone.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Zone.

        MAY be set. Its value is defined by local policy  # noqa: E501

        :param account: The account of this Zone.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def nameservers(self):
        """Gets the nameservers of this Zone.  # noqa: E501

        MAY be sent in client bodies during creation, and MUST NOT be sent by the server. Simple list of strings of nameserver names, including the trailing dot. Not required for slave zones.  # noqa: E501

        :return: The nameservers of this Zone.  # noqa: E501
        :rtype: list[str]
        """
        return self._nameservers

    @nameservers.setter
    def nameservers(self, nameservers):
        """Sets the nameservers of this Zone.

        MAY be sent in client bodies during creation, and MUST NOT be sent by the server. Simple list of strings of nameserver names, including the trailing dot. Not required for slave zones.  # noqa: E501

        :param nameservers: The nameservers of this Zone.  # noqa: E501
        :type: list[str]
        """

        self._nameservers = nameservers

    @property
    def master_tsig_key_ids(self):
        """Gets the master_tsig_key_ids of this Zone.  # noqa: E501

        The id of the TSIG keys used for master operation in this zone  # noqa: E501

        :return: The master_tsig_key_ids of this Zone.  # noqa: E501
        :rtype: list[str]
        """
        return self._master_tsig_key_ids

    @master_tsig_key_ids.setter
    def master_tsig_key_ids(self, master_tsig_key_ids):
        """Sets the master_tsig_key_ids of this Zone.

        The id of the TSIG keys used for master operation in this zone  # noqa: E501

        :param master_tsig_key_ids: The master_tsig_key_ids of this Zone.  # noqa: E501
        :type: list[str]
        """

        self._master_tsig_key_ids = master_tsig_key_ids

    @property
    def slave_tsig_key_ids(self):
        """Gets the slave_tsig_key_ids of this Zone.  # noqa: E501

        The id of the TSIG keys used for slave operation in this zone  # noqa: E501

        :return: The slave_tsig_key_ids of this Zone.  # noqa: E501
        :rtype: list[str]
        """
        return self._slave_tsig_key_ids

    @slave_tsig_key_ids.setter
    def slave_tsig_key_ids(self, slave_tsig_key_ids):
        """Sets the slave_tsig_key_ids of this Zone.

        The id of the TSIG keys used for slave operation in this zone  # noqa: E501

        :param slave_tsig_key_ids: The slave_tsig_key_ids of this Zone.  # noqa: E501
        :type: list[str]
        """

        self._slave_tsig_key_ids = slave_tsig_key_ids

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
        if issubclass(Zone, dict):
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
        if not isinstance(other, Zone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other