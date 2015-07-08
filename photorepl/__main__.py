#!/usr/bin/env python

import atexit
import photorepl
import sys
import threading

try:
    import pgi
    pgi.install_as_gi()
except ImportError:
    pass

from gi.repository import GLib
from photorepl.threads import UIThread
from .photo import Photo


def edit(filename):
    """
    Opens the given filename and spawns a preview window.
    """
    global ui_thread
    return Photo(filename=filename, ui_thread=ui_thread)


if __name__ == '__main__':
    GLib.set_application_name(photorepl.app_name)

    import libraw

    import rawkit
    from rawkit.options import Options
    from rawkit.options import WhiteBalance
    from rawkit.raw import Raw

    # Launch the UI on start if we specify something to open.
    ui_thread = UIThread()
    ui_thread.start()

    if len(sys.argv) > 1:
        photos = [edit(arg) for arg in sys.argv[1:]]

    print("""
    Good morning (UGT)! Welcome to photoREPL, an experimental interface for raw
    photo editing from the command line with `rawkit'.

    The following packages, modules, and classes are imported for you (among
    others):

        libraw

        photorepl
        photorepl.photo.Photo

        rawkit
        rawkit.options.Options
        rawkit.options.WhiteBalance
        rawkit.raw.Raw

    The following functions are also available:

        edit(filename)

    For help, use the `help()' function, eg. `help(Photo)'.
    """)

    if len(sys.argv) == 1:
        print("""
    To get started, why not try opening a photo with:

        myphoto = edit(filename=somephoto)
        """)
    elif len(sys.argv) == 2:
        print("The file `{}' is available as photos[0].".format(
            sys.argv[1]))
    elif len(sys.argv) > 2:
        print("The files {} are available in the photos[] array.".format(
            sys.argv[1:]))

    @atexit.register
    def on_exit():
        print("""
        Goodbye. If photoREPL immediately exited, be sure you're running
        photoREPL with `python -i -m photorepl' so that it can fall back to a
        prompt.
        """)
