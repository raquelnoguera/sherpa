# Sherpa
Programmatic SERP checker.

It uses APIs from different sources to execute Search and SERP queries to Google.

Searches for Keywords are executed for different markets. Both list of markets and list of
keywords is extracted from files that are passed as parameters to the main script.

# Purpose
The purpose of this tool is to automate SEO search and SERP queries and analyse the results. 

If you set SEO policies on different markets, this tool can be used to check if your SEO settings are working as 
expected.

# Usage

## Search

A search returns a list of entries for the keyword used. This is the command to execute a search:

```
python search.py ./keywords.json ./outputfilename
```

where *keywords.json* is a file that contains the keywords for SERP. It has the following structure:

```
[
    {
        "name": "keyword1",
        "keywords": ["search keyword 1", "search keyword 2", "search keyword 3"],
        "markets": ["AT", "BE", "CH", "CY", "CZ", "DE", "DK", "ES", "FI", "FR", "GB", "GR", "HR", "IE", "IT", "NL", "NO", "PL", "PT", "SE", "SI", "SK"]
    },
    {
        "name": "keyword1_es",
        "keywords": ["search keyword Spanish 1", "search keyword Spanish 2", "search keyword Spanish 3", "search keyword Spanish 4"],
        "markets": ["ES"]
    }
]
```
and *outputfilename* is the filename for the output excel file, which will be suffixed with ".xlsx".

By default, a search returns the top 25 entries. The number of entries can be set between 10 and 100 as follows:

```
python search.py -n 50 ./keywords.json ./outputfilename
```

where the value of n is the requested result length.

## SERP

A SERP returns the position of a specific website for a keyword. For example, it returns the position of the wikipedia
website for a search of keyword "best online encyclopedia". In only searches among the top 100 entries. If wikipedia is
not among the top 100, then it returns value -1. 

The command to execute for SERP is:

```
python serp.py ./keywords.json ./outputfilename
```

where *keywords.json* is a file that contains the keywords for SERP. It has the following structure:

```
[
    {
        "name": "keyword1",
        "keywords": ["search keyword 1", "search keyword 2", "search keyword 3"],
        "markets": ["AT", "BE", "CH", "CY", "CZ", "DE", "DK", "ES", "FI", "FR", "GB", "GR", "HR", "IE", "IT", "NL", "NO", "PL", "PT", "SE", "SI", "SK"],
        "site: "www.wikipedia.com"
    },
    {
        "name": "keyword1_es",
        "keywords": ["search keyword Spanish 1", "search keyword Spanish 2", "search keyword Spanish 3", "search keyword Spanish 4"],
        "markets": ["ES"],
        "site: "www.wikipedia.com"
    }
]
```
and *outputfilename* is the filename for the output excel file, which will be suffixed with ".xlsx".

