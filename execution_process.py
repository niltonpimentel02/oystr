import jsonschema
import requests
from decouple import config
from flask import request, Response
from flask_jsonschema_validator import JSONSchemaValidator


def routes(app):
    JSONSchemaValidator(app=app, root="schemas")

    @app.route('/notification', methods=['POST'])
    @app.validate('execution_process_validation_fields', 'execution_process')
    def post_webhook():
        evt = request.json['evt']
        bot = request.json['bot']
        execution = request.json['execution']
        if evt == 'ExecutionFinishedWithError':
            message = f"[{evt} - {bot}] a execução {execution} terminou com erros."
        else:
            message = f"[{evt} - {bot}] a execução {execution} terminou com sucesso."
        requests.post(config('WEBHOOK_SITE', default='https://webhook.site/115e0920-2466-4523-a6ac-c514bb3ac0c1'),
                      data=message)
        return message

    @app.errorhandler(jsonschema.ValidationError)
    def onValidationError(e):
        return Response("There was a validation error: " + str(e), 400)
