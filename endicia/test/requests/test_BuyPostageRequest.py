from endicia.requests.RecreditRequest import RecreditRequest
from endicia.builders.BuyPostageXmlBuilder import BuyPostageXmlBuilder

from endicia.util.DumpBinaryData import dumpToFile

def test_RecreditRequest_make_request():
	"""RecreditRequst should return a status of 0"""
	request = RecreditRequest()

	builder = BuyPostageXmlBuilder()

	builder.setPartnerID( "abcd" )
	builder.setRequestID( "123456" )
	builder.setAccountID( "123456" )
	builder.setPassPhrase( "password" )
	builder.setRecreditAmount( 10 )

	_map = request.get( builder )

	assert _map["Status"] == 0
