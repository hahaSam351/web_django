from django.shortcuts import render
import pandas as pd


# Create your views here.
def vis_df(request) :
    # df = pd.read_csv('./data_time.csv')
    # context = {'df':df}
    # return render(request, 'test1/vis_df.html', context)
    return render(request, 'test1/vis_df.html')