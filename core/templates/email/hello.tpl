{% extends "mail_templated/base.tpl" %}

{% block subject %}
hi
{% endblock %}

{% block html %}
{{token}}
{% endblock %}