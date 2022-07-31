# trab-final-tebd

### Arquivos explicados

- complete_news.json: Arquivo JSON contendo todas as notícias (não é utilizado no processo. O news.json que é utilizado).
- final_result.txt: Resultado final obtido após todo o processo.
- final_transformation.py: Segundo script python a ser rodado, responsável pela realização da query desejada no arquivo Turtle gerado.
- jarql-1.0.0.jar: Arquivo jar responsável por viabilizar a utilização do projeto JARQL.
- json_to_turtle.py: Primeiro script python a ser rodado, responsável pela transformação de JSON em Turtle.
- news.json: Arquivo JSON contendo as notícias que serão usadas no processo.
- original_query.sparql: Query SPARQL que gera o mapeamento total de cada link de notícia com cada atributo da notícia.
- query.sparql: Query SPARQL a ser utilizada na execução do script final_transformation.py.
- results.ttl: Arquivo Turtle gerado ao rodar o script json_to_turtle.py.
- run_full_process.py: Script python que executa todo o processo necessário, facilitando os cenários em que queremos rodar tudo, pois evita ter que rodar cada etapa manualmente.
- transform.query: Query utilizada no json_to_turtle.py para gerar o arquivo Turtle sem a presença do prefixo jarql:

### Como rodar o processo todo

Como descrito acima na explicação dos arquivos, basta rodar o run_full_process.py tendo em mente que será utilizado o news.json como dataset inicial de notícias e o query.sparql como query SPARQL responsável por gerar nosso output final desejado. Esses dois arquivos finais, portanto, são de fácil manipulação e adaptação pelo usuário.

### Como rodar etapas individuais do processo

Os arquivos json_to_turtle.py e final_transformation.py também são possíveis de serem rodados, caso queiramos rodar apenas a primeira ou segunda etapa, respectivamente, do processo.
