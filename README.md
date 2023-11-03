# soilpedia.nl

Van 1995 tot 2015 heeft het SKB netwerk onderzoek gedaan naar bodem en ondergrond met als doel een betere leefomgeving. Soilpedia is hier een onderdeel van.

Deze repository bevat een clone van de informatie uit soilpedia in het geval deze website ooit uit de lucht gehaald wordt.

Om de inhoud te clonen is een [python script](sitemap2pdf.py) gebruikt en een nodejs app om de pdf inhoud om te zetten naar markdown, en een [script](./docx-to-md.sh) om docx om te zetten naar markdown. Deze conversie geeft soms wat overwachte zinsafbrekingen, van harte uitgenodigd om  mee te helpen om deze documenten weer netjes te maken.

```
[sitemap2pdf.py](sitemap2pdf.py)
npx @opendocsg/pdf2md --inputFolderPath=./pdf --outputFolderPath=./docs --recursive
```

Heb je ideeën/opmerkingen over de inhoud? Maak een [Issue](./issues) of [Pull request](./pulls) aan.