from flask import Flask, request, jsonify
application = Flask(__name__)

# Map BIC onto project
MAPPER = {
    "BIC1": "projectA",
    "BIC2": "projectB",
    "BIC3": "projectC",
    "default": "default-project"
}

@application.route("/")
def hello():
    bic = request.args.get("bic", "")

    project = MAPPER.get(bic, MAPPER.get("default", ""))

    resp = {"version": 3, "status": "ok", "err": "", "bic": bic, "project": project}

    #return jsonify(resp)
    return resp

if __name__ == "__main__":
    application.run()
