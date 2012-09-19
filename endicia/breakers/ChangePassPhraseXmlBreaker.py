from EndiciaXmlBreaker import EndiciaXmlBreaker
from EndiciaXmlBreaker import MissingValueXmlError
from lxml import etree
from schema import Schema, And, Use, Optional

class ChangePassPhraseXmlBreaker( EndiciaXmlBreaker ):

	schema = Schema( { 
		"Status": And( Use( int ), lambda n: n >= 0 ),
		Optional( "ErrorMessage" ): Use( str ),
		"RequesterID": And( Use( str ), lambda n: len( n ) <= 50 ),
		"RequestID": And( Use( str ), lambda n: len( n ) <= 50 )
	})

	def __init__( self ):
		EndiciaXmlBreaker.__init__( self )

	def to_map( self ):
		_map = {}

		tree = etree.fromstring( self.xml )

		_map["Status"] = tree.findtext( "Status" )
		_map["RequesterID"] = tree.findtext( "RequesterID" )
		_map["RequestID"] = tree.findtext( "RequestID" )

		if _map["Status"] != "0":
			_map["ErrorMessage"] = tree.findtext( "ErrorMessage" )

		_map = self.schema.validate( _map )

		self.map = _map

		return self.map
