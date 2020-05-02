import pandas_datareader as dr
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.resources import INLINE, CDN
from bokeh.palettes import Category10
from bokeh.embed import components
import itertools

def grapher(startdate, enddate, stocks):
    #Sources information from Yahoo Finance for stock + ticker
    df = dr.DataReader(stocks,'yahoo',startdate,enddate)['Adj Close']
    df['DateTime']=df.index
    df.set_index('DateTime', inplace=True)

    #Generates colors from the Category10 list from the bokeh.palettes library (for the chart)
    def color_gen():
        yield from itertools.cycle(Category10[10])
    color = color_gen()

    #chart + hover tool generated here
    cds = ColumnDataSource(df)

    f=figure(title=f'Adjusted Close Graph between {startdate} and {enddate}', x_axis_type="datetime", sizing_mode='stretch_both')
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

    script, div1 = components(f)
    cdn_js = CDN.js_files[0]
    
    #Returns the parts necessary to generate a Bokeh chart.
    return[script, div1, cdn_js]

#Formula used to clean the stocklist to make it parseable by the grapher function
def cleaner(dirty):
    new = []
    for item in dirty:
        new.append(item.strip(" "))
    return(new)
    





