import threading

from gi.repository import Gtk, Gdk
from photorepl.views.preview import Preview


class UIThread(threading.Thread):

    """
    A thread for displaying UI elements and photos. This thread shouldn't
    maintain any state which must be preserved, and should act as a daemon
    thread which exits when the main thread (the REPL) is terminated.
    """

    def __init__(self):
        """
        Initialize the ui thead, making sure it's a daemon thread which will
        exit when the main thread is terminated.
        """

        super(UIThread, self).__init__()
        self.daemon = True

    def run(self):
        """
        Create the preview window and run the Gtk main loop when the UI thead
        is started.
        """
        Gdk.threads_init()

        Gdk.threads_enter()
        Gtk.main()
        Gdk.threads_leave()

    def open_window(self, filename=None, rawfile=None):
        """
        Open a new preview window with the given preview file and raw file.
        """
        return Preview(filename=filename, rawfile=rawfile, show=True)
