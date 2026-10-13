"""Data cleaning functions for library pipeline.

The cleaning module

This module contains functions for cleaning and standardising data.
All functions return new DataFrames without modifying the input.
"""

import logging
import pandas as pd

logger = logging.getLogger(__name__)


def remove_duplicates(df, subset=None):
    """Remove duplicate rows from DataFrame."""
    df = df.copy()  # Work on a copy!

    original_rows = len(df)
    df = df.drop_duplicates(subset=subset)
    removed_rows = original_rows - len(df)

    logger.info(f"Removed {removed_rows} duplicate rows")

    return df


def handle_missing_values(df, strategy="drop", fill_value=None, columns=None):
    """Handle missing values in DataFrame."""
    df = df.copy()

    if columns is None:
        columns = df.columns

    if strategy == "drop":
        df = df.dropna(subset=columns)
        logger.info("Dropped rows with missing values")

    elif strategy == "fill":
        df[columns] = df[columns].fillna(fill_value)
        logger.info(f"Filled missing values with '{fill_value}'")

    else:
        raise ValueError("strategy must be 'drop' or 'fill'")

    return df


def standardise_dates(df, date_columns, date_format="%Y-%m-%d"):
    """Standardise date columns to consistent format."""
    df = df.copy()

    for column in date_columns:
        df[column] = (
            pd.to_datetime(df[column], errors="coerce")
            .dt.strftime(date_format)
        )

    logger.info(f"Standardised date columns: {date_columns}")

    return df