# IO 

**IO** is a blog base on Python + Django ([IO Repository](https://github.com/xushvai/io)).  
In a few minutes you'll be set up with a minimal, responsive blog like the one below !  
![1](docs/1.png)  

## Quick Start  

### Clone repository  
```
git clone https://github.com/xushvai/io.git  
```

### Environmental preparations  
The environment must be 'Python2.7(devel) + Django1.7.1 + MySQL'.  

Installation of Python refer to https://www.python.org/downloads.   
Installation of MySQL refer to http://www.mysql.com/downloads.   
Installation of Django just do :   
```
sudo pip install django==1.7.1
```
Auto install other requirements : 
```
python install_requirements.py   
```
*(The location of the file 'install_requirements.py' is [io/install_requirements.py](./install_requirements.py))*

If the 'pip' is not installed in your environment, follow the steps below to complete the installation :  
```
curl https://bootstrap.pypa.io/ez_setup.py -o - | python  
```
```
easy_install pip  
```




### Config Database   








Fork IO to your User Repository

Fork this repo, then rename the repository to yourgithubusername.github.io.

Your Jekyll blog will often be viewable immediately at <http://yourgithubusername.github.io> (if it's not, you can often force it to build by completing step 2)

![Step 1](/images/step1.gif "Step 1")

### Step 2) Customize and view your site

Enter your site name, description, avatar and many other options by editing the _config.yml file. You can easily turn on Google Analytics tracking, Disqus commenting and social icons here too.

Making a change to _config.yml (or any file in your repository) will force GitHub Pages to rebuild your site with jekyll. Your rebuilt site will be viewable a few seconds later at <http://yourgithubusername.github.io> - if not, give it ten minutes as GitHub suggests and it'll appear soon

> There are 3 different ways that you can make changes to your blog's files:

> 1. Edit files within your new username.github.io repository in the browser at GitHub.com (shown below).
> 2. Use a third party GitHub content editor, like [Prose by Development Seed](http://prose.io). It's optimized for use with Jekyll making markdown editing, writing drafts, and uploading images really easy.
> 3. Clone down your repository and make updates locally, then push them to your GitHub repository.

![_config.yml](/images/config.png "_config.yml")
  
### Step 3) Publish your first blog post

Edit `/_posts/2014-3-3-Hello-World.md` to publish your first blog post. This [Markdown Cheatsheet](http://www.jekyllnow.com/Markdown-Style-Guide/) might come in handy.

![First Post](/images/first-post.png "First Post")

## Questions?

[Open an Issue](https://github.com/xushvai/io/issues/new) and let's chat!
