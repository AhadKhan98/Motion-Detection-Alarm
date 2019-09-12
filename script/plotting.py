from bokeh.plotting import figure, show, output_file
import pandas

class Figure():

    def __init__(self,df):
        self.df = df

    def create_graph(self):
        fig = figure(x_axis_type='datetime',height=100,width=500,sizing_mode='scale_width',title="Motion Graph")
        fig.yaxis.minor_tick_line_color = None # Removes tickers from Y Axis
        fig.ygrid[0].ticker.desired_num_ticks=1
        quadrant = fig.quad(left=self.df["Start"],right=self.df["End"],bottom=0,top=1,color="green")
        output_file("Graph.html")
        show(fig)
