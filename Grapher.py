import pandas_datareader as dr
import pandas as pd
import plotly.graph_objects as go

def grapher(stocks, startdate, enddate):
    #Sources information from Yahoo Finance for stock + ticker
    def form(startdate,enddate):
        return(dr.DataReader(stocks,'yahoo',startdate,enddate)['Adj Close'])

    df=form(startdate,enddate)
    df=pd.DataFrame(df)
    df['DateTime']=df.index
    df.set_index('DateTime', inplace=True)
    df = df.round(decimals=2)

    #Creates the chart
    fig = go.Figure()
    for item in df:
        fig.add_trace(go.Scatter(x=df.index, y=df[item], name=item))

    fig.update_layout(hovermode='x unified', 
                      title = f'Adjusted Close Graph between {startdate} and {enddate}',
                      xaxis_title='Date',
                      yaxis_title='Adjusted Close')

    fig.update_yaxes(tickprefix="$")

    return(fig.to_html())

#Formula used to clean the stocklist to make it parseable by the grapher function
def cleaner(dirty):
    new = []
    for item in dirty:
        new.append(item.strip(' '))
    return(new)
    





