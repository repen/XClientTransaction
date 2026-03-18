import re

ADDITIONAL_RANDOM_NUMBER: int = 3
DEFAULT_KEYWORD: str = "obfiowerehiring"

ON_DEMAND_FILE_URL: str = "https://abs.twimg.com/responsive-web/client-web/ondemand.s.{filename}a.js"
ON_DEMAND_FILE_REGEX: re.Pattern = re.compile(r'(?<!\d)(\d+):"ondemand\.s"')
ONDEMAND_HASH_PATTERN: str = "{}:\"([0-9a-f]+)\""

INDICES_REGEX: re.Pattern = re.compile(
    r"""(\(\w{1}\[(\d{1,2})\],\s*16\))+""", flags=(re.VERBOSE | re.MULTILINE))

MIGRATION_REDIRECTION_REGEX: re.Pattern = re.compile(
    r"""(http(?:s)?://(?:www\.)?(twitter|x){1}\.com(/x)?/migrate([/?])?tok=[a-zA-Z0-9%\-_]+)+""", re.VERBOSE)


if __name__ == "__main__":
    pass
