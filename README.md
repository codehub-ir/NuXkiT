# NuXkiT
NuXkiT is a featured CodeHub Command-Line Interface (CLI) allows admins to interact with statistics on the client side. NuX uses RESTful API service to transfer data. Also you need to be signed in as an admin on the server. In this case, CodeHub can generate a new token for you, so you can use the achieved token key to integrate with suggestions, snippets, and teammates are submitted in the database.

### Login
First, you can use the facilities if you log in. You are able to login/out any time you want with commanders.

### Commander
NuX is kind of console-based program lets you to communicate in an interactive shell. Here is a listed table that shows you the available commands in NuX.

|  Command        | Description                | Short Form  |
| :-------------: | :------------------------: | :---------: |
| `snippet`       | to show snippets           | `snip`      |
| `teammate`      | to show teammates          | `team`      |
| `suggest`       | to show suggestions        | `sugg`      |
| `help`          | to see the admin manual    | `help`      |
| `logout`        | logout and login into NuX  | `logout`    |
| `clear`         | to clear the console       | `clea`      |
| `exit`          | to exit the cocnsole       | `exit`      |

### End-points (According to [CodeHub Admin APIs](https://github.com/CodeHub-Contributors/CodeHub#admin-api))
You may need to transfer data from the client side to the server using APIs, so there is no concerns. 
#### 1. Authentication
CodeHub is a Token-based website that allows admins to transfer data using Application/JSON style. After the migration you can access to `../api/vX/admin/login` or `../api/vX/admin/logout` to both logging in or logging out from the website.

#### 3. See Snippets
Use `../api/vX/admin/snippet` to show all saved snippets from all users. You can also use `../api/vX/admin/snippet/<SID>` for CRUD access.

#### 4. See Teammates
To see teammates and add how much you want, you can locate in `../api/vX/admin/team`. Use `../api/vX/admin/team/<ID>` to modify any teammate you want.

#### 5. See Suggestions
To change, create, and show any suggestion use the following addresses. (You have to be logged in as the superuser if you want the CRUD access)
```
../api/vX/admin/suggest/
../api/vX/admin/suggest/<ID>
```

### Fork
Fork for free :)
