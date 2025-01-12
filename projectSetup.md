# Facing problems

## permistion dinaid for the powershell

> solve this problem by this command
- **This Command set the permissions globaly**
``` bash
-ExecutionPolicy RemoteSigned -Scope CurrentUser
````

- **This command set permissions for only this project**
``` bash 
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```