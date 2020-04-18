import pandas_datareader as dr
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.resources import INLINE
from bokeh.palettes import Category10
import itertools

#Select stocks and time period here:
stocks=['FB','AAPL','AMZN','NFLX','GOOG']
startdate='2019/01/01'
enddate='2020/01/01'

#Sources information from Yahoo Finance for stock + ticker
def form(startdate,enddate):
    return(dr.DataReader(stocks,'yahoo',startdate,enddate)['Adj Close'])

df=form(startdate,enddate)
df['DateTime']=df.index
df.set_index('DateTime', inplace=True)
print(df.head())

#Generates colors from the Category10 list from the bokeh.palettes library (for the chart)
def color_gen():
    yield from itertools.cycle(Category10[10])
color = color_gen()

#chart + hover tool generated here
cds = ColumnDataSource(df)

f=figure(title=f'Adjusted Close Graph between {startdate} and {enddate}', x_axis_type="datetime")
f.xaxis.axis_label = 'Date'
f.yaxis.axis_label = 'Adj. Close'

for item, color in zip(stocks, color_gen()):
    f.line(x='DateTime', y=item, color=color, line_width=2, source=cds, legend_label=item)

tooltips = [('Date: ', '@DateTime{%F}')]
for item in stocks:
    tooltips.append((f'{item} adj. close: ', (f'@{item}' + '{$0.2f}')))
    
hover=HoverTool(tooltips=tooltips,
          formatters={'@DateTime': 'datetime'})

f.legend.location = "top_left"
f.legend.click_policy="hide"
f.add_tools(hover)

#output file is generated here
output_file(f'{stocks}.html', mode="inline")

show(f)