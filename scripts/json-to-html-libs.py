import json

html_string = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">

        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.1/css/jquery.dataTables.css">
        <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.5.1.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.13.1/js/jquery.dataTables.js"></script>

        <script type="text/javascript" class="init">
          $(document).ready( function () {
            $('#table_id').DataTable();
          } );
        </script>
        <style>
          body {
            font-family: Tahoma, Verdana, sans-serif;
            margin: 30px;
          }
        </style>
    </head>
    <body>

        <h2>Libraries on GitHub</h2>

<table id="table_id" class="display">
  <thead>
  <tr>
    <th>Country</th>
    <th>City</th>
    <th>Organisation</th>
    <th>Repositories</th>
  </tr>
  </thead>
  <tbody id="myTable">
  '''
with open("all-libs.json", 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for org in data["organisations"]:
        html_string += "<tr><td>" + org['country'] + "</td><td>" + org['city'] + "</td><td><a href=\"" + org['url'] + "\">" + org['name'] + "</a></td><td>" + str(len(org['repositories'])) + "</td></tr>\n"

html_string += '''
  </tbody>
</table>
</body>
'''
with open('libraries.html', 'w', encoding='utf8') as html_file:
    html_file.write(html_string)
