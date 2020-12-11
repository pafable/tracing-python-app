from myapp import models, app
import setup

app.run(debug=False, threaded=True, port=8080)