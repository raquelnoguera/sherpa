# Sherpa
Programmatic SERP checker.

It uses APIs from different sources to execute SERP queries to various search engines.

Searches for Keywords o combinations of keywords are executed for different markets. Both list of markets and list of
keywords is extracted from files that are passed as parameters to the main script.

# Purpose
The purpose of this tool is to automate SERP queries and analyse the results. 

If you set SEO policies on different markets, this tool can be used to check if your SEO settings are working as 
expected.

# Usage

```
python main.py ./keywords.json ./outputfilename
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
        "markets": ["es"]
    }
]
```

and *outputfilename* is the filename for the output excel file, which will be suffixed with ".xlsx".
