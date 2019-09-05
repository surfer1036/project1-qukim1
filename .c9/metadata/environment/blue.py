{"changed":true,"filter":false,"title":"blue.py","tooltip":"/blue.py","value":"import random, requests, json\nimport flask\nimport os\n\n\napp = flask.Flask(__name__)\n\n\napi_token = '3yEHJrYc03grMh7SUZsRlZKDlQv-3NK0EyJ3iZQquV69HlpaCU9p28OoUejFOLu5'\nurl = \"https://api.genius.com/search?q=Outkast\"\nmy_headers = {\n    \"Authorization\": \"Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-\"\n}\n\nresponse = requests.get(url, headers=my_headers)\njson_body = response.json()\n\n\n@app.route(\"/\")  \ndef index(): \n    r = random.randint(1, 10)\n    photo = json_body[\"response\"][\"hits\"][r][\"result\"][\"song_art_image_url\"]\n    title = json_body[\"response\"][\"hits\"][r][\"result\"][\"full_title\"]\n    artist = json_body[\"response\"][\"hits\"][r][\"result\"][\"primary_artist\"][\"image_url\"]\n    \n    return flask.render_template(\n       \"index.html\",\n        album_src=photo, title_src=title, artist_src=artist) \n  \napp.run(\n    port=int(os.getenv('PORT', 8080)),\n    host=os.getenv('IP', '0.0.0.0')\n)\n","undoManager":{"mark":103,"position":100,"stack":[[{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"insert","lines":[" "],"id":591}],[{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"insert","lines":["a"],"id":592},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"insert","lines":["r"]},{"start":{"row":30,"column":44},"end":{"row":30,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":45},"end":{"row":30,"column":46},"action":"insert","lines":["i"],"id":593},{"start":{"row":30,"column":46},"end":{"row":30,"column":47},"action":"insert","lines":["s"]},{"start":{"row":30,"column":47},"end":{"row":30,"column":48},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":48},"end":{"row":30,"column":49},"action":"insert","lines":["_"],"id":594},{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"insert","lines":["s"]},{"start":{"row":30,"column":50},"end":{"row":30,"column":51},"action":"insert","lines":["r"]},{"start":{"row":30,"column":51},"end":{"row":30,"column":52},"action":"insert","lines":["c"]}],[{"start":{"row":30,"column":52},"end":{"row":30,"column":53},"action":"insert","lines":["="],"id":595}],[{"start":{"row":30,"column":53},"end":{"row":30,"column":54},"action":"insert","lines":["a"],"id":596},{"start":{"row":30,"column":54},"end":{"row":30,"column":55},"action":"insert","lines":["r"]},{"start":{"row":30,"column":55},"end":{"row":30,"column":56},"action":"insert","lines":["t"]},{"start":{"row":30,"column":56},"end":{"row":30,"column":57},"action":"insert","lines":["o"]},{"start":{"row":30,"column":57},"end":{"row":30,"column":58},"action":"insert","lines":["s"]}],[{"start":{"row":30,"column":57},"end":{"row":30,"column":58},"action":"remove","lines":["s"],"id":597},{"start":{"row":30,"column":56},"end":{"row":30,"column":57},"action":"remove","lines":["o"]},{"start":{"row":30,"column":55},"end":{"row":30,"column":56},"action":"remove","lines":["t"]}],[{"start":{"row":30,"column":55},"end":{"row":30,"column":56},"action":"insert","lines":["t"],"id":598},{"start":{"row":30,"column":56},"end":{"row":30,"column":57},"action":"insert","lines":["i"]},{"start":{"row":30,"column":57},"end":{"row":30,"column":58},"action":"insert","lines":["s"]},{"start":{"row":30,"column":58},"end":{"row":30,"column":59},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":59},"end":{"row":30,"column":60},"action":"insert","lines":["g"],"id":599},{"start":{"row":30,"column":60},"end":{"row":30,"column":61},"action":"insert","lines":["i"]},{"start":{"row":30,"column":61},"end":{"row":30,"column":62},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":62},"end":{"row":30,"column":63},"action":"insert","lines":[" "],"id":600}],[{"start":{"row":30,"column":62},"end":{"row":30,"column":63},"action":"remove","lines":[" "],"id":601},{"start":{"row":30,"column":61},"end":{"row":30,"column":62},"action":"remove","lines":["t"]},{"start":{"row":30,"column":60},"end":{"row":30,"column":61},"action":"remove","lines":["i"]},{"start":{"row":30,"column":59},"end":{"row":30,"column":60},"action":"remove","lines":["g"]}],[{"start":{"row":33,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["#    title = json_body[\"response\"][\"hits\"][0][\"result\"][\"full_title\"]","#    return flask.render_template(","#        \"index.html\",","#        title_src=title)","    "],"id":602},{"start":{"row":32,"column":8},"end":{"row":33,"column":0},"action":"remove","lines":["",""]},{"start":{"row":32,"column":4},"end":{"row":32,"column":8},"action":"remove","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"remove","lines":["    "]},{"start":{"row":31,"column":3},"end":{"row":32,"column":0},"action":"remove","lines":["",""]},{"start":{"row":31,"column":2},"end":{"row":31,"column":3},"action":"remove","lines":[" "]}],[{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"remove","lines":["",""],"id":603},{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":47},"end":{"row":12,"column":0},"action":"remove","lines":["",""],"id":604}],[{"start":{"row":9,"column":78},"end":{"row":10,"column":0},"action":"remove","lines":["",""],"id":605}],[{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"remove","lines":["2"],"id":606}],[{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"insert","lines":["1"],"id":607}],[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"remove","lines":["r"],"id":608}],[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"insert","lines":["0"],"id":609}],[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"remove","lines":["0"],"id":610}],[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"insert","lines":["1"],"id":611}],[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"remove","lines":["1"],"id":612}],[{"start":{"row":25,"column":43},"end":{"row":25,"column":44},"action":"insert","lines":["0"],"id":613}],[{"start":{"row":25,"column":57},"end":{"row":25,"column":66},"action":"remove","lines":["image_url"],"id":614},{"start":{"row":25,"column":57},"end":{"row":25,"column":66},"action":"insert","lines":["image_url"]}],[{"start":{"row":25,"column":4},"end":{"row":25,"column":68},"action":"remove","lines":["artist = json_body[\"response\"][\"hits\"][0][\"result\"][\"image_url\"]"],"id":616}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"insert","lines":["#"],"id":617}],[{"start":{"row":30,"column":1},"end":{"row":30,"column":65},"action":"insert","lines":["artist = json_body[\"response\"][\"hits\"][0][\"result\"][\"image_url\"]"],"id":618}],[{"start":{"row":30,"column":65},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":619},{"start":{"row":31,"column":0},"end":{"row":31,"column":1},"action":"insert","lines":["#"]}],[{"start":{"row":28,"column":40},"end":{"row":28,"column":59},"action":"remove","lines":[", artist_src=artist"],"id":620}],[{"start":{"row":31,"column":1},"end":{"row":31,"column":20},"action":"insert","lines":[", artist_src=artist"],"id":621}],[{"start":{"row":31,"column":20},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":622}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "],"id":623}],[{"start":{"row":32,"column":4},"end":{"row":32,"column":5},"action":"insert","lines":["p"],"id":624},{"start":{"row":32,"column":5},"end":{"row":32,"column":6},"action":"insert","lines":["r"]},{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"insert","lines":["i"]},{"start":{"row":32,"column":7},"end":{"row":32,"column":8},"action":"insert","lines":["n"]},{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":32,"column":9},"end":{"row":32,"column":11},"action":"insert","lines":["()"],"id":625}],[{"start":{"row":32,"column":9},"end":{"row":32,"column":11},"action":"remove","lines":["()"],"id":626},{"start":{"row":32,"column":8},"end":{"row":32,"column":9},"action":"remove","lines":["t"]},{"start":{"row":32,"column":7},"end":{"row":32,"column":8},"action":"remove","lines":["n"]},{"start":{"row":32,"column":6},"end":{"row":32,"column":7},"action":"remove","lines":["i"]},{"start":{"row":32,"column":5},"end":{"row":32,"column":6},"action":"remove","lines":["r"]},{"start":{"row":32,"column":4},"end":{"row":32,"column":5},"action":"remove","lines":["p"]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "],"id":627}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":5},"action":"insert","lines":["p"],"id":628},{"start":{"row":33,"column":5},"end":{"row":33,"column":6},"action":"insert","lines":["r"]},{"start":{"row":33,"column":6},"end":{"row":33,"column":7},"action":"insert","lines":["i"]},{"start":{"row":33,"column":7},"end":{"row":33,"column":8},"action":"insert","lines":["n"]},{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":33,"column":9},"end":{"row":33,"column":11},"action":"insert","lines":["()"],"id":629}],[{"start":{"row":33,"column":10},"end":{"row":33,"column":65},"action":"insert","lines":["json_body[\"response\"][\"hits\"][0][\"result\"][\"image_url\"]"],"id":630}],[{"start":{"row":33,"column":3},"end":{"row":33,"column":66},"action":"remove","lines":[" print(json_body[\"response\"][\"hits\"][0][\"result\"][\"image_url\"])"],"id":631}],[{"start":{"row":24,"column":68},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":632},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":25,"column":4},"end":{"row":26,"column":0},"action":"insert","lines":["",""]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":67},"action":"insert","lines":[" print(json_body[\"response\"][\"hits\"][0][\"result\"][\"image_url\"])"],"id":633}],[{"start":{"row":26,"column":4},"end":{"row":26,"column":5},"action":"remove","lines":[" "],"id":634}],[{"start":{"row":26,"column":66},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":635},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":27,"column":4},"end":{"row":28,"column":0},"action":"insert","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":24,"column":68},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":636},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":25,"column":4},"end":{"row":26,"column":0},"action":"insert","lines":["",""]},{"start":{"row":26,"column":0},"end":{"row":26,"column":4},"action":"insert","lines":["    "]},{"start":{"row":26,"column":4},"end":{"row":27,"column":0},"action":"insert","lines":["",""]},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "]},{"start":{"row":27,"column":4},"end":{"row":28,"column":0},"action":"insert","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]},{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"insert","lines":["",""]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["p"]},{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["r"]},{"start":{"row":29,"column":6},"end":{"row":29,"column":7},"action":"insert","lines":["i"]},{"start":{"row":29,"column":7},"end":{"row":29,"column":8},"action":"insert","lines":["n"]},{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":29,"column":9},"end":{"row":29,"column":11},"action":"insert","lines":["()"],"id":637}],[{"start":{"row":29,"column":10},"end":{"row":29,"column":12},"action":"insert","lines":["\"\""],"id":638}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"insert","lines":["p"],"id":639},{"start":{"row":30,"column":5},"end":{"row":30,"column":6},"action":"insert","lines":["r"]},{"start":{"row":30,"column":6},"end":{"row":30,"column":7},"action":"insert","lines":["i"]},{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":["n"]},{"start":{"row":30,"column":8},"end":{"row":30,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":9},"end":{"row":30,"column":11},"action":"insert","lines":["()"],"id":640}],[{"start":{"row":30,"column":10},"end":{"row":30,"column":39},"action":"insert","lines":["json_body[\"response\"][\"hits\"]"],"id":641}],[{"start":{"row":29,"column":4},"end":{"row":31,"column":66},"action":"remove","lines":["print(\"\")","    print(json_body[\"response\"][\"hits\"])","    print(json_body[\"response\"][\"hits\"][0][\"result\"][\"image_url\"])"],"id":642}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":643}],[{"start":{"row":18,"column":0},"end":{"row":20,"column":66},"action":"insert","lines":["print(\"\")","    print(json_body[\"response\"][\"hits\"])","    print(json_body[\"response\"][\"hits\"][0][\"result\"][\"image_url\"])"],"id":644}],[{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"remove","lines":["    "],"id":645}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "],"id":646}],[{"start":{"row":32,"column":2},"end":{"row":32,"column":3},"action":"insert","lines":["\\"],"id":647}],[{"start":{"row":32,"column":2},"end":{"row":32,"column":3},"action":"remove","lines":["\\"],"id":648},{"start":{"row":32,"column":1},"end":{"row":32,"column":2},"action":"remove","lines":[" "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":1},"action":"remove","lines":[" "]},{"start":{"row":31,"column":4},"end":{"row":32,"column":2},"action":"remove","lines":["","  "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"remove","lines":["    "]},{"start":{"row":30,"column":4},"end":{"row":31,"column":0},"action":"remove","lines":["",""]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":30,"column":0},"action":"remove","lines":["",""]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "]},{"start":{"row":28,"column":4},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":7},"end":{"row":18,"column":8},"action":"insert","lines":["*"],"id":649},{"start":{"row":18,"column":8},"end":{"row":18,"column":9},"action":"insert","lines":["*"]},{"start":{"row":18,"column":9},"end":{"row":18,"column":10},"action":"insert","lines":["*"]},{"start":{"row":18,"column":10},"end":{"row":18,"column":11},"action":"insert","lines":["*"]}],[{"start":{"row":19,"column":35},"end":{"row":19,"column":37},"action":"insert","lines":["[]"],"id":650}],[{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"insert","lines":["0"],"id":651}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":1},"action":"insert","lines":["#"],"id":652}],[{"start":{"row":19,"column":38},"end":{"row":19,"column":40},"action":"insert","lines":["[]"],"id":653}],[{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"insert","lines":["r"],"id":654},{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"remove","lines":["e"],"id":655},{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"remove","lines":["r"]}],[{"start":{"row":19,"column":39},"end":{"row":19,"column":41},"action":"insert","lines":["''"],"id":656}],[{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"insert","lines":["r"],"id":657},{"start":{"row":19,"column":41},"end":{"row":19,"column":42},"action":"insert","lines":["e"]},{"start":{"row":19,"column":42},"end":{"row":19,"column":43},"action":"insert","lines":["s"]},{"start":{"row":19,"column":43},"end":{"row":19,"column":44},"action":"insert","lines":["u"]},{"start":{"row":19,"column":44},"end":{"row":19,"column":45},"action":"insert","lines":["l"]},{"start":{"row":19,"column":45},"end":{"row":19,"column":46},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"remove","lines":["'"],"id":658}],[{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"insert","lines":["\""],"id":659}],[{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"remove","lines":["'"],"id":660}],[{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"insert","lines":["\""],"id":661}],[{"start":{"row":19,"column":48},"end":{"row":19,"column":50},"action":"insert","lines":["[]"],"id":662}],[{"start":{"row":19,"column":49},"end":{"row":19,"column":51},"action":"insert","lines":["\"\""],"id":663}],[{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"insert","lines":["x"],"id":664}],[{"start":{"row":19,"column":51},"end":{"row":19,"column":65},"action":"insert","lines":["primary_artist"],"id":665}],[{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"remove","lines":["x"],"id":666}],[{"start":{"row":19,"column":66},"end":{"row":19,"column":68},"action":"insert","lines":["[]"],"id":667}],[{"start":{"row":19,"column":67},"end":{"row":19,"column":76},"action":"insert","lines":["image_url"],"id":668}],[{"start":{"row":19,"column":76},"end":{"row":19,"column":77},"action":"insert","lines":["\""],"id":669}],[{"start":{"row":19,"column":67},"end":{"row":19,"column":68},"action":"insert","lines":["\""],"id":670}],[{"start":{"row":20,"column":0},"end":{"row":20,"column":63},"action":"remove","lines":["#print(json_body[\"response\"][\"hits\"][0][\"result\"][\"image_url\"])"],"id":671},{"start":{"row":19,"column":80},"end":{"row":20,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":33,"column":40},"end":{"row":33,"column":59},"action":"insert","lines":[", artist_src=artist"],"id":672}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":77},"action":"insert","lines":["json_body[\"response\"][\"hits\"][0][\"result\"][\"primary_artist\"][\"image_url\"]"],"id":673}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["a"],"id":674},{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["r"]},{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["t"]},{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["i"]},{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"remove","lines":["s"],"id":675}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["s"],"id":676},{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":[" "],"id":677},{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["="]}],[{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":[" "],"id":678}],[{"start":{"row":35,"column":0},"end":{"row":36,"column":20},"action":"remove","lines":["#artist = json_body[\"response\"][\"hits\"][0][\"result\"][\"image_url\"]","#, artist_src=artist"],"id":679},{"start":{"row":35,"column":0},"end":{"row":35,"column":1},"action":"insert","lines":["]"]}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":1},"action":"remove","lines":["]"],"id":680}],[{"start":{"row":28,"column":4},"end":{"row":29,"column":4},"action":"remove","lines":["","    "],"id":681},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "]},{"start":{"row":27,"column":86},"end":{"row":28,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":35,"column":2},"end":{"row":35,"column":3},"action":"remove","lines":[" "],"id":682},{"start":{"row":35,"column":1},"end":{"row":35,"column":2},"action":"remove","lines":[" "]},{"start":{"row":35,"column":0},"end":{"row":35,"column":1},"action":"remove","lines":[" "]},{"start":{"row":34,"column":4},"end":{"row":35,"column":0},"action":"remove","lines":["",""]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"remove","lines":["    "]},{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["",""]},{"start":{"row":32,"column":2},"end":{"row":33,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":18,"column":0},"end":{"row":20,"column":0},"action":"remove","lines":["print(\"****\")","print(json_body[\"response\"][\"hits\"][0][\"result\"][\"primary_artist\"][\"image_url\"])",""],"id":683},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":24,"column":43},"end":{"row":24,"column":44},"action":"remove","lines":["0"],"id":684}],[{"start":{"row":24,"column":43},"end":{"row":24,"column":44},"action":"insert","lines":["r"],"id":685}],[{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["\\"],"id":686}],[{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":["\\"],"id":687},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":["#"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":24},"action":"remove","lines":["import requests_oauthlib"],"id":688},{"start":{"row":0,"column":29},"end":{"row":1,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":34,"column":0},"end":{"row":43,"column":0},"action":"remove","lines":["","\"\"\" ","url = \"https://api.twitter.com/1.1/account/verify_credentials.json\"","oauth = requests_oauthlib.OAuth1(","    \"C7naPh6NBJhMYBX1JMAnLX67d\", ","    \"AkZqf5Dq6cnVlpVfMYDuGTaA3y0SLOxjGcS98swGs94ItLH1EL\",","    \"3846948017-Vsqn57lvX9zmjtslCoA0gENtbs3jJP21OkyPvYQ\",","    \"EVunEKabWXO69Kqi6uqkgIhxgUkzSwWayk1JsT9y77R1G\"",")",""],"id":689}],[{"start":{"row":39,"column":1},"end":{"row":42,"column":0},"action":"remove","lines":["print(response.json())","","\"\"\"",""],"id":690},{"start":{"row":39,"column":0},"end":{"row":39,"column":1},"action":"remove","lines":["#"]},{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":35,"column":0},"end":{"row":36,"column":0},"action":"remove","lines":["",""],"id":691},{"start":{"row":34,"column":0},"end":{"row":35,"column":0},"action":"remove","lines":["",""]},{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":33,"column":0},"end":{"row":35,"column":0},"action":"remove","lines":["","response = requests.get(url, auth=oauth)",""],"id":692}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":75},"action":"insert","lines":["https://api.twitter.com/1.1/search?q=outkast&src=recent_search_click"],"id":695}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"remove","lines":["t"],"id":695}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":45},"action":"remove","lines":["https://api.genius.com/search?q=Outkas"],"id":696}]]},"ace":{"folds":[],"scrolltop":127,"scrollleft":0,"selection":{"start":{"row":18,"column":17},"end":{"row":18,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567712004431}