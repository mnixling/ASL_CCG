"""This file is for the ASL OpenCCG grammar.xml file"""

output_file_name = r'C:\Users\manua\Desktop\openccg-master\grammars\ASL\grammar.xml'

with open(output_file_name, 'w') as f_OUT:
    print("""<?xml version="1.0"?>

<!--
This grammar is built for a thesis project composed of data collected from the NCSLGR Corpus. The data came from:
http://www.bu.edu/asllrp/ncslgr.html
Michael Nix created this grammar.
-->

<grammar name="ASL"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="../grammar.xsd"
>

  <lexicon file="lexicon.xml"/>
  <morphology file="morph.xml"/>
  <rules file="rules.xml"/>
  <testbed file="testbed.xml"/>

</grammar>""", file=f_OUT)
