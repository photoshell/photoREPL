version = '0.0.1'
app_name = 'photoREPL'

try:
    import pgi
    pgi.install_as_gi()
except ImportError:
    pass
