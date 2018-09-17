# Die Filterblasen der Anderen?

## -Work in progress-

### 1. Anwendung

Dies ist eine Anwendung zum Testen der Visualisierungskapazitäten der Python-Bibliothek 'plotly' basiernd auf Daten gewonnen mithilfe der Python-Bibliothek 'tweepy'.


### 2. Daten

#### 2.1 Beschreibung

Grundlage der Daten sind ca. 4000 Twitter-Accounts, eingeteilt in vier Gruppen : Die erste Gruppe basiert auf einer Liste politisch konservativ bis extrem konservativ eingestellter Accounts zusammengetragen im Rahmen der 'Reconquista Internet'-Aktion Jan Böhmermanns. Aufgenommen in die Gruppe wurden die tausend Accounts mit den meisten Followern. Die drei anderen Gruppen basieren jeweils auf tausend Followern der Accounts von 'Spiegel Online', 'Taz - Die Tageszeitung', und der 'Identitäten Bewegung Österreich'.

Über die Twitter-API wurden die Tweets dieser vier Gruppen im Zeitraum vom 19. August bis zum 6. September erfasst. Dieser Zeitraum wurde gewählt aufgrund der sich gleichzeitig in Chemnitz entfaltenden Ereignisse.

#### 2.2 Problematik

Vor allem in den Gruppen 2 bis 4 finden sich viele Nutzer, deren Accounts privat geschaltet sind und daher über die Twitter-API nicht verfügbar sind. Weiterhin sind manche Tweets durch Löschung nicht mehr verfügbar. Außerdem wurde nicht überprüft, ob hinter den Accounts Bots stehen oder nicht. Für die Darstellung ist dies allerdings zunächst vernachlässigbar. Weiterhin variiert das Tweet-Verhalten stark zwischen Nutzern, vor allem zwischen 'professionellen' und 'privaten'. Grundsätzlich ist in Frage zu stellen, wie repräsentativ Twitter als Datengrundlage ist.


### 3. Inhaltliches Ziel

Die Anwendung versucht, das Twitter-Verhalten der ersten Gruppe, der 'Böhermann-Liste', nachzuzeichnen. Zum Vergleich werden die anderen drei als Kontrollgruppen herangezogen.


### 4. Methodik

Visualisiert werden die von den jeweiligen Gruppen verwendeten Hashtags im Zeitraum vom 19. August bis zum 6. September. Die Darstellung wurde beschränkt auf die Hashtags, die an einem der Tage in diesem Zeitraum entweder der am häufigsten oder zweithäufigsten innerhalb dieser Gruppen verwendet wurden. Diese wurden der Anzahl nach auf einem Zeitstrahl als Liniendiagramm dargestellt.

Aufgrund der außergewöhnlich hohen Zahl von Tweets unter dem Hashtag 'Chemnitz' wurden außerdem die Volltexte dieses Subsets von Tweets einbezogen. Disen wurden nach den am häufigsten verwendeten Wörtern und den am häufigsten verwendeten Adjektiv-Subjekt Kombinationen visualisiert.
