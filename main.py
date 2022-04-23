import argparse
import yaml
import requests
import csv
from datetime import date


def csv_to_array(csv_url):
    with requests.Session() as s:
        download = s.get(csv_url)
        decoded_content = download.content.decode("utf-8")
        cr = csv.reader(decoded_content.splitlines(), delimiter=",")
        my_list = list(cr)
        return my_list


def get_csv_url(ad_network, date):
    if len(ad_network) > 0:
        for url in ad_network:
            if (
                str(date.year) in url
                and str(date.month) in url
                and str(date.day) in url
            ):
                return url


def pars_yaml():
    with open("advertising_network.yaml", "r") as stream:
        try:
            ad_network = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return ad_network


def parse_cli():
    parser = argparse.ArgumentParser(
        description="The application takes adNetwork and date as input parameters. It then retrieves each report for these input parameters from the URLs provided in the advertising_network.YAML file and stores it in a database."
    )
    parser.add_argument(
        "--adNetwork",
        "-a",
        action="store",
        required=True,
        type=str,
        choices=["SuperNetwork", "AdUmbrella"],
        help='Choose between "SuperNetwork" or "AdUmbrella"',
    )
    parser.add_argument(
        "--date",
        "-d",
        action="store",
        required=True,
        type=date.fromisoformat,
        help='Date in format "YYYY-MM-DD", Example: 2014-01-28',
    )

    return vars(parser.parse_args())


def main():
    """
    Entry point for the program
    """
    # Parse arguments
    cli_config = parse_cli()
    ad_network = cli_config["adNetwork"]
    date = cli_config["date"]

    # Pars yaml
    data = pars_yaml()
    data_url = data["reports"][ad_network]

    csv_url = get_csv_url(data_url, date)
    csv_array = csv_to_array(csv_url)
    print(csv_array)


if __name__ == "__main__":
    main()
