file_out_path = r'C:\Users\manua\Desktop\openccg-master\grammars\ASL\rules.xml'

with open(file_out_path, 'w') as f_OUT:
    print("""<?xml version="1.0" encoding="UTF-8"?>

<!--
This file contains the combinatory rules.
-->

<rules
  name="ASL2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="../rules.xsd"
>

  <!-- Application -->
  <application dir="forward"/>
  <application dir="backward"/>

  <!-- Harmonic Composition -->
  <composition dir="forward" harmonic="true"/>
  <composition dir="backward" harmonic="true"/>

  <!-- Crossed Composition -->
  <composition dir="forward" harmonic="false"/>
  <composition dir="backward" harmonic="false"/>

  <!-- Type-raising -->
  <typeraising dir="forward" useDollar="false"/>
  <typeraising dir="backward" useDollar="true"/>
  
  <!-- N-to-NP -->
  <typechanging name="n-to-np">
    <arg>
      <atomcat type="n"/>
    </arg>
    <result>
      <atomcat type="np"/>
    </result>
  </typechanging>
  
  <!-- TOPIC RAISING -->
  <typechanging name="topic">
    <arg>
      <atomcat type="np"/>
    </arg>
    <result>
      <complexcat>
        <atomcat type="s"/>
        <slash dir="/" mode="."/>
        <complexcat>
          <atomcat type="s"/>
          <slash dir="/" mode="."/>
          <atomcat type="np"/>
        </complexcat>
      </complexcat>
    </result>
  </typechanging>
  
  <!-- SUBJECT PRO-DROP -->
  <typechanging name="subj pro-drop">
    <arg>
      <complexcat>
        <atomcat type="s"/>
        <slash dir="\\" mode="."/>
        <atomcat type="np"/>
      </complexcat>
    </arg>
    <result>
      <atomcat type="s"/>
    </result>
  </typechanging>
  
  <!-- OBJECT PRO-DROP -->
  <typechanging name="obj pro-drop">
    <arg>
      <complexcat>
        <atomcat type="s"/>
        <slash dir="\\" mode="."/>
        <atomcat type="np"/>
        <slash dir="/" mode="."/>
        <atomcat type="np"/>
      </complexcat>
    </arg>
    <result>
      <complexcat>
        <atomcat type="s"/>
        <slash dir="\\" mode="."/>
        <atomcat type="np"/>
      </complexcat>
    </result>
  </typechanging>
  
  

  
  <!-- Intrans-topic -->
  <typechanging name="intrans-top">
    <arg>
      <complexcat>
        <atomcat type="s"/>
        <slash dir="\\" mode="."/>
        <atomcat type="np"/>
      </complexcat>
    </arg>
    <result>
      <complexcat>
        <atomcat type="s"/>
        <slash dir="/" mode="."/>
        <atomcat type="np"/>
      </complexcat>
    </result>    
  </typechanging>
  
  <!-- Transitive-topic -->
  <typechanging name="trans-top">
    <arg>
      <complexcat>
        <atomcat type="s"/>
        <slash dir="\\" mode="."/>
        <atomcat type="np"/>
        <slash dir="/" mode="."/>
        <atomcat type="np"/>
      </complexcat>
    </arg>
    <result>
      <complexcat>
        <atomcat type="s"/>
        <slash dir="/" mode="."/>
        <atomcat type="np"/>
        <slash dir="/" mode="."/>
        <atomcat type="np"/>
      </complexcat>
    </result>
  </typechanging>
  
  <!-- SENTENTIAL CONJUNCTION -->
  <typechanging name="sent-conj">
    <arg>
      <atomcat type="s"/>
    </arg>
    <result>
      <complexcat>
        <atomcat type="s"/>
        <slash dir="\\" mode="."/>
        <atomcat type="s"/>
      </complexcat>
    </result>
  </typechanging>
  
  <!-- TWIN (BACKWARD CROSSED COMPOSITION) -->
  <typechanging name="TWIN">
    <arg>
      <atomcat type="np"/>
    </arg>
    <result>
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
    </result>
  </typechanging>
  
  </rules>""", file=f_OUT)

