from EndiciaXmlBuilder import EndiciaXmlBuilder
from EndiciaXmlBuilder import ValueToLongError
from lxml.builder import E

class ChangePassPhraseXmlBuilder( EndiciaXmlBuilder ):

	xml = {}

	def __init__( self ):
		EndiciaXmlBuilder.__init__( self )

	def setPartnerID( self, __id ):
		if len( __id ) <= 50:
			self.xml["RequesterID"] = __id
		else:
			raise ValueToLongError( "PartnerID", str( __id ) )

	def setRequestID( self, __id ):
		if len( __id ) <= 50:
			self.xml["RequestID"] = __id
		else:
			raise ValueToLongError( "RequestID", str( __id ) )

	def setAccountID( self, __id ):
		if len( __id ) <= 6:
			self.xml["AccountID"] = __id
		else:
			raise ValueToLongError( "AccountID", str( __id ) )

	def setPassPhrase( self, passPhrase ):
		if len( passPhrase ) <= 64:
			self.xml["PassPhrase"] = passPhrase
		else:
			raise ValueToLongError( "PassPhrase", str( passPhrase ) )

	def setNewPassPhrase( self, newPassPhrase ):
		if len( newPassPhrase ) <= 64:
			self.xml["NewPassPhrase"] = newPassPhrase
		else:
			raise ValueToLongError( "NewPassPhrase", str( newPassPhrase ) )

	def to_xml( self ):
		self.xmlString = (
			E.ChangePassPhraseRequest(
				E.RequesterID( self.xml["RequesterID"] ),
				E.RequestID( self.xml["RequestID"] ),
				E.CertifiedIntermediary( 
					E.AccountID( self.xml["AccountID"] ),
					E.PassPhrase( self.xml["PassPhrase"] )
				),
				E.NewPassPhrase( self.xml["NewPassPhrase"] )
			)
		)

		return self.xmlString
