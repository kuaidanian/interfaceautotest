import json

json_data = """{
   "favourite":{
      "bkmrk":{
         "id1490843709594066":{
            "guid":"904eff52277f403b89f6410fe2758646.11",
            "lcate":"1"
         },
         "id1490843712805183":{
            "guid":"58457f60eca64025bc43a978f9c98345.16",
            "lcate":"2"
         },
         "id149084371467327":{
            "guid":"a0f907f9dc8b40f689b083f3eba7228b.16",
            "lcate":"3"
         },
         "id1490843716295393":{
            "guid":"eb75d929455e468bb712e7bc2025d11a.16",
            "lcate":"4"
         }
      }
   }
}"""

data = json.loads(json_data)
for v in data['favourite']['bkmrk'].values():
    print("%s;%s" % (v['lcate'],  v['guid']))