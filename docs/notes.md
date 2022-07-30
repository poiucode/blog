<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>

    <title>Blog</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="../docs/css/style.css" rel="stylesheet">
</head><body>
    <div class="container">
      <div class="row">
        <h1>Say hello to my little blog!</h1>
      </div>
      <div class="row">
          <div class="col">
              <ol class="list-unstyled">
                  <li><a href="index.html">Home</a></li>
                  <li><a href="notes.md">Blog</a></li>
                  <li><a href="contact.html">Contact</a></li>
              </ol>
          </div>
          <div class="col-sm-8">  # Notes from the Keyboard

## June 23 
So I installed ubuntu on my chromebook in a separate partition. Followed instructions from the unbuntu site [here](https://ubuntu.com/tutorials/install-ubuntu-on-chromebook#1-overview). git wasn't included in the installation and so I had to install it, which I googled (as I've been doing with virtually everything), and I then had trouble connecting to github because of the need for a PAT (Personal Authentication Token), or PAT. I found the PAT solution to be ... onerous. Too many things to link up and I didn't like that they expire -- which would mean yet another thing I'd need to keep track of... so forget that. But SSH (Secure Shell Protocol) was another option and I went with that. Then this happened:  
- If missing public key: sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C99B11DEB97541F0
Then I found this: 
## github keeps asking for password after established ssh keys ... need to reset origin to SSH ...not HTTPs
- You’ll have to also adjust the remote URL your local repository uses to access your Github repository. 
- That URL decides which protocol (SSH or HTTPS) Git uses. 
- You can find the URLs behind the green “Code” button on your repository page.

Once you have the one you want, you can use git remote to set which URL to use:
```
git remote set-url origin <URL>
git remote set-url --push origin <URL>
https://github.community/t/ssh-keys-set-up-but-github-still-asks-for-password/159841 
```
 
## _June 25_ - 
- I loaded ubuntu xfce onto my Chromebook and got it working since ubuntu unity was too large
- Installed git since not preinstalled with xfce
- refamiliarized myself with git workflow
- set up ssh on local
- had trouble syncing to github for 1/2h and then found the answer: i needed to update remote origin to SSH from HTTPs because when I originally cloned the repo into my local folder, I used HTTPs! 
- updated personalhomepage/index.html on my local machine from the fork I updated other day (this was the repo I cloned and fixed with https to ssh) and then figured out how to create a PR ... which had to be done in my fork, not the repo owner's

## _June 26_
HW 1 
HINT:For free stock photos:  pixabay.com
HINT:For great free backgrounds, check out:  www.toptal.com/designers/subtlepatterns/
HINT:For gorgeous background gradients, check out:  www.webcore-it.com/colorful-background/  [this link doesn't work]

- [Rename key folders](https://askubuntu.com/questions/22592/is-it-safe-to-rename-special-user-folders) Looked into renaming folders like Documents Downloads to lowercase so I don't have to type uppercase for bash commands

## _June 28_

- Continuing work on HW1 and 2 and now I'mbuilding templates. I decided to build files and folders locally and then create repo and push everything. But my push wound up going to a different repo even though I cloned the new one into local folder. 
- used [this](https://stackoverflow.com/questions/17986615/one-command-to-create-a-directory-and-file-inside-it-linux-command) to create folder and files inthe same command 

	- first thing I did to fix was to undo the pushing using these commands from [here](https://www.linkedin.com/pulse/how-undo-last-push-git-revert-merge-hasnt-been-migrated-yadav): 
```
git reset --hard 543acea
git push --force
```
- Now I'm figuring out how to reset origin ... and here's how to do it: ` git remote set-url origin git@github.com:poiucode/my-blog.git

#### Tips from homework
- JotForm for a nice “contact me” form:  jotform.com 
- Disqus for a comment section on your blog:  disqus.com

### OOPS!
- I committed my files then pushed to Github ... only to discover that I had overwritten all the files in my local directory with files from Michael's github personalhomepage. I still don't know exactly how this happened. 

## _June 29_
### OOPS! (cont'd)
My error last night falls into the old "don't code when you're tired" vein because just like woodworking...you'll hurt yourself. In this case, it was overwriting the Homework 1 files I'd spent a couple hours on over the weekend. Not a big deal since not mission critical and a good time in my learning for this to happen ... but still.  [note: would be nice to build a way to enter these notes and easily push to a blog through bash or with quick git command]. Anyway, after digging for a few minutes to see how to reverse after realizing what I'd done, I went to bed (actually , watched a mediocre show, then bed). 

I woke up this morning with some clarity -- i **did** commit before my fatal error... so maybe there's a way to view the contents of the old files from that prior commit. I need to figure out how to use git checkout to do this... but first, I'm revisitng what I tried to do over weekend which is to show I/O of my bash terminal session. [This](https://askubuntu.com/questions/758991/bash-shell-output-history-file-location) is a really good summary of that.   

I dug around and tried to check out older commits but saw only one commit with something like `HEAD of 0000000 to 2308852` ... which wasn't encouraging. I tried a bit more but it seems I really did manage to write over my files with files from a remote origin i had forked from days before (michaelpb personalhomepage). The problem was a command I ran late at night where git told me something about my remote origin and working from a different place in the commit history or something, and told me to try a command to `reset remote branch upstream` or something like that. I've tried figuring out how to print out my entire bash screen but didn't want to spend too much time down *that* rabbit hole, though I did find the `history` command (which was also on the Kickstart cheatsheet btw, but hadn't seen previously). Anyway, I still don't understand exactly what happened... but I learned a lesson based on two things I did wrong: 
1. **branch** !!! Always create separate branches when mucking around. And 
2. **cp** not **mv** when getting files to another folder for a push. I moved the files to a new folder I created with the idea of pushing to the empty repo I created... but had I just copied them, then even after the overwrite (minor) debacle, I'd have had the original files too. 

#### Lesson Learned! 

And then my chromebook died (low power)...which began another leg of the journey as I discovered on reboot that... *I couldn't get back into ubuntu!!*

I then spent 1/2hr googling to figure out and nothing worked: none of the `chroot` or `sudo startxfce` commands. Nothing. But something really interesting then happened -- I can't remember exactly, but I think I stumbled on a blog post that mentioned you can enable Linux from *inside* ChromeOS!!! Which I immediately did to my utter delight because I realized this is the best of both worlds: 
- I have access to a bash shell and the ability to navigate the file system and run commands as *sudo* ...
- while being inside ChromeOS and having access to files and settings and using Chrome which has the best browser performance and makes life just better (because it's faster). 

I was finding that XFCE -- the *budget* (joking...it's lightweight) ubuntu installation I needed b/c Unity was too big had serious deficiencies and issues that were taking me back to my first linux install in 1999 -- dragging a window for example would be super slow and leave happy trails on the screen: stuff that's been worked out *decades ago!!!* and that's a serious drag on time. But one resulting issue was that I had taken some time with this file...and it was now "lost" in a partition I couldn't access. 

But I then figured out (through googling, of course) that I could access the shell with `ctrl shift [right arrow i.e. where F2 key would be]` and that takes you to the shell where you type username `chronos` (no pwd) to get in. I figured out where my files were located and cd'd to them and copied into ChromeOS downloads (in `mnt/chromeos`) which is the only accessible folder that's shared between the partition and ChromeOS partition (from which I was working with Linux).  

After I got some files back, I worked on getting a good text editor and installed gedit which I'd used for the past few days on the ubuntu partition, but about an hour in, it totally crashed and I coudln't even find the process in the Task Manager list. So I restarted the machine. 

I messed around with vim for 20 mins or so with the vimtutor but realized I was too tired and wanted something out of the box and easy...which is when I (re)discovered the built-in Text app on Chrome -- and it's really good. File management is in a pane on the left, really intuitive, and it recognized markdown. So, it's better than gedit and easier to use.

Off to bed.

## June 30
Worked on 2.3 Python exercises. Need to get this down in order to do HW2 building a templated mini personal site

## July 1
Did some more 2.3 exercises. Ran `git status` and realized that git isn't enabled in my workingdirectory. 
Got these errors: 
```
fatal: not a git repository (or any parent up to mount point /mnt)
Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
```
And so I googled and found [this](https://stackoverflow.com/questions/16853624/git-discovery-across-filesystem-not-set) on Stack Overflow and scrolled down and found a less popular answer but which seemed to fit my issue and ran this command: `export GIT_DISCOVERY_ACROSS_FILESYSTEM=1`
 
This command ended up working and I created the `blog` repo on github, cloned into local, and did `git status` and everything looks good! 

## July 2
Task at hand: create branches, build my build files (build.sh and build.py), merge, and push. I spoke with Michael yesterday and went over my plan with the build files being the most complicated--but still quite easy. 

**Python**: just need to open the files, assign to a variable (which I will keep adding text to),then use write to write to a new file. 
1. Built index page and ran in terminal. First error of the day: 
```
jon@penguin:/mnt/chromeos/GoogleDrive/MyDrive/projects/blog$ python3 build.py 
  File "/mnt/chromeos/GoogleDrive/MyDrive/projects/blog/build.py", line 4
    index = open("./templates/head.html).read()
                                               ^
SyntaxError: EOL while scanning string literal
```
Turns out, as you can see above, I forgot to close the file paths with closing quotation mark... 

2. Next error was this: 
```
Traceback (most recent call last):
  File "/mnt/chromeos/GoogleDrive/MyDrive/projects/blog/build.py", line 8, in <module>
    open(index, "w+").write("./docs")
```
I ran the command a second time just because...that's what rookies do I guess...and then I saw my mistake: I was writing this text into a directory...but *not into any file!!* Fixed by making it `./docs/index.html`  ... let's see what we get!

3. Oops! I had the commands swapped: `open` needs to open--or create if it doesn't exist--the file name/path; `write` will write in the variable or string (i.e. text). 
This worked ... sort of. The page and left column render ... but not text from content folder. Looked at page source of the newly created/rendered index.html file in the browser and see that there's a hanging </div> tag. Tells me I need to fix html in one of my templates. 

4. Deleted the hanging <\/div> ... but still no success. :(  Hmmm... everything looks good on the face of it... but I need to use a print statement to see what my `index` variable looks like in my python file to see how it's concatening the files and why ./content/index.html isn't in there. And of course ... validation! That content is missing from print statement just like in the rendered file. I must have the filepath wrong. ... but no, my index.html file was empty! Even though I had it in my text editor with text. I closed that file in teh text editor and, of course, just like happened over the weekend when I overwrote all my files with git...I couldn't find it anymore. AGain, no biggie, since I didn't have much I"d written in that file anyway. Now it all works! Time to write the next pages on the site...

5. pages written but I discovered something else (I have a nagging feeling discovery won't end...but that's why I'm doing this!!): my style sheet was linked to the wrong folder andnot generating, but that gave me pause to look at other files and as I was tweaking filenames (particularly this file) I had a Eureka kind of moment: e.g. for this file, blog.md, I have a copy in /docs and /content but if I were to accidentally mess up the filepath for my site generators (either python or bash), I could overwrite files. And having already dealt with that a couple times, I'm like thrice bitten tres shy! So this just reinforces the need to be extra cautious and careful, not to do big stuff when tired, and even for small file ops like this, to consider using a file manager instead of command line. Of course, in the future as multiple files are handled, that won't be an option. 

## July 3
Woke up this morning to begin work on the PR's -- for bash and python site generators. Now...I've already wired up my site and got those working, so I'm doing this a bit backwards. But no worries, I've done other changes (like update this file) that I can do for the pull request to get that practice. 
1. I created branch ssg-bash and then a PR on github. But when ready to merge, there's no merge button ... just a "Compare and pull request". I hopped around my page on github but no merge button or option anywhere. So I merged locally. will see what looks like on the next push


## July 26
Put in a few hours building the structure of the site using an object with attributes and a method, found the glob function online to solve problem of how can I get a list of my filepaths, and learned to import an object into another file. This is most progress in weeks! 

## July 29
Got site almost working except for replace function and I pushed to github right before meeting with Michael B. We talked about fixing the replace() to get working, simplifying code, and he reminded me about startswith() as a more readable (and common) alternative to  fnmatch.filter() 

## July 30 
Got site working with replace, refactored more, and in good spot! Onto next lessons to prep for HW4!! 
              </div>
        </div>
    </div>
</body>
</html>