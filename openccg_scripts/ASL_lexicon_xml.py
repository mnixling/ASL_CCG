import re

input_file_name = r'C:\Users\manua\Desktop\NIX_BYU_THESIS\NCSLGR_Corpus_data\pos_and_gloss_tagged.txt'
output_file_name = r'C:\Users\manua\Desktop\openccg-master\grammars\ASL\lexicon.xml'

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
This file contains the lexical families.
-->

<lexicon
  name="ASL"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="../lexicon.xsd"
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

            if adjective_match:
                adjective_count += 1
                pos_tag = adjective_match.group()
                if adjective_count == 1:
                    print('  <!-- ' + '=' * 36 + ' ADJECTIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The ADJECTIVE part of speech has the categories of: np/n, np\\n, np\\np, np/np, n\\n, n/n  -->""", file=f_OUT)
                    print(f"""    <family name="ADJECTIVE" pos="{pos_tag}">
      <entry name="np/n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>

      <entry name="np\\n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>

      <entry name="np\\np">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>

      <entry name="np/np">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>

      <entry name="n\\n">
        <complexcat>
          <atomcat type="n"/>
          <slash dir="\\" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>

      <entry name="n/n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

                if adjective_match:
                    pos_tag = adjective_match.group()
                    if adjective_count == 2:
                        print('  <!-- ' + '=' * 36 + ' ADJECTIVE ' + '=' * 36 + ' -->', file=f_OUT)
                        print("""  <!-- The ADJECTIVE part of speech has the categories of: np|n  -->""", file=f_OUT)
                        print(f"""    <family name="ADJECTIVE" pos="{pos_tag}" closed="true">
            <entry name="np|n">
              <complexcat>
                <atomcat type="np"/>
                <slash dir="|" mode="&lt; &gt;"/>
                <atomcat type="n"/>
              </complexcat>
            </entry>
            <member stem="FUNNY"/>
            </family>\n""", file=f_OUT)

            if adverb_match:
                adverb_count += 1
                pos_tag = adverb_match.group()
                if adverb_count == 1:
                    print('  <!-- ' + '=' * 36 + ' ADVERB ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The ADVERB part of speech has the categories of: (s\\np)/(s\\np), (s\\np)\\(s\\np), s/np -->""", file=f_OUT)
                    print(f"""    <family name="ADVERB" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>

      <entry name="(s\\np)\\(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>

      <entry name="s/np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if adverb_match:
                pos_tag = adverb_match.group()
                if adverb_count == 2:
                    print('  <!-- ' + '=' * 36 + ' ADVERB ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The ADVERB part of speech has the category of: (np\\np)\\(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="ADVERB" pos="{pos_tag}" closed="true">
      <entry name="(np\\np)\\(s\\np)">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
      <member stem="IX-loc*i"/>
      <member stem="IX-loc*j"/>
    </family>\n""", file=f_OUT)

            if aspect_match:
                aspect_count += 1
                pos_tag = aspect_match.group()
                if aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The ASPECT part of speech has the category of: (s\\np)/(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="ASPECT" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if classifier_match:
                classifier_count += 1
                pos_tag = classifier_match.group()
                if classifier_count == 1:
                    print('  <!-- ' + '=' * 36 + ' CLASSIFIER ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The CLASSIFIER  part of speech has different categories based upon the type of classifier.  -->""", file=f_OUT)
                bcl_classifier_match = re.search('2hBCL|2halt\.BCL|BCL', i)
                bpcl_classifier_match = re.search('2hBPCL|BPCL', i)
                dcl_classifier_match = re.search('1hDCL|2hDCL|2halt\.DCL|DCL', i)
                icl_classifier_match = re.search('2hICL|2halt\.ICL|ICL', i)
                lcl_classifier_match = re.search('2hLCL|2halt\.LCL|LCL', i)
                pcl_classifier_match = re.search('2hPCL|PCL', i)
                scl_classifier_match = re.search('2hSCL|2halt\.SCL|SCL', i)

                if bcl_classifier_match and classifier_count == 2:
                    print(f"""    <family name="CLASSIFIER" pos="BCL">
      <entry name="s\\np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)
                if bpcl_classifier_match and classifier_count == 6:
                    print(f"""    <family name="CLASSIFIER" pos="BPCL">
      <entry name="s\\np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>

      <entry name="np">
        <atomcat type="np"/>
      </entry>
    </family>\n""", file=f_OUT)
                if dcl_classifier_match and classifier_count == 1:
                    print(f"""    <family name="CLASSIFIER" pos="DCL">
      <entry name="np/n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>

      <entry name="np\\n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>

      <entry name="np">
        <atomcat type="np"/>
      </entry>
    </family>\n""", file=f_OUT)
                if icl_classifier_match and classifier_count == 29:
                    print(f"""    <family name="CLASSIFIER" pos="ICL">
      <entry name="s\\np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)
                if lcl_classifier_match and classifier_count == 37:
                    print(f"""    <family name="CLASSIFIER" pos="LCL">
      <entry name="np">
        <atomcat type="np"/>
      </entry>
    </family>\n""", file=f_OUT)
                if pcl_classifier_match and classifier_count == 44:
                    print(f"""    <family name="CLASSIFIER" pos="PCL">
      <entry name="np">
        <atomcat type="np"/>
      </entry>
    </family>\n""", file=f_OUT)
                if scl_classifier_match and classifier_count == 48:
                    print(f"""    <family name="CLASSIFIER" pos="SCL" closed="true">
          <entry name="(s\\np)/np">
            <complexcat>
              <atomcat type="s"/>
              <slash dir="\\" mode="."/>
              <atomcat type="np"/>
              <slash dir="/" mode="."/>
              <atomcat type="np"/>
            </complexcat>
          </entry>
          <member stem="SCL*3'vehicle_sink'"/>
        </family>\n""", file=f_OUT)

                if scl_classifier_match and classifier_count == 49:
                    print(f"""    <family name="CLASSIFIER" pos="SCL">
      <entry name="np">
        <atomcat type="np"/>
      </entry>

      <entry name="s">
        <atomcat type="s"/>
      </entry>

      <entry name="s\\np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if complementizer_match:
                complementizer_count += 1
                pos_tag = complementizer_match.group()
                if complementizer_count == 1:
                    print('  <!-- ' + '=' * 36 + ' COMPLEMENTIZER ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The COMPLEMENTIZER part of speech has the category of: s/s -->""", file=f_OUT)
                    print(f"""    <family name="COMPLEMENTIZER" pos="{pos_tag}">
      <entry name="s/s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="/" mode="."/>
          <atomcat type="s"/>
          </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if conjunction_match:
                conjunction_count += 1
                pos_tag = conjunction_match.group()
                if conjunction_count == 1:
                    print('  <!-- ' + '=' * 36 + ' CONJUNCTION ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The CONJUNCTION part of speech has the categories of: np\\n/n, s/s/s -->""", file=f_OUT)
                    print(f"""    <family name="CONJUNCTION" pos="{pos_tag}">
      <entry name="np\\n/n">
      <complexcat>
        <atomcat type="np"/>
        <slash dir="\\" mode="."/>
        <atomcat type="n"/>
        <slash dir="/" mode="."/>
        <atomcat type="n"/>
      </complexcat>
      </entry>

      <entry name="s/s/s">
      <complexcat>
        <atomcat type="s"/>
        <slash dir="/" mode="."/>
        <atomcat type="s"/>
        <slash dir="/" mode="."/>
        <atomcat type="s"/>
      </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if determiner_match:
                determiner_count += 1
                pos_tag = determiner_match.group()
                if determiner_count == 1:
                    print('  <!-- ' + '=' * 36 + ' DETERMINER ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The DETERMINER part of speech has the category of: np/n -->""", file=f_OUT)
                    print(f"""    <family name="DETERMINER" pos="{pos_tag}">
      <entry name="np/n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if demonstrative_match:
                demonstrative_count += 1
                pos_tag = demonstrative_match.group()
                if demonstrative_count == 1:
                    print('  <!-- ' + '=' * 36 + ' DEMONSTRATIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The DEMONSTRATIVE part of speech has the category of: np/n -->""", file=f_OUT)
                    print(f"""    <family name="DEMONSTRATIVE" pos="{pos_tag}">
      <entry name="np/n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if discourse_marker_match:
                discourse_marker_count += 1
                pos_tag = discourse_marker_match.group()
                if discourse_marker_count == 1:
                    print('  <!-- ' + '=' * 36 + ' DISCOURSE_MARKER ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The DISCOURSE_MARKER part of speech has the categories of: s\\s, s/s -->""", file=f_OUT)
                    print(f"""    <family name="DISCOURSE_MARKER" pos="{pos_tag}">
      <entry name="s\\s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>

      <entry name="s/s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="/" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if modal_match:
                modal_count += 1
                pos_tag = modal_match.group()
                if modal_count == 1:
                    print('  <!-- ' + '=' * 36 + ' MODAL ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The MODAL part of speech has the categories of: (s\\np)/(s\\np), (s\\np)\\(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="MODAL" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>

      <entry name="(s\\np)\\(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if modal_plus_negation_match:
                modal_plus_negation_count += 1
                pos_tag = modal_plus_negation_match.group()
                if modal_plus_negation_count == 1:
                    print('  <!-- ' + '=' * 36 + ' MODAL+NEGATION ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The MODAL+NEGATION part of speech has the categories of: (s\\np)/(s\\np), (s\\np)\\(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="MODAL+NEGATION" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>

      <entry name="(s\\np)\\(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if negation_match:
                negation_count += 1
                pos_tag = negation_match.group()
                if negation_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NEGATION ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The NEGATION part of speech has the categories of: (s\\np)/(s\\np), (s\\np)\\(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>

      <entry name="(s\\np)\\(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if negation_plus_aspect_match:
                negation_plus_aspect_count += 1
                pos_tag = negation_plus_aspect_match.group()
                if negation_plus_aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NEGATION+ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The NEGATION+ASPECT part of speech has the categories of: (s\\np)/(s\\np), (s\\np)\\(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="NEGATION+ASPECT" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>

      <entry name="(s\\np)\\(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if negation_plus_verb_match:
                negation_plus_verb_count += 1
                pos_tag = negation_plus_verb_match.group()
                if negation_plus_verb_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NEGATION+VERB ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The NEGATION+VERB part of speech has the category of: (s\\np)/np -->""", file=f_OUT)
                    print(f"""    <family name="" pos="{pos_tag}">
      <entry name="(s\\np)/np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if noun_match:
                noun_count += 1
                pos_tag = noun_match.group()
                if noun_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NOUN ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The NOUN part of speech has the category of: n -->""", file=f_OUT)
                    print(f"""    <family name="NOUN" pos="{pos_tag}">
      <entry name="n">
        <atomcat type="n"/>
      </entry>
    </family>\n""", file=f_OUT)

            if noun_match:
                pos_tag = noun_match.group()
                if noun_count == 2:
                    print('  <!-- ' + '=' * 36 + ' NOUN ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The NOUN part of speech has the category of: n/n -->""", file=f_OUT)
                    print(f"""    <family name="NOUN" pos="{pos_tag}" closed="true">
      <entry name="n">
        <complexcat>
          <atomcat type="n"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>
     <member stem="TURKEY"/>
     <member stem="CAR"/>
     <member stem="GRASS"/>
    </family>\n""", file=f_OUT)

            if number_match:
                number_count += 1
                pos_tag = number_match.group()
                if number_count == 1:
                    print('  <!-- ' + '=' * 36 + ' NUMBER ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The NUMBER part of speech has the categories of: np/n, np\\n, np -->""", file=f_OUT)
                    print(f"""    <family name="NUMBER" pos="{pos_tag}">
      <entry name="np/n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>

      <entry name="np\\n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>
      
      <entry name="np">
        <atomcat type="np"/>
      </entry>
    </family>\n""", file=f_OUT)

            if particle_match:
                particle_count += 1
                pos_tag = particle_match.group()
                if particle_count == 1:
                    print('  <!-- ' + '=' * 36 + ' PARTICLE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The PARTICLE part of speech has the category of: s\\s -->""", file=f_OUT)
                    print(f"""    <family name="PARTICLE" pos="{pos_tag}">
      <entry name="s\\s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if possessive_match:
                possessive_count += 1
                pos_tag = possessive_match.group()
                if possessive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' POSSESSIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The POSSESSIVE part of speech has the category of: np/np -->""", file=f_OUT)
                    print(f"""    <family name="" pos="{pos_tag}">
      <entry name="np/np">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>

      <entry name="np\\np/np">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if preposition_match:
                preposition_count += 1
                pos_tag = preposition_match.group()
                if preposition_count == 1:
                    print('  <!-- ' + '=' * 36 + ' PREPOSITION ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The PREPOSITION part of speech has the category of: (s\\s)/np -->""", file=f_OUT)
                    print(f"""    <family name="PREPOSITION" pos="{pos_tag}">
      <entry name="(s\\s)/np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="s"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if pronoun_match:
                pronoun_count += 1
                pos_tag = pronoun_match.group()
                if pronoun_count == 1:
                    print('  <!-- ' + '=' * 36 + ' PRONOUN ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The PRONOUN part of speech has the category of: np -->""", file=f_OUT)
                    print(f"""    <family name="PRONOUN" pos="{pos_tag}">
      <entry name="np">
        <atomcat type="np"/>
      </entry>
    </family>\n""", file=f_OUT)

            if pronoun_match:
                pos_tag = pronoun_match.group()
                if pronoun_count == 2:
                    print('  <!-- ' + '=' * 36 + ' PRONOUN ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The PRONOUN part of speech has the category of: np\\np\\(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="PRONOUN" pos="{pos_tag}" closed="true">
      <entry name="np\\np\\(s\\np)">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>
          </complexcat>
        </complexcat>
      </entry>
      <member stem="IX-3p*i"/>
    </family>\n""", file=f_OUT)

            if proper_noun_match:
                proper_noun_count += 1
                pos_tag = proper_noun_match.group()
                if proper_noun_count == 1:
                    print('  <!-- ' + '=' * 36 + ' PROPER NOUN ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The PROPER NOUN part of speech has the category of: np -->""", file=f_OUT)
                    print(f"""    <family name="PROPER NOUN" pos="{pos_tag}">
      <entry name="np">
        <atomcat type="np"/>
      </entry>
    </family>\n""", file=f_OUT)

            if quantifier_match:
                quantifier_count += 1
                pos_tag = quantifier_match.group()
                if quantifier_count == 1:
                    print('  <!-- ' + '=' * 36 + ' QUANTIFIER ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The QUANTIFIER part of speech has the category of: np/n -->""", file=f_OUT)
                    print(f"""    <family name="QUANTIFIER" pos="{pos_tag}">
      <entry name="np/n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if quantifier_plus_wh_word_match:
                quantifier_plus_wh_word_count += 1
                pos_tag = quantifier_plus_wh_word_match.group()
                if quantifier_plus_wh_word_count == 1:
                    print('  <!-- ' + '=' * 36 + ' QUANTIFIER+WH-WORD ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The QUANTIFIER+WH-WORD part of speech has the category of: np\\n -->""", file=f_OUT)
                    print(f"""    <family name="QUANTIFIER+WH-WORD" pos="{pos_tag}">
      <entry name="np\\n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if quantifier_underscore_plus_underscore_wh_word_match:
                quantifier_underscore_plus_underscore_wh_word_count += 1
                pos_tag = quantifier_underscore_plus_underscore_wh_word_match.group()
                if quantifier_underscore_plus_underscore_wh_word_count == 1:
                    print('  <!-- ' + '=' * 36 + ' QUANTIFIER_+_WH-WORD ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The QUANTIFIER_+_WH-WORD part of speech has the category of: np/n  -->""", file=f_OUT)
                    print(f"""    <family name="QUANTIFIER_+_WH-WORD" pos="{pos_tag}">
      <entry name="np/n">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if reflexive_match:
                reflexive_count += 1
                pos_tag = reflexive_match.group()
                if reflexive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' REFLEXIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The REFLEXIVE part of speech has the categories of: np, np/np, np\\np  -->""", file=f_OUT)
                    print(f"""    <family name="" pos="{pos_tag}">
      <entry name="np">
        <atomcat type="np"/>
      </entry>

      <entry name="np/np">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>

      <entry name="np\\np">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if tense_match:
                tense_count += 1
                pos_tag = tense_match.group()
                if tense_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The TENSE part of speech has the category of: (s\\np)/(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="TENSE" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if tense_plus_aspect_match:
                tense_plus_aspect_count += 1
                pos_tag = tense_plus_aspect_match.group()
                if tense_plus_aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE+ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The TENSE+ASPECT part of speech has the category of: (s\\np)/(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if tense_underscore_plus_underscore_aspect_match:
                tense_underscore_plus_underscore_aspect_count += 1
                pos_tag = tense_underscore_plus_underscore_aspect_match.group()
                if tense_underscore_plus_underscore_aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE_+_ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The TENSE_+_ASPECT part of speech has the category of: (s\\np)/(s\\np)  -->""", file=f_OUT)
                    print(f"""    <family name="TENSE_+_ASPECT" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if tense_plus_negation_match:
                tense_plus_negation_count += 1
                pos_tag = tense_plus_negation_match.group()
                if tense_plus_negation_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE+NEGATION ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The TENSE+NEGATION part of speech has the category of: (s\\np)/(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="TENSE+NEGATION" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if tense_underscore_plus_underscore_negative_match:
                tense_underscore_plus_underscore_negative_count += 1
                pos_tag = tense_underscore_plus_underscore_negative_match.group()
                if tense_underscore_plus_underscore_negative_count == 1:
                    print('  <!-- ' + '=' * 36 + ' TENSE_+_NEGATIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The TENSE_+_NEGATIVE part of speech has the category of: (s\\np)/(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="TENSE_+_NEGATIVE" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if verb_plus_aspect_match:
                verb_plus_aspect_count += 1
                pos_tag = verb_plus_aspect_match.group()
                if verb_plus_aspect_count == 1:
                    print('  <!-- ' + '=' * 36 + ' VERB+ASPECT ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The VERB+ASPECT part of speech has the category of:(s\\np)/(s\\np) -->""", file=f_OUT)
                    print(f"""    <family name="VERB+ASPECT" pos="{pos_tag}">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>          
          </complexcat>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if verb_ditransitive_match:
                verb_ditransitive_count += 1
                pos_tag = verb_ditransitive_match.group()
                if verb_ditransitive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' VERB-DITRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The VERB-DITRANSITIVE part of speech has the category of: ((s\\np)/np)/np -->""", file=f_OUT)
                    print(f"""    <family name="VERB-DITRANSITIVE" pos="{pos_tag}">
      <entry name="((s\\np)/np)/np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if verb_intransitive_match:
                verb_intransitive_count += 1
                pos_tag = verb_intransitive_match.group()
                if verb_intransitive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' VERB-INTRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The VERB-INTRANSITIVE part of speech has the category of: s\\np -->""", file=f_OUT)
                    print(f"""    <family name="VERB-INTRANSITIVE" pos="{pos_tag}">
      <entry name="s\\np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if verb_transitive_match:
                verb_transitive_count += 1
                pos_tag = verb_transitive_match.group()
                if verb_transitive_count == 1:
                    print('  <!-- ' + '=' * 36 + ' VERB-TRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The VERB-TRANSITIVE part of speech has the category of: (s\\np)/np -->""", file=f_OUT)
                    print(f"""    <family name="VERB-TRANSITIVE" pos="{pos_tag}">
      <entry name="(s\\np)/np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if verb_transitive_match:
                verb_transitive_count += 1
                pos_tag = verb_transitive_match.group()
                if verb_transitive_count == 2:
                    print('  <!-- ' + '=' * 36 + ' VERB-TRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The VERB-TRANSITIVE part of speech has the category of: (s\\np)/s/np -->""", file=f_OUT)
                    print("""  <!-- This is a closed class family for transitive verbs with sentential complements-->""",file=f_OUT)
                    print(f"""    <family name="VERB-TRANSITIVE" pos="{pos_tag}" closed="true">
      <entry name="(s\\np)/s/np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="s"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
      <member stem="1hADMIT"/>
      <member stem="1hIMAGINE"/>
      <member stem="1hNOTICE*j"/>
      <member stem="1hWANT"/>
      <member stem="ASK_2"/>
      <member stem="ASK_2*k"/>
      <member stem="CAUSE"/>
      <member stem="DECIDE"/>
      <member stem="KNOW"/>
      <member stem="KNOW+"/>
      <member stem="KNOW-THAT"/>
      <member stem="REFUSE"/>
      <member stem="REQUIRE"/>
      <member stem="SUGGEST"/>
      <member stem="TELL"/>
      <member stem="TELL*k"/>
      <member stem="TELL*l"/>
      <member stem="TELL*m"/>
      <member stem="TELL*n"/>
      <member stem="TELL*p"/>
      <member stem="TELL*t"/>
      <member stem="TELL*u"/>
      <member stem="TELL*j"/>
      <member stem="TELL*i"/>
    </family>\n""", file=f_OUT)

            if verb_transitive_match:
                verb_transitive_count += 1
                pos_tag = verb_transitive_match.group()
                if verb_transitive_count == 3:
                    print('  <!-- ' + '=' * 36 + ' VERB-TRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The VERB-TRANSITIVE part of speech has the category of: (s\\np)/(s\\np) -->""", file=f_OUT)
                    print("""  <!-- This is a closed class family for transitive verbs with sentential complements-->""", file=f_OUT)
                    print(f"""    <family name="VERB-TRANSITIVE" pos="{pos_tag}" closed="true">
      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>
          </complexcat>
        </complexcat>
      </entry>
      <member stem="GO"/>
      <member stem="j*GO"/>
    </family>\n""", file=f_OUT)

            if verb_transitive_match:
                verb_transitive_count += 1
                pos_tag = verb_transitive_match.group()
                if verb_transitive_count == 4:
                    print('  <!-- ' + '=' * 36 + ' VERB-TRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The VERB-TRANSITIVE part of speech has the category of: (s\\np)/s -->""", file=f_OUT)
                    print("""  <!-- This is a closed class family for transitive verbs with sentential complements-->""",file=f_OUT)
                    print(f"""    <family name="VERB-TRANSITIVE" pos="{pos_tag}" closed="true">
      <entry name="s\\np/s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>
      <member stem="SAY"/>
      <member stem="KNOW"/>
      <member stem="DECIDE"/>
      <member stem="WANT"/>
    </family>\n""", file=f_OUT)

            if wh_word_match:
                wh_word_count += 1
                pos_tag = wh_word_match.group()
                if wh_word_count == 1:
                    print('  <!-- ' + '=' * 36 + ' WH-WORD ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The WH-WORD part of speech has the categories of: np -->""", file=f_OUT)
                    print(f"""    <family name="WH-WORD" pos="{pos_tag}">
      <entry name="np">
        <atomcat type="np"/>
      </entry>
    </family>\n""", file=f_OUT)

            if wh_word_match:
                pos_tag = wh_word_match.group()
                if wh_word_count == 2:
                    print('  <!-- ' + '=' * 36 + ' WH-WORD ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The WH-WORD part of speech has the categories of: s/s, s\\s -->""", file=f_OUT)
                    print(f"""    <family name="WH-WORD" pos="{pos_tag}" closed="true">
      <entry name="s/s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="/" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>

      <entry name="s\\s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>
      <member stem="#WHEN"/>
      <member stem="#WHY"/>
      <member stem="(1h)HOW-MANY/MANY"/>
      <member stem="(25)WHY"/>
      <member stem="(Y)WHY"/>
      <member stem="(Y)WHY+"/>
      <member stem="HOW"/>
      <member stem="HOW+"/>
      <member stem="HOW-MANY/MANY"/>
      <member stem="WHY^NOT"/>
    </family>\n""", file=f_OUT)

            if wh_plus_particle_match:
                wh_plus_particle_count += 1
                pos_tag = wh_plus_particle_match.group()
                if wh_plus_particle_count == 1:
                    print('  <!-- ' + '=' * 36 + ' WH+PARTICLE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The WH+PARTICLE part of speech has the category of: s\\s -->""", file=f_OUT)
                    print(f"""    <family name="WH+PARTICLE" pos="{pos_tag}">
      <entry name="s\\s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if xxx_intrans_match:
                xxx_intrans_count += 1
                pos_tag = xxx_intrans_match.group()
                if xxx_intrans_count == 1:
                    print('  <!-- ' + '=' * 36 + ' XXX-INTRANSITIVE ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The XXX-INTRANSITIVE part of speech has the category of: s\\np -->""", file=f_OUT)
                    print(f"""    <family name="XXX-INTRANSITIVE" pos="{pos_tag}">
      <entry name="s\\np">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if xxx_match:
                xxx_count += 1
                pos_tag = xxx_match.group()
                if xxx_count == 1:
                    print('  <!-- ' + '=' * 36 + ' XXX ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The XXX part of speech has the categories of: s\\s, s/s -->""", file=f_OUT)
                    print(f"""    <family name="XXX" pos="{pos_tag}">
      <entry name="s\\s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>

      <entry name="s/s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="/" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>
    </family>\n""", file=f_OUT)

            if xxx_match:
                pos_tag = xxx_match.group()
                if xxx_count == 2:
                    print('  <!-- ' + '=' * 36 + ' XXX ' + '=' * 36 + ' -->', file=f_OUT)
                    print("""  <!-- The XXX  part of speech has the category of: n/n, np/np, (s\\np)/(s\\np), s/s  -->""", file=f_OUT)
                    print(f"""    <family name="XXX" pos="{pos_tag}" closed="true">
      <entry name="n/n">
        <complexcat>
          <atomcat type="n"/>
          <slash dir="/" mode="."/>
          <atomcat type="n"/>
        </complexcat>
      </entry>

      <entry name="np/np">
        <complexcat>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </entry>

      <entry name="(s\\np)/(s\\np)">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="\\" mode="."/>
          <atomcat type="np"/>
          <slash dir="/" mode="."/>
          <complexcat>
            <atomcat type="s"/>
            <slash dir="\\" mode="."/>
            <atomcat type="np"/>
          </complexcat>
        </complexcat>
      </entry>

      <entry name="s/s">
        <complexcat>
          <atomcat type="s"/>
          <slash dir="/" mode="."/>
          <atomcat type="s"/>
        </complexcat>
      </entry>
      <member stem="false_start"/>
      <member stem="'focus'"/>
      <member stem="(1)'focus'"/>
      <member stem="(G)'focus'"/>
      <member stem="1'focus'"/>
      <member stem="5'focus'"/>
      <member stem="5'focus'*i"/>
      <member stem="B'focus'"/>
      <member stem="B-L'focus'"/>
      <member stem="G'focus'"/>
      <member stem="H'focus'"/>
      <member stem="L'focus'"/>
    </family>\n""", file=f_OUT)



        print('\n</lexicon>\n', file=f_OUT)





