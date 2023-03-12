
jamorasep
=========


.. image:: https://img.shields.io/pypi/v/jamorasep.svg
   :target: https://pypi.python.org/pypi/jamorasep
   :alt: pypi

.. image:: https://github.com/tachi-hi/jamorasep/actions/workflows/test.yml/badge.svg
   :target: https://github.com/tachi-hi/jamorasep/actions/workflows/test.yml
   :alt: CI

.. image:: https://img.shields.io/pypi/l/jamorasep.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT

Japanese text parser to separate Hiragana/Katakana string into morae (syllables).

License
-------

Copyright :copyright: 2023 Hideyuki Tachibana, `MIT License <https://github.com/tachi-hi/jamorasep/blob/master/LICENSE>`_

Usage
-----
Install
^^^^^^^

.. code-block:: bash

    pip install jamorasep

Code Example
^^^^^^^^^^^^

.. code-block:: python

   # import
   import jamorasep
   jamorasep.parse("シャンプーハット", output_format="katakana")
   jamorasep.parse("シャンプーハット", output_format="simple-ipa")
   jamorasep.parse("シャンプーハット", output_format="kunrei")
   jamorasep.parse("シャンプーハット", output_format="hepburn")
