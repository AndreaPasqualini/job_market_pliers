#!/usr/bin/env python3


import sys
import pandas as pd
import webbrowser


def yes_no_to_bool(string):
    if string == 'yes':
        return True
    elif string == 'no':
        return False
    else:
        raise ValueError(f'Unsupported argument value "{string}".')


def clean_ejm(src, today):
    cols = ['Id',
            'Ad title',
            'Types',
            'Institution',
            'City',
            'Country',
            'Deadline']
    subset = src[cols]
    ejm_today = subset[subset['Deadline'] == today].drop('Deadline', axis=1)
    ejm_today['url'] = 'https://econjobmarket.org/positions/' + ejm_today['Id'].astype(str)
    ejm_today['locations'] = ejm_today['Country'].str.upper() + ' ' + ejm_today['City']
    ejm_today.drop(['Id', 'City', 'Country'], axis=1, inplace=True)
    rename_dict = {'Ad title': 'title',
                   'Types': 'type',
                   'Institution': 'institution'}
    return ejm_today.rename(columns=rename_dict)


def clean_joe(src, today):
    cols = ['joe_issue_ID',
            'jp_id',
            'jp_section',
            'jp_institution',
            'jp_title',
            'locations',
            'Application_deadline']
    subset_joe = src_joe[cols]
    joe_today = subset_joe[subset_joe['Application_deadline'] == f'{today} 00:00:00'].drop('Application_deadline', axis=1)
    joe_today['url'] = 'https://www.aeaweb.org/joe/listing.php?JOE_ID=' + joe_today['joe_issue_ID'].astype(str) + '_' + joe_today['jp_id'].astype(str)
    joe_today.drop(['joe_issue_ID', 'jp_id'], axis=1, inplace=True)
    rename_dict = {'jp_title': 'title',
                   'jp_section': 'type',
                   'jp_institution': 'institution'}
    return joe_today.rename(columns=rename_dict)


if __name__ == '__main__':

    ejm_src_file = sys.argv[1]
    joe_src_file = sys.argv[2]
    date = sys.argv[3]  # in the format "yyyy-mm-dd"

    write_csv_to_disk = yes_no_to_bool(sys.argv[4])
    open_all_in_browser = yes_no_to_bool(sys.argv[5])

    src_ejm = pd.read_csv(ejm_src_file, encoding='utf-8', header=1)
    src_joe = pd.read_csv(joe_src_file, encoding='utf-8')

    ejm_on_date = clean_ejm(src_ejm, date)
    joe_on_date = clean_joe(src_joe, date)
    deadlines_on_date = pd.concat([ejm_on_date, joe_on_date], ignore_index=True)

    if write_csv_to_disk:
        deadlines_on_date.to_csv(f'./deadlines_{date}.csv', index=False, encoding='utf-8')

    if open_all_in_browser:
        all_urls = deadlines_on_date.url
        for url in all_urls:
            _ = webbrowser.open(url)
