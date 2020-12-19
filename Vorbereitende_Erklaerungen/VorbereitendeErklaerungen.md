# Inhalt

- [Vorbereitende Erklärungen](#vorbereitende-erklärungen)
  - [F-Strings](#f-strings)
  - [List-Comprehensions](#list-comprehensions)

## Vorbereitende Erklärungen

Dieses Tutorial richtet sich zwar schon an Leute die bereits die Grundlagen von Python kennen und verstehen, aber ich werde kurz f-Strings und List-Comprehensions erklären, weil ich diese Konzepte in den Codebeispielen regelmäßig verwende, wer das kennt, kann diesen Teil überspringen. Und direkt mit [Kapitel 1](<#kapitel-1:-fortgeschrittenes-(klassen)-design>) starten.

---

### f-Strings

F-Strings steht für "formatted string literals". Sie kennzeichnen sich dadurch aus, dass vor dem Anführungszeichen des Strings ein f steht. (Klein- oder Großschreibweise spielt dabei keine Rolle, typischerweise verwendet man das kleine f). Innerhalb des Strings dürfen geschweifte Klammern stehen, welche einen Pythonausdruck enthalten. Im einfachsten Fall ist das eine Variable, komplexere Ausdrücke funktionieren aber auch.

Die f-Strings wandeln den Ausdruck der geschwiften Klammen in einen String um und werden im Anschluss ein ganz normaler String behandelt. Die Idee dahinter ist, dass man im Code den String vollständig beschreibt und auch ohne die eingefügten Inhalte zu kennen weiß, wie dieser String am Ende aussieht.

```py
mein_name = 'Geralonx'
mein_alter = 30
gruss = f"Grueß dich, mein Name ist {mein_name}, ich bin {mein_alter} Jahre alt."
print(gruss)


# Vorgänger Methode
gruss_alt = "Grueß dich, mein Name is {}, ich bin {} Jahre alt.".format(mein_name, mein _alter)
```

<pre>
> Grueß dich, mein Name ist Geralonx, ich bin 30 Jahre alt.
</pre>

Mit der alten Methode reißt es einem beim Lesen des Codes aus dem Fluss. Man muss in die Format-Methode am Ende reingucken und sich dann selbst noch die übergeben Attribute in den String denken. F-Strings sollen es halt einfacher machen.

Mittels dem f-String f"{value}" wird auf die str-Darstellung des Value-Objekts zurückgegriffen. Wenn man allerdings f"{value!r}" wird auf die repr-Darstellung zurückgegriffen. Was das ist und warum das in einzelnen Fällen wichtig ist wird später noch genauer erklärt.

<sub>(Randnotiz 1: Auch wenn es f-Strings bereits Seit Python 3.6 (2016) gibt bin ich erst dieses Jahr vollständig auf die Verwendung von f-Strings umgestiegen. Vorher habe ich immer mit .format() gearbeitet, weil mir diese Darstellung sehr gut gefiel und ich die es deshlab nicht für nötig hielt mir die f-Strings anzugucken.</sub>

<sub>(Randnotiz 2: Ja, die gezeigte .format() Methode ist in dieser Form die einfachste Version. Man konnte dort auch schon mit Keywords innerhalb der geschweiften Klammern arbeiten, um einen 'Lesefluss' zu erzeuge, aber es bleibt dabei, dass man am Ende die Zuweisung erst im .format() erkennt und nich direkt im String selber.)
</sub>

<br/>

---

### List-Comprehensions

List-Comprehensions sind präzise Ausdrücke, um eine Liste mit Ergebnissen von einer Operation, welche auf die einzelnen Mitglieder einer Sequenz oder Iterator angewendet werden, zu erzeugen (Frei übersetzt aus der Python-Dokumentation). Bitte was? Im häufigsten Fall ersetzten List-Comprehensions for-Loops, welche eine Liste oder ein Dict erzeugen. Die Syntax einer List-Comprehension sieht folgendermaßen aus:

<pre>
> liste = [expression for item in sequence [, condition]]
</pre>

Beispiel / Vergleich mit einer for-Loop:

```py
# For-Loop um die Quadrate der Zahlen 0-9 zu erzeugen
for_loop_list = []
for i in range(10):
    for_loop_list.append(i*i)

# List-Comprehension um die Quadrahte der Zahlen 0-9 zu erzeugen.
list_comp_list = [i*i for i in range(10)]

# expression : i*i
# item : i
# sequence: range(10)


# Ausgabe
print("For-Loop-Result:\t", for_loop_list)
print("List-Comp-Result:\t", list_comp_list)
```

<pre>
> For-Loop-Result:         [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
> List-Comp-Result:        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
</pre>

Die List-Comprehension vereinigt 3 Zeilen Code von einer Empty-List-Initialisierung und das Füllen mit einer for-Loop zu einer einzigen. Es ist auch möglich Bedingungen in die List-Comprehension einzubauen.

```py
# List Comprehension mit einer Bedingung, welche nur die geraden Zahlen quadriert.
new_list = [i*i for i in range(10) if i%2 == 0]
print(new_list)

# Das gleiche Ergebnis ließe sich beispielsweise mit folgendem Code erreichen
new_list = []
for i in range(10):
    if i%2 == 0:
        new_list.append(i*i)
```

<pre>
> [0, 4, 16, 36, 64]
</pre>

List-Comprehensions können die Leserlichkeit verbessern, wenn man sie versteht und lesen kann. Einfache List-Comprehensions schneiden von der Performance meistens auch noch besser ab als die entsprechenden for-Loop Konstrukte. Darauf möchte ich aber nicht tiefer eingehen.

Man kann mit List-Comprehensions aber auch ganz schönen Unfug treiben und den Scheiß unendlich tief verschachteln oder vieles mehr. Ich werde dazu auch ein File verlinken, wo ich mal solche Konstrukte zeige und umschreibe.

Hier sind mal ein paar Methoden aus einer Klasse, welche ich zum WebScrapen der Steam-Angebote verwendet habe. Dort habe ich völlig übertrieben, um die List-Comps zu verstehen, aber das geht definitiv zu weit, wenn es um einfach zu verstehenden Code geht.

```py
def filter_games_by_tags(self, tag):
    filtered_list = [game for game in self.steam_discount_list if(game['tag_list'] is not None and set(tag).issubset(game['tag_list']))]
    return filtered_list

def filter_games_by_price(self, max_price, min_price=0.00):
    filtered_list = [game for game in self.steam_discount_list if(min_price < game['actual_price'] <= max_price)]
    return filtered_list

def most_common_tags(self):
    all_tags_flat = [tag for game in self.steam_discount_list if game['tag_list'] is not None for tag in game['tag_list']]
    occur = [[tag, all_tags_flat.count(tag)] for tag in set(all_tags_flat)]
    self.most_common_tags = sorted(occur, key = lambda x: x[1], reverse=True)
```

Funktioniert es? Ja. Ist es einfach zu verstehen? Nein. Zur Übung oder aus Langeweile könnt ihr diese Konstrukte ja mal auseinander nehmen, gerade die Methode 'most_common_tags' ist übel, wenn man noch nicht genau verstanden hat, wie diese aufgebaut sind.
<br/>

<sub>(Hint: Zerlegt die Comprehension von hinten oder von vorne und stoppt immer bei Keywords wie if oder for. Nehmt den Teil bis zu dem Keyword und schmeißt alles bis dahin in eine eigene Zeile. Wenn man von hinten anfängt, dann baut man das Konstrukt von innen nach außen auf, umgekehert wenn man vorne anfängt. Am Ende muss man nur noch die Expression, also den vordersten Teil, in das innere übersetzten. Eine Schritt für Schritt Anleitung ist hier: [Loesung List-Comprehension](https://github.com/Geralonx/Classes_Tutorial/blob/master/Vorbereitende_Erklaerungen/_2_list_comp_loesung.py)) </sub>

<sub>(Randnotiz 1: Es gibt das gleiche auch für Dicts, also Dict-Comprehensions. Die Syntax ist 1:1 wie ber für die List. Das einzige was sich ändert ist, dass man die Comprehensions mit {} statt [] schreibt und sicherstellen muss, dass die Expression ein Key-Value-Pair ist.)</sub>
