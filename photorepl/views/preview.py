from threading import Lock

from photorepl import app_name
from gi.repository import Gtk, GdkPixbuf


class Preview(Gtk.Window):

    """
    The preview window, which shows photos as you edit them.
    """

    def __init__(self, filename=None, show=True):
        super().__init__()

        self.set_wmclass(app_name, app_name)
        self.set_title(app_name)
        self.set_default_size(800, 600)

        self.settings = Gtk.Settings.get_default()
        self.settings.set_property('gtk-application-prefer-dark-theme', True)

        self.box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 0)

        self.mutex = Lock()

        if filename is not None:
            self.render_photo(filename)

        self.add(self.box)

        if show:
            self.show_all()

    def render_photo(self, filename):
        self.mutex.acquire()

        try:
            self.box.remove(self.image)
        except AttributeError:
            pass

        pix = GdkPixbuf.Pixbuf.new_from_file_at_scale(filename, 800, -1, True)
        print(pix)
        self.image = Gtk.Image.new_from_pixbuf(pix)
        self.box.pack_start(self.image, True, True, 0)

        self.mutex.release()
