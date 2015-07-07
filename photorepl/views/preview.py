from photorepl import app_name
from gi.repository import Gtk


class Preview(Gtk.Window):

    """
    The preview window, which shows photos as you edit them.
    """

    def __init__(self, show=True):
        super().__init__()

        self.set_wmclass(app_name, app_name)
        self.set_title(app_name)

        self.connect('delete-event', Gtk.main_quit)
        if show:
            self.show_all()
