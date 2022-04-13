# Blazing fast URL shortener 🚀

This url shortener is built with FastAPI and asyncpg driver for Postgres, so you can expect it to be pretty responsive (3-6 ms).

## Getting started with local server

1. CD into project root and install python packages with `pipenv install` or you with preffered package manager.
2. Spin up new local postgres database. This setup uses Postgres *asyncpg* driver.
3. Create `.env` file with the following contents and modify your postgres credentials/db name.

```
DATABASE_URL=postgresql+asyncpg://postgres:root@localhost/dbname
APPLICATION_SECRET=123456
CURRENT_HOST=http://127.0.0.1:8000
PRIVATE_MODE=False
ENV_NAME=development
```
4. Run `uvicorn app:app --reload`
5. Inspect API documentation served with Swagger [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Private mode

If your don't want to go public, then set `PRIVATE_MODE=True` and adjust your client request headers to include Authorization token.

Sample:
`"Authorization": "Bearer {APPLICATION_SECRET}"`


