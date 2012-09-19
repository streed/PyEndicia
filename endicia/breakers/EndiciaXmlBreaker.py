
class MissingValueXmlError( Exception ):
	def __init__( self, val ):
		self.val = val

	def __str__( self ):
		return repr( "The Xml document was missing '%s'" % ( self.val ) )

class EndiciaXmlBreaker:
	def __init__( self ):
		pass

	def setXmlString( self, xml ):
		self.xml = xml

	def to_map( self ):
		pass
