.. _schema:

Structured Data Generation
==========================

For generating data by schema, just create an instance of :class:`~mimesis.schema.Field`
object, which takes any string which represents the name of data
provider in format *provider.method_name* (explicitly defines that the
method *method_name* belongs to data-provider *provider*) or *method* (will be
chosen the first provider which has a method *method_name*) and the
**\**kwargs** of the method *method_name*, after that you should
describe the schema in lambda function (or any other callable object) and pass it to
the object :class:`~mimesis.schema.Schema` and call method :meth:`~mimesis.schema.Schema.create`.

Optionally, you can apply a *key function* to result returned by the
method, to do it, just pass the parameter `key` with a callable object
which returns final result.

Example of usage:

.. code:: python

    from mimesis.enums import Gender
    from mimesis.locales import Locale
    from mimesis.schema import Field, Schema

    _ = Field(locale=Locale.EN)
    schema = Schema(
        schema=lambda: {
            "pk": _("increment"),
            "uid": _("uuid"),
            "name": _("text.word"),
            "version": _("version", pre_release=True),
            "timestamp": _("timestamp", posix=False),
            "owner": {
                "email": _("person.email", domains=["test.com"], key=str.lower),
                "token": _("token_hex"),
                "creator": _("full_name", gender=Gender.FEMALE),
            },
        iterations=2
    })
    schema.create()


Output:

.. code:: json

    [
      {
        "pk": 1,
        "uid": "c1b2fda1-762b-4c0b-aef7-e995e19758b6",
        "name": "brother",
        "version": "3.0.6-alpha.9",
        "timestamp": "2016-12-07T13:26:54Z",
        "owner": {
          "email": "tewing1841@test.com",
          "token": "09960ce907dee56a3c4a6730b7e1ff6ad9620b878c68ff978bfe296da09c1b4b",
          "creator": "Travis Burton"
        }
      },
      {
        "pk": 2,
        "uid": "b0f33a7e-0e3e-4bf0-92df-3ba869add555",
        "name": "disney",
        "version": "2.6.0-alpha.11",
        "timestamp": "2017-02-11T10:45:27Z",
        "owner": {
          "email": "cyprus1904@test.com",
          "token": "a087fadffce394141d3e93c895e4da6db906a60fd0886bad909dc179861b4650",
          "creator": "Dot Anderson"
        }
      },
    ]


By default, :class:`~mimesis.schema.Field` works only with providers which supported by :class:`~mimesis.Generic`,
to change this behavior should be passed parameter *providers* with a sequence of data providers:

.. code:: python

    from mimesis.schema import Field
    from mimesis.locales import Locale
    from mimesis import builtins

    custom_providers = (
         builtins.RussiaSpecProvider,
         builtins.NetherlandsSpecProvider,
    )
    _ = Field(Locale.EN, providers=custom_providers)

    _('snils')
    # Output: '239-315-742-84'

    _('bsn')
    # Output: '657340522'


The scheme is an iterator, so you can iterate over it, for example like this:


.. code:: python

    from mimesis import Schema, Field
    from mimesis.locales import Locale

    field = Field(Locale.DE)

    schema = Schema(
        schema=lambda: {
            "pk": field("increment"),
            "name": field("full_name"),
            "email": field("email", domains=["example.org"]),
        },
        iterations=100,
    )


    for obj in schema:
        print(obj)

Output:

.. code:: text

    {'pk': 1, 'name': 'Lea Bohn', 'email': 'best2045@example.org'}
    ...
    {'pk': 100, 'name': 'Karsten Haase', 'email': 'dennis2024@example.org'}


Field vs Fieldset
-----------------

The main difference between :class:`~mimesis.schema.Field` and :class:`~mimesis.schema.Fieldset` is that
:class:`~mimesis.schema.Fieldset` generates a set (well, actually a ``list``) of values for a given field,
while :class:`~mimesis.schema.Field` generates a single value.

Let's take a look at the example:

.. code:: python

    >>> from mimesis import Field, Fieldset
    >>> from mimesis.locales import Locale

    >>> field = Field(locale=Locale.EN)
    >>> fieldset = Fieldset(locale=Locale.EN)

    >>> field("name")
    Chase

    >> [field("name") for _ in range(3)]
    ['Nicolle', 'Kelvin', 'Adaline']

    >>> fieldset("name", i=3)
    ['Basil', 'Carlee', 'Sheryll']


The keyword argument **i** is used to specify the number of values to generate.
If **i** is not specified, a reasonable default value (which is 10) is used.

The :class:`~mimesis.schema.Fieldset` class is a subclass of :class:`~mimesis.schema.BaseField` and inherits
all its methods, attributes and properties. This means that API of :class:`~mimesis.schema.Fieldset` is almost the same
as for :class:`~mimesis.schema.Field` which is also a subclass of :class:`~mimesis.schema.BaseField`.

Almost, because an instance of :class:`~mimesis.schema.Fieldset` accepts keyword argument **i**.

While it may not be necessary in most cases, it is possible to override the default name
of a keyword argument **i** for a specific field.

Let's take a look at the example:

.. code:: python

    >>> from mimesis import Fieldset
    >>> class MyFieldset(Fieldset):
    ...     fieldset_iterations_kwarg = "wubba_lubba_dub_dub"

    >>> fs = MyFieldset(locale=Locale.EN)
    >>> fs("name", wubba_lubba_dub_dub=3)
    ['Janella', 'Beckie', 'Jeremiah']

    # The order of keyword arguments doesn't matter.
    >>> fs("name", wubba_lubba_dub_dub=3, key=str.upper)
    ['RICKY', 'LEONORE', 'DORIAN']


Fieldset and Pandas
-------------------

If your aim is to create synthetic data for your `Pandas dataframes <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>`_ ,
you can make use of the :class:`~mimesis.schema.Fieldset` as well.

With :class:`~mimesis.schema.Fieldset`, you can create datasets that are
similar in structure to your real-world data, allowing you to perform accurate
and reliable testing and analysis:

.. code:: python

    import pandas as pd
    from mimesis.schema import Fieldset
    from mimesis.locales import Locale

    fs = Fieldset(locale=Locale.EN, i=5)

    df = pd.DataFrame.from_dict({
        "ID": fs("increment"),
        "Name": fs("person.full_name"),
        "Email": fs("email"),
        "Phone": fs("telephone", mask="+1 (###) #5#-7#9#"),
    })

    print(df)

Output:

.. code:: text

    ID             Name                          Email              Phone
    1     Jamal Woodard              ford1925@live.com  +1 (202) 752-7396
    2       Loma Farley               seq1926@live.com  +1 (762) 655-7893
    3  Kiersten Barrera      relationship1991@duck.com  +1 (588) 956-7099
    4   Jesus Frederick  troubleshooting1901@gmail.com  +1 (514) 255-7091
    5   Blondell Bolton       strongly2081@example.com  +1 (327) 952-7799


Isn't it cool? Of course, it is!


Probability-Expression Syntax
-----------------------------

Real-world data can be messy and may contain missing values.
This is why generating data with **None** values may be useful
to create more realistic synthetic data.

Luckily, you can achieve this by using **probability-expression** syntax:

.. code:: python

    >>> from mimesis import Fieldset
    >>> from mimesis.locales import Locale
    >>> from mimesis.random import random

    >>> fieldset = Fieldset(Locale.EN, i=5)
    >>> fieldset("email[none=0.3]")

    [None, None, None, 'bobby1882@gmail.com', None]

In the example above, the probability of generating a **None** value is 0.3, which is 30%.

If the probability-expression and key function are **both defined**,
then the key function is **exclusively applied** to truthy values.

.. code:: python

    >>> fieldset = Fieldset(Locale.EN, i=5)
    >>> fieldset("email[none=0.3]", key=str.upper)

    [None, 'BOB1235@DUCK.COM', None, None, None]

Exporting Data
--------------

You can export data as JSON, CSV or as pickled representations of objects:

.. code:: python

    from mimesis.locales import Locale
    from mimesis.schema import Field, Schema

    _ = Field(locale=Locale.EN)
    schema = Schema(schema=lambda: {
        "pk": _("increment"),
        "name": _("text.word"),
        "version": _("version"),
        "timestamp": _("timestamp", posix=False),
    })
    schema.to_csv(file_path='data.csv', iterations=1000)
    schema.to_json(file_path='data.json', iterations=1000)
    schema.to_pickle(file_path='data.obj', iterations=1000)


Example of the content of ``data.csv`` (truncated):

.. code:: text

    pk,uid,name,version,timestamp
    1,save,6.8.6-alpha.3,2018-09-21T21:30:43Z
    2,sponsors,6.9.6-rc.7,2015-03-02T06:18:44Z
    3,after,4.5.6-rc.8,2022-03-31T02:56:15Z
    4,queen,9.0.6-alpha.11,2008-07-22T05:56:59Z

