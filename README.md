# web-accessibility-analyzer

## DESCRIPTION:
    Welcome to this prototype for analyzing website accessibility!
    This script will use webscraping to analyze the DOM of a given site.
    It will consider the following criteria:
        1. Whether or not the <html> tag includes the 'lan' attribute (for translating screen readers)
        2. Whether or not headings [any <h1>...<h6>] are included in content (for screen reader organization)
        3. Whether or not all included images have alt text (also screen readers/visually impaired)
    Enter a URL to see the results of this analysis! See usage below.

## USAGE:
    `python analyzer.py 0` for regular usage, prompted for URL (including surrounding quotes [sorry, lazy])
    `python analyzer.py 1` for ~debug~ that polls my personal accessible(ish) website
    OUTPUT is printed object in form of `('HAS HTML LAN: {T/F}', 'HAS HEADINGS: {T/F}', 'HAS ALT TEXT: {T/F}')`

# Enjoy :D
