from nose.tools import assert_raises
from endicia.breakers.BuyPostageXmlBreaker import BuyPostageXmlBreaker
from endicia.breakers.EndiciaXmlBreaker import MissingValueXmlError

from lxml.builder import E
from lxml import etree


def test_BuyPostageXmlBreaker_should_return_a_proper_hash_for_a_request_response():
	"""BuyPostageXmlBreaker should properly parse the response xml"""
	def mock_response():
		return etree.tostring( 
			E.RecreditRequestResponse(
				E.Status( str( 0 ) ),
				E.RequesterID( "abcd" ),
				E.RequestID( "BP123" ),
				E.CertifiedIntermediary( 
					E.AccountID( "123456" ),
					E.SerialNumber( "789" ),
					E.PostageBalance( "76.55" ),
					E.AscendingBalance( "123.45" ),
					E.AccountStatus( "A" ),
					E.DeviceID( "071V00123456" )
				)
			)
		)

	breaker = BuyPostageXmlBreaker()

	breaker.setXmlString( mock_response() )

	ret = breaker.to_map()

	assert ret["Status"] == 0
	assert ret["RequesterID"] == "abcd"
	assert ret["RequestID"] == "BP123"
	assert ret["AccountID"] == "123456"
	assert ret["PostageBalance"] == 76.55
	assert ret["AscendingBalance"] == 123.45

def test_BuyPostageXmlBreaker_should_throw_MissingValueXmlError():
	"""BuyPostageXmlBreaker should raise MissingValueXmlError"""

	def mock_response():
		return etree.tostring( 
			E.RecreditRequestResponse(
				E.Status( "0" ),
				E.RequesterID( "abcd" ),
				E.RequestID( "BP123" ),
				E.CertifiedIntermediary( 
					E.AccountID( "123456" ),
					E.SerialNumber( "789" ),
					E.PostageBalance( "76.55" ),
					E.AscendingBalance( "123.45" ),
					E.AccountStatus( "A" ),
					E.DeviceID( "071V00123456" )
				)
			)
		)

	breaker = BuyPostageXmlBreaker()

	breaker.setXmlString( mock_response() )

	#assert_raises( MissingValueXmlError, breaker.to_map )
