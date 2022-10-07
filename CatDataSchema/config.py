import os

# The sqlalchemy toolkit uses Database urls which follow RFC-1738 protocol to create an engine
# The syntax: dialect+driver://postgres_username:password@host:port/database
# DATABASE_URL = os.getenv(
#     "DATABASE_URL",
#     "postgresql+psycopg2://metabase_catwatcher_user:metabase_catwatcher_pw@localhost:5432/metabase_catwatcher_db",
# )

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://metabase_catwatcher_test_user:metabase_catwatcher_test_pw@db:5432/metabase_catwatcher_test_db",
)

