import pandas_datareader as dr
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, LabelSet, HoverTool
from bokeh.resources import INLINE

#Select stock (singular ticker) and time period here:
stock='AAPL'
startdate='2019/01/01'
enddate='2020/01/01'

#Sources information from Yahoo Finance for stock + ticker
def form(startdate,enddate):
    return(dr.DataReader(stock,'yahoo',startdate,enddate)['Adj Close'])

df=form(startdate,enddate)

#Chart + hover tool generated here
cds = ColumnDataSource(dict(DateTime=df.index,
                       val=df))

f=figure(title=f'{stock} Adjusted Close Graph between {startdate} and {enddate}', x_axis_type="datetime")
f.xaxis.axis_label = 'Date'
f.yaxis.axis_label = 'Adj. Close'

f.line(x='DateTime',y='val', color='green', line_width=2, source=cds)

hover=HoverTool(tooltips=[('Date: ', '@DateTime{%F}'),
                          ("Adj. Close: ","$@{val}{0.2f}")],
          formatters={'@DateTime': 'datetime',
                      'Adj. Close' : 'printf'},
               mode='vline')

f.add_tools(hover)

output_file(f'{stock}.html', mode="inline")

show(f)