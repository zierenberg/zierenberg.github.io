---
layout: page
title: News
permalink: /news/
---

<ul class="post-list">
  {% for post in site.posts %}
    <news>
    <dl>
      <dt>
      <span class="post-meta">{{ post.date | date: "%d. %m. %Y:" }}</span>
      </dt>
      <dd>
      {{ post.title }} (<a class="post-link" href="{{ post.url | prepend: site.baseurl }}">read more</a>)
      </dd>
    </dl>
    </news>
  {% endfor %}
</ul>
