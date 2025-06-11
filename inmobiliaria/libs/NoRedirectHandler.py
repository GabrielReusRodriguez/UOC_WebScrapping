import urllib

""" 
Para que urlopen ignore los redirect tenemos que implementar una subclase de httpredirecthandler  y luego instala NUESTRO handler para que
cada vez que reciba un 302 ejecute un codigo "vacio" que devuevle el code , pero no sigue el redirect.
"""
#import urllib2

#urllib.HTTPRedirectHandler
# install alternative handler to stop urllib2 from following redirects
#class NoRedirectHandler(urllib.HTTPRedirectHandler):
class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
	# alternative handler
	def http_error_300(self,req,fp,code,msg,header_list):
		data = urllib.request.addinfourl(fp,header_list,req.get_full_url())
		#data.status = code
		data.code = code

		return data

	# setup aliases
	http_error_301 = http_error_300
	http_error_302 = http_error_300
	http_error_303 = http_error_300
	http_error_307 = http_error_300

urllib.request.install_opener(
	urllib.request.build_opener(NoRedirectHandler())
)