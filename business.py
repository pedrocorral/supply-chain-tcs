
import pandas       as     pd
import numpy        as     np
from   scipy.stats  import norm

class Logic():

    σ0            = 0.35
    ss_cost0      = 11.37
    rush_cost0    = 15.13

    @staticmethod
    def generate_data(σ, ss_cost, rush_cost):
        # Generate SL values ranging from 0 to 1 (0% to 100%)
        sl        = np.arange(5000) * 0.0002 + 0.5

        ss_cost   = Logic.SS_cost(sl, σ, ss_cost)
        transport = Logic.rush_orders_cost(sl, rush_cost)

        T_cost    = transport + ss_cost
        min_value = np.nanmin(T_cost)
        min_index = np.nanargmin(T_cost)
        opt_sl    = sl[min_index]

        index_95  = 2250
        EV_opt    = T_cost[index_95] - T_cost[min_index]
        # print       (f"index_95 = {index_95}, min_index = {min_index}, indices = {sl.shape}")
        # print       (f"T_cost(95%) = {T_cost[index_95]}, opt_T_cost={T_cost[min_index]}")
        # Create a DataFrame from the generated values
        data      = pd.DataFrame({
            'SL':   sl,
            'TCS':  T_cost
        })
        return      data, opt_sl, EV_opt

    @staticmethod
    def rush_orders_cost(sl, cost):
        return      (50 - sl) * cost

    @staticmethod
    def SS(sl, σ):
        # Calculate the value for each SL
        z_values  = norm.ppf(sl)
        # Calculate the value for each SL
        SS        = z_values * σ
        return      SS

    @staticmethod
    def SS_cost(sl, σ, ss_cost):
        return      ss_cost * Logic.SS(sl, σ)
