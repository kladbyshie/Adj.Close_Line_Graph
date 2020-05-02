# Adj.Close_Stock_Grapher
Currently hosted on https://adjcloseapp.herokuapp.com/

Adjusted close grapher, making a line graph of the stock and time period selected. There are 4 core iterations of the same concept;

CURRENT: Version 4, master branch:
* The code has been updated to use Plotly instead of Bokeh , which has cut down most of the code bulk and also includes the unified hover tool that was desired for the past 3 iterations. This has retained the same Flask web app GUI from version 3. Additionally, it has a Procfile, for Heroku hosting. 

Version 3, FlaskAdj.Close branch:
* Contains a Flask web app GUI. This was my first foray into creating Flask interfaces (I previously used TKinter but I wanted something a bit more modern). It uses Flask-wtforms for input validation. The only remaining issue is no unified hover tool.

Version 2, old branch (Multi):
* Can handle an expandable multitude of stocks, separated by commas. This is the main thing I wanted to update from Version 1, since comparing multiple stocks is incredibly useful. I figured out how to use a color generator to assign colors dynamically, and the legend also works well. This has the full "core" functionality.

Version 1, old branch :
* Can only handle one stock at a time. I couldn't think of a good way to create dynamically assigned colors to however many stocks would be queued up, and decided to only give it one-stock functionality.




