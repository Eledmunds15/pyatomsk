import pyatomsk

# ---------------------------
# Test for import pyatomsk
# ---------------------------
def test_import_pyatomsk():
    assert pyatomsk is not None

# ---------------------------
# Test for atomsk version
# ---------------------------
def test_version():
    pyatomsk.version()