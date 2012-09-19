from base64 import b64decode as decode

def dumpToFile( filename, data ):
	with open( filename, "wb" ) as f:
		f.write( decode( data ) )

