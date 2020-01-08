### Creare utente/post da shell flask python

venv_flask) (base) Pasquales-MacBook-Pro:personal-blog--python-and-flask pasqualespica$ flask shell
Python 3.7.3 (default, Mar 27 2019, 16:54:48) 
[Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
App: blog [development]
Instance: /Users/pasqualespica/my_data/PAS7B/pers/CORSI_/udemy/blog-personale-con-python-e-flask/personal-blog--python-and-flask/instance
>>> from blog import db
>>> from blog.models import Post, User
>>> u = User(username='test', email='tststs@mialmail', password='apfwirryuorwg')
]>>> db.session.add(u)
>>> db.session.commit()

>>> p = Post(title='primo post', body='some random data stuffs', author=u)
>>> db.session.add(p)
>>> db.session.commit()

poi Controllare tramite DB Browser

################################################################################################################################

#### queries / user / password hashing

>>> from blog import db
>>> from blog.models import Post, User
>>> Post.query.all()
[<Post 1>]
>>> User.query.all()
[<User 1>]
>>> u = User.query.get(1)
>>> u.email
'tststs@mialmail'
"query" e' l'analogo di "objects" su Django

>>> p = Post(title='secondo post', body='secondo psto body', author=u)
>>> db.session.add(p)
>>> db.session.commit()

>>> post_queryset = Post.query.all()
>>> post_queryset
[<Post 1>, <Post 2>]

Per evitare di importare sempre DB e modelli si puo;' definire 
@app.shell_context_processor

--- Esempio Utente non esiste
>>> dir()
['Post', 'User', '__builtins__', 'app', 'db', 'g']
>>> u = User.query.get(2)
>>> u
>>> type (u)
>>> User.query.first()
User('1', 'test', 'tststs@mialmail')

--- Filter e FilterBy
>>> Post.query.filter(User.username=="test").all()
[Post('1', 'primo post', Post('2', 'secondo post']
>>> Post.query.filter(User.username=="test")
<flask_sqlalchemy.BaseQuery object at 0x1117203c8>

Anche piu' filtri alla volta ...

>>> Post.query.filter(User.username=="test", User.id==1).all()
[Post('1', 'primo post', Post('2', 'secondo post']

Un metodo piu' rapido per fare queste interrogazioni e' usare FilterBy
>>> User.query.filter_by(username="test").all()
[User('1', 'test', 'tststs@mialmail')]

>>> User.query.filter(User.username=="test").all()
[User('1', 'test', 'tststs@mialmail')]

Aggiornamento instance nel nostro DB
ex. aggiornare titolo
>>> p = Post.query.first()
>>> p
Post('1', 'primo post'
>>> p
Post('1', 'primo post'
>>> p.title="primo posto UPD"
>>> db.session.commit()

Per cancellare invece ...
>>> p = Post.query.get(2)
>>> p
Post('2', 'secondo post')
>>> db.session.delete(p)
>>> db.session.commit()
>>> Post.query.all()
[Post('1', 'primo posto UPD')]

################################################################################################################################


####

################################################################################################################################




