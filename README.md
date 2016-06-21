Random Utils
=====
Lookup
----
A small python script to lookup and map dictionary values to an incoming stream of input.

**Usage**

    python lookup.py -d <delimiter> -f <field> -l <lookupfile>
-d/[--delimiter]	Delimiter character to split the incoming stream. Default delimiter is ','.
-f[--field]		Field that needs to be looked and substituted. Default is the first field.
-l[--lookupfile]	The file that has the dictionary mapping.

**Note:** File needs to be in JSON format with the root node named as 'data'.

	{
	  "data": {
		    "key":"value",
		    "key":"value",
		    ...
		  }
	}

**Example**

	cat FEB_2014_data.csv | lookup -d "," -f 2 -l codes.json
