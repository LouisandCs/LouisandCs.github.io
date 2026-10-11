---
layout: page
permalink: /publications/
title: Research
nav: true
nav_order: 1
---

<!-- al-folio's Publications page, renamed Research in the navigation. -->
<!-- TODO: Add real entries to _bibliography/papers.bib. -->
{% capture bibliography_html %}{% bibliography %}{% endcapture %}
{% assign bibliography_text = bibliography_html | strip_html | strip %}
{% if bibliography_text != "" %}
{% include bib_search.liquid %}
<div class="publications">
{{ bibliography_html }}
</div>
{% else %}
Publications will be added soon.
{% endif %}
