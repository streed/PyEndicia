from endicia.requests.ChangePassPhraseRequest import ChangePassPhraseRequest
from endicia.builders.ChangePassPhraseXmlBuilder import ChangePassPhraseXmlBuilder

from lxml.builder import E

def test_ChangePassPhraseRequest_returns_a_successful_request():
	"""ChangePassPhraseRequest should reutrn a successful request where status == 0"""
	request = ChangePassPhraseRequest()

	builder = ChangePassPhraseXmlBuilder()

	builder.setPartnerID( "abcd" )
	builder.setRequestID( "1234" )
	builder.setAccountID( "123456" )
	builder.setPassPhrase( "123456" )
	builder.setNewPassPhrase( "1234567" )

	_map = request.get( builder )

	assert _map["Status"] == 0
