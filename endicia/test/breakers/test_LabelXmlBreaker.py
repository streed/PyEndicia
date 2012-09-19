from nose.tools import assert_raises
from endicia.breakers.LabelXmlBreaker import LabelXmlBreaker

from lxml.builder import E
from lxml import etree

def test_LabelXmlBreaker_should_return_a_proper_hash_for_a_request_response():
	"""LabelXmlBreaker should parse the returned xml properly"""	
	def mock_response():
		return etree.tostring( E.LabelRequestResponse(
			E.Status( str( 0 ) ),
			E.ErrorMessage( "None" ),
			E.Base64LabelImage( "This_is_fake" ),
			E.PIC( str( 123 ) ),
			E.TrackingNumber( str( 1234567890 ) ),
			E.FinalPostage( str( 5.00 ) ),
			E.TransactionID( str( 789 ) ),
			E.TransactionDateTime( str( 20101220060019 ) ),
			E.PostmarkDate( str( 20080508 ) ),
			E.PostageBalance( str( 123.45 ) ),
#			E.PostagePrice( 
#				E.Postage( 
#					E.IntraBMC( "FALSE" ),
#					E.Pricing( "CommercialBase" ),
#					TotalAmount=str( 5.44 )
#				),
#				E.Fees(
#					E.MailService( "Priority Mail" ),
#					E.Zone( str( 4 ) ),
#					E.ElectronicReturnReceipt( str( 0 ) ),
#					E.InsuredMail( str( 0 ) ),
#					E.RegisteredMAil( str( 0 ) ),
#					E.RestrictedDelivery( str( 0 ) ),
#					E.ReturnReceipt( str( 0 ) ),
#					E.ReturnReceiptForMerchandise( str( 0 ) ),
#					E.SignatureConfifirmation( str( 1.95 ) ),
#					E.SpecialHandling( str( 0 ) ),
#					TotalAmount=str( 1.95 )
#				),
#				TotalAmount=str( 7.39 )
#			)
		) )

		
	breaker = LabelXmlBreaker()

	breaker.setXmlString( mock_response() )

	ret = breaker.to_map()
	
	assert ret["Status"] == 0
	assert ret["ErrorMessage"] == "None"
	assert ret["Base64LabelImage"] == "This_is_fake"
	assert ret["PIC"] == "123"
	assert ret["TrackingNumber"] == "1234567890"
	assert ret["FinalPostage"] == 5.0
	assert ret["TransactionID"] == 789
	assert ret["TransactionDateTime"] == "20101220060019"
	assert ret["PostmarkDate"] == "20080508"
	assert ret["PostageBalance"] == 123.45
	#assert ret["PostagePrice"] == "7.39"
	#assert ret["Pricing"] == "CommercialBase"
	#assert ret["IntraBMC"] == "FALSE"
	#TODO: Do I want to record the fees? 
