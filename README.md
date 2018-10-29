# TextJammer

Using the Unicode looking like characters we can transform a text to make it less machine readable.
~~~
Usage : python transform.py ARGS file
positional arguments:
  file     encoded in UTF-8

optional arguments:
  -h, --help  show this help message and exit
  -c          Latin letters remplaced by Greek and Cyrillic letters
  -z          add zero width joiner/non-joiner
  -d          digits remplacement
  --all       all parameters
  --unicode   all unicode confusable chars
~~~


The ´-c´ option transforms the text by randomly changing the Latin letters into Cyrillic and Greek looking-like letters. The text is visually the same on regular text editors, but remains altered. 

The ´-z´ randomly inserts [zero-width joiner][4] and [zero-width non-joiner][3] chararcters within the text.It usually doesn't affect the reading for a Latin text (English, French, Spanish...)

#### Replacing randomly the Latin characters by Greek or Cyrillic letters and adding the ZWJ ([from Barack Obama Wikipedia's page][2]) :

Β‍а‌r‍а‍с‍k‌ Η‌u‍ѕ‍ѕ‍е‍і‍n‌ О‌b‌а‌m‍а‍ І‍І‍ (b‌ο‍r‌n‍ Α‌u‍g‍u‍ѕ‍t‌ 4, 1961) і‍ѕ‌ а‌n‌ А‍m‌е‌r‍і‍с‌а‍n‌ а‌t‌t‍о‌r‌n‌е‌y‍ а‌n‌d‌ р‍ο‍l‍і‌t‍і‍с‌і‍а‌n‌ w‍h‍ο‍ ѕ‌е‌r‌v‍е‌d‌ а‌ѕ‍ t‌h‌е‍ 44t‍h‌ Ρ‍r‍е‍ѕ‍і‌d‌е‌n‌t‍ ο‍f‍ t‌h‌е‌ U‌n‌і‍t‍е‌d‍ Ѕ‌t‍а‍t‍е‍ѕ‌ f‍r‍ο‌m‍ Ј‌а‍n‌u‌а‍r‍y‍ 20, 2009, t‍ο‍ Ј‍а‌n‌u‍а‍r‍y‌ 20, 2017. А‌ m‌е‌m‍b‍е‍r‌ о‌f‍ t‍h‍е‍ D‍е‍m‍ο‌с‍r‌а‍t‌і‌с‍ Ρ‍а‍r‌t‍y‌, h‌е‍ w‌а‍ѕ‌ t‌h‌е‍ f‍і‍r‍ѕ‍t‌ Α‍f‍r‌і‍с‍а‌n‌ А‍m‍е‍r‌і‌с‍а‌n‌ t‌ο‍ ѕ‌е‍r‍v‌е‍ а‍ѕ‌ р‍r‍е‍ѕ‌і‌d‍е‌n‍t‌. Η‌е‌ w‌а‍ѕ‍ р‌r‌е‍v‌і‍ο‌u‌ѕ‌l‌y‌ а‍ U‌n‌і‌t‍е‌d‍ Ѕ‍t‌а‌t‍е‌ѕ‍ Ѕ‍е‌n‍а‍t‌ο‌r‌ f‌r‌о‍m‍ І‌l‍l‌і‍n‍ο‌і‍ѕ‌ а‌n‌d‍ а‌ m‌е‌m‌b‍е‌r‍ ο‌f‌ t‍h‌е‌ І‌l‌l‍і‍n‍ο‌і‍ѕ‌ Ѕ‌t‍а‌t‍е‍ Ѕ‍е‍n‌а‌t‌е‌.

Funny thing is regular search engines can't find the original webpage (as free online plagiarism checkers).

#### Using all of the confusable characters of unicode (see [the unicode confusable characters][1]), we can generate weird looking text worthy of old spam messages : 

Β𝙖𝚛𝜶𝒸𝜿 𝙃ц𝓼𝐬ⅇ𝒾ո  ՕᏏ𝕒mａ II ﴾𝙗ｏᴦ𝝿 𝘼𝔲ɡᴜ𝗌𝘵 𝟺¸ 1৭𝟨1﴿ ι𝓈 𝖺𝔫 𝗔m𝒆𝓇ӏ𝑐⍺𝖓 𝙖𝛕𝘁𝞼𝒓π𝔢𝑦 ⍺𝟉𝚍 𝜚𝜎𝟙˛𝓉𝖎𝖼𝗶𝞪ℼ wհ𝞂 ƽ𝑒𝙧ט𝑒𝖽 𝕒ѕ 𝚝ｈ𝒆 𝟺𝟦𝘁𝘩 ℙ𝐫℮𝕤𝜄𝐝𝐞𝜛𝛕 ං𝔣 𝚝𝓱𝔢 𝐔𝚗𝔦τеꓒ Ѕ𝙩ɑτ𝙚𝚜 ẝ𝖗𝞸m 𝑱𝘢𝚗𝓊а𝔯ｙ Ꙅ0٫ 𝟸00Ꝯ٫ 𝘁𝔬 𝙹𝒂ռ𝚞𝑎𝙧𝔂 𝟸0¸᠎Ꙅ01𝟟․ ᗅ mℯm𝖇𝚎ᴦ 𝙤𝐟 𝗍һ𝕖 𝐷𝓮m𝚘𝐜𝙧𝖆т𝒾ⅽ 𝔓𝙖𝓇т𝛾¸᠎ℎ𝕖  wɑ𝙨 𝓽𝚑℮᠎𝕗ı𝐫ｓ𝓽 Αքгⅈᴄ𝛂𝑛 𝚨m𝔢𝑟ⅰ𝙘𝒂𝘯 τⲟ 𝙨𝒆𝔯𝞶𝓮  𝘢𝓈 𝞎𝗋𝖊𝘴˛𝔡𝕖ϖ𝞃۔ Нℯ wａ𝔰 ϱⲅ𝙚ט𝐢𝒐ս𝔰𝟷𝜸 𝞪 𝖴𝖓⍳𝕥℮ⅆ 𝗦𝝉𝛂𝖙ℯ𝕤 Տ𝖊π𝙖𝒕ം𝖗 𝖿𝐫ⲟm I|𝗹𝞲𝚗𝝈ｉ𝚜 𝑎𝑛𝐝 ａ m𝐞m𝖻ℯ𝓻 ℴſ 𝒕հ𝚎 Iⵏ𝔩𝖎𝕟օɪ𝓼 Տ𝑡α𝞃ｅ Ѕ𝓮𝗇𝓪𝖙𝒆․


It is also possible using this method to generate differents strings.
For instances each of the following strings is unique :
* G‍u‍і‍l‍l‌а‌u‍m‌е
* G‌‍u‍‍і‍‍l‍‍l‍‌а‍‌u‌‍m‍‌е
* G‌‌‍u‌‍‍і‍‍‍l‌‍‍l‌‍‌а‌‍‌u‌‌‍m‍‍‌е
* G‌‌‌‍u‌‌‍‍і‍‍‍‍l‌‌‍‍l‌‌‍‌а‌‌‍‌u‌‌‌‍m‌‍‍‌е
* G‌‌‌‌‍u‌‌‌‍‍і‌‍‍‍‍l‍‌‌‍‍l‌‌‌‍‌а‍‌‌‍‌u‌‌‌‌‍m‌‌‍‍‌е
* G‌‌‌‌‌‍u‍‌‌‌‍‍і‌‌‍‍‍‍l‍‍‌‌‍‍l‌‌‌‌‍‌а‌‍‌‌‍‌u‌‌‌‌‌‍m‍‌‌‍‍‌е
* G‍‌‌‌‌‌‍u‌‍‌‌‌‍‍і‍‌‌‍‍‍‍l‌‍‍‌‌‍‍l‌‌‌‌‌‍‌а‍‌‍‌‌‍‌u‌‌‌‌‌‌‍m‌‍‌‌‍‍‌е
* G‌‍‌‌‌‌‌‍u‍‌‍‌‌‌‍‍і‌‍‌‌‍‍‍‍l‌‌‍‍‌‌‍‍l‍‌‌‌‌‌‍‌а‍‍‌‍‌‌‍‌u‍‌‌‌‌‌‌‍m‍‌‍‌‌‍‍‌е
* G‌‌‍‌‌‌‌‌‍u‌‍‌‍‌‌‌‍‍і‍‌‍‌‌‍‍‍‍l‍‌‌‍‍‌‌‍‍l‌‍‌‌‌‌‌‍‌а‍‍‍‌‍‌‌‍‌u‍‍‌‌‌‌‌‌‍m‍‍‌‍‌‌‍‍‌е
* G‍‌‌‍‌‌‌‌‌‍u‌‌‍‌‍‌‌‌‍‍і‌‍‌‍‌‌‍‍‍‍l‌‍‌‌‍‍‌‌‍‍l‍‌‍‌‌‌‌‌‍‌а‍‍‍‍‌‍‌‌‍‌u‌‍‍‌‌‌‌‌‌‍m‍‍‍‌‍‌‌‍‍‌е
* G‌‍‌‌‍‌‌‌‌‌‍u‌‌‌‍‌‍‌‌‌‍‍і‍‌‍‌‍‌‌‍‍‍‍l‌‌‍‌‌‍‍‌‌‍‍l‍‍‌‍‌‌‌‌‌‍‌а‍‍‍‍‍‌‍‌‌‍‌u‌‌‍‍‌‌‌‌‌‌‍m‌‍‍‍‌‍‌‌‍‍‌е
* ... check the Guillaume.txt file for more examples



[1]: http://www.unicode.org/Public/security/revision-03/confusablesSummary.txt "Unicode "
[2]: https://en.wikipedia.org/wiki/Barack_Obama "Obama"
[3]: https://en.wikipedia.org/wiki/Zero-width_non-joiner "ZWNJ"
[4]: https://en.wikipedia.org/wiki/Zero-width_joiner "ZWJ"

