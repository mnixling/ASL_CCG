from bs4 import BeautifulSoup as BS
import re

partial_path = r'C:\Users\manua\Desktop\NCSLGR_data\ncslgr-xml'

dominant_hand_pos_id_list = []  # A list of lists of [[<POS>, <POS ID>], [<POS>, <POS ID>]] for the dominant hand
non_dominant_hand_pos_id_list = []  # A list of lists of [[<POS>, <POS ID>], [<POS>, <POS ID>]] for the non-dominant hand

dominant_hand_gloss = []  # Contains the dominant hand gloss words
non_dominant_hand_gloss = []  # Contains the non-dominant hand gloss words

dominant_hand_unlabeled_gloss_list = []  # Contains those gloss words that do not have an associated POS tag id number
non_dominant_hand_unlabeled_gloss_list = []  # Contains those gloss words that do not have an associated POS tag id number

dominant_hand_pos_id_number_list = []  # Contains the POS id numbers corresponding to the dominant hand gloss
non_dominant_hand_pos_id_number_list = []  # Contains the POS id numbers corresponding to the non-dominant hand gloss

dominant_hand_GLOSS_POS_id_num_list = []  # Contains the <GLOSS> and <POS ID NUMBER> for the dominant hand
non_dominant_hand_GLOSS_POS_id_num_list = []  # Contains the <GLOSS> and <POS ID NUMBER> for the non-dominant hand

unwanted_tags_40000d = re.compile(r'400\d+')

with open(partial_path + r'\accident.xml', 'r') as f_IN:
    soup = BS(f_IN.read(), 'xml')

    # lines 27-41 extracts all the POS labels and their corresponding POS ID codes for dominant and non-dominant hands
    for dom_field_tag in soup.find_all('FIELD', {'LABEL': 'POS'}):
        for dom_value_tags in dom_field_tag.find_all('VALUE'):
            if unwanted_tags_40000d.search(dom_value_tags['ID']):
                x = 0  # this is here to satisfy the if condition
            else:
                dominant_hand_POS_ID = [dom_value_tags['NAME'], dom_value_tags['ID']]
                dominant_hand_pos_id_list.append(dominant_hand_POS_ID)

    for non_dom_field_tag in soup.find_all('FIELD', {'LABEL': 'POS2'}):
        for non_dom_value_tags in non_dom_field_tag.find_all('VALUE'):
            if unwanted_tags_40000d.search(non_dom_value_tags['ID']):
                x = 0  # this is here to satisfy the if condition
            else:
                non_dominant_hand_POS_ID = [non_dom_value_tags['NAME'], non_dom_value_tags['ID']]
                non_dominant_hand_pos_id_list.append(non_dominant_hand_POS_ID)

    # Lines 45-66 is only for dominant hand gloss
    for utterance_tag in soup.find_all('UTTERANCE'):
        for dominant_track_tags in utterance_tag.find_all('TRACK', {'FID': '10000'}):
            for dominant_a_tags in dominant_track_tags.find_all('A'):
                if dominant_a_tags.has_attr('VID'):
                    y = 0  # this skips over the A-tags that do not have gloss information; i.e. no string data
                # The following elif statements seperate the gloss that does not have an associated POS label
                elif ('5' in dominant_a_tags.string) and ('CL' not in dominant_a_tags.string) and ('WHY' not in dominant_a_tags.string) and ('MAN' not in dominant_a_tags.string):
                    dominant_hand_unlabeled_gloss = dominant_a_tags.string
                    dominant_hand_unlabeled_gloss_list.append(dominant_hand_unlabeled_gloss)
                elif '\"quote\"' in dominant_a_tags.string:
                    dominant_hand_unlabeled_quote = dominant_a_tags.string
                    dominant_hand_unlabeled_gloss_list.append(dominant_hand_unlabeled_quote)
                elif 'false start' in dominant_a_tags.string:
                    dominant_unlabeled_false_start = dominant_a_tags.string
                    dominant_hand_unlabeled_gloss_list.append(dominant_unlabeled_false_start)
                else:
                    dominant_hand_gloss.append(dominant_a_tags.string)  # only for dominant hand gloss

        for dominant_hand_FID_value in utterance_tag.find_all('TRACK', {'FID': '27'}):
            for unwanted_a_tag in dominant_hand_FID_value.find_all('A', {'E': '2600', 'S': '1867', 'VID': '14'}):  # this is an extra tag that should not be there
                unwanted_a_tag.decompose()
            for dominant_a_tags_two in dominant_hand_FID_value.find_all('A'):
                dominant_hand_pos_id_number_list.append(dominant_a_tags_two['VID'])

        # Lines 69-93 is only for non-dominant hand gloss
        for non_dominant_track_tags in utterance_tag.find_all('TRACK', {'FID': '10001'}):
            for non_dominant_a_tags in non_dominant_track_tags.find_all('A'):
                if non_dominant_a_tags.has_attr('VID'):
                    y = 0  # this skips over the A-tags that do not have gloss information; i.e. no string data
                elif 'G\"focus\"' in non_dominant_a_tags.string:
                    non_dominant_g_focus = non_dominant_a_tags.string
                    non_dominant_hand_unlabeled_gloss_list.append(non_dominant_g_focus)
                elif '(1)\"focus\"' in non_dominant_a_tags.string:
                    non_dominant_1_focus = non_dominant_a_tags.string
                    non_dominant_hand_unlabeled_gloss_list.append(non_dominant_1_focus)
                elif '5\"reluctance\"' in non_dominant_a_tags.string:
                    non_dominant_hand_5_reluctance = non_dominant_a_tags.string
                    non_dominant_hand_unlabeled_gloss_list.append(non_dominant_hand_5_reluctance)
                elif '5\"I don\'t know\"' in non_dominant_a_tags.string:
                    non_dominant_hand_5_dont_know = non_dominant_a_tags.string
                    non_dominant_hand_unlabeled_gloss_list.append(non_dominant_hand_5_dont_know)
                elif '5"what\'s going on?"' in non_dominant_a_tags.string:
                    non_dominant_hand_whats_going_on = non_dominant_a_tags.string
                    non_dominant_hand_unlabeled_gloss_list.append(non_dominant_hand_whats_going_on)
                else:
                    non_dominant_hand_gloss.append(non_dominant_a_tags.string)

            for non_dominant_hand_FID_value in utterance_tag.find_all('TRACK', {'FID': '29'}):
                for non_dominant_a_tags_two in non_dominant_hand_FID_value.find_all('A'):
                    non_dominant_hand_pos_id_number_list.append(non_dominant_a_tags_two['VID'])

"""Code blocks from 97 to 105 take the gloss from both the dominant and non-dominant hand and
associates the gloss with the part of speech id number--[GLOSS, ID]"""
for (dom_hand_word_gloss, dom_hand_pos_id_num) in zip(dominant_hand_gloss, dominant_hand_pos_id_number_list):
    dom_hand_gloss_pos_id_num = dom_hand_word_gloss, dom_hand_pos_id_num
    TEMPORARY_dominant_hand_GLOSS_POS_id_num_list = list(dom_hand_gloss_pos_id_num)
    dominant_hand_GLOSS_POS_id_num_list.append(TEMPORARY_dominant_hand_GLOSS_POS_id_num_list)

for (non_dom_word_gloss, non_dom_hand_pos_id_num) in zip(non_dominant_hand_gloss, non_dominant_hand_pos_id_number_list):
    non_dom_hand_gloss_pos_id_num = non_dom_word_gloss, non_dom_hand_pos_id_num
    TEMPORARY_non_dominant_hand_GLOSS_POS_id_num_list = list(non_dom_hand_gloss_pos_id_num)
    non_dominant_hand_GLOSS_POS_id_num_list.append(TEMPORARY_non_dominant_hand_GLOSS_POS_id_num_list)

# lines 108-116 arrange the output to be in <POS> <GLOSS> ordering
for item_a in dominant_hand_GLOSS_POS_id_num_list:
    for item_b in dominant_hand_pos_id_list:
        if item_a[1] == item_b[1]:  # compares the POS id numbers of both lists
            item_a[1] = item_b[0]  # replaces the POS id number (item_a) with the POS label (item_b)

for item_c in non_dominant_hand_GLOSS_POS_id_num_list:
    for item_d in non_dominant_hand_pos_id_list:
        if item_c[1] == item_d[1]:  # compares the POS id numbers of both lists
            item_c[1] = item_d[0]  # replaces the POS id number (item_c) with the POS label (item_d)

"""
Lines 124-172 arranges the output for the file pos_gloss.txt to be <POS> <GLOSS WORD>. Any whitespace that happens 
between quotes gets replaced with an underscore. For example, BCL"holding and examining hand" becomes 
BCL"holding_and_examining_hand". This is because OpenCCG cannot recognize words within quotes separated by whitespace as 
belonging together. 
"""
with open(r'C:\Users\manua\Desktop\NIX_BYU_THESIS\NCSLGR_Corpus_data\pos_and_gloss.txt', 'a') as f_OUT_POS_gloss:
    with open(r'C:\Users\manua\Desktop\NIX_BYU_THESIS\NCSLGR_Corpus_data\only_gloss.txt', 'a') as f_OUT_gloss:
        with open(r'C:\Users\manua\Desktop\NIX_BYU_THESIS\NCSLGR_Corpus_data\only_pos.txt', 'a') as f_OUT_POS:
            for dom_item in dominant_hand_GLOSS_POS_id_num_list:
                if 'Discourse Marker' in dom_item[1]:
                    dom_item[1] = re.sub('Discourse Marker', 'Discourse_Marker', dom_item[1])
                if 'Proper Noun' in dom_item[1]:
                    dom_item[1] = re.sub('Proper Noun', 'Proper_Noun', dom_item[1])
                if 'Tense + Aspect' in dom_item[1]:
                    dom_item[1] = re.sub('Tense \+ Aspect', 'Tense_+_Aspect', dom_item[1])
                if 'Quantifier + Wh-word' in dom_item[1]:
                    dom_item[1] = re.sub('Quantifier \+ Wh-word', 'Quantifier_+_Wh-word', dom_item[1])
                if '"' in dom_item[0]:
                    if ' ' in dom_item[0]:
                        dom_item[0] = re.sub(' ', '_', dom_item[0])
                if ':' in dom_item[0]:
                    dom_item[0] = re.sub(':', '*', dom_item[0])
                dom_item[0] = re.sub('"', "'", dom_item[0])

                print(dom_item[1], dom_item[0], file=f_OUT_POS_gloss)  # dom_item[1] is the POS, dom_item[0] is the GLOSS
                print(dom_item[0], file=f_OUT_gloss)
                print(dom_item[1], file=f_OUT_POS)

            for non_dom_item in non_dominant_hand_GLOSS_POS_id_num_list:
                non_dom_item[0] = non_dom_item[0].rstrip()
                if 'Proper Noun' in non_dom_item[1]:
                    non_dom_item[1] = re.sub('Proper Noun', 'Proper_Noun', non_dom_item[1])
                if '"' in non_dom_item[0]:
                    if ' ' in non_dom_item[0]:
                        non_dom_item[0] = re.sub(' ', '_', non_dom_item[0])
                if ':' in non_dom_item[0]:
                    non_dom_item[0] = re.sub(':', '*', non_dom_item[0])
                non_dom_item[0] = re.sub('"', "'", non_dom_item[0])

                print(non_dom_item[1], non_dom_item[0], file=f_OUT_POS_gloss)  # non_dom_item[1] is the POS, non_dom_item[0] is the GLOSS
                print(non_dom_item[0], file=f_OUT_gloss)
                print(non_dom_item[1], file=f_OUT_POS)

            for dom_XXX in dominant_hand_unlabeled_gloss_list:
                dom_XXX = dom_XXX.rstrip()
                if ' ' in dom_XXX:
                    dom_XXX = re.sub(' ', '_', dom_XXX)
                print('XXX', dom_XXX, file=f_OUT_POS_gloss)

            for non_dom_XXX in non_dominant_hand_unlabeled_gloss_list:
                non_dom_XXX = non_dom_XXX.rstrip()
                if ' ' in non_dom_XXX:
                    non_dom_XXX = re.sub(' ', '_', non_dom_XXX)
                print('XXX', non_dom_XXX, file=f_OUT_POS_gloss)