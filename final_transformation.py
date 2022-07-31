import rdflib

def final_transformation():

    filename = "results.ttl"

    g = rdflib.Graph()

    data = ''
    with open(filename, "r", encoding='cp1252') as file:
        for line in file:
            data += line
    g.parse(data=data, format='ttl', )

    with open("query.sparql", "r") as file:
        query = file.read()

    qres = g.query(query)

    with open("final_result.txt", "w") as file:
        for row in qres:
            for elem in row:
                file.write(str(elem.toPython()) + "\t")
            file.write('\n')

if __name__ == "__main__":
    final_transformation()
