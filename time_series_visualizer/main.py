import time
import os
import time_series_visualizer as tsv

fig1 = tsv.draw_line_plot()
print("Saved line_plot.png")
time.sleep(0.2)

fig2 = tsv.draw_bar_plot()
print("Saved bar_plot.png")
time.sleep(0.2)

fig3 = tsv.draw_box_plot()
print("Saved box_plot.png")
time.sleep(0.2)

try:
    for fname in ('line_plot.png','bar_plot.png','box_plot.png'):
        if os.path.exists(fname):
            print(f"Opening {fname}")
            os.startfile(fname)
except Exception:
    pass
