# Adj.Close_Stock_Grapher

Adjusted close grapher, making a line graph of the stock and time period selected, and then exporting the file as a portable HTML file (named stockname.html). The graph includes a Hover Tool showing date and adj.close, making it easy to check the info. I included an HTML showing how the graph output looks like.

The code features the following:
* Pandas Datareader, used to source stock data from Yahoo Finance for the stock and date period selected.
* Bokeh, used to graph the stock data from Yahoo Finance

Room for growth:
* Multiple stock input. Easily the most useful addition I can think of, and using a for loop to graph a line for each stock in the list would not be tricky. The tricky part is making the ColumnDataSource to be flexible enough to accept whatever the list of stocks is (ie. if user adds 5 stocks, the ColumnDataSource should automatically pull the info for the 5 stocks from the df that PandasDatareader generates, so that the for loop making the lines can easily pull info from there).There's definitely some sort of workaround there, just need to research it more.
* GUI? Making a TKinter GUI (or even a Flask interface) wouldn't be too bad of an idea, but the app is already so easy to use that I'm not sure if it would be worth it.
