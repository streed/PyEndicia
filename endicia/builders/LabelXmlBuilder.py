from lxml.builder import E
from EndiciaXmlBuilder import EndiciaXmlBuilder
from DimensionsXmlBuilder import DimensionsXmlBuilder

class InvalidLabelValueError( Exception ):
	def __init__( self, value ):
		self.value = value
	
	def __str__( self ):
		return repr( "The value \"%s\" was not valid for this Label type" % ( self.value ) )

class RequiredLabelValueError( Exception ):
	def __init__( self, value ):
		self.value = value

	def __str__( self ):
		return repr( "This label is missing a required label value for it's %s" % ( self.value ) )

class RequiredBecauseLabelValueError( Exception ):
	def __init__( self, value, reason ):
		self.value = value
		self.reason = reason
	
	def __str__( self ):
		return repr( "The option %s is required because %s" % ( self.value, self.reason ) )

class LabelXmlBuilder( EndiciaXmlBuilder ):

	xml = {}
	
	def __init__( self ):
		EndiciaXmlBuilder.__init__( self )	
	
	def setByMap( self, options ):
		if "Test" in options:
			self.setTest()

		if "LabelType" in options:
			self.setLabelType( options["LabelType"] )

		if "LabelSubType" in options and ( options["LabelType"] in [ "Domestic", "International" ] ):
			self.setLabelSubType( options["LabelSubType"] )
		elif "LabelSubType" in options and ( not options["LabelType"] in [ "Domestic", "International" ] ):
			self.setLabelSubType( options["LabelSubType"] )
		else:
			raise RequiredBecauseLabelValueError( "LabelSubType", "LabelType is either Domestic or International" )

		if "LabelSize" in options:
			self.setLabelSize( options["LabelSize"] )

		if "ImageFormat" in options:
			self.setImageFormat( options["ImageFormat"] )

		if "ImageResolution" in options:
			self.setImageResolution( options["ImageResolution"] )

		if "RequesterID" in options:
			self.setRequestID( options["RequesterID"] )
		else:
			raise RequiredLabelValueError( "RequesterID" )

		if "AccountID" in options:
			self.setAccountID( options["AccountID"] )
		else:
			raise RequiredLabelValueError( "AccountID" )

		if "PassPhrase" in options:
			self.setPassPhrase( options["PassPhrase"] )
		else:
			raise RequiredLabelValueError( "PassPhrase" )

		if "MailClass" in options:
			self.setMailClass( options["MailClass"] )

		if "DateAdvance" in options:
			self.setDateAdvance( options["DateAdvance"] )

		if "WeightOz" in options:
			self.setWeightOunces( options["WeightOz"] )
		else:
			raise RequiredLabelValueError( "WeightOz" )

		if "MailpieceShape" in options:
			self.setMailPieceShape( options["MailpieceShape"] )
		else:
			raise RequiredLabelValueError( "MailpieceShape" )

		if "MailpieceDimensions" in options:
			self.setDimensions( options["MailpieceDimensions"] )
		else:
			raise RequiredLabelValueError( "Dimensions" )

		if "ShipDate" in options:
			self.setShipDate( options["ShipDate"] )
		else:
			raise RequiredLabelValueError( "ShipDate" )

		if "IncludePostage" in options:
			self.setIncludePostage( options["IncludePostage"] )
		
		if "ToAddress" in options:
			self.setToAddress( options["ToAddress"] )
		else:
			raise RequiredLabelValueError( "ToAddress" )
		
		if "FromAddress" in options:
			self.setFromAddress( options["FromAddress"] )
		else:
			raise RequiredLabelValueError( "FromAddress" )

		if "PartnerCustomerID" in options:
			self.setPartnerCustomerID( options["PartnerCustomerID"] )
		else:
			raise RequiredLabelValueError( "PartnerCustomerID" )

		if "PartnerTransactionID" in options:
			self.setPartnerTransactionID( options["PartnerTransactionID"] )
		else:
			raise RequiredLabelValueError( "PartnerTransactionID" )

	
	def setTest( self ):
		self.xml['Test'] = "Yes"
	
	def setLabelType( self, _type ):
		if _type in [ "Default", "CertifiedMail", "DestinationConfirm", "Domestic", "International" ]:
			self.xml["LabelType"] = _type
		else:
			raise InvalidLabelValueError( _type )

	def setLabelSubType( self, subType ):
		if subType in [ "Integrated", "None" ]:
			self.xml["LabelSubType"] = subType
		else:
			raise InvalidLabelValueError( subType )

	def setLabelSize( self, size ):
		if size in [ "4x6", "4x5", "4x4.5" ]:
			self.xml["LabelSize"] = size
		else:
			raise InvalidLabelValueError( size )

	def setImageFormat( self, _format ):
		if _format in [ "GIF", "JPEG", "PDF", "PNG" ]:
			self.xml["ImageFormat"] = _format
		else:
			raise InvalidLabelValueError( _format )

	def setImageResolution( self, resolution ):
		if resolution in [ "203", "300" ]:
			self.xml["ImageResolution"] = resolution
		else:
			raise InvalidLabelValueError( resolution )

	def setRequestID( self, _id ):
		self.xml["RequesterID"] = _id

	def setAccountID( self, _id ):
		self.xml["AccountID"] = _id

	def setPassPhrase( self, passphrase ):
		self.xml["PassPhrase"] = passphrase

	def setMailClass( self, mailclass ):
		if mailclass in [ "Express", "First", "LibraryMail", "MediaMail", "ParcelPost", "ParcelSelect", "Priority", "CriticalMail",
					"StandardMail", "ExpressMailInternational", "FirstClassMailInternational", "PriorityMailInternational", "GXG" ]:
			self.xml["MailClass"] = mailclass
		else:
			raise InvalidLabelValueError( mailclass )

	def setDateAdvance( self, dateadvance ):
		if dateadvance >= 0 and dateadvance <= 7:
			self.xml["DateAdvance"] = dateadvance
		else:
			raise InvalidLabelValueError( dateadvance )

	def setWeightOunces( self, ounces ):
		self.xml["WeightOz"] = ounces	

	#TODO: Add the other mail piece shapes
	def setMailPieceShape( self, shape ):
		if shape in [ "Card", "Letter", "Flat", "Parcel", "LargeParcel", "IrregularParcel" ]:
			self.xml["MailpieceShape"] = shape
		else:
			raise InvalidLabelValueError( shape )

	def setDimensions( self, dimensions ):
		if len( dimensions ) == 3:
			helper = DimensionsXmlBuilder()
			self.xml["MailpieceDimensions"] = helper( dimensions )
		else:
			raise TypeError( "Expected a 3-tuple for the mail dimensions" )

	def setShipDate( self, dateStr ):
		self.xml["ShipDate"] = dateStr

	def setShipTime( self, timeStr ):
		self.xml["ShipTime"] = timeStr

	def setIncludePostage( self, val ):
		self.xml["IncludePostage"] = val

	def setToAddress( self, toAddress ):
		if hasattr( toAddress, "__call__" ):
			self.xml['ToAddress'] = toAddress()
		else:
			self.xml["ToAddress"] = toAddress

	def setFromAddress( self, fromAddress ):
		if hasattr( fromAddress, "__call__" ):
			self.xml['FromAddress'] = fromAddress()
		else:
			self.xml["FromAddress"] = fromAddress
	
	def setPartnerCustomerID( self, customerID ):
		self.xml["PartnerCustomerID"] = customerID

	def setPartnerTransactionID( self, transactionID ):
		self.xml["PartnerTransactionID"] = transactionID
	
	def to_xml( self ):
		self.xmlString = (
			E.LabelRequest(
				E.Test( self.xml["Test"] ),
				#E.LabelType( self.xml["LabelType"] ),
				#E.LabelSubType( self.xml["LabelSubType"] ),
				E.LabelSize( self.xml["LabelSize"] ),
				E.ImageFormat( self.xml["ImageFormat"] ),
				E.ImageResolution( self.xml["ImageResolution"] ),
				E.RequesterID( self.xml["RequesterID"] ),
				E.AccountID( self.xml["AccountID"] ),
				E.PassPhrase( self.xml["PassPhrase"] ),
				E.MailClass( self.xml["MailClass"] ),
				E.WeightOz( str( self.xml["WeightOz"] ) ),
				E.MailpieceShape( self.xml["MailpieceShape"] ),
				E.PartnerCustomerID( self.xml["PartnerCustomerID"] ),
				E.PartnerTransactionID( self.xml["PartnerTransactionID"] ),
			)
		)

		if "LabelType" in self.xml:
			self.xmlString.append( E.LabelType( self.xml["LabelType"] ) )
			self.xmlString.append( E.LabelSubType( self.xml["LabelSubType"] ) )

		if not self.xml["MailpieceShape"] in [ "Card", "Letter", "Flat" ]:
			self.xmlString.append( self.xml["MailpieceDimensions"] )

		for e in self.xml["FromAddress"]:
			self.xmlString.append( e )
		for e in self.xml["ToAddress"]:
			self.xmlString.append( e )

		self.xmlString.append( E.RubberStamp1( "Bitcoin's postage store:" ) )
		self.xmlString.append( E.RubberStamp2( "BitPostage.net" ) )

		return self.xmlString

