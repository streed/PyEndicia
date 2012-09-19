from lxml.builder import E
from EndiciaXmlBuilder import EndiciaXmlBuilder

class InvalidAddressTypeError( Exception ):
	def __init__( self, value ):
		self.value = value

	def __str__( self ):
		return repr( "The value \"%s\" is not a valid address type" % ( self.value ) )

class AddressXmlBuilder( EndiciaXmlBuilder ):

	xml = {}

	def __init__( self, _type="From" ):
		EndiciaXmlBuilder.__init__( self )
		self._type = _type

	def setName( self, name ):
		self.xml["Name"] = name
	
	def setCompany( self, company ):
		self.xml["Company"] = company

	def setAddress1( self, address ):
		self.xml["Address1"] = address
	
	def setAddress2( self, address ):
		self.xml["Address2"] = address

	def setCity( self, city ):
		self.xml["City"] = city

	def setState( self, state ):
		self.xml["State"] = state 
	
	def setPostalCode( self, postalCode ):
		self.xml["PostalCode"] = postalCode

	def setCountry( self, country ):
		self.xml["Country"] = country

	def setPhone( self, phone ):
		self.xml["Phone"] = phone

	def setEmail( self, email ):
		self.xml["EMail"] = email

	def setCountryCode( self, countrycode ):
		self.xml["CountryCode"] = countrycode

	def to_xml( self ):
		if self._type == "To":
			return self.to_xml_to()
		elif self._type == "From":
			return self.to_xml_from()
		else:
			raise InvalidAddressTypeError( self._type )
		
		
	def to_xml_to( self ):
		self.xmlString = ( 
			E.ToName( self.xml["Name"] ),
			E.ToCompany( self.xml['Company'] ),
			E.ToAddress1( self.xml['Address1'] ),
			E.ToAddress2( self.xml['Address2'] ),
			E.ToCity( self.xml['City'] ),
			E.ToState( self.xml['State'] ),
			E.ToPostalCode( self.xml['PostalCode'] )
			#E.ToZIP4( self.xml['ZIP4'] ),
			#E.ToPhone( self.xml['Phone'] ),
			#E.ToEMail( self.xml['EMail'] )
		)

		return self.xmlString

	def to_xml_from( self ):
		self.xmlString = (
			E.FromName( self.xml["Name"] ),
			E.FromCompany( self.xml["Company"] ),
			E.ReturnAddress1( self.xml["Address1"] ),
			E.ReturnAddress2( self.xml["Address2"] ),
			E.FromCity( self.xml["City"] ),
			E.FromState( self.xml["State"] ),
			E.FromPostalCode( self.xml["PostalCode"] ),
			#E.FromZIP4( self.xml["ZIP4"] ),
			E.FromCountry( self.xml["Country"] ),
			#E.FromPhone( self.xml["Phone"] ),
			#E.FromEMail( self.xml["EMail"] )
		)

		return self.xmlString
