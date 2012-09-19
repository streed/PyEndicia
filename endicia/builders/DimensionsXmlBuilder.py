from lxml.builder import E
from EndiciaXmlBuilder import EndiciaXmlBuilder

class DimensionsXmlBuilder( EndiciaXmlBuilder ):
	def __init__( self ):
		pass
	def __call__( self, dims ):
		self.dims = dims
		
		self.xmlString = ( 
			E.MailpieceDimensions (
				E.Length( str( dims[0] ) ),
				E.Width( str( dims[1] ) ),
				E.Height( str( dims[2] ) )
			)
		)

		return self.xmlString
