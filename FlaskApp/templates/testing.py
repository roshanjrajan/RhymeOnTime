<!DOCTYPE html>
<html lang="en">

<head>
  <title>This is a test</title>

  <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="http://getbootstrap.com/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
</head>

<body>
  <title>This is a test</title>
  {% if name %}
    <h1>Hello {{name}}!</h1>
  {% else %}
  <button onclick="window.location.href='/'" type="button"
  class="btn btn-lg btn-primary">Home</button>
  {%endif%}
</body>


</html>
