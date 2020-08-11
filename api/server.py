from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


class AuthorTexts(Resource):

    def get(self, author_name):
        dataset = get_json()
        question_from_author = {}
        authors_texts = filter(lambda x:x["author"]==author_name, dataset)
        for author_text in authors_texts:
            question_from_author['pergunta'] = author_text['text']
        return question_from_author
            


def get_json():
    json_url = '../scrap_stackoverflow/scrap_stackoverflow/spiders/stackoverflow_result.json'
    with open(json_url) as json_file:
        dataset = json.load(json_file)
    return dataset


api.add_resource(AuthorTexts, '/authortexts/<author_name>/')

if __name__ == "__main__":
    app.run(debug=True)