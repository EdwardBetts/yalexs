"""Constants."""

from .backports.enum import StrEnum
from dataclasses import dataclass


class Brand(StrEnum):
    AUGUST = "august"
    YALE_ACCESS = "yale_access"
    YALE_HOME = "yale_home"
    YALE_GLOBAL = "yale_global"


DEFAULT_BRAND = Brand.AUGUST

BASE_URLS = {
    Brand.AUGUST: "https://api-production.august.com",
    Brand.YALE_ACCESS: "https://api-production.august.com",
    Brand.YALE_HOME: "https://api.aaecosystem.com",
    Brand.YALE_GLOBAL: "https://api.aaecosystem.com",
}

BRANDS = {
    Brand.AUGUST: "August",
    Brand.YALE_ACCESS: "Yale Access",
    Brand.YALE_HOME: "Yale Home",
    Brand.YALE_GLOBAL: "Yale Global",
}

BRANDING = {
    Brand.AUGUST: "august",
    Brand.YALE_ACCESS: "yale",
    Brand.YALE_HOME: "yale",
    Brand.YALE_GLOBAL: "yale",
}


@dataclass
class BrandConfig:
    """Brand configuration."""

    name: str
    branding: str
    access_token_header: str
    api_key_header: str
    branding_header: str
    api_key: str
    supports_doorbells: bool


HEADER_VALUE_API_KEY_OLD = "7cab4bbd-2693-4fc1-b99b-dec0fb20f9d4"
HEADER_VALUE_API_KEY = "d9984f29-07a6-816e-e1c9-44ec9d1be431"

HEADER_AUGUST_ACCESS_TOKEN = "x-august-access-token"  # nosec
HEADER_AUGUST_API_KEY = "x-august-api-key"  # nosec
HEADER_AUGUST_BRANDING = "x-august-branding"

HEADER_ACCESS_TOKEN = "x-access-token"  # nosec
HEADER_API_KEY = "x-api-key"  # nosec
HEADER_BRANDING = "x-branding"

BRAND_CONFIG: dict[Brand, BrandConfig] = {
    Brand.AUGUST: BrandConfig(
        name="August",
        branding="august",
        access_token_header=HEADER_AUGUST_ACCESS_TOKEN,
        api_key_header=HEADER_AUGUST_API_KEY,
        branding_header=HEADER_AUGUST_BRANDING,
        api_key=HEADER_VALUE_API_KEY,
        supports_doorbells=True,
    ),
    Brand.YALE_ACCESS: BrandConfig(
        name="Yale Access",
        branding="yale",
        access_token_header=HEADER_AUGUST_ACCESS_TOKEN,
        api_key_header=HEADER_AUGUST_API_KEY,
        branding_header=HEADER_AUGUST_BRANDING,
        api_key=HEADER_VALUE_API_KEY,
        supports_doorbells=True,
    ),
    Brand.YALE_HOME: BrandConfig(
        name="Yale Home",
        branding="yale",
        access_token_header=HEADER_ACCESS_TOKEN,
        api_key_header=HEADER_API_KEY,
        branding_header=HEADER_BRANDING,
        api_key=HEADER_VALUE_API_KEY,
        supports_doorbells=True,
    ),
    Brand.YALE_GLOBAL: BrandConfig(
        name="Yale Global",
        branding="yale",
        access_token_header=HEADER_ACCESS_TOKEN,
        api_key_header=HEADER_API_KEY,
        branding_header=HEADER_BRANDING,
        # Sadly we currently do not have a way to avoid
        # having the API key in the code because it must
        # run on the user's device
        api_key="d16a1029-d823-4b55-a4ce-a769a9b56f0e",
        supports_doorbells=False,
    ),
}

PUBNUB_TOKENS = {
    Brand.AUGUST: {
        "subscribe": "sub-c-1030e062-0ebe-11e5-a5c2-0619f8945a4f",
        "publish": "pub-c-567d7f2d-270a-438a-a785-f0af12ad8312",
    },
    Brand.YALE_ACCESS: {
        "subscribe": "sub-c-1030e062-0ebe-11e5-a5c2-0619f8945a4f",
        "publish": "pub-c-567d7f2d-270a-438a-a785-f0af12ad8312f",
    },
    Brand.YALE_HOME: {
        "subscribe": "sub-c-c9c38d4d-5796-46c9-9262-af20cf6a1d42",
        "publish": "pub-c-353e8881-cf58-4b26-9baf-96f296de0677",
    },
    # YALE_GLOBAL will eventually WebSockets for push updates
    # but for now we will use the same as YALE_HOME until we
    # can finish the WebSockets implementation
    Brand.YALE_GLOBAL: {
        "subscribe": "sub-c-c9c38d4d-5796-46c9-9262-af20cf6a1d42",
        "publish": "pub-c-353e8881-cf58-4b26-9baf-96f296de0677",
    },
}

CONFIGURATION_URLS = {
    Brand.AUGUST: "https://account.august.com",
    Brand.YALE_ACCESS: "https://account.august.com",
    Brand.YALE_HOME: "https://account.aaecosystem.com",
    Brand.YALE_GLOBAL: "https://account.aaecosystem.com",
}
