import os
import json
from  import Elasticsearch

# Search utility for lunhg/WebWhatsapp-Wrapper
# Usage
# logger = Logger(<options>)
# #Options
# - config: an Array of dictionaries that define a host and a port for a server to Elasticsearch
# - index: the term to be found
class Elasticsearch(object):

  def __init__(self, **kwargs):
    self.driver = kwargs.get('driver')

  def setup(self, **kwargs):
    self.es = elasticsearch.Elasticsearch(kwargs.get('config'))
    self.index = kwargs.get('index')

  # Implement a handle function to be called on
  # lunhg/Webwhatsapp-Wrapper
  def handle(self, chat, message):
    result = self.es.search(index=self.index, body={
      'query': {
        'match': {
          'tag': message.content
        }
      }
    })
    hits = result['hits']['hits']
    if len(hits) == 0:
      chat.send_message('Não achei nenhum termo correspondente')
      return
    hits = hits[:3]
    hits.reverse()
    for term in hits:
      self.driver.send_media(term['_source']['path'], chat.id, '')
