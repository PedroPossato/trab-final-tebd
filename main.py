import rdflib

filename = "results.ttl"

g = rdflib.Graph()

data = ''
with open(filename, "r", encoding='cp1252') as file:
    for line in file:
        data += line
g.parse(data=data, format='ttl', )

query = """
PREFIX : <http://example.com/>
PREFIX jarql: <http://jarql.com/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>

SELECT ?link ?b ?c
WHERE {
    ?a ?b ?c.
    ?a :link ?link.
    FILTER NOT EXISTS {
        FILTER(REGEX(str(?b), "link", "i"))
    }

}
ORDER BY ASC(?a)
"""

qres = g.query(query)

with open("final_result.txt", "w") as file:
    for row in qres:
        for elem in row:
            file.write(elem.toPython() + "\t")
        file.write('\n')
