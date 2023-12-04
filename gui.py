
import streamlit         as     st
import matplotlib.pyplot as     plt
import matplotlib.ticker as mticker

import business

class GUI:

    def __init__(self):
        self.ss_cost     = None
        self.σ           = None

    def call_controler(self):
        self.on_change     (self.σ, self.ss_cost)

    def setup_controls(self):
        # Input for SS_cost
        self.ss_cost     = st.sidebar.slider(
            "Safety Stock Cost (€)", 
            min_value    = 0.0,
            max_value    = 100.0,
            value        = business.Logic.ss_cost0, 
            step         = 0.01,
            format       = "%f€"
        )

        self.rush_cost   = st.sidebar.slider(
            "(Rush) Transport Cost (€)",  
            min_value    = 0.0,
            max_value    = 100.0,
            value        = business.Logic.rush_cost0,
            step         = 0.01,
            format       = "%f€"
        )

        self.σ           = st.sidebar.slider(
            "Forecast error/demand variability (σ as %)", 
            min_value    = 0.0,
            max_value    = 200.0,
            value        = 100 * business.Logic.σ0,
            step         = 0.01,
            format       = "%.2f%%"
        ) / 100

    def show_data(self, data, opt_sl):
        # Plotting the data
        fig, ax          = plt.subplots()            

        ax.plot            (data['SL'], data['TCS'])
        ax.set_xlabel      ('Inventory\'s Service Level')
        ax.set_ylabel      ('Total Cost to Serve (€)')
        ax.set_title       ('Total Cost to Serve per Service Level')

        # Formatting the x-axis as percentage
        ax.xaxis         . set_major_formatter(mticker.PercentFormatter(xmax=1.0))
        # Formatting the y-axis as Euros
        euro_formatter   = mticker.FuncFormatter(lambda x, pos: f'{x:.2f}€')
        ax.yaxis         . set_major_formatter(euro_formatter)

        # Add a dashed vertical line
        ax.axvline         (x = opt_sl, color = 'green', lw = 1,
                            linestyle = '--', label = '{100 * opt_sl:.1f}% SL')

        st.pyplot          (fig)

    def show(self, data, opt_sl, EV_opt):
        st.title           (f"Opt. Empirical Value: {EV_opt:.1f}€\nOptimal Service Level: {100 * opt_sl:.1f}%\nΔSL = {100 * (opt_sl - 0.95):.1f}%")
        self.show_data     (data, opt_sl)
