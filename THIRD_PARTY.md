# Componenti di terze parti

I sorgenti sotto `sources/` conservano licenze e copyright upstream. Lo snapshot e la provenienza sono in `research/source-lock.json`; i file di licenza inclusi nei progetti restano parte dell'archivio. Fork e copie di uno stesso upstream sono identificati nel catalogo.

Il player asciinema è la versione 3.11.0, distribuita con la licenza Apache-2.0 originale in `player/LICENSE`. Provenienza: https://github.com/asciinema/asciinema-player/tree/v3.11.0 . Non sono stati caricati video su asciinema.org.

Le wheel Markdown 3.8.2, pyte 0.8.2 e wcwidth 0.2.13 includono i propri metadata/licenze. Sono usate per generare il report e verificare le registrazioni, non per simulare output dei test.

I pacchetti Debian in `vendor/` conservano metadata e copyright originali. Le versioni sono nei nomi dei pacchetti. La distribuzione di riferimento e i relativi sorgenti sono disponibili su https://deb.debian.org/debian/ e https://sources.debian.org/ .

I moduli e programmi nativi sotto `native/` sono identificati da SHA256 e provenienza in `research/native-manifest.json`. Ghostel e Kuro usano le release indicate; Cooked e Alacritty sono accompagnati dai sorgenti fissati e log/workflow di build. vterm viene ricostruito da `scripts/prepare.py`. L'archivio contiene anche i sorgenti dei backend esterni acquisiti. Le licenze di questi componenti non sono sostituite dalla licenza degli strumenti dello studio.
