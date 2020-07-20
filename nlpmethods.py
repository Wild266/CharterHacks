import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)

MY_FNAME = "SARA"
MY_LNAME = "SARA"

def respond(text, transcript, sentiment):
   text = text.lower()
   transcript.append(text)
   matcher = Matcher(nlp.vocab)
   doc = nlp(text)
   response = ""
   namedentities = give_namedentities(doc)
   print(namedentities)
   if len(namedentities)>0:
      response += f"Does {namedentities[0]} interest you?"
      return response


#   full_name = extract_full_name(doc)
   basin = give_base(doc)
   subjects = give_subjects(doc)
   directobjs = give_directobj(doc)
   roots = give_ROOT(doc)
#    nc = give_nounchunks(doc)
   if len(subjects)>=1:
      return f"Oh! I'm a chatbot so I don't know what a {subjects[0]} is. Could you tell me about it? Please"
   if len(directobjs) >=1:
      return f"Tell me more about {directobjs[0]}"
   if text == "yes":
      return "Great! I can't wait"
   if text == "no":
      return "why not?"
   if "your name" in text or "SARA" in text:
         return "My name is SARA"

   
   if nlp("do") in roots:
      if "die" in basin:
         response = "do you want to talk about it?"
         return response
      if sentiment == "POSITIVE":
         return "You make me feel good :)"
   response = "Interesting, would you like to tell me more?"
   return response





def extract_full_name(nlp_doc):
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    matcher.add('FULL_NAME', None, pattern)
    matches = matcher(nlp_doc)
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        return span.text
def give_base(introduction_doc):
   print ([token.text for token in introduction_doc])
   sentences = list(introduction_doc.sents)
   coreword = [token for token in introduction_doc if not token.is_stop]
   basewords = []
   for token in coreword:
        basewords.append(token.lemma_)
   return basewords
def give_subjects(nlp_doc):
   s = []
   for token in nlp_doc:
      if token.dep_ == "nsubj":
         s.append(token.text)
      #print (token.text, token.tag_, token.head.text, token.dep_)
   return s
def give_directobj(nlp_doc):
   s = []
   for token in nlp_doc:
      if token.dep_ == "dobj":
         s.append(token.text)
      #print (token.text, token.tag_, token.head.text, token.dep_)
   return s
def give_ROOT(nlp_doc):
   s = []
   for token in nlp_doc:
      if token.dep_ == "ROOT":
         s.append(token)
      #print (token.text, token.tag_, token.head.text, token.dep_)
   return s
def give_nounchunks(nlp_doc):
   return nlp_doc.noun_chunks
def give_namedentities(nlp_doc):
   return nlp_doc.ents
