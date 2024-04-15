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

class RingStatisticItem(object):
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
        'name': 'str',
        'type': 'str',
        'size': 'int',
        'value': 'list[SimpleStatisticItem]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'size': 'size',
        'value': 'value'
    }

    def __init__(self, name=None, type=None, size=None, value=None):  # noqa: E501
        """RingStatisticItem - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._size = None
        self._value = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this RingStatisticItem.  # noqa: E501

        Item name  # noqa: E501

        :return: The name of this RingStatisticItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RingStatisticItem.

        Item name  # noqa: E501

        :param name: The name of this RingStatisticItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this RingStatisticItem.  # noqa: E501

        Set to \"RingStatisticItem\"  # noqa: E501

        :return: The type of this RingStatisticItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RingStatisticItem.

        Set to \"RingStatisticItem\"  # noqa: E501

        :param type: The type of this RingStatisticItem.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def size(self):
        """Gets the size of this RingStatisticItem.  # noqa: E501

        Ring size  # noqa: E501

        :return: The size of this RingStatisticItem.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RingStatisticItem.

        Ring size  # noqa: E501

        :param size: The size of this RingStatisticItem.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def value(self):
        """Gets the value of this RingStatisticItem.  # noqa: E501

        Named values  # noqa: E501

        :return: The value of this RingStatisticItem.  # noqa: E501
        :rtype: list[SimpleStatisticItem]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RingStatisticItem.

        Named values  # noqa: E501

        :param value: The value of this RingStatisticItem.  # noqa: E501
        :type: list[SimpleStatisticItem]
        """

        self._value = value

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
        if issubclass(RingStatisticItem, dict):
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
        if not isinstance(other, RingStatisticItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
