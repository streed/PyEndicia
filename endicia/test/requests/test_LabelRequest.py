from endicia.requests.LabelRequest import LabelRequest
from endicia.builders.LabelXmlBuilder import LabelXmlBuilder

from endicia.util.DumpBinaryData import dumpToFile

from lxml.builder import E

def test_LabelRequest_make_request():
	"""LabelRequest should return a successful request with a status == 0 and a proper label returned"""
	request = LabelRequest()

	def mockToAddress():
		ret = (
			#E.ToCompany( "fake" ),
			E.ToName( "Sean" ),
			E.ToAddress1( "123 Fake" ),
			E.ToAddress2( "" ),
			E.ToCity( "faketilly" ),
			E.ToState( "VA" ),
			E.ToPostalCode( "20000" ),
			#E.ToZIP4( "1234" ),
			#E.ToPhone( "1234567890" ),
			#E.ToEMail( "fake@fake.com" )
		)

		return ret

	def mockFromAddress():
		ret = (
			E.FromName( "David" ),
			#E.FromCompany( "Fake company" ),
			E.ReturnAddress1( "123 fake" ),
			E.ReturnAddress2( "" ),
			E.FromCity( "faketilly" ),
			E.FromState( "VA" ),
			E.FromPostalCode( "20000" ),
			#E.FromZIP4( "1234" ),
			#E.FromPhone( "1234567890" )
		)

		return ret

	builder = LabelXmlBuilder()

	builder.setTest()
	builder.setLabelType( "Domestic" )
	builder.setLabelSubType( "None" )
	builder.setLabelSize( "4x6" )
	builder.setImageFormat( "JPEG" )
	builder.setImageResolution( "300" )
	builder.setRequestID( "123456" )
	builder.setAccountID( "123456" )
	builder.setPassPhrase( "x" )
	builder.setMailClass( "First" )
	builder.setDateAdvance( 0 )
	builder.setWeightOunces( 4.1 )
	builder.setMailPieceShape( "Parcel" )
	builder.setDimensions( ( 10.0, 10.0, 1 ) )
	builder.setToAddress( mockToAddress )
	builder.setFromAddress( mockFromAddress )
	builder.setPartnerCustomerID( "123456" )
	builder.setPartnerTransactionID( "123456" )

	_map = request.get( builder )

	dumpToFile( "test/data/test_images/test_domestic.jpg", _map["Base64LabelImage"] )

	assert _map["Status"] == 0
	
	builder.setLabelType( "Default" )

	_map = request.get( builder )

	dumpToFile( "test/data/test_images/test_default.jpg", _map["Base64LabelImage"] )

	assert _map["Status"] == 0
