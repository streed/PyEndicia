"""
	RecreditRequest -- This makes the request to Endicia to replenish the account with money.
		
		This class will return the status of the replishment, if it was a success or not.
"""

from endicia.breakers.BuyPostageXmlBreaker import BuyPostageXmlBreaker
from EndiciaRequest import EndiciaRequest

class RecreditRequest( EndiciaRequest ):
	def __init__( self ):
		EndiciaRequest.__init__( self )	
		self.breaker = BuyPostageXmlBreaker()
		self.endiciaCommand = "/BuyPostageXML"
		self.endiciaPostName = "recreditRequestXML"
