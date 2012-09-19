from nose.tools import assert_raises
from endicia.builders.BuyPostageXmlBuilder import BuyPostageXmlBuilder
from endicia.builders.BuyPostageXmlBuilder import InvalidCreditAmountError
from endicia.builders.EndiciaXmlBuilder import ValueToLongError

from lxml import etree
from lxml.builder import E

def test_BuyPostageXmlBuilder_should_throw_exceptions_when_passed_invalid_values():
	"""Passing wrong values should throw the respective exception"""
	builder = BuyPostageXmlBuilder()

	assert_raises( ValueToLongError, builder.setPartnerID, "123456789012345678901234567890123456789012345678901" )
	assert_raises( ValueToLongError, builder.setRequestID, "123456789012345678901234567890123456789012345678901" )
	assert_raises( ValueToLongError, builder.setAccountID, "1234567" )	
	assert_raises( ValueToLongError, builder.setPassPhrase, "12345678901234567890123456789012345678901234567890123456789012345" )
	assert_raises( InvalidCreditAmountError, builder.setRecreditAmount, 0 )


