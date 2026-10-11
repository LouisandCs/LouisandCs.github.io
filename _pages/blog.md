---
layout: page
permalink: /blog/
title: Blog
nav: true
nav_order: 3
---

{% if site.posts.size == 0 %}
Posts will be added soon.
{% else %}
<ul class="post-list">
  {% for post in site.posts %}
  <li>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p class="post-meta">{{ post.date | date: "%B %d, %Y" }}</p>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
  </li>
  {% endfor %}
</ul>
{% endif %}
