# Oktatási Hivatal kérdőív kitöltő script

Az nem régiben az OH által kiadott form automatikus kitöltésére írt script.

#### Requirements

* [Python 3](https://www.python.org/)
* [Selenium 4](https://pypi.org/project/selenium/)
* [Chrome webdriver](https://chromedriver.chromium.org/) illetve a hozzátartozó böngésző
  Utóbbi kettő a pip install -r requirements.txt parancs lefuttatásával telepíthetőek

#### Futtatás

**macOS / Linux**

```
python3 script.py
```

**Windows**

```
python script.py
```

#### **Működés**

A program két módon tud működni:

* Random generált válaszokkal tölti ki a kérdőívet
* A felhasználó ki tudja tölteni a kérdőívet a programon belül és azokkal a válaszokkal fog kérdőíveket kitölteni a program

Először a program feltesz egy eldöntendő kérdést, `Saját válaszokkal szeretnéd kitölteni? (i/n)`. A felhasználó az alábbiakkal válaszolhat: i, n, igen, nem. Ha igennel vagy annak megfelelőjével válaszol akkor a program végig megy az összes kérdésen és a felhasználó számok segítségével dönthet. Ha a nemet vagy annak megfelelőt válaszol akkor a program minden alkalommal más válaszokkal fogja a kérdőívet kitölteni, kivéve az utolsó előtti `Kérjük, jelölje, hogy egyetért-e Ön azzal, hogy a pedagógusok a tanulókat is bevonják a bérezésükkel kapcsolatos demonstrációkba?` ahol minden esetben az `igen` opciót fogja választani, illetve az utlsó kérdésre egy előre megírt[ nyílt levelet](https://www.facebook.com/pedagogusok.d.szakszervezete/posts/4898945936880604/) fog bemásolni. A program egy végtelen ciklusban fogja kitölteni a kérdőívet amíg a felhasználó bele nem avatkozik.

#### Contribution

Bármilyen javítást, plusz feature-t szívesen várok, nyissatok pull requestet, vagy issue-t!
