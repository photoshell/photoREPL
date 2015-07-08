import os

from gi.repository import Gtk, GdkPixbuf
from photorepl import app_name
from threading import Lock


class Preview(Gtk.Window):

    """
    The preview window, which shows photos as you edit them.
    """

    def __init__(self, filename=None, rawfile=None, show=True):
        super().__init__()

        self.set_wmclass(app_name, app_name)
        self.rawfile = rawfile
        self.set_title(app_name)
        self.set_default_size(800, 600)

        self.settings = Gtk.Settings.get_default()

        try:
            self.settings.set_property(
                'gtk-application-prefer-dark-theme',
                True
            )
        except TypeError:
            # Can't do this if we're using pgi for some reason.
            pass

        self.box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)

        self.mutex = Lock()

        if filename is not None:
            self.render_photo(filename)

        self.add(self.box)

        if show:
            self.show_all()

    def set_title(self, title):
        """
        Sets the title of the preview window.
        """

        if self.rawfile is None:
            super().set_title(title)
        else:
            super().set_title('{} — {}'.format(
                title,
                os.path.basename(self.rawfile)
            ))

    def render_photo(self, filename):
        """
        Renders the given photo (generally in PGM format) in the preview
        window.
        """

        self.mutex.acquire()

        self.set_title(app_name)

        try:
            self.box.remove(self.image)
        except AttributeError:
            pass

        pix = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename, 800, -1, True)
        self.image = Gtk.Image.new_from_pixbuf(pix)
        self.box.pack_start(self.image, True, True, 0)
        self.show_all()

        self.mutex.release()
