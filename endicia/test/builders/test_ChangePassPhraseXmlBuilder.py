from nose.tools import assert_raises
from endicia.builders.ChangePassPhraseXmlBuilder import ChangePassPhraseXmlBuilder
from endicia.builders.EndiciaXmlBuilder import ValueToLongError

def test_ChangePassPhraseXmlBuilder_invalid_values():
	"""ChangePassPhraseXmlBuilder should raise ValueToLongError when each value is pass a value longer than required"""
	builder = ChangePassPhraseXmlBuilder()
	
	assert_raises( ValueToLongError, builder.setPartnerID, "123456789012345678901234567890123456789012345678901" )
	assert_raises( ValueToLongError, builder.setRequestID, "123456789012345678901234567890123456789012345678901" )
	assert_raises( ValueToLongError, builder.setAccountID, "1234567" )
	assert_raises( ValueToLongError, builder.setPassPhrase, "12345678901234567890123456789012345678901234567890123456789012345" )
