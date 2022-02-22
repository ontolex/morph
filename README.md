# OntoLex Morphology Module

The Morphology Module for the OntoLex Model

For more details see the Wiki: https://www.w3.org/community/ontolex/wiki/Morphology

## Draft spec

Draft for definitions resides under [draft.md](draft.md).

The [HTML template](index.html) is still empty, if finalized, it will be exposed via https://ontolex.github.io/morph/.

## GDrive

Much information is scattered on Google Drive, and only mirrorred here.
See https://www.w3.org/community/ontolex/wiki/Morphology for the original link.

In particular, this pertains to the folders
- `minutes/`
- `data/gdrive`

For updating the local mirror, run

    $> bash -e ./sync-gdrive.sh

See notes in `sync-gdrive.sh` for how to configure the `rclone` command.

To facilitate searchability, `sync-gdrive.sh` will also produce a text export of the GDrive minutes under `minutes_txt/`.
