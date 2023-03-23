import spacy
import fitz
import gradio as gr
import json  #do not import if you do not use it
import PyPDF2
from spacy.tokens import DocBin #do not import if you do not use it
from tqdm import tqdm #do not import if you do not use it
from sklearn.model_selection import train_test_split #do not import if you do not use it


def resume_parser(file_path):
  doc = fitz.open(file_path.name)
  text = ""
  for page in doc:
    text = text + str(page.get_text())
  doc = nlp(text)
  entity_dict = {}
  for ent in doc.ents:
    if ent.label_ not in entity_dict:
      entity_dict[ent.label_] = [ent.text]
    else:
      entity_dict[ent.label_].append(ent.text)
  entity_list = []
  for label, values in entity_dict.items():
    if len(values) == 1:
      entity_list.append({label: values[0]})
    else:
      entity_list.append({label: [value for value in values]})
  return entity_list

demo = gr.Interface(resume_parser,"file", "json")
demo.launch(debug=True,share=True)
