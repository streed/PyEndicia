from EndiciaXmlBreaker import EndiciaXmlBreaker
from EndiciaXmlBreaker import MissingValueXmlError
from lxml import etree
from schema import Schema, And, Use, Optional

class LabelXmlBreaker( EndiciaXmlBreaker ):

	schema = Schema( 
		{ 
			"Status": And( Use( int ), lambda n: n >= 0 ), 
			Optional( "ErrorMessage" ): Use( str ),
			"Base64LabelImage": str,
			"PIC": And( str, len ), 
			"TrackingNumber": And( str, len ),
			"FinalPostage": Use( float ),
			"TransactionID": Use( int ),
			"TransactionDateTime": Use( str ),
			"PostmarkDate": Use( str ),
			"PostageBalance": Use( float ),
			}
		)

	def __init__( self ):
		EndiciaXmlBreaker.__init__( self )

	def to_map( self ):
		_map = {}

		tree = etree.fromstring( self.xml )

		_map["Status"] = tree.findtext( "Status" )
		_map["Base64LabelImage"] = tree.findtext( "Base64LabelImage" )
		_map["PIC"] = tree.findtext( "PIC" )
		_map["TrackingNumber"] = tree.findtext( "TrackingNumber" )
		_map["FinalPostage"] = tree.findtext( "FinalPostage" )
		_map["TransactionID"] = tree.findtext( "TransactionID" )
		_map["TransactionDateTime"] = tree.findtext( "TransactionDateTime" )
		_map["PostmarkDate"] = tree.findtext( "PostmarkDate" )
		_map["PostageBalance"] = tree.findtext( "PostageBalance" )
		_map["ErrorMessage"] = tree.findtext( "ErrorMessage" )
		_map["FinalPostage"] = tree.findtext( "FinalPostage" )

		_map = self.schema.validate( _map )
		
		self.map = _map

		return self.map
