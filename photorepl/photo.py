import os
import tempfile

from gi.repository import Gdk

from rawkit.options import Options
from rawkit.raw import Raw


class AutoUpdatingOptions(Options):

    """
    A set of options that update the photo when they are updated.
    """

    def __init__(self, attrs=None, photo=None):
        super().__init__(attrs=attrs)
        self.photo = photo

    def __setattr__(self, name, value):
        try:
            Options.__setattr__(self, name, value)
            self.update()
        except AttributeError:
            self.__dict__['name'] = value

    def update(self):
        """
        Updates the photo which contains these options.
        """

        if self.photo is not None:
            self.photo.update()


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
            self.update()
            self.show()

    def __setattr__(self, name, value):
        if name == 'options' and type(value) is Options:
            self.__dict__['options'] = AutoUpdatingOptions(
                attrs=dict(zip(
                    value.keys(),
                    value.values()
                )),
                photo=self
            )
            try:
                self.update()
            except AttributeError:
                pass
        else:
            Raw.__setattr__(self, name, value)

    def show(self):
        """
        Show the preview window.
        """

        Gdk.threads_enter()
        self.preview = self.ui_thread.open_window(
            self.tempfile,
            rawfile=self.filename
        )
        Gdk.threads_leave()

    def update(self):
        """
        Updates the photo on disk and in the preview pane.
        """

        self.save(filename=self.tempfile, filetype='ppm')
        try:
            Gdk.threads_enter()
            self.preview.render_photo(filename=self.tempfile)
        except AttributeError:
            pass
        finally:
            Gdk.threads_leave()

    def close(self):
        """
        Cleans up the underlying raw file and unlinks any temp files.
        """

        super().close()
        os.unlink(self.tempfile)
