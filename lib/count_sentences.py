#!/usr/bin/env python3

class MyString:
  def __init__(self):
    self._word="Hey"

  @property
  def value(self):
    return self._word
  
  @value.setter
  def value(self,new_value):
    if type(new_value) is str:
      self._word=new_value

    else:
      print("The value must be a string.")
  def is_sentence(self):
    return self._word.endswith(".")
  def is_question(self):
    return self._word.endswith("?")
  def is_exclamation(self):
    return self._word.endswith("?")
  def count_sentences(self):
    modified_version=self.word.replace("!","*").replace(".","*").replace("?","*")
    the_list=modified_version.split("* ")
    return len(the_list)
    
# string=MyString()
# string.value="Hallo"
# print(string.value)
