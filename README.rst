photoREPL
=========

``photoREPL`` is an experimental UI build around the rawkit_ (docs_) raw photo
editing library for Python.

photoREPL drops you at a Python prompt, with a few custom functions and a copy
of rawkit imported, and spawns a preview window for any photos you edit. As you
make changes to your photos, the image in the preview window is updated to
reflect those changes, giving you near real time editing directly from Python
without a lot of extra update calls!

To run try: ::

    make run

or run it directly: ::

    python -i -m photorepl [some_raw_photos]

you can also install it via pip: ::

    pip install photorepl

.. _rawkit: https://github.com/photoshell/rawkit
.. _docs: https://rawkit.readthedocs.org/
