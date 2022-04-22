import argparse
import yaml
from datetime import date

def pars_yaml():
    with open('advertising_network.yaml', 'r') as stream:
        try:
            ad_network = (yaml.safe_load(stream))
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
        choices=['SuperNetwork', 'AdUmbrella'],
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
    cli_config = parse_cli()
    ad_network = cli_config["adNetwork"]
    date = cli_config["date"]

    print(date)
    data = pars_yaml()
    print(data['reports'][ad_network])


if __name__ == "__main__":
    main()
