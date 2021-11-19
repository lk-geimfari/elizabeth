About Mimesis
=============

What Mimesis is?
----------------

The problem that **Mimesis** solves and solves it perfectly is generating data.
When you need to populate database, create complex structured JSON/XML files,
anonymize data taken from productive services then **Mimesis** is this is
exactly what you need.

What Mimesis is Not?
--------------------

**Mimesis** is **not object factory** and it was not developed for using with
specific database or ORM (such as Django ORM, SQLAlchemy etc.).
It does not mean that you can't use it with ORM on the contrary,
this will be done very simply, this only means that possibly you'll
need third-party libraries to do it, like `mimesis-factory <https://github.com/lk-geimfari/mimesis-factory>`_ or another one.

What is the fake data?
----------------------
Fake data is a type of data that does not contain any useful or sensitive data, but serves to
reserve space where real data is nominally present. Fake data can be used as a placeholder for
both testing and operational purposes. For testing, dummy data can also be used as stubs.

What does name mean?
--------------------

Mimesis (`/maɪˈmiːsəs/ <https://en.wikipedia.org/wiki/Help:IPA/English>`_;
`Ancient Greek <https://en.wikipedia.org/wiki/Ancient_Greek_language>`_: μίμησις (*mīmēsis*), from μιμεῖσθαι (*mīmeisthai*),
"to imitate", from μῖμος (mimos), "imitator, actor") is a critical and philosophical
term that carries a wide range of meanings, which include imitation, representation,
mimicry, imitatio, receptivity, nonsensuous similarity, the act of resembling,
the act of expression, and the presentation of the self.

Why octopus?
------------
Basically, because octopuses are cool guys, but also because of the
fantastic `mimicry <https://en.wikipedia.org/wiki/Mimicry>`_ abilities of some families of octopuses.
Have you ever hear about `Thaumoctopus mimicus <https://en.wikipedia.org/wiki/Mimic_octopus>`_?
Just read about that guy, because he is a really badass one.

Features
--------
The key features are:

- **Easy**: Designed to be easy to use and learn.
- **Multilingual**: Supports data for `a lot of languages <https://mimesis.name/getting_started.html#locales>`_.
- **Performance**: The `fastest <https://mimesis.name/foreword.html#performance>`_ data generator available for Python.
- **Data variety**: Supports `a lot of data providers <https://mimesis.name/api.html>`_ for a variety of purposes.
- **Country-specific data providers**: Provides data specific only for `some countries <https://mimesis.name/api.html#builtin-data-providers>`_.
- **Extensibility**: You can create your own data providers and use them with Mimesis.
- **Generic data provider**: The `simplified <https://mimesis.name/getting_started.html#generic-provider>`_ access to all the providers from a single object.
- **Zero hard dependencies**: Does not require any modules other than the Python standard library.
- **Schema-based generators**: Provides an easy mechanism to generate data by the schema of any complexity.


Advantages
----------
This library offers a number of advantages over other similar libraries, such as Faker:

-  **Performance**: Significantly faster than other similar libraries.
-  **Completeness**: Strives to provide many detailed providers that offer a variety of data generators.
-  **Simplicity**: Does not require any modules other than the Python standard library.


Performance
-----------

Below you can see the result of `performance comparison <https://gist.github.com/lk-geimfari/99c5b45906be5299a3088f42c3f55bf4>`_ of Mimesis and Faker:


Generating 10k full names
~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------------------+---------------------+------------------------+------------------------+
| Library  | Method name                            | Iterations          |  Uniqueness            |  Runtime (in seconds)  |
+==========+========================================+=====================+========================+========================+
|  Mimesis | :meth:`~mimesis.Person.full_name`      | 10 000              |  9988 (99.88%)         |  0.137                 |
+----------+----------------------------------------+---------------------+------------------------+------------------------+
|  Faker   | **Faker.name()**                       | 10 000              |  9363 (93.63%)         |  1.758                 |
+----------+----------------------------------------+---------------------+------------------------+------------------------+

Generating 100k full names
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------------------+---------------------+------------------------+------------------------+
| Library  | Method name                            | Iterations          |  Uniqueness            |  Runtime (in seconds)  |
+==========+========================================+=====================+========================+========================+
|  Mimesis | :meth:`~mimesis.Person.full_name`      | 100 000             |  98 265 (98.27%)       |  1.344                 |
+----------+----------------------------------------+---------------------+------------------------+------------------------+
|  Faker   | **Faker.name()**                       | 100 000             |  71 067 (71.07%)       |  17.375                |
+----------+----------------------------------------+---------------------+------------------------+------------------------+

Generating 1 million full names
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------------------------------------+---------------------+------------------------+------------------------+
| Library  | Method name                            | Iterations          |  Uniqueness            |  Runtime (in seconds)  |
+==========+========================================+=====================+========================+========================+
|  Mimesis | :meth:`~mimesis.Person.full_name`      | 1 000 000           |  847 645 (84.76%)      |  13.685                |
+----------+----------------------------------------+---------------------+------------------------+------------------------+
|  Faker   | **Faker.name()**                       | 1 000 000           |  330 166 (33.02%)      |  185.945               |
+----------+----------------------------------------+---------------------+------------------------+------------------------+
