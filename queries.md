To get "instance of" results. This example is for "dog".

```
select distinct ?x ?xLabel where {
  ?x wdt:P31 wd:Q144.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
```

To get "instance of" and "subclass" results. This example is for "dog".

```
select distinct ?x where {
  ?x wdt:P31/wdt:P279* wd:Q144
}
```


