from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

class Figure():

    def __init__(self,df):
        self.df = df

    def create_graph(self):
        try:
            self.df["Start_String"]=self.df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S") # Converts datetime object into string for graph representation
            self.df["End_String"]=self.df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
        except AttributeError: # If object is not a datetime object, then it does nothing
            pass
        cds = ColumnDataSource(self.df) # Data source containing times the object entered and exited the frame

        fig = figure(x_axis_type='datetime',height=100,width=500,sizing_mode='scale_width',title="Motion Graph")
        fig.yaxis.minor_tick_line_color = None # Removes tickers from Y Axis
        fig.ygrid[0].ticker.desired_num_ticks=1 # Removes excessive cells from the grid

        hover = HoverTool(tooltips=[("Start","@Start_String"),("End","@End_String")]) # Implements hover functionality for further information
        fig.add_tools(hover)

        quadrant = fig.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)


        output_file("Graph.html")
        show(fig)
