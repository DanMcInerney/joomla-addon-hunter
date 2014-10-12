joomla-addon-hunter
===================

Find potential SQLi in Joomla URLs. Had a need for [NBS 0.3](https://forum.intern0t.org/perl-python/3431-nbs-0-3-a.html) recently but that tool is broken so I rewrote the addon scanner part to find vulnerable addons in Joomla installs.


Usage
------

```shell
pip install --user requests
git clone https://github.com/DanMcInerney/joomla-addon-hunter
cd joomla-addon-hunter
python joomla-addon-hunter.py -u http://example.com
```
