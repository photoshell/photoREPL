from photorepl import app
from gi.repository import Gtk, GLib

class Preview(Gtk.Window):

    def __init__(self, show=True):
        super().__init__()
        GLib.set_application_name(app)
        self.set_wmclass(app, app)
        self.set_title(app)
        self.connect('delete-event', Gtk.main_quit)
        if show:
            self.show_all()
