import sys

def help(*args, **kargs):
    print("help() not implemented in this environment", file=sys.stderr)


def _assert_equal(want, got):
    if want != got:
        print("assert_equal failed: want:\n\t{!r}\ngot:\n\t{!r}".format(want, got), file=sys.stderr)


def _assert_raises(errtype, call, *args, **kargs):
    try:
        call(*args, **kargs)
        print("assert_raises failed: no exception thrown, {} expected".format(errtype), file=sys.stderr)
    except Exception as e:
        if not isinstance(e, errtype):
            print("assert_raises failed: want error type {!r}, got\n{}".format(errtype, e), file=sys.stderr)
        return

