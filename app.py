import streamlit         as st
import pandas            as pd
import matplotlib.pyplot as plt
import numpy             as np

import gui
import controller

class TCS:

    def __init__(self):
        self.data  = None
        self.gui   = gui.GUI()
        controller . show_GUI(self)

app = TCS()

