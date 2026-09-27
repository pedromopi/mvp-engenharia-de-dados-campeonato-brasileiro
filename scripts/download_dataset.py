#!/usr/bin/env python3
"""Baixa uma versão reproduzível do dataset do Brasileirão no Kaggle."""

from __future__ import annotations

import argparse
from pathlib import Path

import kagglehub


DATASET_HANDLE = "adaoduque/campeonato-brasileiro-de-futebol"
DEFAULT_VERSION = 18
DEFAULT_OUTPUT_DIR = Path("data/raw/campeonato-brasileiro")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Baixa o dataset Campeonato Brasileiro de Futebol do Kaggle."
    )
    parser.add_argument(
        "--version",
        type=int,
        default=DEFAULT_VERSION,
        help=f"Versão do dataset no Kaggle (padrão: {DEFAULT_VERSION}).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Diretório de destino (padrão: {DEFAULT_OUTPUT_DIR}).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Baixa novamente mesmo que os arquivos já existam.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    versioned_handle = f"{DATASET_HANDLE}/versions/{args.version}"
    downloaded_path = kagglehub.dataset_download(
        versioned_handle,
        output_dir=str(output_dir),
        force_download=args.force,
    )

    files = sorted(path for path in Path(downloaded_path).iterdir() if path.is_file())
    print(f"Dataset: {versioned_handle}")
    print(f"Destino: {downloaded_path}")
    print("Arquivos:")
    for path in files:
        print(f"- {path.name} ({path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
