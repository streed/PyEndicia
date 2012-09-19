from lxml.builder import E

class ValueToLongError( Exception ):
	def __init__( self, param, value ):
		self.param = param
		self.value = value

	def __str__( self ):
		return repr( "The %s param was given the following value %s and it was too long." % ( self.param, self.value ) )

class EndiciaXmlBuilder:
	def __init__( self ):
		pass
	def to_string( self ):
		pass
	def to_hash( self ):
		pass
	def to_json( self ):
		pass
