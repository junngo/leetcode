import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website)

# Copy and read at clipboard
nfl_frame = pd.read_clipboard()
print(nfl_frame)
print(nfl_frame.columns)
print(nfl_frame.Rank)
print(nfl_frame['Won'])

