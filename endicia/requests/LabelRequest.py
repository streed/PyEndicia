"""
	LabelRequest -- This makes the request to Endicia to do the actual grab of the label inforamtion.
			the other requests.

			This class will return a Hash of the xml which will be returned by the EndiciaXmlHelper
"""
#stuff
from endicia.breakers.LabelXmlBreaker import LabelXmlBreaker
from endicia.requests.EndiciaRequest import EndiciaRequest

class LabelRequest( EndiciaRequest ):
	def __init__( self ):
		EndiciaRequest.__init__( self )
		self.breaker = LabelXmlBreaker()
		self.endiciaCommand = "/GetPostageLabelXML"
		self.endiciaPostName = "labelRequestXML"
