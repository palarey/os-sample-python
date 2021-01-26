from flask import Flask, request
application = Flask(__name__)

@application.route("/")
def hello():
    bic = request.args.get("bic", "<none>")
    return "Hello New/Modified World! bic: {}".format(bic)

if __name__ == "__main__":
    application.run()
