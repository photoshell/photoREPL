import os
import tempfile

from gi.repository import Gdk
from rawkit.raw import Raw


class Photo(Raw):

    """
    A photo comprises a raw file which can be edited and will update the
    associated preview window (if any).
    """

    def __init__(self, filename=None, ui_thread=None):
        super().__init__(filename=filename)

        (self.fhandle, self.tempfile) = tempfile.mkstemp()
        self.filename = filename
        self.ui_thread = ui_thread

        if self.ui_thread is not None:
            Gdk.threads_enter()
            self.ui_thread.open_window()
            Gdk.threads_leave()

    def update(self):
        """
        Updates the photo on disk and in the preview pane.
        """

        self.save(filename=self.tempfile, filetype='ppm')

    def close(self):
        """
        Cleans up the underlying raw file and unlinks any temp files.
        """

        super().close()
        os.unlink(self.tempfile)
