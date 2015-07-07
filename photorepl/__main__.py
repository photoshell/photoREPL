#!/usr/bin/env python

import atexit
import photorepl
import threading

from gi.repository import Gtk, GLib

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
        self.windows = []

    def run(self):
        """
        Create the preview window and run the Gtk main loop when the UI thead
        is started.
        """
        self.open_window()
        Gtk.main()

    def open_window(self, photo=None):
        """
        Open a preview window.
        """
        self.windows.append(Preview(photo=photo, show=True))


def edit(photo=None):
    """
    Open a preview window.
    """
    global ui_thread
    ui_thread.open_window(photo)


if __name__ == '__main__':
    GLib.set_application_name(photorepl.app_name)

    import libraw

    import rawkit
    from rawkit.options import Options
    from rawkit.options import WhiteBalance
    from rawkit.raw import Raw

    # Launch the UI on start
    ui_thread = UIThread()
    ui_thread.start()

    print("""
    Good morning (UGT)! Welcome to photoREPL, an experimental interface for raw
    photo editing from the command line with `rawkit`.

    The following packages, modules, and classes are imported for you:

        libraw

        rawkit
        rawkit.options.Options
        rawkit.options.WhiteBalance
        rawkit.raw.Raw

    The following functions are also available:

        edit(photo=None) — Opens the preview window, editing the given file path or an existing photo.
    """)

    @atexit.register
    def on_exit():
        print("""
        Goodbye. If photoREPL immediately exited, be sure you're running
        photoREPL with `python -i -m photorepl' so that it can fall back to a
        prompt.
        """)
