import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')
matcher = Matcher(nlp.vocab)
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
         s.append(token.dep_)
      print (token.text, token.tag_, token.head.text, token.dep_)
   return s
def give_directobj(nlp_doc):
   s = []
   for token in nlp_doc:
      if token.dep_ == "dobj":
         s.append(token.dep_)
      print (token.text, token.tag_, token.head.text, token.dep_)
   return s
def give_ROOT(nlp_doc):
   s = []
   for token in nlp_doc:
      if token.dep_ == "ROOT":
         s.append(token)
      print (token.text, token.tag_, token.head.text, token.dep_)
   return s
def give_nounchunks(nlp_doc):
   return nlp_doc.noun_chunks
def give_namedentities(nlp_doc):
   return nlp_doc.ents
