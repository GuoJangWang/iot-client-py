# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from arduino_iot_rest.configuration import Configuration


class ThingSketch(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        '_pass': 'str',
        'ssid': 'str'
    }

    attribute_map = {
        '_pass': 'pass',
        'ssid': 'ssid'
    }

    def __init__(self, _pass=None, ssid=None, local_vars_configuration=None):  # noqa: E501
        """ThingSketch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__pass = None
        self._ssid = None
        self.discriminator = None

        if _pass is not None:
            self._pass = _pass
        if ssid is not None:
            self.ssid = ssid

    @property
    def _pass(self):
        """Gets the _pass of this ThingSketch.  # noqa: E501

        The wifi password  # noqa: E501

        :return: The _pass of this ThingSketch.  # noqa: E501
        :rtype: str
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """Sets the _pass of this ThingSketch.

        The wifi password  # noqa: E501

        :param _pass: The _pass of this ThingSketch.  # noqa: E501
        :type: str
        """

        self.__pass = _pass

    @property
    def ssid(self):
        """Gets the ssid of this ThingSketch.  # noqa: E501

        The wifi ssid to connect  # noqa: E501

        :return: The ssid of this ThingSketch.  # noqa: E501
        :rtype: str
        """
        return self._ssid

    @ssid.setter
    def ssid(self, ssid):
        """Sets the ssid of this ThingSketch.

        The wifi ssid to connect  # noqa: E501

        :param ssid: The ssid of this ThingSketch.  # noqa: E501
        :type: str
        """

        self._ssid = ssid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, ThingSketch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThingSketch):
            return True

        return self.to_dict() != other.to_dict()
