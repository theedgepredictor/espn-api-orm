
# ESPN API Interaction Instructions

This document provides specific guidance for interacting with the ESPN API in the context of the `espn-api-orm` project.

## General Principles

- **Use Official Endpoints:** Reference the latest endpoint list at https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c for all API calls.
- **Parameterization:** Always use parameters such as `{YEAR}`, `{TEAM_ID}`, `{EVENT_ID}` for flexibility and extensibility. Avoid hardcoding values.
- **HTTP Requests:** Use Python's `requests` library for all HTTP interactions. Handle errors and timeouts gracefully.
- **Rate Limiting:** Be aware of ESPN's rate limits. Implement retry logic and backoff strategies if necessary.
- **Authentication:** Most endpoints are public, but if authentication is required, document the process and keep tokens secure.

## Data Handling

- **Response Validation:** Validate API responses for expected structure and handle missing or malformed data.
- **Mapping to Classes:** Map API responses to Python classes and objects, following the ORM-like structure of the project.
- **Caching:** Consider caching frequent or expensive API calls to reduce load and improve performance.

## Error Handling

- Log errors with sufficient detail for debugging.
- Raise informative exceptions for API failures.
- Provide fallback mechanisms for partial or failed responses.

## Documentation

- Document all new endpoints and parameters in the README and in this instructions file.
- Add usage examples for new API interactions.

## Reference Materials

- [API Endpoint List](https://gist.github.com/nntrn/ee26cb2a0716de0947a0a4e9a157bc1c)
- [ESPN's hidden API endpoints](https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b)
- [espn-wiki](https://github.com/nntrn/espn-wiki/wiki)


For further details, see the main Copilot instructions file and the README.
