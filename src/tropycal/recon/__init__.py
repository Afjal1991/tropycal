r"""Functionality for reading and analyzing recon data."""
print("in recon")
from .dataset import ReconDataset

import sys
if 'sphinx' not in sys.modules:
    from .plot import ReconPlot