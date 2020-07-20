from argparse import ArgumentParser

import scrapy

def setup_parser():
    parser = ArgumentParser()
    
    parser.add_argument("--config", desc = "A file with all of the the data needed to scrape the novel.")
    parser.add_argument("--url", desc="The url to scrape")
    
    return parser.parse_args ()