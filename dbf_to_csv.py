import csv
import argparse
from dbfread import DBF


def dbf_to_csv(args):
    for file in args:
        csv_file = file + ".csv"
        # The original DBF standard defines to use ISO8859-1
        table = DBF(file, encoding='ISO8859-1')
        with open(csv_file, "w", encoding="utf-8", newline="") as outf:
            writer = csv.writer(outf)
            writer.writerow(table.field_names)
            for record in table:
                writer.writerow(list(record.values()))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "dbf_filename", help=(
            """
            Name of dbfs files you want to convert example:
            file1.dbf or various files example: file1.dbf,file2.dbf
            """
        )
    )
    args = parser.parse_args().dbf_filename.split(",")

    dbf_to_csv(args)
