
jamorasep
=========


.. image:: https://img.shields.io/pypi/v/jamorasep.svg
   :target: https://pypi.python.org/pypi/jamorasep
   :alt: pypi

.. image:: https://readthedocs.org/projects/jamorasep/badge/?version=latest
   :target: https://jamorasep.readthedocs.io/en/latest
   :alt: Documentation Status

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

   import jamorasep

   jamorasep.parse("シャンプーハット")
   # => ['シャ', 'ン', 'プ', 'ー', 'ハ', 'ッ', 'ト']

   jamorasep.parse("シャンプーハット", output_format="katakana")
   # => ['シャ', 'ン', 'プ', 'ー', 'ハ', 'ッ', 'ト']

   jamorasep.parse("シャンプーハット", output_format="simple-ipa")
   # => ['ɕa', 'N', 'pu', ':', 'ha', 'Q', 'to']

   jamorasep.parse("シャンプーハット", output_format="kunrei")
   # => ['sya', 'n', 'pu', ':', 'ha', 't', 'to']

   jamorasep.parse("シャンプーハット", output_format="hepburn")
   # => ['sha', 'n', 'pu', ':', 'ha', 't', 'to']

See `Kana Mapping Table <https://jamorasep.readthedocs.io/en/latest/kanamap.html>`_ for the full mapping of each output format.
