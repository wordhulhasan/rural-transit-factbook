"""Application entry point."""

__author__ = "Ali Rahim-Taleqani"
__copyright__ = "Copyright 2020, The SGR Project"
__credits__ = ["Dilip Mistry"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Dilip Mistry"
__email__ = "dilip dot mistry at ndsu dot edu"
__status__ = "Development"

from flaskapp import init_app

app = init_app()

if __name__ == "__main__":
    app.run()
