from SPARQLWrapper import SPARQLWrapper, JSON, BASIC, DIGEST


def execute_query(query):
    sparql = SPARQLWrapper("https://lov.linkeddata.es/dataset/lov/sparql")
    sparql.setHTTPAuth(DIGEST)
    sparql.setReturnFormat(JSON)
    sparql.setQuery(query)
    try:
        ret = sparql.query().convert()
        print(ret)
        return ret
    except Exception as e:
        print(e)