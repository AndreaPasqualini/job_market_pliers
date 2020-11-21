# Job Market Pliers

> A program that won't make you miss application deadlines.<br>
> 👉 Intended audience: Candidates on the Job Market for Economists.

This repository is interesting only for the file [pliers.py](./pliers.py).
The file is supposed to be used in a terminal.

First, download the files that EJM (https://econjobmarket.org) and JOE (https://aeaweb.org/joe/listings) offer for you. They are different from each other and difficult to control (e.g., too many columns for a human to read).
EJM offers a CSV file, which is ready to be used by this program.
_JOE offers a XLS file, which needs to be manually converted to CSV before use (see below for the reason)._
Second, open the terminal in the folder where the file [pliers.py](./pliers.py) is, together with the CSV files.

Due to the terms and conditions of EJM and JOE, I am not allowed to post their files here. Therefore you need to download them by yourself.
However, the file [example.ipynb](example.ipynb) shows an example of what to expect out of my program.


## Dependencies

- [pandas](https://pandas.pydata.org/): used to read tabular data and ply it
- [webbrowser](https://docs.python.org/3/library/webbrowser.html): used to optionally open relevant job postings in the browser


## Usage

In a terminal that sees a Python 3 executable, which in turn knows the required dependencies listed above, run (the dollar sign denotes the default [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) prompt):

```
$ pliers.py ejm_csv_file joe_csv_file date save_to_disk open_in_browser
```

where

- `ejm_csv_file` _(required)_: string describing the path to the CSV you can download from https://econjobmarket.org.
- `joe_csv_file` _(required)_: string describing the path to the CSV you can obtain from https://aeaweb.org/joe/listings.
  > ⚠️ You cannot download directly a CSV file, you must first download the XLS and manually convert it to CSV. This happens because the XLS file the AEA builds is corrupted according to `xlrd` (see [this Stack Overflow question](https://stackoverflow.com/questions/12705527/reading-excel-files-with-xlrd) for the kind or exception it raises).
- `date` _(required)_: the date used to filter the deadlines of job postings, in the format `yyyy-mm-dd` (the dashes are compulsory for string matching).
- `save_to_disk` _(optional)_: either `yes` or `no` (default: `yes`) to choose whether the program saves a easier-to-read comprehensive CSV file for you.
- `open_in_browser` _(optional)_: either `yes` or `no` (default: `no`) to choose whether the program opens _all_ job postings, both on EJM and JOE, whose deadline is on `date`.
  > 🚨 Depending on `date`, this might open a metric ton of tabs. Be prepared to bring your computer to its knees (e.g., November 15, 2020).


## Tips

Check out the job postings some days before their application deadlines. This is important for two reasons.
1. Some vacancies require that you apply via email or via their own website, and therefore you need your letters of recommendation to be sent by the deadline.
1. Sometimes the EJM and JOE websites become painfully slow. An example was the EJM website on November 15, 2020, where a lot of people connected (a lot of deadlines that day). The server behind EJM could just not keep up with everybody. This is even more relevant if you use the option `open_in_browser`.

> ⚠️ This code does NOT filter out duplicate entries across websites. It is often the case that employers post the same vacancy both on EJM and JOE. You will find these duplicates in what this code returns. It is up to you to figure it out. I have found no reliable criterion to flag duplicates.
