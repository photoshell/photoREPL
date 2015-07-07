#!/usr/bin/env python

import atexit
import threading

from gi.repository import Gtk
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
        self.daemon=True

    def run(self):
        """
        Create the preview window and run the Gtk main loop when the UI thead
        is started.
        """
        self.preview = Preview(show=True)
        Gtk.main()


def preview():
    """
    Sets up the global state for the UI Thread and starts it if it doesn't
    exist, and if it does starts it if it's not started.
    """

    # Launch the UI on start
    ui_thread = UIThread()
    ui_thread.start()
    return ui_thread




if __name__ == '__main__':
    print("""
    Welcome to photoREPL, an experimental interface for raw photo editing from
    the command line with rawkit.

    The following packages, modules, and classes are imported for you:

        libraw

        rawkit
        rawkit.options.Options
        rawkit.options.WhiteBalance
        rawkit.raw.Raw

    The following functions are also available:

        preview() — Opens the preview window if you've closed it.
    """)

    import libraw

    import rawkit
    from rawkit.options import Options
    from rawkit.options import WhiteBalance
    from rawkit.raw import Raw

    ui_thead = preview()

    @atexit.register
    def on_exit():
        print("""
        Goodbye. If photoREPL immediately exited, be sure you're running
        photoREPL with `python -i -m photorepl' so that it can fall back to a
        prompt.
        """)
