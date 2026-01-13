from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError
from models import Session, Advertisement
from errors import HttpError
from schema import CreateAdvertRequest, UpdateAdvertRequest, validate

app = Flask(__name__)


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(response):
    request.session.close()
    return response


@app.errorhandler(HttpError)
def error_handler(err: HttpError):
    http_response = jsonify({'error': err.message})
    http_response.status_code = err.status_code
    return http_response


def get_advert_by_id(advert_id: int) -> Advertisement:
    advert = request.session.get(Advertisement, advert_id)
    if advert is None:
        raise HttpError(404, 'Advertisement not found')
    return advert


def add_advert(advert: Advertisement) -> None:
    try:
        request.session.add(advert)
        request.session.commit()
    except IntegrityError:
        raise HttpError(409, 'Advert already exists')


class AdvertView(MethodView):

    def get(self, advert_id):
        advert = get_advert_by_id(advert_id)
        return jsonify(advert.convert_json)


    def post(self):
        json_data = validate(CreateAdvertRequest, request.json)
        advert = Advertisement(
            title=json_data['title'],
            author=json_data['author'],
        )
        add_advert(advert)
        return jsonify(advert.convert_json)


    def patch(self, advert_id):
        json_data = validate(UpdateAdvertRequest, request.json)
        advert = get_advert_by_id(advert_id)
        if 'title' in json_data:
            advert.title = json_data['title']
        if 'author' in json_data:
            advert.author = json_data['author']
        add_advert(advert)
        return jsonify(advert.id_json)


    def delete(self, advert_id:int):
        advert = get_advert_by_id(advert_id)
        request.session.delete(advert)
        request.session.commit()
        return jsonify({'message': 'Advertisement deleted'})


advert_view = AdvertView.as_view('advert_view')

app.add_url_rule('/all_advertisements/', view_func=advert_view, methods=['POST'])

app.add_url_rule(
    '/all_advertisements/<int:advert_id>',
    view_func=advert_view,
    methods=['GET', 'PATCH', 'DELETE']
)



if __name__ == '__main__':
    app.run()
    