"""
	Request -- The base class for all request subclasses.
		This class will house the basic functionality the subclasses simply passs a 
		different breaker to this class and it will handle everything else. It will
		return the result of the breaker class.
"""

import inject
import logging
import urllib
import httplib2
from lxml import etree
from urllib import urlencode

class EndiciaRequest:
	@inject.param( "endiciaPartnerId", bindto="123456" )
	@inject.param( "endiciaAccountId", bindto="123456" )
	@inject.param( "endiciaPassPhrase", bindto="x" )
	@inject.param( "endiciaBaseUrl", bindto="www.envmgr.com" )
	@inject.param( "endiciaUrlPath", bindto="/LabelService/EwsLabelService.asmx" )
	@inject.param( "endiciaCommand", bindto="/Do_Nothing" )
	def __init__( self, endiciaPartnerId, endiciaAccountId, endiciaPassPhrase, endiciaBaseUrl, endiciaUrlPath, endiciaCommand ):
		self.endiciaPartnerId = endiciaPartnerId
		self.endiciaAccountId = endiciaAccountId
		self.endiciaBaseUrl = endiciaBaseUrl
		self.endiciaUrlPath = endiciaUrlPath
		self.endiciaCommand = endiciaCommand

		self.http = httplib2.Http()

	def get( self, request ):	

		url = "https://%s%s%s" % ( self.endiciaBaseUrl, self.endiciaUrlPath, self.endiciaCommand )

		logging.info( "Sending request to \"%s\"" % ( url ) )
		
		requestString = self.buildRequest( request )

		headers = { "Content-Type": "application/x-www-form-urlencoded" }

		response, content = self.http.request( url, "POST", body=requestString, headers=headers )

		logging.info( "Parsing the response" )

		content = content.replace( " xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns=\"www.envmgr.com/LabelService\"", "" )

		self.breaker.setXmlString( content )

		return self.breaker.to_map()

	def buildRequest( self, request ):
		xmlString = etree.tostring( request.to_xml() )
		return "%s=%s" % ( self.endiciaPostName, xmlString ) 
