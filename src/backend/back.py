import os
import time
from flask import Flask, jsonify, request
import bleach
import requests

app = Flask(__name__)


@app.route('/messages', methods=['GET'])
def get_messages():
    return "hello get", 201


@app.route('/forks/<from_workspace>/<from_repo_slug>/<access_token>/<to_workspace>/<to_repo_slug>/<app_ref>/<location>/<name>/<environment>/<owner>/<admins>', methods=['POST'])
def forks_repo(from_workspace, from_repo_slug, access_token, to_workspace, to_repo_slug, app_ref, location, name, environment, owner, admins):
    url = 'https://api.bitbucket.org/2.0/repositories/' + \
        from_workspace + '/' + from_repo_slug + '/forks'

    payload = "{\n \"name\": \""+to_repo_slug + \
        "\",\n \"workspace\": {\n \"slug\": \"" + \
        to_workspace+"\"\n }\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer' + access_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))

    return jsonify(app_ref=app_ref,
                   location=location,
                   name=name,
                   environment=environment,
                   owner=owner,
                   admins=admins)


@app.route('/pullrequests/<from_workspace>/<from_repo_slug>/<from_branch>/<access_token>/<to_branch>/<title>', methods=['POST'])
def pullrequests_repo(from_workspace, from_repo_slug, from_branch, access_token, to_branch, title):
    url = 'https://api.bitbucket.org/2.0/repositories/' + \
        from_workspace + '/' + from_repo_slug + '/pullrequests'

    payload = "{\n \"title\": \""+title+"\",\n    \"source\": {\n \"branch\": {\n \"name\": \""+from_branch + \
        "\"\n }\n },\n \"destination\": {\n  \"branch\": {\n \"name\": \"" + \
        to_branch+"\"\n }\n }\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer' + access_token
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text.encode('utf8'))

    return "Successful PR", 201


if __name__ == '__main__':
    # start Flask server
    # Flask's debug mode is unrelated to ptvsd debugger used by Cloud Code
    app.run(debug=False, port=os.environ.get('PORT'), host='0.0.0.0')
