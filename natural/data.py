try:
    from io import BytesIO
except ImportError:
    from cStringIO import StringIO as BytesIO
from natural.constant import PRINTABLE


def printable(sequence):
    '''
    Return a printable string from the input ``sequence``

    :param sequence: byte or string sequence
    '''
    return ''.join(map(lambda c: c if c in PRINTABLE else '.', sequence))


def hexdump(stream):
    '''
    Display stream contents in hexadecimal and ASCII format. The ``stream``
    specified must either be a file-like object that supports the ``read``
    method to receive bytes, or it can be a string.

    To dump a file::

        >>> hexdump(file(filename))

    Or to dump stdin::

        >>> import sys
        >>> hexdump(sys.stdin)

    :param stream: stream input
    '''

    if isinstance(stream, basestring):
        stream = BytesIO(stream)

    row = 0
    while True:
        data = stream.read(16)
        if not data:
            break

        hextets = data.encode('hex').ljust(32)
        canonical = printable(data)

        print '%08x %s  %s  |%s|' % (row * 16,
            ' '.join(hextets[x:x + 2] for x in xrange(0x00, 0x10, 2)),
            ' '.join(hextets[x:x + 2] for x in xrange(0x10, 0x20, 2)),
            canonical,
        )
        row += 1