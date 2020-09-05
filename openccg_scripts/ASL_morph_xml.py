import re

input_file_name = r'C:\Users\manua\Desktop\NIX_BYU_THESIS\NCSLGR_Corpus_data\pos_and_gloss_tagged.txt'
output_file_name = r'C:\Users\manua\Desktop\openccg-master\grammars\ASL\morph.xml'

adjective_count = 0
adverb_count = 0
aspect_count = 0
classifier_count = 0
complementizer_count = 0
conjunction_count = 0
demonstrative_count = 0
determiner_count = 0
discourse_marker_count = 0
modal_count = 0
modal_plus_negation_count = 0
negation_count = 0
negation_plus_aspect_count = 0
negation_plus_verb_count = 0
noun_count = 0
number_count = 0
particle_count = 0
possessive_count = 0
preposition_count = 0
pronoun_count = 0
proper_noun_count = 0
quantifier_count = 0
quantifier_plus_wh_word_count = 0
quantifier_underscore_plus_underscore_wh_word_count = 0
reflexive_count = 0
tense_count = 0
tense_plus_aspect_count = 0
tense_underscore_plus_underscore_aspect_count = 0
tense_plus_negation_count = 0
tense_underscore_plus_underscore_negative_count = 0
verb_plus_aspect_count = 0
verb_ditransitive_count = 0
verb_intransitive_count = 0
verb_transitive_count = 0
wh_word_count = 0
wh_plus_particle_count = 0
xxx_intrans_count = 0
xxx_count = 0

with open(input_file_name, 'r') as f_IN:
    with open(output_file_name, 'w') as f_OUT:
        print("""<?xml version="1.0" encoding="UTF-8"?>
<!--
This file contains the morph entries.
-->

<morph
  name="ASL"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="../morph.xsd"
>""", file=f_OUT)

        for i in f_IN:
            adjective_match = re.search('^Adjective', i)
            adverb_match = re.search('^Adverb', i)
            aspect_match = re.search('^Aspect', i)
            classifier_match = re.search('^Classifier', i)
            complementizer_match = re.search('^Complementizer', i)
            conjunction_match = re.search('^Conjunction', i)
            demonstrative_match = re.search('^Demonstrative', i)
            determiner_match = re.search('^Determiner', i)
            discourse_marker_match = re.search('^Discourse_Marker', i)
            modal_match = re.search('^Modal', i)
            modal_plus_negation_match = re.search('^Modal\+Negation', i)
            negation_match = re.search('^Negation', i)
            negation_plus_aspect_match = re.search('^Negation\+Aspect', i)
            negation_plus_verb_match = re.search('^Negation\+Verb', i)
            noun_match = re.search('^Noun', i)
            number_match = re.search('^Number', i)
            particle_match = re.search('^Particle', i)
            possessive_match = re.search('^Possessive', i)
            preposition_match = re.search('^Preposition', i)
            pronoun_match = re.search('^Pronoun', i)
            proper_noun_match = re.search('^Proper_Noun', i)
            reflexive_match = re.search('^Reflexive', i)
            quantifier_match = re.search('^Quantifier', i)
            quantifier_plus_wh_word_match = re.search('^Quantifier\+Wh-word', i)
            quantifier_underscore_plus_underscore_wh_word_match = re.search('^Quantifier_\+_Wh-word', i)
            tense_match = re.search('^Tense', i)
            tense_plus_aspect_match = re.search('^Tense\+Aspect', i)
            tense_underscore_plus_underscore_aspect_match = re.search('^Tense_\+_Aspect', i)
            tense_plus_negation_match = re.search('^Tense\+Negation', i)
            tense_underscore_plus_underscore_negative_match = re.search('^Tense_\+_Negative', i)
            verb_plus_aspect_match = re.search('^Verb\+Aspect', i)
            verb_ditransitive_match = re.search('^Verb-ditrans', i)
            verb_intransitive_match = re.search('^Verb-intrans', i)
            verb_transitive_match = re.search('^Verb-trans', i)
            wh_word_match = re.search('^Wh-word', i)
            wh_plus_particle_match = re.search('Wh\+Particle', i)
            xxx_intrans_match = re.search('^XXX-intrans', i)
            xxx_match = re.search('^XXX', i)

            word_matching_string = re.search('\s(.*)', i)

            if adjective_match:
                adjective_count += 1
                pos_tag = adjective_match.group()
                if adjective_count == 1:
                    print('  <!-- ' + '=' * 36 + ' ADJECTIVE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if adverb_match:
                adverb_count += 1
                pos_tag = adverb_match.group()
                if adverb_count == 1:
                    print('  <!-- ' + '=' * 36 + ' ADVERB ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if aspect_match:
                aspect_count += 1
                pos_tag = aspect_match.group()
                if aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if classifier_match:
                classifier_count += 1
                if classifier_count == 1:
                    print('  <!-- ' + '=' * 36 + ' CLASSIFIER ' + '=' * 36 + ' -->', file=f_OUT)
                bcl_classifier_match = re.search('2hBCL|2halt\.BCL|BCL', i)
                bpcl_classifier_match = re.search('2hBPCL|BPCL', i)
                dcl_classifier_match = re.search('1hDCL|2hDCL|2halt\.DCL|DCL', i)
                icl_classifier_match = re.search('2hICL|2halt\.ICL|ICL', i)
                lcl_classifier_match = re.search('2hLCL|2halt\.LCL|LCL', i)
                pcl_classifier_match = re.search('2hPCL|PCL', i)
                scl_classifier_match = re.search('2hSCL|2halt\.SCL|SCL', i)
                if bcl_classifier_match:
                    word = word_matching_string.group(1)
                    print(f"""    <entry pos="BCL" word="{word}"/>""", file=f_OUT)
                if bpcl_classifier_match:
                    word = word_matching_string.group(1)
                    print(f"""    <entry pos="BPCL" word="{word}"/>""", file=f_OUT)
                if dcl_classifier_match:
                    word = word_matching_string.group(1)
                    print(f"""    <entry pos="DCL" word="{word}"/>""", file=f_OUT)
                if icl_classifier_match:
                    word = word_matching_string.group(1)
                    print(f"""    <entry pos="ICL" word="{word}"/>""", file=f_OUT)
                if lcl_classifier_match:
                    word = word_matching_string.group(1)
                    print(f"""    <entry pos="LCL" word="{word}"/>""", file=f_OUT)
                if pcl_classifier_match:
                    word = word_matching_string.group(1)
                    print(f"""    <entry pos="PCL" word="{word}"/>""", file=f_OUT)
                if scl_classifier_match:
                    word = word_matching_string.group(1)
                    print(f"""    <entry pos="SCL" word="{word}"/>""", file=f_OUT)

            if complementizer_match:
                complementizer_count += 1
                pos_tag = complementizer_match.group()
                if complementizer_count == 1:
                    print('  <!-- ' + '=' * 36 + ' COMPLEMENTIZER ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if conjunction_match:
                conjunction_count += 1
                pos_tag = conjunction_match.group()
                if conjunction_count == 1:
                    print('  <!-- ' + '=' * 36 + ' CONJUNCTION ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if demonstrative_match:
                demonstrative_count += 1
                pos_tag = demonstrative_match.group()
                if demonstrative_count == 1:
                    print('  <!-- ' + '=' * 36 + ' DEMONSTRATIVE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if determiner_match:
                determiner_count += 1
                pos_tag = determiner_match.group()
                if determiner_count == 1:
                    print('  <!-- ' + '=' * 36 + ' DETERMINER ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if discourse_marker_match:
                discourse_marker_count += 1
                pos_tag = discourse_marker_match.group()
                if discourse_marker_count == 1:
                    print('  <!-- ' + '=' * 36 + ' DISCOURSE_MARKER ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if modal_match:
                modal_count += 1
                pos_tag = modal_match.group()
                if modal_count == 1:
                    print('  <!-- ' + '=' * 36 + ' MODAL ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if modal_plus_negation_match:
                modal_plus_negation_count += 1
                pos_tag = modal_plus_negation_match.group()
                if modal_plus_negation_count == 1:
                    print('  <!-- ' + '=' * 36 + ' MODAL+NEGATION ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if negation_match:
                negation_count += 1
                pos_tag = negation_match.group()
                if negation_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NEGATION ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if negation_plus_aspect_match:
                negation_plus_aspect_count += 1
                pos_tag = negation_plus_aspect_match.group()
                if negation_plus_aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NEGATION+ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if negation_plus_verb_match:
                negation_plus_verb_count += 1
                pos_tag = negation_plus_verb_match.group()
                if negation_plus_verb_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NEGATION+VERB ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if noun_match:
                noun_count += 1
                pos_tag = noun_match.group()
                if noun_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NOUN ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if number_match:
                number_count += 1
                pos_tag = number_match.group()
                if number_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NUMBER ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if particle_match:
                particle_count += 1
                pos_tag = particle_match.group()
                if particle_count == 1:
                    print('  <!-- ' + '=' * 36 + ' PARTICLE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if possessive_match:
                possessive_count += 1
                pos_tag = possessive_match.group()
                if possessive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' POSSESSIVE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if preposition_match:
                preposition_count += 1
                pos_tag = preposition_match.group()
                if preposition_count == 1:
                    print('  <!-- ' + '=' * 36 + ' PREPOSITION ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if pronoun_match:
                pronoun_count += 1
                pos_tag = pronoun_match.group()
                if pronoun_count == 1:
                    print('  <!-- ' + '=' * 36 + ' PRONOUN ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if proper_noun_match:
                proper_noun_count += 1
                pos_tag = proper_noun_match.group()
                if proper_noun_count == 1:
                    print('  <!-- ' + '=' * 36 + ' PROPER NOUN ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if quantifier_match:
                quantifier_count += 1
                pos_tag = quantifier_match.group()
                if quantifier_count == 1:
                    print('  <!-- ' + '=' * 36 + ' QUANTIFIER ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if quantifier_plus_wh_word_match:
                quantifier_plus_wh_word_count += 1
                pos_tag = quantifier_plus_wh_word_match.group()
                if quantifier_plus_wh_word_count == 1:
                    print('  <!-- ' + '=' * 36 + ' QUANTIFIER+WH-WORD ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if quantifier_underscore_plus_underscore_wh_word_match:
                quantifier_underscore_plus_underscore_wh_word_count += 1
                pos_tag = quantifier_underscore_plus_underscore_wh_word_match.group()
                if quantifier_underscore_plus_underscore_wh_word_count == 1:
                    print('  <!-- ' + '=' * 36 + ' QUANTIFIER_+_WH-WORD ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if reflexive_match:
                reflexive_count += 1
                pos_tag = reflexive_match.group()
                if reflexive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' REFLEXIVE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if tense_match:
                tense_count += 1
                pos_tag = tense_match.group()
                if tense_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if tense_plus_aspect_match:
                tense_plus_aspect_count += 1
                pos_tag = tense_plus_aspect_match.group()
                if tense_plus_aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE+ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if tense_underscore_plus_underscore_aspect_match:
                tense_underscore_plus_underscore_aspect_count += 1
                pos_tag = tense_underscore_plus_underscore_aspect_match.group()
                if tense_underscore_plus_underscore_aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE_+_ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if tense_plus_negation_match:
                tense_plus_negation_count += 1
                pos_tag = tense_plus_negation_match.group()
                if tense_plus_negation_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE+NEGATION ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if tense_underscore_plus_underscore_negative_match:
                tense_underscore_plus_underscore_negative_count += 1
                pos_tag = tense_underscore_plus_underscore_negative_match.group()
                if tense_underscore_plus_underscore_negative_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE_+_NEGATIVE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if verb_plus_aspect_match:
                verb_plus_aspect_count += 1
                pos_tag = verb_plus_aspect_match.group()
                if verb_plus_aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' VERB+ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if verb_ditransitive_match:
                verb_ditransitive_count += 1
                pos_tag = verb_ditransitive_match.group()
                if verb_ditransitive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' VERB-DITRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if verb_intransitive_match:
                verb_intransitive_count += 1
                pos_tag = verb_intransitive_match.group()
                if verb_intransitive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' VERB-INTRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if verb_transitive_match:
                verb_transitive_count += 1
                pos_tag = verb_transitive_match.group()
                if verb_transitive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' VERB-TRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if wh_word_match:
                wh_word_count += 1
                pos_tag = wh_word_match.group()
                if wh_word_count == 1:
                    print('  <!-- ' + '=' * 36 + ' WH-WORD ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if wh_plus_particle_match:
                wh_plus_particle_count += 1
                pos_tag = wh_plus_particle_match.group()
                if wh_plus_particle_count == 1:
                    print('  <!-- ' + '=' * 36 + ' WH+PARTICLE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if xxx_intrans_match:
                xxx_intrans_count += 1
                pos_tag = xxx_intrans_match.group()
                if xxx_intrans_count == 1:
                    print('  <!-- ' + '=' * 36 + ' XXX-INTRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)

            if xxx_match:
                xxx_count += 1
                pos_tag = xxx_match.group()
                if xxx_intrans_count == 1:
                    print('  <!-- ' + '=' * 36 + ' XXX ' + '=' * 36 + ' -->', file=f_OUT)
                word = word_matching_string.group(1)
                print(f"""    <entry pos="{pos_tag}" word="{word}"/>""", file=f_OUT)




        print('\n</morph>\n', file=f_OUT)