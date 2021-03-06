from gerry_research import exporter, collector, constants as cnst, cleaner


def main():
    df = cleaner.clean(
        df=collector.collect_multiple_data_files(
            files=cnst.DATA_FILES, duplcate_subset=[cnst.GAME_COLUMN, cnst.SCORE_COLUMN]
        )
    )
    df = collector.merge_output_files(df)
    exporter.export(df, str(cnst.OUTPUT_FILE))


if __name__ == "__main__":
    main()
