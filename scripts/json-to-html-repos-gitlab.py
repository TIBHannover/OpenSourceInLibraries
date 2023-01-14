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

        <h2>Library Repositories on GitLab</h2>

<table id="table_id" class="display">
  <thead>
  <tr>
    <th>Organisation</th>
    <th>Repository</th>
    <th>Stars</th>
    <th>Forks</th>
    <th>Last updated</th>
  </tr>
  </thead>
  <tbody id="myTable">
  '''
with open("all-libs-gitlab.json", 'r') as json_file:
  data = json.load(json_file)
  for org in data["organisations"]:
      for repo in org['repositories']:
          # print(type(repo))
          # if type(repo) is dict:
          #     if str(repo['license']) != "None":
          #         license = repo['license']['spdx_id']
          #     else:
          #         license = " "
          html_string += "<tr><td>" + org['name'] + "</td><td><a href=\"" + repo['web_url'] + "\">" + repo['name'] + "</a></td><td>" + str(repo['star_count']) + "</td><td>" + str(repo['forks_count']) + "</td><td>" + repo['last_activity_at'].split("T")[0] + "</td></tr>\n"

html_string += '''
  </tbody>
</table>
</body>
'''
with open('repositories-gitlab.html', 'w', encoding='utf8') as html_file:
    html_file.write(html_string)
