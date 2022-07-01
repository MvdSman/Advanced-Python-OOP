import justpy as jp

import api
import documentation

jp.Route('/api', api.Api.serve)
jp.Route('/', documentation.Docs.serve)
jp.justpy(port=8001)
