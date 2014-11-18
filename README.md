## 目录结构

```
xblog/
  |_____ xblog/
  |        |_____ __init__.py
  |        |_____ settings.py : 全局设置
  |        |_____ urls.py : 全局url路径
  |        |_____ wsgi.py
  |
  |_____ manage.py
  |
  |_____ apps/ : 所有的app都存放于此
  |        |_____ __init__.py
  |        |_____ home/ : 负责主页的业务
  |                 |_____ __init__.py
  |                 |_____ urls.py
  |                 |_____ views.py
  |                 |_____ models.py : 一个model对应于数据库中的一张表
  |
  |_____ templates/ : 模板存放于此
           |_____ home/ : 对应于apps/home
                    |_____ index.html                  	
	
```


