from pathlib import Path

def export_csv(dataframe, filename, output_dir):
    output_dir.mkdir(exist_ok=True)
    dataframe.to_csv(output_dir / filename)