from flask import Flask
from housing.logger import logging

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    logging.info("We are testing logging module")
    return "Updated to test CI/CD pipeline"


if __name__=="__main__":
    app.run(debug=True)
