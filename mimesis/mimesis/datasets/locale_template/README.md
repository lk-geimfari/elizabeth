## How to Add a New Locale

This is a template of the dataset directory structure for a specific locale.

There are seven JSON files (`File name`) that contain data related to various data providers (`Provider`):

* `address.json` - Address()
* `builtin.json` - YourSpecProvider()
* `datetime.json` - Datetime()
* `finance.json` - Finance()
* `food.json` - Food()
* `person.json` - Person()
* `text.json` - Text()

## Steps to Follow Before Submitting a Pull Request for Adding Support for a New Locale:

1. Copy the folder from `locale_template` to `your-locale-code`.
2. Ensure that you have replaced all `["Tests""]` sections with data specific to your locale.
3. Remove all `"__COMMENT_KEY__": "Description"` from the JSON files. This data is only for developers.
4. Add your locale to the `mimesis.enums.Locale` class.
5. Format the content of JSON files alphabetically using a tool like [jsoneditoronline.org](http://jsoneditoronline.org).
6. If your locale uses a shortened address format, add your locale code to `SHORTENED_ADDRESS_FMT` in `mimesis/datasets/int/address.py`.
7. Make sure you have added the currency symbol for your locale to `CURRENCY_SYMBOLS` in `mimesis/datasets/int/finance.py`.
8. Ensure that you have added your locale code to `ISBN_GROUPS` in `mimesis/datasets/int/code.py`.
9. Run tests and confirm that all tests pass successfully.
10. Add yourself as a contributor in `CONTRIBUTORS.md`.

#### You can grab code of your locale from the table below:

|       |                                |       |                          |
|-------|--------------------------------|-------|--------------------------|
| af    | Afrikaans                      | sq    | Albanian                 |
| ar-sa | Arabic (Saudi Arabia)          | ar-iq | Arabic (Iraq)            |
| ar-eg | Arabic (Egypt)                 | ar-ly | Arabic (Libya)           |
| ar-dz | Arabic (Algeria)               | ar-ma | Arabic (Morocco)         |
| ar-tn | Arabic (Tunisia)               | ar-om | Arabic (Oman)            |
| ar-ye | Arabic (Yemen)                 | ar-sy | Arabic (Syria)           |
| ar-jo | Arabic (Jordan)                | ar-lb | Arabic (Lebanon)         |
| ar-kw | Arabic (Kuwait)                | ar-ae | Arabic (U.A.E.)          |
| ar-bh | Arabic (Bahrain)               | ar-qa | Arabic (Qatar)           |
| eu    | Basque (Basque)                | bg    | Bulgarian                |
| be    | Belarusian                     | ca    | Catalan                  |
| zh-tw | Chinese (Taiwan)               | zh-cn | Chinese (PRC)            |
| zh-hk | Chinese (Hong Kong SAR)        | zh-sg | Chinese (Singapore)      |
| hr    | Croatian                       | cs    | Czech                    |
| da    | Danish                         | nl    | Dutch (Standard)         |
| nl-be | Dutch (Belgium)                | en    | English                  |
| en-us | English (United States)        | en-gb | English (United Kingdom) |
| en-au | English (Australia)            | en-ca | English (Canada)         |
| en-nz | English (New Zealand)          | en-ie | English (Ireland)        |
| en-za | English (South Africa)         | en-jm | English (Jamaica)        |
| en    | English (Caribbean)            | en-bz | English (Belize)         |
| en-tt | English (Trinidad)             | et    | Estonian                 |
| fo    | Faeroese                       | fa    | Farsi                    |
| fi    | Finnish                        | fr    | French (Standard)        |
| fr-be | French (Belgium)               | fr-ca | French (Canada)          |
| fr-ch | French (Switzerland)           | fr-lu | French (Luxembourg)      |
| gd    | Gaelic (Scotland)              | ga    | Irish                    |
| de    | German (Standard)              | de-ch | German (Switzerland)     |
| de-at | German (Austria)               | de-lu | German (Luxembourg)      |
| de-li | German (Liechtenstein)         | el    | Greek                    |
| he    | Hebrew                         | hi    | Hindi                    |
| hu    | Hungarian                      | is    | Icelandic                |
| id    | Indonesian                     | it    | Italian (Standard)       |
| it-ch | Italian (Switzerland)          | ja    | Japanese                 |
| ko    | Korean                         | ko    | Korean (Johab)           |
| lv    | Latvian                        | lt    | Lithuanian               |
| mk    | Macedonian (FYROM)             | ms    | Malaysian                |
| mt    | Maltese                        | no    | Norwegian (Bokmal)       |
| no    | Norwegian (Nynorsk)            | pl    | Polish                   |
| pt-br | Portuguese (Brazil)            | pt    | Portuguese (Portugal)    |
| rm    | Rhaeto-Romanic                 | ro    | Romanian                 |
| ro-mo | Romanian (Republic of Moldova) | ru    | Russian                  |
| ru-mo | Russian (Republic of Moldova)  | sz    | Sami (Lappish)           |
| sr    | Serbian (Cyrillic)             | sr    | Serbian (Latin)          |
| sk    | Slovak                         | sl    | Slovenian                |
| sb    | Sorbian                        | es    | Spanish (Spain)          |
| es-mx | Spanish (Mexico)               | es-gt | Spanish (Guatemala)      |
| es-cr | Spanish (Costa Rica)           | es-pa | Spanish (Panama)         |
| es-do | Spanish (Dominican Republic)   | es-ve | Spanish (Venezuela)      |
| es-co | Spanish (Colombia)             | es-pe | Spanish (Peru)           |
| es-ar | Spanish (Argentina)            | es-ec | Spanish (Ecuador)        |
| es-cl | Spanish (Chile)                | es-uy | Spanish (Uruguay)        |
| es-py | Spanish (Paraguay)             | es-bo | Spanish (Bolivia)        |
| es-sv | Spanish (El Salvador)          | es-hn | Spanish (Honduras)       |
| es-ni | Spanish (Nicaragua)            | es-pr | Spanish (Puerto Rico)    |
| sx    | Sutu                           | sv    | Swedish                  |
| sv-fi | Swedish (Finland)              | th    | Thai                     |
| ts    | Tsonga                         | tn    | Tswana                   |
| tr    | Turkish                        | uk    | Ukrainian                |
| ur    | Urdu                           | ve    | Venda                    |
| vi    | Vietnamese                     | xh    | Xhosa                    |
| ji    | Yiddish                        | zu    | Zulu                     |

