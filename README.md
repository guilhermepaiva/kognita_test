# kognita_test
Scrap do Stackoverflow usando scrapy.

## Primeiros passos
Antes de tudo, é preciso instalar as dependências do projeto.


``` pip install -r requirements.txt ```

## Coleta dos dados
Nesse momento, o sistema faz uma busca na página inicial utilizando o termo *python*. Para realizar o scrap se posicione dentro da pasta *spiders* no seguinte caminho:
```kognita_test/scrap_stackoverflow/scrap_stackoverflow/spiders``` e rode o seguinte comando:
```scrapy runspider stackoverflow.py -o stackoverflow_result.json```

O resultado da busca é um arquivo chamado *stackoverflow_result.json*. Um exemplo de parte desse arquivo pode ser visto abaixo:
```
[
    {
        "title": "Adding write.writerow to a Selenium Script resulted in not every row has quotation mark",
        "text": "so I use this GitHub Repo to mine Youtube comments. Then I added the following code so that the result would automatically be stored in a CSV file.But the in the CSV file Any solutions?",
        "author": "Fawwaz Zaini Ahmad",
        "date": "2020-08-11 13:19:16Z",
        "tags": [
            "python",
            "selenium"
        ]
    },
    {
        "title": "Loop and Melt over multiple columns in python? [duplicate]",
        "text": "See picture attached for what I'm trying to accomplish. I have no problem melting over one column, but as soon as I try to loop, it breaks.Get an error that Data needs to be 1-dimensional.",
        "author": "chicagobeast12",
        "date": "2020-08-11 12:44:29Z",
        "tags": [
            "python",
            "pandas"
        ]
    },
```
## Disponibilização dos dados por meio de uma API

Os dados coletados podem ser acessados por meio de uma API. Essa API possui apenas um *endpoint* GET e recebe como parâmetro o nome do autor do post.

Para acessar, é preciso entrar na pasta chamada *api* no seguinte caminho ```kognita_test/api``` e então rodar o seguinte comando:
``` python server.py```.

Com o servidor em funcionamento, acesse um *endpoint* no browser utilizando o seguinte padrão de url ```http://localhost:5000/authortexts/<nomedoautor>/``` onde o ```<nomedoautor>``` é o nome de algum autor que foi coletado na etapa anterior.

Por exemplo, vamos acessar as perguntas feitas pelo autor chamado *Giles*. A consulta deve ser feita na url ```http://localhost:5000/authortexts/Giles/``` e o resultado obtido pode ser visto abaixo:
```
{
    "pergunta": "I want to filter a dataframe after having done a group by on it but am getting a keyerror, here is some example code:I want to avoid using reset_index as in the final code I will have several dataframes of similar shape that I will be aggregating/merging/concatenating.I am sure I must be missing something obvious.How can I use the column names to filter the grouped dataframe?Thanks."
}
```
## Pontos que ainda precisam ser feitos:
* Coleta de dados
  * Coletar as respostas para as perguntas;
  * Coletar os comentários da pergunta e os comentários da(s) resposta(s).
  * Caso os comentários de uma pergunta/resposta tenham que ser expandidos (show # more comments), estes também devem ser coletados.
  
* Disponibilização dos dados por meio de uma API
  * Retornar as respostas e os comentários feitos pelo autor.

