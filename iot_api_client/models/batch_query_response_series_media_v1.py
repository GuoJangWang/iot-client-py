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


class BatchQueryResponseSeriesMediaV1(object):
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
        'aggr': 'str',
        'expression': 'str',
        'metric': 'str'
    }

    attribute_map = {
        'aggr': 'aggr',
        'expression': 'expression',
        'metric': 'metric'
    }

    def __init__(self, aggr=None, expression=None, metric=None):  # noqa: E501
        """BatchQueryResponseSeriesMediaV1 - a model defined in OpenAPI"""  # noqa: E501

        self._aggr = None
        self._expression = None
        self._metric = None
        self.discriminator = None

        self.aggr = aggr
        self.expression = expression
        self.metric = metric

    @property
    def aggr(self):
        """Gets the aggr of this BatchQueryResponseSeriesMediaV1.  # noqa: E501

        Aggregation type  # noqa: E501

        :return: The aggr of this BatchQueryResponseSeriesMediaV1.  # noqa: E501
        :rtype: str
        """
        return self._aggr

    @aggr.setter
    def aggr(self, aggr):
        """Sets the aggr of this BatchQueryResponseSeriesMediaV1.

        Aggregation type  # noqa: E501

        :param aggr: The aggr of this BatchQueryResponseSeriesMediaV1.  # noqa: E501
        :type: str
        """
        if aggr is None:
            raise ValueError("Invalid value for `aggr`, must not be `None`")  # noqa: E501

        self._aggr = aggr

    @property
    def expression(self):
        """Gets the expression of this BatchQueryResponseSeriesMediaV1.  # noqa: E501

        Query  # noqa: E501

        :return: The expression of this BatchQueryResponseSeriesMediaV1.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this BatchQueryResponseSeriesMediaV1.

        Query  # noqa: E501

        :param expression: The expression of this BatchQueryResponseSeriesMediaV1.  # noqa: E501
        :type: str
        """
        if expression is None:
            raise ValueError("Invalid value for `expression`, must not be `None`")  # noqa: E501

        self._expression = expression

    @property
    def metric(self):
        """Gets the metric of this BatchQueryResponseSeriesMediaV1.  # noqa: E501

        Metric name  # noqa: E501

        :return: The metric of this BatchQueryResponseSeriesMediaV1.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this BatchQueryResponseSeriesMediaV1.

        Metric name  # noqa: E501

        :param metric: The metric of this BatchQueryResponseSeriesMediaV1.  # noqa: E501
        :type: str
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

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
        if not isinstance(other, BatchQueryResponseSeriesMediaV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
