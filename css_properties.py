import re
def css_properties(css):
    properties = []
    cssList = re.split(';|{|}', css)
    for c in range(len(cssList)):
        if ':' in cssList[c]:
            prop = re.split(':', cssList[c])
            properties.append((prop[0].strip(), prop[1].strip()))
    return properties

'''
# test
print(css_properties("""
#LasVegas .billboard {text-decoration: blink; }

.ninja, #Snowden { visibility: hidden; }


.oliveoil
{
  z-index: 1;
}
.water
{
  z-index: 0;
}

#poop {
  float  : none  ;
  color  : brown ;

  width  : 15cm  ;
  height : 120cm ;
}

.God { position: absolute; display: none; }
#blackhole { padding: -9999em; }

.word {  font-family:    "Comic Sans", "Times New Roman", sans-serif  ;  }
"""))
'''