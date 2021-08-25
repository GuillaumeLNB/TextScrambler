# TextJammer

Using the Unicode confusable characters, we can transform a text to a almost looking like one.
~~~
Usage : python main.py file

Print out the text file using different characters

positional arguments:
  file                  encoded in UTF-8

optional arguments:
  -h, --help            show this help message and exit
  -l LEVEL, --level LEVEL
                        
                                1: insert non printable characters within the text
                                2: replace some latin letters to their Greek or Cyrilic equivalent
                                3: insert non printable characters and change the some latin  to their Greek or Cyrilic equivalent
                                4: insert non printable chraracters change all possible letter to a randomly picked unicode letter equivalent
  -g GENERATE           Scramble x times the string
  -o OUTFILE            The output file

~~~



##Examples

#### Replacing randomly the Latin characters by Greek or Cyrillic letters and adding the ZW(N)J on the demo text:
 
~~~
TextScrambler/src$ python main.py ../txt_files/text_demo.txt  --level 2
  
Неrman Μelvillе (Аugust 1, 1819 – Sерtеmbеr 28, 1891) waѕ аn Amerіcan nοvеliѕt, shοrt stоry wrіtеr, and рoеt οf thе Amеriсаn Rеnaissаnсе реrіοd. Amοng his bеѕt-knοwn works arе Мoby-Diсk (1851), Τyрee (1846), а romаntiсized aсcοunt of his ехperienсеs in Pоlynеѕіа, and Віlly Βudd, Sаilоr, а роѕthumοuѕly рublіshed nοvella. Аlthοugh hiѕ rеputatiоn wаs nоt hіgh аt the tіme оf hіѕ dеath, thе centеnnіаl οf hіѕ bіrth іn 1919 was thе startіng pοint οf a Мelvillе rеvіval аnd Mοby-Dісk grеw to be cоnsіdеrеd оne οf thе grеаt Αmerican novеls.
~~~

Funny thing is search engines can't find the original webpage (as free online plagiarism checkers). Searching for "Μelvillе" (copy-paste it) on Google doesn't return any match, though "Melville" does.

#### Using all of the confusable characters of unicode (see [the unicode confusable characters][1]), we can generate weird looking text worthy of old spam messages : 

~~~
TextScrambler/src$ python main.py ../txt_files/text_demo.txt  --level 4
~~~
  Ⲏ‌𝚎‌𝓻‍m‍а‌n‍ ‍Ꮇ‌𝚎‌𝚕‍𝝂‍𝛊‌𝟷‍ﺎ‍𝓮‍ ‍〔‍𝞐‍ꞟ‌𝒈‍𝞾‍𝔰‌𝗍‌ ‍1‍,‍ ‍1‍8‌1‍𑢬‌ ‍–‍ ‌Տ‌ҽ‌⍴‍𝕥‍𝓮‌m‌𝚋‌𝓮‌𝕣‌ ‌🯲‍𝟾‍,‍ ‍1‍𝟪‌Ꝯ‌1‍〕‍ ‌ꮃ‌𝔞‍ｓ‍ ‌ａ‌𝑛‌ ‍𐊠‌m‍℮‍𝕣‍і‍𝔠‌α‌ռ‌ ‍𝒏‍𝞼‍𝕧‍ℯ‌ᛁ‌𝞲‌𝘴‍𝒕‌ꓹ‍ ‌𝗌‌𝙝‍𑣗‍𝔯‌𝔱‌ ‌𝑠‌𝘵‍𝘰‌𝕣‍γ‍ ‍𝑤‍ⲅ‌𝞲‍𝗍‍𝐞‌𝓻‍,‍ ‌𝒶‍𝓃‍ⅆ‌ ‍𝚙‍𝞼‌𝕖‍𝔱‌ ‍ဝ‍𝖿‌ ‍𝖙‌𝓱‌𝖊‌ ‍ᗅ‌m‌𝖊‍ⲅ‍𝘪‌𝒸‍𝛼‍ռ‍ ‌𝚁‍e‌𝗇‌𝕒‌𝒾‌𝒔‌ｓ‌𝐚‌𝘯‌𝖼‌𝑒‌ ‍𝔭‍𝗲‍ꭈ‍і‍ℴ‍𝔡‍.‌ ‍𝑨‌m‌ⲟ‍𝚗‌ƍ‍ ‌հ‍ⅈ‍𝙨‍ ‌𝙗‍℮‌s‍𝒕‍⁃‌𝕜‌𝗇‌௦‍ա‌n‍ ‍𑜎‍ᴑ‍ⲅ‌k‍ꜱ‍ ‌ɑ‍𝗋‍ｅ‍ ‌𝔐‌ﮩ‌Ꮟ‍𝛄‍‒‍𝖣‌𝖎‍𝙘‌𝓀‍ ‌［‌1‍𞣋‌𑢻‌1‍❳‌,‌ ‍Τ‍ꭚ‍𝐩‍е‌𝖊‍ ‌(‌1‍𝟪‍4‌𝟨‌)‍,‍ ‌𝖆‍ ‍𝒓‌ﻩ‌m‌𝙖‍ո‌𝚝‌𝝸‍𝒄‍ɩ‌𝘇‌𝐞‌𝚍‍ ‍𝖆‌c‌𝓬‍𝗼‌𝘶‌𝒏‍𝖙‌ ‌٥‌𝘧‍ ‌𝗁‌𝕚‍𝙨‌ ‍ℯ‌𝚡‍ⲣ‌℮‌𝚛‌𝐢‍𝒆‌𝒏‌𝑐‍𝐞‌𑣁‍ ‍ı‌𝖓‌ ‌𝑃‍𐓪‌𐊊‍𝛄‌𝐧‍ℯ‌𐑈‌ͺ‍𝛼‍‚‍ ‌𝒶‍𝙣‌𝗱‌ ‌𐊂‍і‍ℑ‌𝝞‌ｙ‍ ‌𝖡‌𝛖‍d‍ⅆ‌ꓹ‍ ‌𐐠‍𝑎‍𝜾‌𝗜‌ഠ‌ꭇ‌٫‍ ‍𝖆‌ ‍𝔭‍ᴏ‍𝒔‍𝑡‌𝘩‍𝚞‌m‌۵‍𝒖‍𝚜‍𐌠‍𝓎‌ ‍𝜌‍𐓶‌𝔟‌Ɩ‍𝚤‍𝘀‍𝚑‍𝔢‍ꓒ‌ ‌𝗻‌ﮦ‍𝘷‌ℯ‌ا‌𞣇‍𝒶‍܂‍ ‌ꓮ‌𝕀‍𝐭‍𝒉‌ﮫ‌𝕦‍ℊ‍𝔥‌ ‌𝗵‍𝚒‍𝗌‍ ‌𝗋‍𝑒‌𝞺‍𑣘‍𝘵‌𝗮‍𝚝‍ι‍ﮫ‍𝓷‍ ‍w‌⍺‍s‌ ‍n‍օ‌𝙩‌ ‍𝚑‍⍳‍𝓰‍𝙝‍ ‍ａ‍𝖙‍ ‌𝐭‌𝖍‍𝔢‌ ‍𝔱‌𝕚‌m‌𝐞‍ ‌𐓪‍𝑓‍ ‍𝒽‍ꙇ‌𝚜‌ ‍𝘥‌𝙚‍ɑ‍𝙩‌𝕙‍‚‌ ‌𝚝‍𝕙‌ҽ‌ ‍𝔠‍𝖊‌ո‌𝐭‌𝗲‌𝓃‌𝖓‌𝖎‍𝘢‌ℓ‌ ‍𝞼‌𝖋‌ ‌𝔥‌𑣃‍𝐬‍ ‍𝐛‌𝜾‍𝔯‍𝓽‌հ‌ ‍𝚒‍ռ‍ ‌1‍𝟫‍1‌𑣌‍ ‌ɯ‍𝔞‌s‌ ‌𝒕‌𝗁‌𝙚‌ ‌𝘴‌𝓽‌𝑎‍ꭈ‍𝗍‍ӏ‌𝖓‍𝖌‍ ‍𝛒‍𞺄‌𝐢‌𝗻‍𝑡‍ ‌൦‌𝖋‍ ‍ａ‍ ‍Ⅿ‍𝚎‍𝔩‌ｖ‌𝜾‌𝙄‍Ι‌𝖊‌ ‍г‌𝙚‌𝛎‍ι‍𝝼‌𝚊‌Ｉ‍ ‌𝙖‍ո‍ⅆ‍ ‍М‍𐓪‌𝓫‍𝛄‍–‌𝔇‌𝛊‌𝑐‍𝙠‍ ‍ց‌ꮁ‌ꬲ‌𝐰‍ ‍𝓽‍ｏ‌ ‍𝕓‍е‍ ‌𝒄‌𝝾‌𝓷‌ꜱ‍ͺ‍𝘥‌𝑒‍𝓇‍𝖾‌ⅾ‍ ‍𝛐‌𝓷‌℮‌ ‌𝚘‍𝕗‌ ‍𝓽‍𝓱‍𝓮‌ ‍𝗴‌𝕣‌ꬲ‍𝛂‌𝑡‌ ‌𝚨‌m‌𝖾‌𝖗‌𝜾‌ϲ‌α‌𝐧‌ ‍𝖓‌ﻬ‍𝖛‍ꬲ‍𝙡‍𝒔‍𝅭

#### Generate several unique strings from a text

```
$ echo 'Guillaume' >dummy_file.txt
$ python main.py dummy_file.txt  --level 3 --generate 1000 --outfile Guillaume.txt
$ head Guillaume.txt # each of the following line is unique
G‌u‍і‍l‌l‌a‌u‌m‌e‍
G‍u‌i‍l‍l‍a‍u‍m‍e‍
G‌u‌і‌l‍l‌a‌u‍m‌e‌
G‍u‍і‌l‌l‍a‌u‍m‌е‌
G‌u‌i‌l‌l‍а‌u‍m‌е‍
G‌u‍i‌l‍l‌а‌u‍m‌е‍
G‍u‌i‌l‍l‌a‌u‍m‍e‍
G‍u‌і‌l‍l‍а‍u‍m‍e‌
G‌u‍і‍l‌l‌а‍u‍m‌е‍
G‌u‌і‍l‌l‌а‍u‍m‍e‌
 ...

```
```
>>> guillaumes = open("dummy_file.txt").read().splitlines()
>>> len(set(guillaumes)) == len(guillaumes)
True
>>> # all unique
```

Check the Guillaume.txt file for more examples

see https://en.wikipedia.org/wiki/Word_joiner for more info on word joiners 

[1]: http://www.unicode.org/Public/security/revision-03/confusablesSummary.txt "Unicode "
[2]: https://en.wikipedia.org/wiki/Barack_Obama "Obama"
[3]: https://en.wikipedia.org/wiki/Zero-width_non-joiner "ZWNJ"
[4]: https://en.wikipedia.org/wiki/Zero-width_joiner "ZWJ"

