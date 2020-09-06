The files in this repository were created for a thesis. The thesis document can be found at https://scholarsarchive.byu.edu/etd/8407/.
All the data was downloaded from http://secrets.rutgers.edu/dai/queryPages/querySelection.php. This is the National Center for 
Sign Language and Gesture Resources (NCSLGR) Corpus. This is a corpus of American Sign Language. It was developed under the 
American Sign Language Linguistic Research Project at Boston University under Dr. Carol Neidle. An updated corpus of ASL can be 
found at https://dai.cs.rutgers.edu/dai/s/dai and https://dai.cs.rutgers.edu/dai/s/signbank.

Documentation regarding the NCSLGR Corpus can be found in the following references:

Carol Neidle, Augustine Opoku, Gregory Dimitriadis, and Dimitris Metaxas [2018] NEW Shared & Interconnected ASL Resources: SignStream® 3 Software; DAI 2 for Web Access to Linguistically Annotated Video Corpora; and a Sign Bank. 8th Workshop on the Representation and Processing of Sign Languages: Involving the Language Community (pp. 147-154). LREC 2018, Miyagawa, Japan. May 2018. BU Open Access: https://open.bu.edu/handle/2144/30047 

Carol Neidle and Augustine Opoku [2020]  A User's Guide to the American Sign Language Linguistic Research Project (ASLLRP) Data Access Interface (DAI) 2 — Version 2. Report No. 18, American Sign Language Linguistic Research Project (ASLLRP), Boston University, Boston, MA.



The Python scripts in the "corpus_data_extraction_scripts" folder require the XML files contained in the "ncslgr-xml" folder. The XML files 
serve as input for the Python scripts. These Python scripts will extract all the ASL gloss from the corpus. The extracted gloss can then be 
used as input for the Python scripts in the "openccg_scripts" folder. These scripts build a Combinatory Categorial Grammar grammar of ASL. 
The constructed grammar can then be used by the OpenCCG Parser (http://openccg.sourceforge.net/). OpenCCG will parse the NCSLGR Corpus and 
generate CCG derivational parses of American Sign Language.