"""A module for visualization with tensorboard
"""

from .record_writer import RecordWriter
from .record_reader import RecordReader
from .torchvis import TorchVis
from .writer import FileWriter, SummaryWriter
from .reader import SummaryReader
from .global_writer import GlobalSummaryWriter
__version__ = "dev"
# will be overwritten if run setup.py
# specifically, `python setup.py install` creates [version in setup.py + git SHA hash]
# python setup.py sdist creates a decimal version number
