"""This script creates the testbed.xml file for the OpenCCG grammar ASL."""

import re
input_file_name = r'C:\Users\manua\Desktop\NIX_BYU_THESIS\NCSLGR_Corpus_data\ncslgr_corpus_hand_edited.txt'
output_file_name = r'C:\Users\manua\Desktop\openccg-master\grammars\ASL\testbed.xml'

with open(input_file_name, 'r') as input_file:
    with open(output_file_name, 'w') as output_file:
        print('<?xml version="1.0" encoding="UTF-8"?>', file=output_file)
        print('<regression>', file=output_file)

        for sentence in input_file:
            sentence = re.sub('\n', '', sentence)
            sentence = re.sub('"', "'", sentence)
            sentence = re.sub(':', '*', sentence)

            print(f'<item numOfParses="1" string="{sentence}"/>', file=output_file)

        print('</regression>', file=output_file)
