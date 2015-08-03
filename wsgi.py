from leancloud import Engine


def wsgi_func(environment, start_response):
	start_response("200 OK", [("Content-Type", "text/plain")])
	return ["Hello, gambler!"]



application = Engine(wsgi_func)