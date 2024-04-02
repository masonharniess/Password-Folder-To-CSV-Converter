# Password-Folder-To-CSV-Converter

## Description

A small Python script to fix an idiosyncratic password conversion problem where login details are stored as individual .txt files.

This script converts a collection of .txt files to .csv format for use by Bitwarden password manager. 

The output .csv is conditioned as per the instructions given by [bitwarden.com](https://bitwarden.com/help/condition-bitwarden-import/).

## Formatting

The script assumes the following about formatting:

1. Each set of login details is comprised within its own .txt file. 

2. All login details are stored inside a directory named `directory` — this directory is located within the same parent directory as `passwordConversion.py`.

3. The application or website name is the title of the .txt file minus the extension (e.g., `YouTube.txt`).

4. Each .txt file has two key-value pairs in the following format:
    ```
    Email: myemail@domain.com
    Password: mypassword
    ```

5. Other data might exist in the files, though it will be overlooked unless structured in a key-value pair format, with the key being a case-insensitive variation of 'Email' or 'Password'.

## Discrepancies

The following formatting discrepancies are accounted for:

- There is no preceding or succeeding space between the key and the value separator

- A singular linebreak is present between a key and its respective value.

- The key-value separator (typically a colon) is a hyphen, both with and without a preceding and succeeding space.

