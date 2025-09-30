import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import Boolean, Float, String, Integer, Text, DECIMAL, DATETIME
from sqlalchemy.dialects.mysql import LONGTEXT

from .configuration import (
    MYSQL_USERNAME,
    MYSQL_PASSWORD,
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_DATABASE,
)


# Create metadata
metadata = MetaData()

game_check_table = Table(
    "game_check",
    metadata,
    Column("app_id", String(8), primary_key=True, comment="application_id"),
    Column("is_game", Integer, nullable=True, default=0),
)

game_information_table = Table(
    "game_information",
    metadata,
    Column("app_id", String(8), primary_key=True, comment="outer_application_id"),
    Column("steam_app_id", String(8), nullable=False, comment="inner_application_id"),

    Column("name", String(100), nullable=False, comment="application_name"),
    Column("required_age", Integer, nullable=False, comment=""),
    Column("is_free", Integer, nullable=False, comment=""),
    Column("supported_languages", LONGTEXT, nullable=False, comment=""),
    Column("header_image", String(255), nullable=False, comment=""),
    Column("developers", String(100), nullable=False, comment=""),
    Column("publishers", String(100), nullable=False, comment=""),
    Column("final_formatted", String(8), nullable=False, comment=""),
    Column("release_date", DATETIME, nullable=False, comment=""),
)

game_genre_table = Table(
    "game_genre",
    metadata,
    Column("app_id", String(8), primary_key=True, comment="application_id"),
    Column("genre_id", Integer, primary_key=True),
    Column("genre_description", String(32), nullable=False),
)

game_review_summary_table = Table(
    "game_review_summary",
    metadata,
    Column("recommendation_id", String(16), primary_key=True, comment="recommendation_id"),
    Column("app_id", String(8), nullable=False, comment="application_id"),
    Column("review_score", Float, nullable=False),
    Column("review_score_desc", String(255), nullable=False),
    Column("total_positive", Integer, nullable=True, default=-1),
    Column("total_negative", Integer, nullable=True, default=-1),
    Column("total_reviews", Integer, nullable=True, default=-1),
    Column("capture_date", DATETIME, nullable=False),
)

game_review_detail_table = Table(
    "game_review_detail",
    metadata,
    Column("app_id", String(8), primary_key=True, comment="application_id"),
)


if __name__ == "__main__":
    print(MYSQL_USERNAME)
    print(MYSQL_PASSWORD)
    print(MYSQL_HOST)
    print(MYSQL_PORT)
    print(MYSQL_DATABASE)