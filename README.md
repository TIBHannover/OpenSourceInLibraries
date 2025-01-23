# Open Source Development in Libraries

Lists of Open Source repos from libraries on GitHub and GitLab based on [axel-klinger/BibsOnGitHub](https://github.com/axel-klinger/BibsOnGitHub), [hbunke/BibsOnGitHub](https://github.com/hbunke/BibsOnGitHub) and [Code4LibWiki](http://wiki.code4lib.org/Libraries_Sharing_Code).

If you know a library that is not on the list, please comment on Issue "[New libraries](https://github.com/TIBHannover/OpenSourceInLibraries/issues)"

### Libraries on GitHub
* [Source List](libraries.csv)
* [List of libraries](https://tibhannover.github.io/OpenSourceInLibraries/libraries.html)
* [List of repositories](https://tibhannover.github.io/OpenSourceInLibraries/repositories.html)

### Libraries on GitLab
* [Source List](libraries-gitlab.csv)
* [List of libraries](https://tibhannover.github.io/OpenSourceInLibraries/libraries-gitlab.html)
* [List of repositories](https://tibhannover.github.io/OpenSourceInLibraries/repositories-gitlab.html)

## Add new entries

### GitHub
* edit [libraries.csv](libraries.csv)
* run [csv-to-json.py](scripts/csv-to-json.py) (GitHub Access Token required for more than 60 requests per hour)
| Settings -> Developer Settings -> Personal Access Token: select nothing, it is just for reading -> Generate! 
* run [json-to-html-libs.py](scripts/json-to-html-libs.py) to generate the table libraries
* run [json-to-html-repos.py](scripts/json-to-html-repos.py) to generate the table repositories
* DO NOT COMMIT your personal access token!

### GitLab
* edit [libraries-gitlab.csv](libraries-gitlab.csv)
* will be published at github pages automatically

## License

CC-0 1.0 Universal [https://creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/)
