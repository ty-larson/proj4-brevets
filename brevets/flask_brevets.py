"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)
"""

import flask
from flask import request
import arrow
import acp_times
import config
import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

###
# Pages
###

@app.route("/")
@app.route("/index")
def index():
    """
    Renders the main calculator page.
    """
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')

@app.errorhandler(404)
def page_not_found(error):
    """
    Renders a 404 error page.
    """
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404

###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects km, brevet_dist, and start_time as URL-encoded arguments.
    """
    app.logger.debug("Got a JSON request")
    
    # Extract arguments from the request
    km = request.args.get('km', 0, type=float)
    brevet_dist = request.args.get('brevet_dist', 200, type=int)
    start_time = request.args.get('start_time', type=str)

    app.logger.debug("km={}, brevet_dist={}, start_time={}".format(km, brevet_dist, start_time))
    
    # Perform the calculations using our logic module
    open_t = acp_times.open_time(km, brevet_dist, start_time)
    close_t = acp_times.close_time(km, brevet_dist, start_time)
    
    result = {"open": open_t, "close": close_t}
    return flask.jsonify(result=result)

#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")