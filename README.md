## Useful Git Configuration that one needs

#### Commit Template

> Create a git template 
```
vim ~/.gitmessage.txt

```
> Fill it with what you need. Example commit template below
```
Subject line (try to keep under 50 characters)

Multi-line description of commit,
feel free to be detailed.

[Ticket: X]
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
# modified:   lib/test.rb
#
```


```
git config --global commit.template ~/.gitmessage.txt
```
Then typing git commit will open this template

#### Autocorrect 

This will make git to guess commands after 2 seconds
```
git config --global help.autocorrect 20
```


#### Global Git Ignore
Edit global gitignore file
```
vim ~/.gitignore_global
```
Fill it with the file names that you want to be ignored all the time(Example below)
```
*~
.*.swp
.DS_Store
```

#### Oh-my-posh terminal for windows power shell
Install it
```
Install-Module oh-my-posh -Scope CurrentUser
```
Get color themes
```
Get-PoshThemes
```

```
Set-PoshPrompt -Theme  robbyrussel
```

```
Export-PoshTheme -FilePath ~/.mytheme.omp.json -Format json
```
Edit your own theme then edit your $PROFILE
```
vim $PROFILE
```
Type the below lines to it to make it open with your theme all the time
```
Import-Module oh-my-posh
Set-PoshPrompt -Theme  ~/.mytheme.omp.json
```
#### How to make sure your latest commit is also your branch head
Will show you current commit head information
```
git log -1
```

Will change the your current commit head to latest commit head of the branch
```
git reset --hard
```
or
```
git checkout master
```
will tell your commit is ahead of origin/master then you can run
```
git push
```
