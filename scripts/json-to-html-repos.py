import json

html_string = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">

        <link rel="stylesheet" type="text/css" href="static/datatables/1.13.1/css/jquery.dataTables.css">
        <script type="text/javascript" language="javascript" src="static/jquery/jquery-3.5.1.js"></script>
        <script type="text/javascript" charset="utf8" src="static/datatables/1.13.1/js/jquery.dataTables.js"></script>

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

        <h2>Library Repositories on GitHub</h2>

<table id="table_id" class="display">
  <thead>
  <tr>
    <th>Organisation</th>
    <th>Repository</th>
    <th>License</th>
    <th>Stars</th>
    <th>Forks</th>
    <th>Forked</th>
    <th>Last updated</th>
  </tr>
  </thead>
  <tbody id="myTable">
  '''
with open("all-libs.json", 'r', encoding="utf-8") as json_file:
  data = json.load(json_file)
  for org in data["organisations"]:
      for repo in org['repositories']:
          # print(type(repo))
          if type(repo) is dict:
              if str(repo['license']) != "None":
                  license = repo['license']['spdx_id']
              else:
                  license = " "
              html_string += "<tr><td>" + org['name'] + "</td><td><a href=\"" + repo['html_url'] + "\">" + repo['name'] + "</a></td><td>" + license + "</td><td>" + str(repo['stargazers_count']) + "</td><td>" + str(repo['forks_count']) + "</td><td>" + str(repo['fork']) + "</td><td>" + repo['updated_at'].split("T")[0] + "</td></tr>\n"

html_string += '''
  </tbody>
</table>
</body>
'''
with open('repositories.html', 'w', encoding='utf8') as html_file:
    html_file.write(html_string)
