"""
	ChangePassPhraseRequest -- Makes the change pass phrase request.

		This class will return the status of the pass phrase change, if it was a success or not.
"""

from endicia.breakers.ChangePassPhraseXmlBreaker import ChangePassPhraseXmlBreaker
from EndiciaRequest import EndiciaRequest

class ChangePassPhraseRequest( EndiciaRequest ):
	def __init__( self ):
		EndiciaRequest.__init__( self )
		self.breaker = ChangePassPhraseXmlBreaker()
		self.endiciaCommand = "/ChangePassPhraseXML"
		self.endiciaPostName = "changePassPhraseRequestXML"
