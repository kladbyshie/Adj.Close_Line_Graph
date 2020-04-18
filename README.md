# Adj.Close_Stock_Grapher

Adjusted close grapher, making a line graph of the stock and time period selected. There are 3 core iterations of the same concept;

Version 1 (Adj.Close_Line_Graph):
* Can only handle one stock at a time. I couldn't think of a good way to create dynamically assigned colors to however many stocks would be queued up, and decided to only give it one-stock functionality.

Version 2 (Adj.Close_Line_Graph_Multi):
* Can handle an expandable multitude of stocks, separated by commas. This is the main thing I wanted to update from Version 1, since comparing multiple stocks is incredibly useful. I figured out how to use a color generator to assign colors dynamically, and the legend also works well. This has the full "core" functionality.

Version 3 (FlaskAdj.Close):
* Contains a Flask web app GUI. This was my first foray into creating Flask interfaces (I previously used TKinter but I wanted something a bit more modern). It uses Flask-wtforms for input validation. 

The code features the following:
* Pandas Datareader, used to source stock data from Yahoo Finance for the stock and date period selected.
* Bokeh, used to graph the stock data from Yahoo Finance.
* Flask, used to create an easy-to-use interface.
* Flask-wtforms, used to create forms and basic input validation.
