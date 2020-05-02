from flask import render_template, Flask
from Grapher import grapher, cleaner
from datetime import date, timedelta
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from waitress import serve

app = Flask(__name__)
#rudimentary security key
app.config['SECRET_KEY'] = '2e828bc1828af6a59a88af8247f13519a9f95e4c033fb603fecf5c483356915c621fe5565e7b95f53b0b2e28144d326a30283dabfd4999e071918edc6056372d'


#The form used within the requests, describing all the fields and including an input validator for the dates.
#The default dates are 1 year ago from today to today, and default stocks are FAANG.
class GraphForm(FlaskForm):
    yearago = date.today() - timedelta(days=365)
    startdate = DateField('Start Date',[DataRequired()], default=yearago)
    enddate = DateField('End Date',[DataRequired()], default=date.today)
    stocklist = StringField('Stock tickers', [DataRequired()], default="FB, AAPL, AMZN, NFLX, GOOG")
    submit = SubmitField('Submit')

    def validate_on_submit(self):
        result = super(GraphForm, self).validate()
        if (self.startdate.data > self.enddate.data):
            return False
        else:
            return result

#The one site used for receiving info and showing the graph.
@app.route('/' , methods=['GET','POST'])
def main():
    form = GraphForm()
    message = None
    if form.validate_on_submit():
        stockdata=cleaner(form.stocklist.data.split(","))
        htmlcode = grapher(stockdata, form.startdate.data, form.enddate.data)
        return render_template('main.html', form=form, htmlcode=htmlcode)
    return render_template('main.html', form=form, message=message)
                
if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=5000)