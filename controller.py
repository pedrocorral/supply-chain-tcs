
import business

def show_GUI(tcs):
    tcs.gui  . setup_controls()
    (data,
     opt_sl,
     EV_opt) = business.Logic.generate_data(tcs.gui.σ,
                                            tcs.gui.ss_cost,
                                            tcs.gui.rush_cost)
    tcs.gui  . show(data, opt_sl, EV_opt)
