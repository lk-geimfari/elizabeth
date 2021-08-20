.. _api-reference:

=============
API Reference
=============

This part of the documentation covers all the public interfaces of *Mimesis*.


Random object
=============

Random
------

.. automodule:: mimesis.random
   :members:


Builtin Data Providers
======================

BrazilSpecProvider
------------------

.. autoclass:: mimesis.builtins.BrazilSpecProvider
   :members:
   :special-members: __init__

DenmarkSpecProvider
-------------------

.. autoclass:: mimesis.builtins.DenmarkSpecProvider
   :members:
   :special-members: __init__

NetherlandsSpecProvider
-----------------------

.. autoclass:: mimesis.builtins.NetherlandsSpecProvider
   :members:
   :special-members: __init__

RussiaSpecProvider
------------------

.. autoclass:: mimesis.builtins.RussiaSpecProvider
   :members:
   :special-members: __init__

UkraineSpecProvider
-------------------

.. autoclass:: mimesis.builtins.UkraineSpecProvider
   :members:
   :special-members: __init__

USASpecProvider
---------------

.. autoclass:: mimesis.builtins.USASpecProvider
   :members:
   :special-members: __init__

PolandSpecProvider
------------------

.. autoclass:: mimesis.builtins.PolandSpecProvider
   :members:
   :special-members: __init__

Shortcuts
=========

.. automodule:: mimesis.shortcuts
   :members:


Custom Exceptions
=================

LocaleError
-----------

.. autoclass:: mimesis.exceptions.LocaleError
   :members:

FieldError
----------

.. autoclass:: mimesis.exceptions.FieldError
   :members:

SchemaError
-----------

.. autoclass:: mimesis.exceptions.SchemaError
   :members:

NonEnumerableError
------------------

.. autoclass:: mimesis.exceptions.NonEnumerableError
   :members:


Base Providers
==============

BaseProvider
------------

.. autoclass:: mimesis.providers.BaseProvider
   :members:
   :special-members: __init__

BaseDataProvider
----------------

.. autoclass:: mimesis.providers.BaseDataProvider
   :members:
   :special-members: __init__


Generic Providers
=================

Generic
-------

.. autoclass:: mimesis.Generic
   :members:
   :special-members: __init__



Locale-Dependent Providers
==========================

Address
-------

.. autoclass:: mimesis.Address
   :members:
   :special-members: __init__

Finance
-------

.. autoclass:: mimesis.Finance
   :members:
   :special-members: __init__

Datetime
--------

.. autoclass:: mimesis.Datetime
   :members:
   :special-members: __init__

Food
----
.. autoclass:: mimesis.Food
   :members:
   :special-members: __init__

Person
--------

.. autoclass:: mimesis.Person
   :members:
   :special-members: __init__

Science
-------

.. autoclass:: mimesis.Science
   :members:
   :special-members: __init__

Text
----

.. autoclass:: mimesis.Text
   :members:
   :special-members: __init__


Locale-Independent Providers
=============================

BinaryFile
----------

.. autoclass:: mimesis.BinaryFile
   :members:
   :special-members: __init__

Code
----

.. autoclass:: mimesis.Code
   :members:
   :special-members: __init__

Choice
------

.. autoclass:: mimesis.Choice
   :members:
   :special-members: __init__

Cryptographic
-------------

.. autoclass:: mimesis.Cryptographic
   :members:
   :special-members: __init__

Development
-----------

.. autoclass:: mimesis.Development
   :members:
   :special-members: __init__

File
----

.. autoclass:: mimesis.File
   :members:
   :special-members: __init__

Hardware
--------

.. autoclass:: mimesis.Hardware
   :members:
   :special-members: __init__

Internet
--------

.. autoclass:: mimesis.Internet
   :members:
   :special-members: __init__

Numbers
-------

.. autoclass:: mimesis.Numbers
   :members:
   :special-members: __init__

Path
----

.. autoclass:: mimesis.Path
   :members:
   :special-members: __init__

Transport
---------

.. autoclass:: mimesis.Transport
   :members:
   :special-members: __init__


Schema
======

BaseField
---------

.. autoclass:: mimesis.schema.BaseField
   :members:
   :special-members: __call__

Field
------

.. autoclass:: mimesis.schema.Field
   :members:

Schema
------

.. autoclass:: mimesis.schema.Schema
   :members:

Enums
=====

.. automodule:: mimesis.enums
   :members:
   :undoc-members:
