from EndiciaXmlBreaker import EndiciaXmlBreaker
from EndiciaXmlBreaker import MissingValueXmlError
from lxml import etree
from schema import Schema, And, Use, Optional

class BuyPostageXmlBreaker( EndiciaXmlBreaker ):
	
	schema = Schema( { 
		"Status": And( Use( int ), lambda n: n >= 0 ),
		"RequesterID": And( Use( str ), lambda n: len( n ) <= 50 ),
		"RequestID": And( Use( str ), lambda n: len( n ) <= 50 ),
		"AccountID": And( Use( str ), lambda n: len( n ) <= 6 ),
		"PostageBalance": And( Use( float ), lambda n: n >= 0.0 ),
		"AscendingBalance": And( Use( float ), lambda n: n >= 0.0 ),
		Optional( "ErrorMessage" ): str 
		})


	def __init__( self ):
		EndiciaXmlBreaker.__init__( self )

	def to_map( self ):
		_map = {}

		tree = etree.fromstring( self.xml )

		_map["Status"] = tree.findtext( "Status" )
		if _map["Status"] == None:
			raise MissingValueXmlError( "Status" )

		_map["RequesterID"] = tree.findtext( "RequesterID" )
		if _map["RequesterID"] == None:
			raise MissingValueXmlError( "RequesterID" )

		_map["RequestID"] = tree.findtext( "RequestID" )
		if _map["RequestID"] == None:
			raise MissingValueXmlError( "RequestID" )

		_map["AccountID"] = tree.findtext( "./CertifiedIntermediary/AccountID" )
		if _map["AccountID"] == None:
			raise MissingValueXmlError( "AccountID" )

		_map["PostageBalance"] = tree.findtext( "./CertifiedIntermediary/PostageBalance" )
		if _map["PostageBalance"] == None: 
			raise MissingValueXmlError( "PostageBalance" )

		_map["AscendingBalance"] = tree.findtext( "./CertifiedIntermediary/AscendingBalance" )
		if _map["AscendingBalance"] == None:
			raise MissingValueXmlError( "AscendingBalance" )

		if tree.find( "ErrorMessage" ) != None:
			_map["ErrorMessage"] = tree.findtext( "ErrorMessage" )

		_map = self.schema.validate( _map )

		self.map = _map 

		return self.map
