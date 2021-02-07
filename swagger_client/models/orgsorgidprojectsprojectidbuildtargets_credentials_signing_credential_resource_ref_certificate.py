# coding: utf-8

"""
    Unity Cloud Build

    This API is intended to be used in conjunction with the Unity Cloud Build service. A tool for building your Unity projects in the Cloud.  See https://developer.cloud.unity3d.com for more information.  ## Making requests This website is built to allow requests to be made against the API. If you are currently logged into Cloud Build you should be able to make requests without entering an API key.   You can find your API key in the Unity Cloud Services portal by clicking on 'Cloud Build Preferences' in the sidebar. Copy the API Key and paste it into the upper left corner of this website. It will be used in all subsequent requests.  ## Clients The Unity Cloud Build API is based upon Swagger. Client libraries to integrate with your projects can easily be generated with the [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen).  The JSON schema required to generate a client for this API version is located here:  ``` [API_URL][BASE_PATH]/api.json ```  ## Authorization The Unity Cloud Build API requires an access token from your Unity Cloud Build account, which can be found at https://build.cloud.unity3d.com/login/me  To authenticate requests, include a Basic Authentication header with your API key as the value. e.g.  ``` Authorization: Basic [YOUR API KEY] ```  ## Pagination Paged results will take two parameters. A page number that is calculated based upon the per_page amount. For instance if there are 40 results and you specify page 2 with per_page set to 10 you will receive records 11-20.  Paged results will also return a Content-Range header. For the example above the content range header would look like this:  ``` Content-Range: items 11-20/40 ```  ## Versioning The API version is indicated in the request URL. Upgrading to a newer API version can be done by changing the path.  The API will receive a new version in the following cases:    * removal of a path or request type   * addition of a required field   * removal of a required field  The following changes are considered backwards compatible and will not trigger a new API version:    * addition of an endpoint or request type   * addition of an optional field   * removal of an optional field   * changes to the format of ids  ## Identifiers It should not be assumed that any of the identifiers used in paths will be a perfect match for your user-entered information. If you see unexpected 403s or 404s from API calls then check your identifiers match the ones used by the API. In particular, `projectId` does NOT typically change when the project is renamed and in fact may not be a direct match for the project name even at initial creation time.  To avoid confusion we recommend that instead of using the human-readable autogenerated orgId and projectId available from the API you should instead use:   * org foreign key for `orgId` (available from project APIs as `orgFk` and org APIs as `coreForeignKey`)   * `guid` for `projectId`  All links generated by the API and the Dashboard should follow this format already, making it easy to figure out the correct parameters by making a comparison.  ## Rate Limiting Requests against the Cloud Build API are limited to a rate of 100 per minute. To preserve the quality of service throughout Cloud Build, additional rate limits may apply to some actions. For example, polling aggressively instead of using webhooks or making API calls with a high concurrency may result in rate limiting.  It is not intended for these rate limits to interfere with any legitimate use of the API. Please contact support at <cloudbuild@unity3d.com> if your use is affected by this rate limit.  You can check the returned HTTP headers for any API request to see your current rate limit status.   * __X-RateLimit-Limit:__ maximum number of requests per minute   * __X-RateLimit-Remaining:__ remaining number of requests in the current window   * __X-RateLimit-Reset:__ time at which the current window will reset (UTC epoch seconds)  Once you go over the rate limit you will receive an error response: ``` HTTP Status: 429 {   \"error\": \"Rate limit exceeded, retry in XX seconds\" } ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate(object):
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
        'team_id': 'str',
        'cert_name': 'str',
        'expiration': 'str',
        'is_distribution': 'bool',
        'issuer': 'str',
        'uploaded': 'str'
    }

    attribute_map = {
        'team_id': 'teamId',
        'cert_name': 'certName',
        'expiration': 'expiration',
        'is_distribution': 'isDistribution',
        'issuer': 'issuer',
        'uploaded': 'uploaded'
    }

    def __init__(self, team_id=None, cert_name=None, expiration=None, is_distribution=None, issuer=None, uploaded=None):  # noqa: E501
        """OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate - a model defined in Swagger"""  # noqa: E501

        self._team_id = None
        self._cert_name = None
        self._expiration = None
        self._is_distribution = None
        self._issuer = None
        self._uploaded = None
        self.discriminator = None

        if team_id is not None:
            self.team_id = team_id
        if cert_name is not None:
            self.cert_name = cert_name
        if expiration is not None:
            self.expiration = expiration
        if is_distribution is not None:
            self.is_distribution = is_distribution
        if issuer is not None:
            self.issuer = issuer
        if uploaded is not None:
            self.uploaded = uploaded

    @property
    def team_id(self):
        """Gets the team_id of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501

        generated team id from Apple  # noqa: E501

        :return: The team_id of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :rtype: str
        """
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        """Sets the team_id of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.

        generated team id from Apple  # noqa: E501

        :param team_id: The team_id of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :type: str
        """

        self._team_id = team_id

    @property
    def cert_name(self):
        """Gets the cert_name of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501

        certificate name (from the certificate)  # noqa: E501

        :return: The cert_name of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :rtype: str
        """
        return self._cert_name

    @cert_name.setter
    def cert_name(self, cert_name):
        """Sets the cert_name of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.

        certificate name (from the certificate)  # noqa: E501

        :param cert_name: The cert_name of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :type: str
        """

        self._cert_name = cert_name

    @property
    def expiration(self):
        """Gets the expiration of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501

        expiration date  # noqa: E501

        :return: The expiration of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.

        expiration date  # noqa: E501

        :param expiration: The expiration of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :type: str
        """

        self._expiration = expiration

    @property
    def is_distribution(self):
        """Gets the is_distribution of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501

        if this is a distribution certificate  # noqa: E501

        :return: The is_distribution of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :rtype: bool
        """
        return self._is_distribution

    @is_distribution.setter
    def is_distribution(self, is_distribution):
        """Sets the is_distribution of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.

        if this is a distribution certificate  # noqa: E501

        :param is_distribution: The is_distribution of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :type: bool
        """

        self._is_distribution = is_distribution

    @property
    def issuer(self):
        """Gets the issuer of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501

        issuer of the certificate  # noqa: E501

        :return: The issuer of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.

        issuer of the certificate  # noqa: E501

        :param issuer: The issuer of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def uploaded(self):
        """Gets the uploaded of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501

        uploaded date  # noqa: E501

        :return: The uploaded of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :rtype: str
        """
        return self._uploaded

    @uploaded.setter
    def uploaded(self, uploaded):
        """Sets the uploaded of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.

        uploaded date  # noqa: E501

        :param uploaded: The uploaded of this OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate.  # noqa: E501
        :type: str
        """

        self._uploaded = uploaded

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
        if issubclass(OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate, dict):
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
        if not isinstance(other, OrgsorgidprojectsprojectidbuildtargetsCredentialsSigningCredentialResourceRefCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other