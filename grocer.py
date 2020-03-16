import logging
import platform
import subprocess
import time

import click

from store_search.stores import QFC, FredMeyer, Safeway, Target, WholeFoods


class Browser:
    logger = logging.getLogger(__name__)

    def __init__(self, dry_run=False):
        self.cmd_prefix = None
        self.dry_run = dry_run
        self.configure()

    def configure(self):
        p = platform.system()
        if p in ["Darwin", "Linux"]:
            self.cmd_prefix = ["open"]
        elif p in ["Windows"]:
            self.cmd_prefix = ["cmd", "/c", "start"]

    def open(self, url):
        cmd = self.cmd_prefix + [url]
        self.logger.debug(cmd)
        if not self.dry_run:
            process = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            process.communicate()


@click.command()
@click.option("-d", "--debug/--no-debug", default=False)
@click.option("-n", "--dry-run/--no-dry-run", default=False)
@click.option("-p", "--pause", default=0.1, show_default=True, type=float)
@click.argument("product", nargs=-1)
def cli(product, debug, dry_run, pause):
    logger = logging.getLogger(__name__)
    if debug:
        logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter(
        "{%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    target = Target()
    fred = FredMeyer()
    safeway = Safeway(params={"zipCode": 98122})
    wf = WholeFoods(params={"sort": "relevance", "store": 10630})
    qfc = QFC()

    product = " ".join(product)
    browser = Browser(dry_run=dry_run)
    logger.debug("created brower")
    store_list = [qfc, fred, target, wf, safeway]
    for i, store in enumerate(store_list):
        url = store.url(product)
        browser.open(url)
        if not dry_run and not i == len(store_list) - 1:
            time.sleep(pause)
