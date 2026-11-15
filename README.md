# odoo-onlyoffice — gren 19.0

> **Denna gren är avsiktligt tom.** Modulerna är INTE portade till Odoo 19.
> Grenen finns så att dev-miljöer (`hansolo19`) kan klona den utan att falla,
> men den påstår ingenting om att koden är portad.

## Baseline

| | |
|---|---|
| Källa | `20.0` |
| Moduler | **1** |
| Grenar i repot | `17.0`, `18.0`, `20.0` |

## Moduler

- `onlyoffice_dms_link`

## Blockerare

**1 externa beroenden saknas** i Odoo 19-kärnan och OCA 19.0:

| Beroende | Behövs av |
|---|---|
| `onlyoffice_odoo` | `onlyoffice_dms_link` |

### Prioritering

Ett beroende som blockerar många moduler ger mest nytta att lösa först:

- `onlyoffice_odoo` — frisläpper **1** modul(er)

## Nästa steg

Portering sker på `*-pfile`-maskin med versionsagnostisk kod
(`.p.py` / `.p.xml`). Se `/skill:odoo-pfiles`.
