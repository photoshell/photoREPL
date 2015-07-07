from photorepl import app_name
from gi.repository import Gtk


class Preview(Gtk.Window):

    """
    The preview window, which shows photos as you edit them.
    """

    def __init__(self, photo=None, show=True):
        super().__init__()

        self.set_wmclass(app_name, app_name)
        self.set_title(app_name)

        if show:
            self.show_all()
