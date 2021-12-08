## Useful Git Configuration that one needs

#### Commit Template

> Create a git template 
```zsh
vim ~/.gitmessage.txt

```
> Fill it with what you need. Example commit template below
```txt
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


```zsh
git config --global commit.template ~/.gitmessage.txt
```
Then typing git commit will open this template

#### Autocorrect 

This will make git to guess commands after 2 seconds
```zsh
git config --global help.autocorrect 20
```


#### Global Git Ignore
Edit global gitignore file
```zsh
vim ~/.gitignore_global
```
Fill it with the file names that you want to be ignored all the time(Example below)
```.gitignore
# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary
*.test

# Output of 
*.out
/pact
/pacts
log
logs
*~
.*.swp
.DS_Store
```
Then configure for it to be come into effect by the command below 
```bash
git config --global core.excludesFile '~/.gitignore_global'
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
```zsh
git log -1
```

Will change the your current commit head to latest commit head of the branch
```zsh
git reset --hard
```
or
```zsh
git checkout master
```
will tell your commit is ahead of origin/master then you can run
```zsh
git push
```

#### Oh-my-zsh fast syntax highlighting

Make sure you have installed the zsh terminal with oh-my-zsh

[Syntax highlight](https://github.com/zdharma/fast-syntax-highlighting)


#### Zsh Autocomplete

```zsh
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

Then add following lines to your .zshrc 
```zsh
plugins=(git
        dnf
        zsh-autosuggestions
        )
```

#### How to change author information using git
```zsh
git config --global user.name "John Doe"
```
```zsh
git config --global user.email "john@doe.org"
```
