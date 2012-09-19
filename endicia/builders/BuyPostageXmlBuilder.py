from EndiciaXmlBuilder import EndiciaXmlBuilder
from EndiciaXmlBuilder import ValueToLongError
from lxml.builder import E

class InvalidCreditAmountError( Exception ):
	def __init__( self, value ):
		self.value = value
	
	def __str__( self ):
		return repr( "The following recredit amount: %d is an invalid amount." % self.value )

class BuyPostageXmlBuilder( EndiciaXmlBuilder ):

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

	def setRecreditAmount( self, amount ):
		if amount in [ 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 7500, 10000, 20000 ]:
			self.xml["RecreditAmount"] = str( amount )
		else:
			raise InvalidCreditAmountError( amount )

	def to_xml( self ):
		self.xmlString = ( 
			E.RecreditRequest( 
				E.RequesterID( self.xml["RequesterID"] ),
				E.RequestID( self.xml["RequestID"] ),
				E.CertifiedIntermediary(
					E.AccountID( self.xml["AccountID"] ),
					E.PassPhrase( self.xml["PassPhrase"] )
				),
				E.RecreditAmount( self.xml["RecreditAmount"] )
			)
		)

		return self.xmlString
