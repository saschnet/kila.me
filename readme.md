# Open Source Kinderleichtathletik Auswertung

Dieses Projekt befindet sich aktuell in der Entwicklungsphase.
Ziel ist die Erstellung einer Plattform zur Auswertung von Wettkämpfen der [Kinderleichtathletik (KiLa)](https://www.leichtathletik.de/wettkaempfe/kinderleichtathletik).

Bis zum Abschluss dieses Projekts kann das vorherige closed source Projekt [kila.me](kila.me) kostenfrei als Zwischenlösung genutzt werden.

## Aktueller Status

Aktuell befindet sich das Projekt in der Entwicklungsphase.

### Aktuelle Themen

- Backend wird mit Python 3.11 umgesetzt. Ggf. sehr bald Upgrade auf 3.12.
- Als Datenbank wird PostgreSQL 16 genutzt.
- Entwicklung der Datenbankstruktur. Hier wird sehr viel von der Datenbankstruktur von kila.me übernommen.
- UUIDs für Primary Keys nutzen, um ein dezentrales System langfristig zu unterstützen oder auf inkrementelle Integers setzen?
- Wahl des Frameworks für das Frontend (wird mit TypeScript entwickelt werden)
- Deployment über Docker Compose (Datenbank, Frontend und Backend)
