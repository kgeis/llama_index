# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConfigurableDataSourceNames(str, enum.Enum):
    """
    An enumeration.
    """

    DOCUMENT = "DOCUMENT"
    RAW_FILE = "RAW_FILE"
    DISCORD = "DISCORD"
    ELASTICSEARCH = "ELASTICSEARCH"
    NOTION_PAGE = "NOTION_PAGE"
    SLACK = "SLACK"
    TWITTER = "TWITTER"
    SIMPLE_WEB_PAGE = "SIMPLE_WEB_PAGE"
    TRAFILATURA_WEB_PAGE = "TRAFILATURA_WEB_PAGE"
    BEAUTIFUL_SOUP_WEB_PAGE = "BEAUTIFUL_SOUP_WEB_PAGE"
    RSS = "RSS"
    WIKIPEDIA = "WIKIPEDIA"
    YOUTUBE_TRANSCRIPT = "YOUTUBE_TRANSCRIPT"
    GOOGLE_DOCS = "GOOGLE_DOCS"
    GOOGLE_SHEETS = "GOOGLE_SHEETS"
    READER = "READER"

    def visit(
        self,
        document: typing.Callable[[], T_Result],
        raw_file: typing.Callable[[], T_Result],
        discord: typing.Callable[[], T_Result],
        elasticsearch: typing.Callable[[], T_Result],
        notion_page: typing.Callable[[], T_Result],
        slack: typing.Callable[[], T_Result],
        twitter: typing.Callable[[], T_Result],
        simple_web_page: typing.Callable[[], T_Result],
        trafilatura_web_page: typing.Callable[[], T_Result],
        beautiful_soup_web_page: typing.Callable[[], T_Result],
        rss: typing.Callable[[], T_Result],
        wikipedia: typing.Callable[[], T_Result],
        youtube_transcript: typing.Callable[[], T_Result],
        google_docs: typing.Callable[[], T_Result],
        google_sheets: typing.Callable[[], T_Result],
        reader: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConfigurableDataSourceNames.DOCUMENT:
            return document()
        if self is ConfigurableDataSourceNames.RAW_FILE:
            return raw_file()
        if self is ConfigurableDataSourceNames.DISCORD:
            return discord()
        if self is ConfigurableDataSourceNames.ELASTICSEARCH:
            return elasticsearch()
        if self is ConfigurableDataSourceNames.NOTION_PAGE:
            return notion_page()
        if self is ConfigurableDataSourceNames.SLACK:
            return slack()
        if self is ConfigurableDataSourceNames.TWITTER:
            return twitter()
        if self is ConfigurableDataSourceNames.SIMPLE_WEB_PAGE:
            return simple_web_page()
        if self is ConfigurableDataSourceNames.TRAFILATURA_WEB_PAGE:
            return trafilatura_web_page()
        if self is ConfigurableDataSourceNames.BEAUTIFUL_SOUP_WEB_PAGE:
            return beautiful_soup_web_page()
        if self is ConfigurableDataSourceNames.RSS:
            return rss()
        if self is ConfigurableDataSourceNames.WIKIPEDIA:
            return wikipedia()
        if self is ConfigurableDataSourceNames.YOUTUBE_TRANSCRIPT:
            return youtube_transcript()
        if self is ConfigurableDataSourceNames.GOOGLE_DOCS:
            return google_docs()
        if self is ConfigurableDataSourceNames.GOOGLE_SHEETS:
            return google_sheets()
        if self is ConfigurableDataSourceNames.READER:
            return reader()
