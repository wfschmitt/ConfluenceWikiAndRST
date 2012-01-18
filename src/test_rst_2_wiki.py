import unittest
import rst_2_wiki
import os.path

#=======================================================================================================================
# TestCase
#=======================================================================================================================
class TestCase(unittest.TestCase):
    
    
#    def testDocutils(self):
#        from docutils import core
#        
#        # dict of default settings to override (same as in the cmdline params, but as attribute names:
#        #   "--embed-stylesheet" => "embed_stylesheet"
#        settings_overrides = {}
#
#        base = r'W:/pydev/plugins/com.python.pydev.docs/'
#        for filename in ('manual_101_install.rst',):
#            with file(os.path.join(base, 'merged_homepage', filename), 'r') as f:
#                contents = f.read()
#                # publish as html
#                ret = core.publish_string(
#                    contents,
##                    writer_name='xml',
##                    source_path=path,
#        #            destination_path=os.tempnam(),
#                    settings_overrides=settings_overrides,
#                )
#                print ret

    
    def testIgnore(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
..
    ignore
    ignore

add this
========
''')
        self.assertEqual('\nh1. add this', convert.Convert())
        
        
    def testConversion2(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
.. _`Aptana Studio 3`: http://aptana.com/products/studio3

bla `Aptana Studio 3`_ bla
''')
        self.assertEqual('\n\nbla [Aptana Studio 3|http://aptana.com/products/studio3] bla', convert.Convert())
        
        
    def testConversion3(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
.. _`A`: http://aa

b `A`_ b `A`_ b
''')
        self.assertEqual('\n\nb [A|http://aa] b [A|http://aa] b', convert.Convert())
        
        
    def testConversion4(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
.. _`PyDev c`: pydev_certificate.cer

The first step for that is downloading the `PyDev c`_.
''')
        self.assertEqual('\n\nThe first step for that is downloading the [PyDev c|pydev_certificate.cer].', convert.Convert())
        
    
    def testImage(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
.. image:: images/update_sites.png
   :class: snap
   :align: center 
''')
        self.assertEqual('\n!http://pydev.org/images/update_sites.png|border=1!', convert.Convert())
        
        
    def testLinkToLink(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
.. _http://link: http://link
`http://link`_''')
        self.assertEqual('\n[http://link|http://link]', convert.Convert())
        
        
    def testLinkToLink2(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
.. _http://pydev.org/updates: http://pydev.org/updates
`http://pydev.org/updates`_''')
        self.assertEqual('\n[http://pydev.org/updates|http://pydev.org/updates]', convert.Convert())
        
        
        
    def testBlock(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
::
    something
    something
''')
        self.assertEqual('\n{quote}\n\n    something\n    something\n{quote}', convert.Convert())
        
    def testBlock2(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
such as:
    ::
        An error
''')
        self.assertEqual('\nsuch as:\n{quote}\n\n        An error\n{quote}', convert.Convert())
        
        
    def testTable(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
:A:

    itemA
:B:

    itemB
''')
        

        expected = '''
||A:|    itemA||
||B:|    itemB||'''

        self.assertEqual(expected, convert.Convert())
        
        
    def testTableWithLinks(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
.. _`itemA`: http://aa

:A:
    `itemA`_
''')
        

        expected = '''

||A:|    [itemA|http://aa]||'''

        self.assertEqual(expected, convert.Convert())
        
        
    def testCodeBlock(self):
        convert = rst_2_wiki.ConvertRstToWiki('''
.. sourcecode:: python

    a = 10
    b = 20
''')
        


        self.assertEqual('\n{code:language=python}\n\n\n    a = 10\n    b = 20\n{code}', convert.Convert())
        
    def testCodeBlock2(self):
        convert = rst_2_wiki.ConvertRstToWiki("""
    .. sourcecode:: python

        a = 10
        b = 20
""")
        

        expected = '''
{code:language=python}


        a = 10
        b = 20
{code}'''
        self.assertEqual(expected, convert.Convert())
        
        
        
    def testAnchor(self):
        convert = rst_2_wiki.ConvertRstToWiki("""
`my link`_

_`my link`
-------------------
""")
        

        expected = '''
[#my link]

h1. {anchor: my link}my link'''
        self.assertEqual(expected, convert.Convert())
        
        
#=======================================================================================================================
# main
#=======================================================================================================================
if __name__ == '__main__':
    unittest.main()