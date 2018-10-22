# Elasticearch

Plugin utility for [lunhg/WebWhatsapp-Wrapper](https://www.github.com/lunhg/WebWhatsapp-Wrapper)

# Download

```
$ git clone https://github.com/lunhg/WebWhatsapp-Wrapper-plugin-elasticsearch <path-to-clone>
```

# Usage

Create a class that implements [lunhg/WebWhatsapp-Wrapper-bot](https://www.github.com/lunhg/WebWhatsapp-Wrapper-bot)


```python
import sys
import os
import json
sys.path.append('<path-to-lunhg/WebWhatsapp-Wrapper-bot>')
import bot

# Implement a abstract bot
class Whatsapp(bot.Bot):

  def __init__(self, **kwargs):
    super(Whatsapp, self).__init__(**kwargs)
    # Open and loads configuration for each
    # plugin
    self.plugin(name='elasticsearch', path='<path-to-lunhg/WebWhatsapp-Wrapper-plugin-elasticsearch>')
    ...
    
  # A simple implementation of setup
  # loaded form configuration readed by a json file
  def setup(self):
    super.setup(self.config)
    ...

  # A simple implementation of run with 0.1 seconds
  # between a call and another call, with
  # implementation of handle methods of logger plugin
  def run(self, handles=[]):
    super.run(frameTime=0.1, callbacks=handles)
 
  # self.attributes and self.
  def search(self):
    return self.getattribute('elasticsearch')

if __name__ is '__main__':
  foobarbaz = Whatsapp(client='firefox', ...)
  
  # { "elasticsearch": [{"host": "localhost", "port": "9200"}] }
  with open('<path-to-config>') as json_data:
    data = json.load(json_data)
    foobarbaz.setup(data)
  
  handleSearch = foobarbaz.search().handle
  foobarbaz.run(handles=[handleSearch])

```

