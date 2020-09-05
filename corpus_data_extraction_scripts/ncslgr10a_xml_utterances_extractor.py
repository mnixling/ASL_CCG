"""This script opens the ncslgr10a.xml file and extracts all the uttered sentences. Three different files are created.
The first file contains all the utterances in the corpus. The second file contains only those utterances which are
composed only of the dominant hand. The third file contains those utterances which are a combination of dominant hand
and non-dominant hand signs."""

from bs4 import BeautifulSoup as BS
import re

partial_path = r'C:\Users\manua\Desktop\NCSLGR_data\ncslgr-xml'

dominant_only_gloss = ()
dominant_and_non_dominant_gloss = ()

with open(partial_path + r'\ncslgr10a.xml', 'r') as f_IN:
    with open(r'C:\Users\manua\Desktop\NIX_BYU_THESIS\NCSLGR_Corpus_data\ncslgr_corpus_utterances.txt', 'a') as f_OUT_utts:
        soup = BS(f_IN.read(), 'xml')

        for utterance_tag in soup.find_all('UTTERANCES'):
            for utterance_tags in utterance_tag.find_all('UTTERANCE'):
                if utterance_tags.find_all('TRACK', {'FID': '10001'}):
                    for dominant_track_tags in utterance_tags.find_all('TRACK', {'FID': '10000'}):
                        for dominant_a_tags in dominant_track_tags.find_all('A'):
                            if dominant_a_tags.has_attr('VID'):
                                dominant_a_tags.decompose()
                        for non_dominant_track_tags in utterance_tags.find_all('TRACK', {'FID': '10001'}):
                            for non_dominant_a_tags in non_dominant_track_tags.find_all('A'):
                                if non_dominant_a_tags.has_attr('VID'):
                                    non_dominant_a_tags.decompose()
                    dominant_and_non_dominant_gloss = dominant_track_tags.text, '**NON-DOM**', non_dominant_track_tags.text
                    dominant_and_non_dominant_gloss_string = str(dominant_and_non_dominant_gloss)
                    pattern_match = re.finditer('\"[^\"]+\"', dominant_and_non_dominant_gloss_string)
                    dominant_and_non_dominant_gloss_string = re.sub('\\\\n', ' ', dominant_and_non_dominant_gloss_string)
                    dominant_and_non_dominant_gloss_string = re.sub('\\(', '', dominant_and_non_dominant_gloss_string)
                    dominant_and_non_dominant_gloss_string = re.sub('\\)', '', dominant_and_non_dominant_gloss_string)
                    dominant_and_non_dominant_gloss_string = re.sub("'", '', dominant_and_non_dominant_gloss_string)
                    dominant_and_non_dominant_gloss_string = re.sub(',', '', dominant_and_non_dominant_gloss_string)

                    if pattern_match:  # this code replaces all whitespaces within double quotes with underscores
                        for wanted_string in pattern_match:
                            updated_wanted_string = wanted_string.group().replace(' ', '_')
                            dominant_and_non_dominant_gloss_string = dominant_and_non_dominant_gloss_string.replace(wanted_string.group(), updated_wanted_string)
                    dominant_and_non_dominant_gloss_string = re.sub('"', "'", dominant_and_non_dominant_gloss_string)
                    print(dominant_and_non_dominant_gloss_string.lstrip(), file=f_OUT_utts)

                else:
                    for dominant_track_tags in utterance_tags.find_all('TRACK', {'FID': '10000'}):
                        dominant_only_gloss = 'NO NON-DOM:', dominant_track_tags.text
                    dominant_only_gloss_string = str(dominant_only_gloss)
                    pattern_match = re.finditer('\"[^\"]+\"', dominant_only_gloss_string)
                    dominant_only_gloss_string = re.sub('\\\\n', ' ', dominant_only_gloss_string)
                    dominant_only_gloss_string = re.sub('\\(', '', dominant_only_gloss_string)
                    dominant_only_gloss_string = re.sub('\\)', '', dominant_only_gloss_string)
                    dominant_only_gloss_string = re.sub("'", '', dominant_only_gloss_string)
                    dominant_only_gloss_string = re.sub(',', '', dominant_only_gloss_string)

                    if pattern_match:  # this code replaces all whitespaces within double quotes with underscores
                        for wanted_string in pattern_match:
                            updated_wanted_string = wanted_string.group().replace(' ', '_')
                            dominant_only_gloss_string = dominant_only_gloss_string.replace(wanted_string.group(), updated_wanted_string)

                    dominant_only_gloss_string = re.sub('"', "'", dominant_only_gloss_string)

                    print(dominant_only_gloss_string, file=f_OUT_utts)
