
py2shpss
========


.. image:: https://img.shields.io/pypi/v/jamorasep.svg
   :target: https://pypi.python.org/pypi/jamorasep
   :alt:

.. image:: https://github.com/tachi-hi/jamorasep/workflows/CI/badge.svg
   :target: https://github.com/tachi-hi/jamorasep/actions?query=workflow%3ACI
   :alt: Build Status

.. image:: https://img.shields.io/pypi/l/jamorasep.svg
   :target: https://opensource.org/licenses/MIT
   :alt:

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

   jamorasep.parse("こんにちは", output_format="katakana")
   jamorasep.parse("こんにちは", output_format="simple-ipa")
   jamorasep.parse("こんにちは", output_format="kunrei")
   jamorasep.parse("こんにちは", output_format="hepburn")

External Link
^^^^^^^^^^^^^
https://clrd.ninjal.ac.jp/unidic/UNIDIC_manual.pdf