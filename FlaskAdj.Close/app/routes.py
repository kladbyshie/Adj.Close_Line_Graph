from flask import render_template, Flask
from Grapher import grapher, cleaner
from datetime import date, timedelta
from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
#In an app hosted on a site, this would be in a separate config file, and likely generated for each website instance.
app.config['SECRET_KEY'] = 'h1j3ch184yv12893ujcop2ije92p18h4v1892j'

#The form used within the requests, describing all the fields and including an input validator for the dates.
#The default dates are 1 year ago from today to today, and default stocks are FAANG.
class GraphForm(FlaskForm):
    yearago = date.today() - timedelta(days=365)
    startdate = DateField('Start Date',[DataRequired()], default=yearago)
    enddate = DateField('End Date',[DataRequired()], default=date.today)
    stocklist = StringField('Stocks', [DataRequired()], default="FB, AAPL, AMZN, NFLX, GOOG")
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
        stocklist=cleaner(form.stocklist.data.split(","))
        val = grapher(form.startdate.data, form.enddate.data, stocklist)
        script = val[0]
        div1 = val[1]
        cdn_js = val[2]
        return render_template('main.html', script=script, div1=div1, cdn_js=cdn_js, form=form)
    return render_template('main.html', form=form, message=message)
                
if __name__ == '__main__':
    app.run(debug=True, port=5000)